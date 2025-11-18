# About this directory: `data/european_soccer_leagues/`

## Purpose

This directory contains **all datasets** used in the Skill-vs-Luck analysis for the four major European soccer leagues:

- **Bundesliga (Germany)**
- **La Liga (Spain)**
- **Premier League (England)**
- **Serie A (Italy)**

The datasets here include:
- cleaned real-world match data  
- cleaned real-world standings  
- three separate simulation models (pure luck – goals, pure luck – results, pure skill)  
- reference metadata needed for consistent analysis  

This folder is the **central data hub** of the project.

---

## Folder Structure Overview

data/
└── european_soccer_leagues/
├── actual/
├── pure_luck_goals_based/
├── pure_luck_result_based/
├── pure_skill/
├── source_data/
├── home_advantage_by_league.csv
├── master_team_names.csv
└── readme.md (this file)

---

# 1. `actual/` — Cleaned real-world match & standings data

This folder contains the **official match results and standings** for all leagues and seasons included in the analysis.

### Contents include:

- `*_actual.csv`  
  → cleaned, standardized match-level data  
- `*_standings_all_seasons.csv`  
  → season-by-season league tables (points, wins, draws, goal difference, rank)

### Purpose

This is the **baseline dataset** from which:
- home advantage is computed  
- empirical goal distributions are learned  
- pure-skill rankings are taken  
- real upset frequencies and correlations are measured  

All simulations in other folders depend on the data stored here.

---

# 2. `pure_luck_goals_based/` — Empirical goals-only randomness model

This folder implements a **pure luck model based on goal scoring distributions**.

For each league:
1. The real dataset is used to learn the **empirical distribution of goals scored** per season.  
2. Each match is re-simulated 10 times by **sampling home and away goals independently**.  
3. Standings are recomputed for each simulation seed.  

### Files include:
- `*_simulated_matches_all_seeds.csv`  
- `*_simulated_standings_all_seasons.csv`  
- `pure_luck_goals_all_leagues_combined.csv`  
- `simulate_goals_empirical.ipynb`  

### Purpose

Provides the **luck baseline where randomness emerges from goal scoring volatility**, not from direct match-result sampling.

---

# 3. `pure_luck_result_based/` — Result-only randomness model with home advantage

This folder implements the pure luck model where **match outcomes are drawn randomly**, but each league’s **empirical home advantage** is preserved.

For every match:
- Home win probability = historical `home_win_with_draws / matches_total`  
- Remaining probability is split between draw and away win  
- 10 simulation seeds are run to smooth variance  
- Standings are rebuilt for every seed  

### Files include:
- `*_simulated_matches_all_seeds.csv`  
- `*_simulated_standings_all_seasons.csv`  
- `all_leagues_combined.csv`  
- the notebooks that generated these outputs  

### Purpose

Provides the **pure-luck alternative** where **only outcomes (H/D/A)** are simulated, not goals.

---

# 4. `pure_skill/` — Deterministic skill-only model

This folder contains simulations in a world where **skill fully determines every match**.

Rule:
> The team with the better real-world **end-of-season rank** always wins.

- No randomness  
- No draws  
- Stronger team always defeats weaker team  

### Files include:
- `bundesliga_skilled_matches.csv`  
- `la_liga_skilled_matches.csv`  
- `premier_league_skilled_matches.csv`  
- `serie_a_skilled_matches.csv`  
- `skill_based_league.csv`  
- `skill_simulations.ipynb`  

### Purpose

Provides the **upper bound of predictability**, forming the "skill-only" extreme of the Skill-vs-Luck framework.

---

# 5. `source_data/` — Raw upstream data snapshots

This folder stores **minimally processed** or original datasets used for:
- cross-checking  
- validation  
- reproducibility  

### Files include:
- `Original_Matches.csv`  
- `Original_EloRatings.csv`  
- `readme.md` describing the raw dataset fields  

### Purpose

Ensures that the project can always trace results back to the **true source dataset**, mirroring an industry-standard reproducibility pipeline.

---

# 6. `master_team_names.csv` — Team name standardization map

This file is a **reference mapping** used throughout the project to ensure consistent team identifiers across seasons and leagues.

### Example rows:

| league | season | team_std | team_full        |
|--------|--------|----------|------------------|
| bundesliga | 2004 | BAY | Bayern Munich |
| bundesliga | 2004 | BIE | Bielefeld |
| bundesliga | 2004 | BOC | Bochum |
| bundesliga | 2004 | DOR | Dortmund |

### Purpose

- Enforces a unified naming scheme (`team_std`) across raw, actual, and simulated datasets  
- Prevents mismatched merges caused by inconsistent naming conventions  
- Critical for multi-season and multi-league joins  

---

# 7. `home_advantage_by_league.csv` — Empirical home advantage benchmark

This file summarizes the **historical home bias** of each league.

It is used **only** by the result-based pure luck model in `pure_luck_result_based/`.

### Columns include:
- total matches  
- home wins  
- draws  
- away wins  
- home-win-equivalent metric (H + ⅓·D)  
- home win %  

### Purpose

This is the **only non-random bias** preserved in the result-based simulation framework.

---

## Summary

The `european_soccer_leagues/` directory organizes all real and simulated data needed for the Skill-vs-Luck decomposition into a clean, reproducible hierarchy:

- **actual/** → real-world matches and standings  
- **pure_skill/** → deterministic skill-only world  
- **pure_luck_result_based/** → random outcomes with home advantage  
- **pure_luck_goals_based/** → random goals sampled from empirical distributions  
- **source_data/** → original raw datasets  
- **master_team_names.csv** → consistent team naming  
- **home_advantage_by_league.csv** → structural bias preserved in result-based luck model  

This folder underpins the entire analysis pipeline.

