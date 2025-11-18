# About this directory: `data/european_soccer_leagues/pure_luck_goals_based/`

## Purpose

This folder contains the **goals-based pure luck simulations** for the four major European soccer leagues.  
Unlike the result-based model (which uses only win/draw/loss probabilities), this model simulates **full match scorelines** using *empirical home and away goal distributions* derived directly from the real match data.

This provides a more realistic “random world,” where:
- goals are sampled from the **true per-season scoring tendencies**  
- match results are then derived from those random goals  
- the process is repeated across **10 independent simulation seeds**

These datasets serve as the **luck baseline** for:
- upset frequency (goals-based version)  
- first–second half correlation decomposition  
- win-percentage dispersion decomposition  

---

## How the empirical-goals pure luck model works

This folder is produced using the following steps (implemented in  
[`simulate_goals_empirical.ipynb`](./simulate_goals_empirical.ipynb)):

---

### **1. Build per-season empirical goal distributions**

Using the real match data from:

[`data/european_soccer_leagues/actual/`](../actual/)

For each **season**, we compute:
- frequency distribution of home goals scored  
- frequency distribution of away goals scored  
- normalized probability mass functions

These become the probability distributions from which simulated matches will sample goals.

**Example:**

| Season | Possible Goals | Home Probabilities | Away Probabilities |
|--------|----------------|-------------------|--------------------|
| 2008 | 0–5 | [0.21, 0.35, 0.28, 0.12, ...] | [0.33, 0.29, 0.25, ...] |

---

### **2. Simulate match scorelines from empirical distributions**

For each match:
1. Identify its season  
2. Sample *home goals* from that season’s empirical home goal pmf  
3. Sample *away goals* from the season’s empirical away goal pmf  
4. Convert goals → result (+1 = win, 0 = draw, −1 = loss)  
5. Convert result → points (3/1/0)

This produces a full simulated match dataset with realistic-but-random scores.

---

### **3. Build simulated standings for each seed**

For each seed, we:
- accumulate team points  
- calculate goals for/against, goal difference  
- sort teams by points → goal diff → goals for → alphabetical  
- assign simulated league rank

---

### **4. Run 10 independent simulations**

Each league is simulated for 10 seeds, producing:
- 10 match-level simulations  
- 10 standings tables per league  

These reduce statistical noise and provide a stable baseline for skill–luck decomposition.

---

## Files in this folder

### **1. Simulated match datasets (per league)**

Examples:
- `bundesliga_simulated_matches_all_seeds.csv`  
- `la_liga_simulated_matches_all_seasons.csv`  
- `premier_league_simulated_matches_all_seeds.csv`  
- `serie_a_simulated_matches_all_seasons.csv`

These contain **every match** for every season with 10 simulated goal-based outcomes.

**Schema:**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `date` | Match date |
| `home_team` | Home team code |
| `away_team` | Away team code |
| `true_home_team_result` | Real result (+1/0/−1) |
| `simulated_home_team_result_seed_1` → `seed_10` | Simulated outcomes from goal sampling |
| `hometeamgoals` / `awayteamgoals` | Simulated goals (varies per seed if expanded) |

(Exact columns vary depending on preprocessing).

---

### **2. Simulated standings datasets (per league)**

Examples:
- `bundesliga_simulated_standings_all_seasons.csv`  
- `la_liga_simulated_standings_all_seasons.csv`  
- `premier_league_simulated_standings_all_seasons.csv`  
- `serie_a_simulated_standings_all_seasons.csv`  

Each file aggregates simulation results into full league tables.

**Schema:**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `team` | Team code |
| `rank` | Simulated final standing |
| `simulation_seed` | Seed index (1–10) |

---

### **3. Combined multi-league file**

- `pure_luck_goals_all_leagues_combined.csv`

A concatenated version of all simulated match data across the four leagues.

---

### **4. Supporting notebook**

- `simulate_goals_empirical.ipynb`

This notebook contains:
- code that builds empirical distributions  
- code that simulates goals for each match  
- code that reconstructs standings  
- the batching process for 10 seeds  
- file export logic  

This notebook is required for full reproducibility.

---

## Relationship to other folders

- **Actual data**  
  [`../actual/`](../actual/)  
  → Real matches and standings (baseline for empirical distributions)

- **Pure luck (results-based)**  
  [`../pure_luck_result_based/`](../pure_luck_result_based/)  
  → Random outcomes based only on win/draw/loss probabilities

- **Pure skill**  
  [`../pure_skill/`](../pure_skill/)  
  → Deterministic outcomes: stronger team always wins

---

## Summary

This folder contains the **goal-sampled pure luck simulations**, including:
- 10 independent goal-based simulations per match  
- per-season empirical goal distributions  
- simulated goallines and league tables  
- combined multi-league outputs  
- original simulation code for reproducibility  