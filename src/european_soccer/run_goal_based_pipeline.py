"""
Goal-based simulation pipeline for European soccer leagues.

This script rebuilds the missing outputs for the goals-based (pure-luck) scenario so
they mirror the artifacts that already exist for the result-based simulator.  It:

1. Resamples match goals by season using empirical distributions and writes
   per-league match logs (`*_simulated_matches_all_seeds.csv`) plus the aggregated
   standings tables (`*_simulated_standings_all_seasons.csv`).
2. Generates upset-frequency summaries (overall + per-season) and lightweight
   comparison charts for each simulation seed.
3. Computes first-half vs second-half win persistence metrics and exports the same
   CSV/PNG bundle used by the other simulation types.

Run with: ``python3 src/european_soccer/run_goal_based_pipeline.py``.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from pathlib import Path
from statistics import NormalDist
from typing import Dict, Hashable, Mapping

import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "european_soccer_leagues"
ACTUAL_DIR = DATA_DIR / "actual"
GOAL_SIM_DIR = DATA_DIR / "pure_luck_goals_based"
OUTPUT_DIR = REPO_ROOT / "output" / "european_soccer_leagues"
UPSET_OUTPUT_DIR = OUTPUT_DIR / "upset_frequency" / "pure_luck_goals_based"
CORR_OUTPUT_DIR = OUTPUT_DIR / "correlations" / "pure_luck_goals_based"
MPLCONFIG_DIR = OUTPUT_DIR / ".matplotlib"

os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)

import seaborn as sns
import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt

NUM_SIM_RUNS = 10
MASTER_SEED = 12345
SEED_SEQUENCE = np.random.SeedSequence(MASTER_SEED)
RNG_SEEDS = list(map(int, SEED_SEQUENCE.generate_state(NUM_SIM_RUNS)))


@dataclass(frozen=True)
class LeagueConfig:
    slug: str
    pretty: str

    @property
    def matches_path(self) -> Path:
        return ACTUAL_DIR / f"{self.slug}_actual.csv"

    @property
    def standings_path(self) -> Path:
        return ACTUAL_DIR / f"{self.slug}_standings_all_seasons.csv"

    @property
    def sim_matches_path(self) -> Path:
        return GOAL_SIM_DIR / f"{self.slug}_simulated_matches_all_seeds.csv"

    @property
    def sim_standings_path(self) -> Path:
        return GOAL_SIM_DIR / f"{self.slug}_simulated_standings_all_seasons.csv"


LEAGUES: Dict[str, LeagueConfig] = {
    "bundesliga": LeagueConfig(slug="bundesliga", pretty="Bundesliga"),
    "la_liga": LeagueConfig(slug="la_liga", pretty="La Liga"),
    "premier_league": LeagueConfig(slug="premier_league", pretty="Premier League"),
    "serie_a": LeagueConfig(slug="serie_a", pretty="Serie A"),
}

PALETTE = {
    "Premier League": "#1f77b4",
    "La Liga": "#ff7f0e",
    "Serie A": "#2ca02c",
    "Bundesliga": "#d62728",
}

NORMAL_DIST = NormalDist()


# -----------------------------------------------------------------------------
# Core simulation helpers
# -----------------------------------------------------------------------------

def empirical_goal_dists(
    df: pd.DataFrame,
    season_col: str = "season",
    hg_col: str = "hometeamgoals",
    ag_col: str = "awayteamgoals",
) -> Dict[Hashable, Dict[str, np.ndarray]]:
    """Build per-season empirical goal distributions."""
    dists: Dict[Hashable, Dict[str, np.ndarray]] = {}
    tmp = df[[season_col, hg_col, ag_col]].copy()
    tmp[hg_col] = tmp[hg_col].astype(float).round().astype(int)
    tmp[ag_col] = tmp[ag_col].astype(float).round().astype(int)

    for season, grp in tmp.groupby(season_col):
        hg_counts = grp[hg_col].value_counts().sort_index()
        ag_counts = grp[ag_col].value_counts().sort_index()
        max_g = int(max(hg_counts.index.max(), ag_counts.index.max()))
        goals = np.arange(0, max_g + 1)
        hp = hg_counts.reindex(goals, fill_value=0).to_numpy(dtype=float)
        ap = ag_counts.reindex(goals, fill_value=0).to_numpy(dtype=float)

        hp_sum = hp.sum()
        ap_sum = ap.sum()
        if hp_sum == 0:
            hp = np.ones_like(goals, dtype=float)
            hp_sum = hp.sum()
        if ap_sum == 0:
            ap = np.ones_like(goals, dtype=float)
            ap_sum = ap.sum()

        dists[season] = {
            "goals": goals,
            "home_p": hp / hp_sum,
            "away_p": ap / ap_sum,
        }

    return dists


def simulate_matches_from_empirical(
    df: pd.DataFrame,
    dists: Mapping[Hashable, Dict[str, np.ndarray]],
    season_col: str = "season",
    seed: int | None = None,
) -> pd.DataFrame:
    """Sample match goals from the empirical distributions and recompute points."""
    rng = np.random.default_rng(seed)
    out = df.copy()

    sim_home = []
    sim_away = []
    for season in out[season_col]:
        dist = dists[season]
        goals = dist["goals"]
        sim_home.append(rng.choice(goals, p=dist["home_p"]))
        sim_away.append(rng.choice(goals, p=dist["away_p"]))

    out["hometeamgoals"] = np.asarray(sim_home, dtype=int)
    out["awayteamgoals"] = np.asarray(sim_away, dtype=int)
    diff = out["hometeamgoals"] - out["awayteamgoals"]
    out["hometeamresult"] = np.sign(diff).astype(int)
    out["home_team_points"] = np.where(diff > 0, 3, np.where(diff == 0, 1, 0)).astype(float)
    out["away_team_points"] = np.where(diff < 0, 3, np.where(diff == 0, 1, 0)).astype(float)
    return out


def season_rankings_from_simulation(sim_df: pd.DataFrame) -> pd.DataFrame:
    """Collapse a simulated season into team ranks."""
    home = sim_df[["season", "home_team", "hometeamgoals", "awayteamgoals", "home_team_points"]].copy()
    home.columns = ["season", "team", "goals_for", "goals_against", "points"]
    away = sim_df[["season", "away_team", "awayteamgoals", "hometeamgoals", "away_team_points"]].copy()
    away.columns = ["season", "team", "goals_for", "goals_against", "points"]

    table = pd.concat([home, away], ignore_index=True)
    table = (
        table.groupby(["season", "team"], as_index=False)
        .agg(
            points=("points", "sum"),
            goals_for=("goals_for", "sum"),
            goals_against=("goals_against", "sum"),
        )
    )
    table["goal_diff"] = table["goals_for"] - table["goals_against"]
    table = table.sort_values(
        ["season", "points", "goal_diff", "goals_for", "team"],
        ascending=[True, False, False, False, True],
    ).reset_index(drop=True)
    table["rank"] = table.groupby("season").cumcount() + 1
    return table[["season", "team", "rank"]]


# -----------------------------------------------------------------------------
# File builders
# -----------------------------------------------------------------------------

def rebuild_simulation_files(league: LeagueConfig) -> pd.DataFrame:
    """Simulate matches for a league and emit match/standing CSVs."""
    matches = pd.read_csv(league.matches_path)
    matches = matches.sort_values(["season", "date", "home_team", "away_team"]).reset_index(drop=True)
    dists = empirical_goal_dists(matches)

    match_matrix = matches[["season", "date", "home_team", "away_team", "hometeamresult"]].copy()
    match_matrix = match_matrix.rename(columns={"hometeamresult": "true_home_team_result"})
    rank_frames: Dict[int, pd.DataFrame] = {}

    for idx, rng_seed in enumerate(RNG_SEEDS, start=1):
        sim = simulate_matches_from_empirical(matches, dists, seed=rng_seed)
        match_matrix[f"simulated_home_team_result_seed_{idx}"] = sim["hometeamresult"].to_numpy(dtype=int)
        rank_frames[idx] = season_rankings_from_simulation(sim)

    league.sim_matches_path.parent.mkdir(parents=True, exist_ok=True)
    match_matrix.to_csv(league.sim_matches_path, index=False)

    actual = pd.read_csv(league.standings_path)
    standings = (
        actual[["season", "team_name", "rank"]]
        .rename(columns={"team_name": "team", "rank": "actual_rank"})
        .sort_values(["season", "actual_rank", "team"])
        .reset_index(drop=True)
    )

    for idx, frame in rank_frames.items():
        col = f"simulated_rank_{idx}"
        standings = standings.merge(
            frame.rename(columns={"rank": col}),
            on=["season", "team"],
            how="left",
        )

    league.sim_standings_path.parent.mkdir(parents=True, exist_ok=True)
    standings.to_csv(league.sim_standings_path, index=False)
    return match_matrix


# -----------------------------------------------------------------------------
# Upset frequency outputs
# -----------------------------------------------------------------------------

def upset_stats(truth: pd.Series, preds: pd.Series) -> dict:
    """Return upset math consistent with the existing notebooks."""
    truth = truth.astype(int).to_numpy()
    preds = preds.astype(int).to_numpy()

    draws = truth == 0
    non_draw = ~draws
    upsets = ((preds == 1) & (truth == -1)) | ((preds == -1) & (truth == 1))
    total_matches = len(truth)
    total_upsets = upsets[non_draw].sum() + 0.5 * draws.sum()
    accuracy = (preds == truth).sum() / total_matches if total_matches else 0.0

    return {
        "total_matches": int(total_matches),
        "total_upsets": float(total_upsets),
        "upset_frequency": float(total_upsets / total_matches) if total_matches else 0.0,
        "accuracy": float(accuracy),
    }


def aggregate_upset_overall(per_seed_df: pd.DataFrame) -> pd.DataFrame:
    """Pivot per-seed overall upset data into one wide frame."""
    if per_seed_df.empty:
        return pd.DataFrame(columns=["league", "total_matches", "total_upsets_avg", "upset_frequency_avg"])

    seeds = sorted(per_seed_df["seed"].unique())
    rows: list[dict[str, float | int | str]] = []
    for league, grp in per_seed_df.groupby("league"):
        row: dict[str, float | int | str] = {"league": league}
        matches = grp["total_matches"].dropna()
        row["total_matches"] = int(matches.iloc[0]) if not matches.empty else 0
        for seed in seeds:
            sub = grp[grp["seed"] == seed]
            if sub.empty:
                continue
            row[f"total_upsets_seed_{int(seed)}"] = float(sub["total_upsets"].iloc[0])
            row[f"upset_frequency_seed_{int(seed)}"] = float(sub["upset_frequency"].iloc[0])
        row["total_upsets_avg"] = float(grp["total_upsets"].mean())
        row["upset_frequency_avg"] = float(grp["upset_frequency"].mean())
        rows.append(row)

    ordered_cols = ["league", "total_matches"]
    for seed in seeds:
        ordered_cols.append(f"total_upsets_seed_{int(seed)}")
        ordered_cols.append(f"upset_frequency_seed_{int(seed)}")
    ordered_cols.extend(["total_upsets_avg", "upset_frequency_avg"])
    wide = pd.DataFrame(rows)
    return wide[ordered_cols].sort_values("league").reset_index(drop=True)


def aggregate_upset_seasonal(per_seed_df: pd.DataFrame) -> pd.DataFrame:
    """Pivot per-seed seasonal upset data into one wide frame."""
    if per_seed_df.empty:
        return pd.DataFrame(
            columns=["league", "season", "total_matches", "total_upsets_avg", "upset_frequency_avg"]
        )

    seeds = sorted(per_seed_df["seed"].unique())
    rows: list[dict[str, float | int | str]] = []
    for (league, season), grp in per_seed_df.groupby(["league", "season"]):
        row: dict[str, float | int | str] = {"league": league, "season": int(season)}
        matches = grp["total_matches"].dropna()
        row["total_matches"] = int(matches.iloc[0]) if not matches.empty else 0
        for seed in seeds:
            sub = grp[grp["seed"] == seed]
            if sub.empty:
                continue
            row[f"total_upsets_seed_{int(seed)}"] = float(sub["total_upsets"].iloc[0])
            row[f"upset_frequency_seed_{int(seed)}"] = float(sub["upset_frequency"].iloc[0])
        row["total_upsets_avg"] = float(grp["total_upsets"].mean())
        row["upset_frequency_avg"] = float(grp["upset_frequency"].mean())
        rows.append(row)

    ordered_cols = ["league", "season", "total_matches"]
    for seed in seeds:
        ordered_cols.append(f"total_upsets_seed_{int(seed)}")
        ordered_cols.append(f"upset_frequency_seed_{int(seed)}")
    ordered_cols.extend(["total_upsets_avg", "upset_frequency_avg"])
    wide = pd.DataFrame(rows)
    return wide[ordered_cols].sort_values(["league", "season"]).reset_index(drop=True)


def save_upset_frequency_plots(overall_df: pd.DataFrame, seasonal_df: pd.DataFrame) -> None:
    """Persist the aggregate upset plots using the average columns."""
    if overall_df.empty or seasonal_df.empty:
        return

    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=overall_df,
        x="league",
        y="upset_frequency_avg",
        hue="league",
        palette=PALETTE,
        dodge=False,
        legend=False,
        ax=ax,
    )
    ax.set_ylabel("Upset Frequency")
    ax.set_xlabel("")
    ax.set_ylim(0, 0.6)
    fig.tight_layout()
    fig.savefig(UPSET_OUTPUT_DIR / "upset_frequency_by_league_totals_avg.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6))
    sns.lineplot(
        data=seasonal_df,
        x="season",
        y="upset_frequency_avg",
        hue="league",
        palette=PALETTE,
        marker="o",
        ax=ax,
    )
    ax.set_ylabel("Upset Frequency")
    ax.set_xlabel("Season")
    ax.set_ylim(0, 0.6)
    ax.legend(title="League")
    fig.tight_layout()
    fig.savefig(UPSET_OUTPUT_DIR / "upset_frequency_by_season_all_leagues_avg.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
        data=seasonal_df,
        x="league",
        y="upset_frequency_avg",
        hue="league",
        palette=PALETTE,
        dodge=False,
        legend=False,
        ax=ax,
    )
    ax.set_xlabel("")
    ax.set_ylabel("Upset Frequency")
    ax.set_ylim(0, 0.6)
    fig.tight_layout()
    fig.savefig(UPSET_OUTPUT_DIR / "upset_frequency_boxplot_by_league_avg.png", dpi=300)
    plt.close(fig)


def generate_upset_outputs(league_dfs: Dict[str, pd.DataFrame]) -> None:
    """Write combined upset summaries and plots."""
    UPSET_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for pattern in (
        "overall_upset_frequency_summary_seed_*.csv",
        "season_upset_frequency_summary_seed_*.csv",
        "avg_upset_frequency_by_league_seed_*.png",
        "upset_frequency_by_season_seed_*.png",
        "upset_frequency_boxplot_by_league_seed_*.png",
    ):
        for stale in UPSET_OUTPUT_DIR.glob(pattern):
            stale.unlink(missing_ok=True)

    per_seed_overall = []
    per_seed_seasonal = []

    for seed_idx in range(1, NUM_SIM_RUNS + 1):
        seed_col = f"simulated_home_team_result_seed_{seed_idx}"
        overall_rows = []
        seasonal_rows = []
        for league_name, df in league_dfs.items():
            league_pretty = LEAGUES[league_name].pretty
            stats_all = upset_stats(df["true_home_team_result"], df[seed_col])
            overall_rows.append({"league": league_pretty, **stats_all})

            for season, grp in df.groupby("season"):
                stats_season = upset_stats(grp["true_home_team_result"], grp[seed_col])
                seasonal_rows.append(
                    {"league": league_pretty, "season": int(season), **stats_season}
                )

        overall_df = pd.DataFrame(overall_rows).sort_values("league")
        seasonal_df = pd.DataFrame(seasonal_rows).sort_values(["league", "season"])
        overall_df["seed"] = seed_idx
        seasonal_df["seed"] = seed_idx
        per_seed_overall.append(overall_df)
        per_seed_seasonal.append(seasonal_df)

    if not per_seed_overall or not per_seed_seasonal:
        return

    combined_overall = pd.concat(per_seed_overall, ignore_index=True)
    combined_seasonal = pd.concat(per_seed_seasonal, ignore_index=True)
    league_summary = aggregate_upset_overall(combined_overall)
    season_summary = aggregate_upset_seasonal(combined_seasonal)

    league_summary.to_csv(UPSET_OUTPUT_DIR / "league_upset_frequency_summary_all_seeds.csv", index=False)
    season_summary.to_csv(UPSET_OUTPUT_DIR / "season_upset_frequency_summary_all_seeds.csv", index=False)
    save_upset_frequency_plots(league_summary, season_summary)


# -----------------------------------------------------------------------------
# Correlation outputs
# -----------------------------------------------------------------------------

def build_team_halves(df: pd.DataFrame, seed_idx: int, league: str) -> pd.DataFrame:
    """Compute first/second half win pct for each team-season for a seed."""
    seed_col = f"simulated_home_team_result_seed_{seed_idx}"
    df = df.copy()
    df["match_id"] = np.arange(len(df))

    home = df[["season", "date", "match_id", "home_team", seed_col]].copy()
    home.columns = ["season", "date", "match_id", "team", "result"]
    away = df[["season", "date", "match_id", "away_team", seed_col]].copy()
    away.columns = ["season", "date", "match_id", "team", "result"]
    away["result"] = -away["result"]

    team_games = pd.concat([home, away], ignore_index=True)
    team_games["date"] = pd.to_datetime(team_games["date"])
    team_games = team_games.sort_values(["season", "team", "date", "match_id"])

    rows = []
    for (season, team), grp in team_games.groupby(["season", "team"]):
        n_games = len(grp)
        if n_games == 0:
            continue
        mid = n_games // 2
        first = grp.iloc[:mid]
        second = grp.iloc[mid:]
        rows.append(
            {
                "league": league,
                "season": int(season),
                "team": team,
                "first_half_win_pct": float((first["result"] == 1).mean() if len(first) else 0.0),
                "second_half_win_pct": float((second["result"] == 1).mean() if len(second) else 0.0),
                "n_first": int(len(first)),
                "n_second": int(len(second)),
                "seed": seed_idx,
            }
        )

    return pd.DataFrame(rows)


def spearman_with_normal_approx(x: pd.Series, y: pd.Series) -> tuple[float, float]:
    """Compute Spearman correlation and an approximate two-sided p-value."""
    x_rank = x.rank(method="average").to_numpy(dtype=float)
    y_rank = y.rank(method="average").to_numpy(dtype=float)

    if len(x_rank) < 2 or np.allclose(x_rank, x_rank[0]) or np.allclose(y_rank, y_rank[0]):
        return float("nan"), float("nan")

    corr = float(np.corrcoef(x_rank, y_rank)[0, 1])
    if math.isnan(corr):
        return float("nan"), float("nan")

    n = len(x_rank)
    if n <= 2 or abs(corr) >= 1:
        return corr, 0.0

    t_stat = corr * math.sqrt((n - 2) / max(1e-12, 1 - corr**2))
    tail = 1 - NORMAL_DIST.cdf(abs(t_stat))
    p_value = 2 * tail
    return corr, float(p_value)


def correlation_summaries(team_halves: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return overall + seasonal Spearman correlations."""
    overall_rows = []
    seasonal_rows = []
    for (league, seed), grp in team_halves.groupby(["league", "seed"]):
        if grp.empty:
            continue
        corr, p_val = spearman_with_normal_approx(grp["first_half_win_pct"], grp["second_half_win_pct"])
        overall_rows.append({"league": league, "seed": seed, "spearman_r": corr, "spearman_p": p_val})

    for (season, seed), grp in team_halves.groupby(["season", "seed"]):
        if grp.empty:
            continue
        corr, p_val = spearman_with_normal_approx(grp["first_half_win_pct"], grp["second_half_win_pct"])
        seasonal_rows.append(
            {
                "season": int(season),
                "seed": seed,
                "n_teams": int(len(grp)),
                "spearman_r": corr,
                "spearman_p": p_val,
            }
        )

    overall_df = pd.DataFrame(overall_rows).sort_values(["seed", "league"])
    seasonal_df = pd.DataFrame(seasonal_rows).sort_values(["seed", "season"])
    return overall_df, seasonal_df


def reshape_halves_by_seed(team_halves: pd.DataFrame) -> pd.DataFrame:
    """Pivot the per-seed halves data into a single wide CSV."""
    if team_halves.empty:
        return pd.DataFrame(
            columns=["league", "season", "team", "first_half_win_pct_avg", "second_half_win_pct_avg"]
        )

    seeds = sorted(team_halves["seed"].unique())
    rows: list[dict[str, float | int | str]] = []
    for (league, season, team), grp in team_halves.groupby(["league", "season", "team"]):
        row: dict[str, float | int | str] = {"league": league, "season": int(season), "team": team}
        grp = grp.sort_values("seed")
        for seed in seeds:
            sub = grp[grp["seed"] == seed]
            if sub.empty:
                continue
            row[f"first_half_win_pct_seed_{int(seed)}"] = float(sub["first_half_win_pct"].iloc[0])
            row[f"second_half_win_pct_seed_{int(seed)}"] = float(sub["second_half_win_pct"].iloc[0])

        row["first_half_win_pct_avg"] = float(grp["first_half_win_pct"].mean())
        row["second_half_win_pct_avg"] = float(grp["second_half_win_pct"].mean())
        rows.append(row)

    wide = pd.DataFrame(rows)
    ordered_cols = ["league", "season", "team"]
    for seed in seeds:
        ordered_cols.append(f"first_half_win_pct_seed_{int(seed)}")
        ordered_cols.append(f"second_half_win_pct_seed_{int(seed)}")
    ordered_cols.extend(["first_half_win_pct_avg", "second_half_win_pct_avg"])
    return wide[ordered_cols].sort_values(["league", "season", "team"]).reset_index(drop=True)


def save_league_avg_plots(all_seed_df: pd.DataFrame) -> None:
    """Create one scatter plot per league using the averaged win percentages."""
    if all_seed_df.empty:
        return

    for league, grp in all_seed_df.groupby("league"):
        if grp.empty:
            continue
        fig, ax = plt.subplots(figsize=(6, 6))
        sns.scatterplot(
            data=grp,
            x="first_half_win_pct_avg",
            y="second_half_win_pct_avg",
            ax=ax,
        )
        ax.plot([0, 1], [0, 1], color="black", linestyle="--", linewidth=1)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("First-Half Win % (avg)")
        ax.set_ylabel("Second-Half Win % (avg)")
        ax.set_title(f"{league} Avg First vs Second Half Win%")
        fig.tight_layout()
        slug = league.lower().replace(" ", "_")
        fig.savefig(CORR_OUTPUT_DIR / f"{slug}_first_second_win_pct_avg.png", dpi=300)
        plt.close(fig)


def generate_correlation_outputs(league_dfs: Dict[str, pd.DataFrame]) -> None:
    """Replicate the correlation bundle for the goals-based simulations."""
    CORR_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    per_seed_frames = []

    for seed_idx in range(1, NUM_SIM_RUNS + 1):
        for key, df in league_dfs.items():
            league_pretty = LEAGUES[key].pretty
            halves = build_team_halves(df, seed_idx, league_pretty)
            if halves.empty:
                continue
            per_seed_frames.append(halves)

    if not per_seed_frames:
        return

    combined_all = pd.concat(per_seed_frames, ignore_index=True)
    wide_df = reshape_halves_by_seed(combined_all)
    wide_df.to_csv(CORR_OUTPUT_DIR / "first_second_win_pct_all_seeds.csv", index=False)
    save_league_avg_plots(wide_df)

    overall_df, seasonal_df = correlation_summaries(combined_all)
    overall_df.to_csv(CORR_OUTPUT_DIR / "spearman_first_second_by_league.csv", index=False)
    seasonal_df.to_csv(
        CORR_OUTPUT_DIR / "spearman_first_second_correlations_by_league_season.csv",
        index=False,
    )


# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------

def main() -> None:
    GOAL_SIM_DIR.mkdir(parents=True, exist_ok=True)
    league_match_data: Dict[str, pd.DataFrame] = {}
    for key, league in LEAGUES.items():
        league_match_data[key] = rebuild_simulation_files(league)

    generate_upset_outputs(league_match_data)
    generate_correlation_outputs(league_match_data)


if __name__ == "__main__":
    main()
