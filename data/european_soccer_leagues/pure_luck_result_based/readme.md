# About this directory: 
`data/european_soccer_leagues/pure_luck_result_based/`

## Purpose

This folder contains the **result-based pure luck simulations** for the four major European soccer leagues.  
These simulations are designed to model a world in which **match outcomes are determined entirely by randomness**, except that the model preserves each league’s historical **home-advantage rate**.

Each match is simulated **10 independent times**, producing 10 “seeds” to reduce variance and improve the stability of downstream skill–luck decomposition metrics.

These files form the **luck baseline** for:
- upset-frequency decomposition  
- correlation decomposition  
- dispersion (win-percentage spread) decomposition  

---

## How the pure-luck (result-based) model works

For every match in the real dataset (`actual/`):

### **1. Compute league-level home advantage**

We compute each league’s *home-advantage index*, stored in:  
[`data/european_soccer_leagues/home_advantage_by_league.csv`](../home_advantage_by_league.csv)

This is computed as:
home_equiv = home_wins + draws / 3
home_win_pct = home_equiv / 

This produces a **single scalar index** that measures how favourable the league historically is to home teams.

Example values:

| league | home_win_pct |
|--------|--------------|
| bundesliga | 53.17% |
| la_liga | 55.35% |
| premier_league | 53.85% |
| serie_a | 53.66% |

### **2. How match results are simulated**

The simulation does **not** use the historical probability of home wins, draws, and away wins.

Instead:

- The single scalar `home_win_pct` is used as a **home-bias strength parameter**.
- Draws and away wins are treated **symmetrically** relative to that bias.
- For each match, and for each simulation seed (1–10), an outcome (+1/0/−1) is drawn randomly using this biased process.

In simpler terms:  
> The simulation does *not* try to replicate true H/D/A frequencies.  
> It only ensures that leagues with higher home-advantage produce relatively more home-favoured results.

### **3. Result encoding**

Simulated outcomes use the same encoding as actual data:

- `+1` — Home win  
- `0` — Draw  
- `-1` — Home loss  

### **4. Reconstruction of simulated standings**

After each full-season simulation, we recompute:

- points  
- goal difference  
- goals for/against  
- final league rank  

This produces columns:  
`simulated_rank_1`, `simulated_rank_2`, … `simulated_rank_10`

### **5. Output**

All simulated matches and standings are stored per-league as CSV files.  
A combined file for all leagues is also generated.

Relevant Jupyter notebooks used to generate the files are included for reproducibility.

---

## Files in this folder

### **1. Simulated match-level files (per league)**

Examples:
- `bundesliga_simulated_matches_all_seeds.csv`
- `la_liga_simulated_matches_all_seeds.csv`
- `premier_league_simulated_matches_all_seeds.csv`
- `serie_a_simulated_matches_all_seeds.csv`

Each file contains **every match for every season**, with 10 simulated pure-luck outcomes.

**Schema:**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `date` | Match date |
| `home_team` | Home team code |
| `away_team` | Away team code |
| `true_home_team_result` | Actual result (+1/0/−1) |
| `simulated_home_team_result_seed_1` → `seed_10` | Result-based pure-luck outcomes |

These drive:
- baseline standings  
- pure-luck upset rate  
- correlation comparisons  

---

### **2. Simulated standings files (per league)**

Examples:
- `bundesliga_simulated_standings_all_seasons.csv`
- `la_liga_simulated_standings_all_seasons.csv`
- `premier_league_simulated_standings_all_seasons.csv`
- `serie_a_simulated_standings_all_seasons.csv`

Each file contains **one row per team per season**, listing both real and simulated ranks.

**Schema:**

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `team` | Team code |
| `actual_rank` | Real finishing position |
| `simulated_rank_1` → `simulated_rank_10` | Pure-luck ranking per seed |

Used for:
- dispersion decomposition  
- ranking stability checks  
- skill–luck decomposition  

---

### **3. Combined league file**

- `all_leagues_combined.csv`

This file concatenates the per-league simulation results for multi-league analysis.

---

### **4. Supporting notebooks**

- `simulated_leagues.ipynb`
- `simulated_leagues_standings.ipynb`

These notebooks contain:
- full simulation code  
- ranking reconstruction logic  
- reproducible generation steps  

---

## Relationship to other folders

- **Actual data**  
  [`data/european_soccer_leagues/actual/`](../actual/)  
  (true match results & standings)

- **Pure luck (goals-based)**  
  [`data/european_soccer_leagues/pure_luck_goals_based/`](../pure_luck_goals_based/)  
  (luck model using empirical season-level goal distributions)

- **Pure skill**  
  [`data/european_soccer_leagues/pure_skill/`](../pure_skill/)  
  (deterministic model where the stronger/seeded team always wins)

---

## Summary

This directory provides the **result-based pure luck simulation dataset**, including:

- 10 random outcome-only simulations per match  
- home-bias–preserving random result generator  
- simulated match data  
- simulated standings  
- combined output and reproducible notebooks  