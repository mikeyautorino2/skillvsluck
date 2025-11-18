# About this directory: 
`data/european_soccer_leagues/pure_luck_result_based/`

## Purpose

This folder contains the **result-based pure luck simulations** for the four major European soccer leagues.  
These simulations are designed to model a world in which **match outcomes are determined entirely by randomness**, while preserving each league’s historical **home / draw / away outcome frequencies**.

Each match is simulated **10 independent times**, producing 10 “seeds” to reduce variance and improve the stability of downstream skill–luck decomposition metrics.

These files form the **luck baseline** for:
- upset-frequency decomposition  
- correlation decomposition  
- dispersion (win-percentage spread) decomposition  

---

## How the pure-luck (result-based) model works

For every match in the real dataset (`actual/`), we build a league-level outcome model and then simulate results from it.

### **1. Compute league-level outcome frequencies**

We first compute summary statistics per league and store them in:  
[`data/european_soccer_leagues/home_advantage_by_league.csv`](../home_advantage_by_league.csv)

Each row in that file contains:

- `matches_total` — total number of matches in that league  
- `home_wins` — number of home wins  
- `draws` — number of draws  
- `away_wins` — number of away wins  
- `home_win_with_draws` — a “home-equivalent” index, computed as  
  `home_equiv = home_wins + draws / 3`  
- `home_win_pct` — `100 * home_equiv / matches_total`, interpreted as a **home-favourability index** (draws counted as one-third of a home win)

Example rows:

| league         | matches_total | home_wins | draws | away_wins | home_win_pct |
|----------------|---------------|-----------|-------|-----------|--------------|
| bundesliga     | 6426          | …         | …     | …         | 53.17%       |
| la_liga        | 8740          | …         | …     | …         | 55.35%       |
| premier_league | 8360          | …         | …     | …         | 53.85%       |
| serie_a        | 8518          | …         | …     | …         | 53.66%       |

**For the simulations, we only use the raw counts** `home_wins`, `draws`, and `away_wins` to derive empirical probabilities:

\[
p_\text{home} = \frac{\text{home\_wins}}{\text{matches\_total}}, \quad
p_\text{draw} = \frac{\text{draws}}{\text{matches\_total}}, \quad
p_\text{away} = \frac{\text{away\_wins}}{\text{matches\_total}}
\]

These probabilities are then normalised (as a safety step) so that  
`p_home + p_draw + p_away = 1`.

### **2. How match results are simulated**

For each league:

1. We compute a **single set of league-wide probabilities** `(p_home, p_draw, p_away)` from the actual data, as above.
2. For every match in that league, and for each simulation seed (1–10), we draw a random outcome from:

   - `+1` with probability `p_home`  (home win)  
   - `0`  with probability `p_draw`  (draw)  
   - `-1` with probability `p_away` (away win)

These probabilities are **constant across all matches and seasons within a league**, and do **not** depend on which teams are playing, their standings, or betting odds.  

In other words:

> The simulation replicates each league’s **overall H/D/A frequencies**,  
> but assumes that individual matches are otherwise random, independent draws from that league-level distribution.

### **3. Result encoding**

Simulated outcomes use the same encoding as the actual data:

- `+1` — Home win  
- `0`  — Draw  
- `-1` — Home loss  

The column names follow the pattern:
- `simulated_home_team_result_seed_1`, …, `simulated_home_team_result_seed_10`

### **4. Reconstruction of simulated standings**

For each seed, we recompute standard league-table statistics by treating the simulated outcomes as if they were real:

- points (3 for win, 1 for draw, 0 for loss)  
- goal difference (using actual goals if kept, or derived when needed)  
- goals for / against  
- final league rank (per season, per seed)

These are then merged into a **standings** dataset, producing columns such as:  
`simulated_rank_1`, `simulated_rank_2`, …, `simulated_rank_10` alongside the `actual_rank`.

### **5. Output**

All simulated matches and standings are stored **per league** as CSV files.  
A combined file for all leagues is also generated for cross-league analysis.

Relevant Jupyter notebooks used to generate the files are included for reproducibility.

---

## Files in this folder

### **1. Simulated match-level files (per league)**

Examples:
- `bundesliga_simulated_matches_all_seeds.csv`
- `la_liga_simulated_matches_all_seeds.csv`
- `premier_league_simulated_matches_all_seeds.csv`
- `serie_a_simulated_matches_all_seeds.csv`

Each file contains **every match for every season** of that league, with 10 pure-luck simulations.

**Schema (core columns):**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `date` | Match date |
| `home_team` | Home team code (standardised) |
| `away_team` | Away team code |
| `true_home_team_result` | Actual result (+1/0/−1) |
| `simulated_home_team_result_seed_1` → `simulated_home_team_result_seed_10` | Result-based pure-luck outcomes for each seed |

These are used to construct:
- pure-luck standings  
- pure-luck upset frequencies  
- correlation comparisons  

---

### **2. Simulated standings files (per league)**

Examples:
- `bundesliga_simulated_standings_all_seasons.csv`
- `la_liga_simulated_standings_all_seasons.csv`
- `premier_league_simulated_standings_all_seasons.csv`
- `serie_a_simulated_standings_all_seasons.csv`

Each file contains **one row per team per season**, listing both real and simulated rankings.

**Schema (core columns):**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `team` | Team code |
| `actual_rank` | Real-world finishing position |
| `simulated_rank_1` → `simulated_rank_10` | Pure-luck rank under each simulation seed |

These are used for:
- dispersion (win-percentage spread) under luck  
- ranking stability checks  
- skill–luck decomposition  

---

### **3. Combined league file**

- `all_leagues_combined.csv`  

This file concatenates all simulated match-level data across leagues into a single dataset, which is convenient for comparisons and multi-league plots.

---

### **4. Supporting notebooks**

- `simulated_leagues.ipynb`  
- `simulated_leagues_standings.ipynb`  

These notebooks contain:
- the core simulation logic (reading actual data, computing H/D/A probabilities, simulating outcomes)  
- league-table reconstruction code  
- reproducible steps for regenerating all CSV files in this directory  

---

## Relationship to other folders

- **Actual data**  
  [`data/european_soccer_leagues/actual/`](../actual/)  
  → Real match results and final standings (baseline “real world”).

- **Pure luck (goals-based)**  
  [`data/european_soccer_leagues/pure_luck_goals_based/`](../pure_luck_goals_based/)  
  → Alternative luck model which resamples **goals** from empirical per-season goal distributions rather than directly resampling match outcomes.

- **Pure skill**  
  [`data/european_soccer_leagues/pure_skill/`](../pure_skill/)  
  → Deterministic model where the stronger team in the actual standings always wins in the simulation.

---

## Summary

This directory provides the **result-based pure luck simulation dataset**, including:

- 10 independent outcome-only simulations per match, per league  
- league-level H/D/A frequencies preserved but team identities ignored  
- simulated match-level datasets  
- simulated standings datasets  
- combined multi-league outputs and reproducible notebooks  

It serves as one of the **three core baselines** (actual, pure-skill, pure-luck) used in the Skill-vs-Luck analysis