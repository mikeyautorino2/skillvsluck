# About this directory: `data/european_soccer_leagues/pure_skill/`

## Purpose

This folder contains the **pure-skill deterministic simulations** for the four major European soccer leagues.  
In this model, **match outcomes are determined entirely by team strength**, using the actual end-of-season rankings as a proxy for skill.

This simulation provides the **upper bound of predictability** in the skill–luck spectrum:
- **If skill alone decided every match**, these would be the outcomes.
- There is **no randomness** in this model.
- Stronger teams **always beat** weaker teams.

These files serve as the skill baseline for:
- upset-frequency decomposition  
- correlation decomposition  
- dispersion (win-percentage spread) decomposition  

---

## How the pure-skill model works

The pure-skill simulation uses two real datasets from [`../actual/`](../actual/):

1. **Match-level data**  
   (home team, away team, date, league, real result, etc.)

2. **End-of-season standings**  
   (team, season, points, rank, etc.)

The logic of the skill model is:

> **Whichever team had a better (numerically lower) real-world league rank in that season is assumed to be the stronger team.  
> The stronger team always wins.**

### Steps in the deterministic simulation

For every match in every league:

1. Identify:
   - `home_team`
   - `away_team`
   - the season they belong to

2. Look up both teams’ **actual end-of-season ranks** from the real standings dataset.

3. Apply the deterministic rule:
   - If `home_team_rank < away_team_rank` → home win (`+1`)  
   - Else → home loss (`−1`)  
   - Draws **do not exist** in this model

4. Record:
   - actual match result  
   - deterministic skill-based result

The output contains **one deterministic simulation per league** (no randomness → no seeds needed).

---

## Files in this folder

### **1. League-specific skill-based match files**

These files list the simulated deterministic outcome of every match:

- `bundesliga_skilled_matches.csv`  
- `la_liga_skilled_matches.csv`  
- `premier_league_skilled_matches.csv`  
- `serie_a_skilled_matches.csv`

**Schema:**

| Column | Description |
| --- | --- |
| `league` | League name |
| `season` | Season identifier |
| `date` | Match date |
| `home_team` | Home team |
| `away_team` | Away team |
| `actual_home_team_result` | Real result (+1/0/−1) |
| `skilled_league_home_team_result` | Deterministic result under pure skill (+1/−1) |

### Interpretation

- `+1` means the home team was the stronger team (lower rank).  
- `−1` means the away team was stronger based on actual standings.  
- No draws appear in this dataset.

---

### **2. Aggregate skill-based file**

- `skill_based_league.csv`  

This file is the concatenation of all league-level simulations.  
Useful for multi-league comparisons or analysis of global trends.

---

### **3. Supporting notebook**

- `skill_simulations.ipynb`

Contains the full, reproducible logic for:
- loading real match and standings data  
- applying the deterministic ranking-based outcome rule  
- generating all CSVs in this directory  

---

## Relationship to other folders

- **Actual data**  
  [`data/european_soccer_leagues/actual/`](../actual/)  
  → provides the real matches and real standings used to compute skill dominance

- **Pure luck (goals-based)**  
  [`data/european_soccer_leagues/pure_luck_goals_based/`](../pure_luck_goals_based/)  
  → luck model based on sampling goals from empirical distributions

- **Pure luck (results-based)**  
  [`data/european_soccer_leagues/pure_luck_result_based/`](../pure_luck_result_based/)  
  → luck model based solely on random match outcomes with home-bias strength

---

## Summary

This directory contains the **fully deterministic skill-only simulation** of European soccer leagues:

- Stronger (better-ranked) team always wins  
- No randomness  
- No draws  
- One deterministic simulation per match per league  
- Clean, reproducible CSV outputs for downstream analysis  