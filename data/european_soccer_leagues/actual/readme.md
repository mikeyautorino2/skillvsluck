# About this directory: `data/european_soccer_leagues/actual/`

## Purpose

This folder contains the **cleaned, filtered, and standardized actual match + standings data** derived from the raw source data located in  
[`data/european_soccer_leagues/source_data/`](../source_data/).

All files here reflect **real historical matches** from the Bundesliga, La Liga, Premier League, and Serie A, with all irrelevant columns removed and all team names standardized.  
These clean files serve as the **baseline dataset** for every downstream analysis: correlations, upset frequency, dispersion metrics, and skill–luck decomposition.

---

## Files in this folder

### **1. League-level match files**

Examples:

- `bundesliga_actual.csv`  
- `la_liga_actual.csv`  
- `premier_league_actual.csv`  
- `serie_a_actual.csv`  

Each file contains **one row per match** using a simplified, analysis-ready schema:

| Column | Description |
| --- | --- |
| `league` | League identifier (bundesliga, la_liga, premier_league, serie_a) |
| `season` | Season (first year of season) |
| `date` | Match date (YYYY-MM-DD) |
| `home_team` | Home team (standardized code) |
| `away_team` | Away team (standardized code) |
| `hometeamgoals` | Full-time goals scored by home team |
| `awayteamgoals` | Full-time goals scored by away team |
| `hometeamresult` | +1 = home win, 0 = draw, −1 = home loss |
| `home_team_points` | Points awarded to home team |
| `away_team_points` | Points awarded to away team |
| `OddHome` | Bet365 home-win odds |
| `OddDraw` | Bet365 draw odds |
| `OddAway` | Bet365 away-win odds |

These files serve as the foundation for:

- upset frequency calculations  
- correlation computations  
- dispersion (win-percentage standard deviation)  
- skill–luck decomposition inputs  

---

### **2. League-level standings files**

- `bundesliga_standings_all_seasons.csv`  
- `la_liga_standings_all_seasons.csv`  
- `premier_league_standings_all_seasons.csv`  
- `serie_a_standings_all_seasons.csv`  

Each file provides **one row per (season, team)** summarizing end-of-season performance.

| Column | Description |
| --- | --- |
| `season` | Season identifier |
| `team_name` | Standardized 3-letter club code |
| `points` | Total points |
| `wins` | Wins |
| `draws` | Draws |
| `losses` | Losses |
| `gf` | Goals for |
| `ga` | Goals against |
| `gd` | Goal difference |
| `rank` | Final table position (1 = champion) |

Used for:

- upset frequencies calculations
- half-season correlations  
- dispersion analysis  
- baseline for comparing simulations  

---

### **3. Combined match file**

- `actual_combined_matches.csv`

This aggregates **all four leagues** into a single standardized dataset with identical schema.  
Useful for multi-league comparison plots or combined statistical analysis.

---

## How this data was produced

The pipeline that generated this folder follows these steps:

1. Load raw files from  
   [`data/european_soccer_leagues/source_data/`](../source_data/)

2. Filter to the four target leagues  
   (Bundesliga, La Liga, Premier League, Serie A)

3. Standardize team names using  
   `master_team_names.csv`

4. Remove unused fields from the raw dataset  
   (clusters, disciplinary data, corners, shots, bookmaker meta, etc.)

5. Parse and validate dates, seasons, match identifiers

6. Use match-level data to construct consistent season standings files

The result is a **fully reproducible, analysis-ready** dataset.

---

## Intended use within the project

This folder supplies the data for:

- upset-frequency analysis  
- first-half vs second-half correlations  
- dispersion metric (std dev of win percentage)  
- pure skill–luck decomposition  
- comparing real leagues to simulated leagues  
- cross-league aggregate statistics  

Every simulation folder (`pure_skill`, `pure_luck_goals_based`, `pure_luck_result_based`) is benchmarked against these files.

---

## Summary

This directory contains the cleaned, standardized **actual historical match + standings data** for Europe’s top four leagues.  
It forms the **baseline** for every metric in the Skill-vs-Luck project.