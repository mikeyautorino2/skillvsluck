# Code Directory 

## Purpose

This folder stores the code we wrote to process and analyze the data.

---

## Files in this folder

- `cleaning.ipynb` — Pull raw match/elo CSVs from the upstream GitHub project and standardize columns.
- `descriptive_statistics_new.ipynb` — Exploratory data analysis on the standardized match tables.
- `end_of_season_tables.ipynb` — Build prior-season standings tables (points, ranks, etc.) per league.
- `extract_teams.py` — Map full club names to short codes and export team-season lookup tables.
- `master_team_names_cleaning.ipynb` — Consolidate naming variations, enforce unique abbreviations, update `master_team_names.csv`.
- `seriea_cleaning.ipynb` — League-specific cleanup for Serie A before export to the processed folder.
- `upset_frequency.ipynb` — Compute league/season/team upset metrics using betting odds or standings predictors with draws worth 0.5 upsets.
- `correlations.ipynb` — Compare first-half vs second-half points/goals splits to quantify persistence.
- `simulated_leagues.ipynb` — Monte Carlo simulations to estimate upset likelihood under random draws vs strength-based outcomes.
- `recalculate_upsets.py` — Script version of the upset-frequency pipeline that regenerates CSVs and figures headlessly.

## In Depth Step by Step Walkthrough of Each Code File

### cleaning.ipynb
1. Download the upstream `Original_Matches.csv` / `Original_EloRatings.csv`.
2. Filter to the four target European leagues and rename columns into the unified schema.
3. Persist cleaned per-league tables to `csv/processed/`.

---

### descriptive_statistics_new.ipynb
1. Load each processed league table into pandas.
2. Generate distribution plots (goals, points, odds) and basic summary tables.
3. Export selected figures to `output/european_soccer/figures/descriptive_statistics/`.

---

### end_of_season_tables.ipynb
1. Aggregate match-level results into season-level standings (points, wins, draws, losses, goal stats).
2. Rank clubs within each league-season and compute tie-break columns.
3. Save per-league standings to `csv/auxiliary/*_standings_all_seasons.csv`.

---

### extract_teams.py
1. Read the processed match tables for each league.
2. Standardize club abbreviations via the `create_standardized_name` helper.
3. Emit `[league]_teams.csv` with season/team/abbreviation info (used by downstream analyses).

---

### master_team_names_cleaning.ipynb
1. Combine multiple team lists (processed matches, manual mappings).
2. Resolve duplicates or conflicting abbreviations.
3. Write the curated `master_team_names.csv` used by visualization layers.

---

### seriea_cleaning.ipynb
1. Apply Serie A–specific fixes (date parsing, name corrections).
2. Align schema to the shared processed format.
3. Overwrite `serie_a_std.csv` with the cleaned output.

---

### upset_frequency.ipynb
1. Define reusable predictors: season-ranking vs Bet365 odds.
2. Compute upset metrics where draws contribute 0.5 toward the upset tally.
3. Aggregate by league, season, and team for both predictors and emit plots/CSVs.
4. Produce comparison charts (line + box/whisker) for betting vs standings predictors.

---

### correlations.ipynb
1. Build first-half vs second-half splits for each team-season.
2. Calculate correlation coefficients to assess performance persistence.
3. Export the consolidated metrics to `csv/analysis/correlation_metrics.csv`.

---

