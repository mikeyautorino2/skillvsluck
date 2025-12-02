# About this directory: `data/european_soccer_leagues/`

## Purpose

This directory contains **all datasets** used in the Skill-vs-Luck analysis for the four major European soccer leagues:

- **Bundesliga (Germany)**
- **La Liga (Spain)**
- **Premier League (England)**
- **Serie A (Italy)**

It includes:
- cleaned real-world match & standings data  
- simulation outputs from three different models (pure skill, pure luck – goals, pure luck – results)  
- metadata files required for reliable multi-league analyses  

This folder acts as the **central data hub** for the entire project.

---

# 1. `actual/` — Cleaned real-world match & standings data

This folder contains **standardized historical datasets** for all leagues and seasons.

### Contents:
- `*_actual.csv` → match-level data  
- `*_standings_all_seasons.csv` → final league tables (points, wins, draws, goal difference, rank)

### Purpose:
Provides the **ground-truth baseline** for:
- computing home advantage  
- deriving empirical goal distributions  
- generating pure-skill rankings  
- measuring real upset frequencies and correlations  

All simulations in other folders depend on the data stored here.

---

# 2. `pure_luck_goals_based/` — Empirical goals-only randomness model

This folder implements a luck model in which **goal scoring is random**, but based entirely on **empirical season-level goal distributions**.

Process:
1. For each season, the real match data is used to estimate:
   - distribution of home goals
   - distribution of away goals
2. Each match is re-simulated 10 times by **sampling home and away goals independently**.  
3. Standings are recomputed from simulated results.

### Contents:
- `*_simulated_matches_all_seeds.csv`  
- `*_simulated_standings_all_seasons.csv`  
- `pure_luck_goals_all_leagues_combined.csv`  
- `simulate_goals_empirical.ipynb`  

### Purpose:
Represents a **luck world driven only by random goal scoring**.

---

# 3. `pure_luck_result_based/` — Result-only randomness using empirical H/D/A probabilities

This folder contains pure-luck simulations where **match outcomes (H/D/A)** are drawn randomly according to each league’s **empirical outcome frequencies**.

### How the probabilities are computed (corrected):

For each league:
- We count  
  - number of **home wins**  
  - number of **draws**  
  - number of **away wins**  
  directly from the actual match dataset.
- These raw counts are converted into probabilities:  
  - `p_home = home_wins / total_matches`  
  - `p_draw = draws / total_matches`  
  - `p_away = away_wins / total_matches`

**No weighting or reallocation of probabilities is done.  
Draw probability is not split.  
Away probability is not inferred.  
All three come directly from real historical frequencies.**

These probabilities are then used to simulate match outcomes for each league, 10 times per match.

### Contents:
- `*_simulated_matches_all_seeds.csv`  
- `*_simulated_standings_all_seasons.csv`  
- `all_leagues_combined.csv`  
- notebooks implementing the simulation  

### Purpose:
Provides the **outcome-only pure luck baseline**, driven by real H/D/A frequencies.

---

# 4. `pure_skill/` — Deterministic skill-only model

This folder contains simulations in a world with **no randomness whatsoever**.

Rule:
> The team with the better real-world end-of-season rank always wins.

Thus:
- no draws  
- weaker teams never beat stronger teams  

### Contents:
- `bundesliga_skilled_matches.csv`  
- `la_liga_skilled_matches.csv`  
- `premier_league_skilled_matches.csv`  
- `serie_a_skilled_matches.csv`  
- `skill_based_league.csv`  
- `skill_simulations.ipynb`

### Purpose:
Represents the **upper bound of predictability**—the “pure skill” extreme in the Skill-vs-Luck framework.

---

# 5. `source_data/` — Raw upstream snapshots

These are **minimally processed original data files**, included for traceability.

Purpose:
- audit trail  
- validation  
- complete reproducibility  

---

# 6. `master_team_names.csv` — Team standardization map

This file provides a **consistent naming scheme** across all datasets.

Example row:

| league | season | team_std | team_full        |
|--------|--------|----------|------------------|
| bundesliga | 2004 | BAY | Bayern Munich |

### Purpose:
- avoids merge errors from inconsistent team names  
- ensures clean cross-season and cross-league joins  

---

# 7. `home_advantage_by_league.csv` — League-level H/D/A summary

This file reports raw historical **home wins, draws, and away wins** for each league.  
It is generated from `actual/` and is used by the **result-based pure luck model**.

Columns include:
- total_matches  
- home_wins  
- draws  
- away_wins  
- computed home_win_pct (from raw counts)

### Purpose:
Provides the **empirical distribution of H/D/A outcomes** used to generate the result-based pure luck simulations.

---

## Summary

`data/european_soccer_leagues/` organizes all real and simulated datasets required for the Skill-vs-Luck study:

- **actual/** → ground-truth matches & standings  
- **pure_skill/** → deterministic skill-only universe  
- **pure_luck_result_based/** → randomness using empirical H/D/A frequencies  
- **pure_luck_goals_based/** → randomness based on empirical goal scoring distributions  
- **source_data/** → original upstream files  
- **master_team_names.csv** → unified naming reference  
- **home_advantage_by_league.csv** → raw H/D/A summary  

This directory underpins every computation and simulation in the project.
