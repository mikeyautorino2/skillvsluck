"""
Build upset-frequency summaries for the pure-skill scenario.

This script reshapes the legacy CSV exports (`all_skill_*_upset_frequency.csv`)
into the same set of league/season summaries and plots that the other
correlation bundles expose.
"""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output" / "european_soccer_leagues" / "upset_frequency" / "pure_skill"
MPLCONFIG_DIR = REPO_ROOT / "output" / "european_soccer_leagues" / ".matplotlib"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

PALETTE = {
    "Premier League": "#1f77b4",
    "La Liga": "#ff7f0e",
    "Serie A": "#2ca02c",
    "Bundesliga": "#d62728",
}


def load_seasonal_source() -> pd.DataFrame:
    """Return the original per-season pure-skill upset results."""
    src = OUTPUT_DIR / "all_skill_seasonal_upset_frequency.csv"
    df = pd.read_csv(src)
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    df = df.rename(columns={"total_predictions": "total_matches"}).copy()
    df["season"] = df["season"].astype(int)
    df["total_matches"] = df["total_matches"].astype(int)
    df["total_upsets"] = df["total_upsets"].astype(float)
    df["upset_frequency"] = df["upset_frequency"].astype(float)
    return df[["league", "season", "total_matches", "total_upsets", "upset_frequency"]]


def build_league_summary(seasonal_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the per-league totals and format like the simulation outputs."""
    agg = (
        seasonal_df.groupby("league", as_index=False)
        .agg(
            total_matches=("total_matches", "sum"),
            total_upsets=("total_upsets", "sum"),
        )
        .sort_values("league")
    )
    agg["upset_frequency"] = agg["total_upsets"] / agg["total_matches"]
    agg["total_upsets_seed_1"] = agg["total_upsets"].astype(float)
    agg["upset_frequency_seed_1"] = agg["upset_frequency"].astype(float)
    agg["total_upsets_avg"] = agg["total_upsets_seed_1"]
    agg["upset_frequency_avg"] = agg["upset_frequency_seed_1"]
    return agg[
        [
            "league",
            "total_matches",
            "total_upsets_seed_1",
            "upset_frequency_seed_1",
            "total_upsets_avg",
            "upset_frequency_avg",
        ]
    ].reset_index(drop=True)


def build_season_summary(seasonal_df: pd.DataFrame) -> pd.DataFrame:
    """Map each row to the new schema with the avg/seed columns."""
    out = seasonal_df.copy()
    out["total_upsets_seed_1"] = out["total_upsets"]
    out["upset_frequency_seed_1"] = out["upset_frequency"]
    out["total_upsets_avg"] = out["total_upsets"]
    out["upset_frequency_avg"] = out["upset_frequency"]
    return out[
        [
            "league",
            "season",
            "total_matches",
            "total_upsets_seed_1",
            "upset_frequency_seed_1",
            "total_upsets_avg",
            "upset_frequency_avg",
        ]
    ].sort_values(["league", "season"]).reset_index(drop=True)


def save_plots(league_summary: pd.DataFrame, season_summary: pd.DataFrame) -> None:
    """Persist the average-based upset visuals for the pure-skill outputs."""
    if league_summary.empty or season_summary.empty:
        return

    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=league_summary,
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
    fig.savefig(OUTPUT_DIR / "upset_frequency_by_league_totals_avg.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6))
    sns.lineplot(
        data=season_summary,
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
    fig.savefig(OUTPUT_DIR / "upset_frequency_by_season_all_leagues_avg.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
        data=season_summary,
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
    fig.savefig(OUTPUT_DIR / "upset_frequency_boxplot_by_league_avg.png", dpi=300)
    plt.close(fig)


def main() -> None:
    season_df = load_seasonal_source()
    league_summary = build_league_summary(season_df)
    season_summary = build_season_summary(season_df)
    league_summary.to_csv(OUTPUT_DIR / "league_upset_frequency_summary_all_seeds.csv", index=False)
    season_summary.to_csv(OUTPUT_DIR / "season_upset_frequency_summary_all_seeds.csv", index=False)
    save_plots(league_summary, season_summary)


if __name__ == "__main__":
    main()
