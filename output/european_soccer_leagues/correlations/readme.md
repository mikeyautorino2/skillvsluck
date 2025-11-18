# About this directory: 
`output/european_soccer_leagues/correlations/`

## Purpose

This folder contains the **first–half vs second–half win-percentage correlation analysis** for:

- **Actual** match results  
- **Pure luck (goals-based)** simulations  
- **Pure luck (results-based)** simulations  
- **Pure skill** simulations  

The goal is to measure how predictable team performance is within a season by asking:

> **Do teams that perform well in the first half of a season also perform well in the second half?**

We compute this using **Spearman rank correlation**, both:
- **per season, per league**, and  
- **overall across all seasons**.

All CSVs and PNGs in this folder support correlation-based components of the **Skill vs Luck** decomposition.

---

## Folder Structure

```text
correlations/
│
├── actual/
├── pure_luck_goals_based/
├── pure_luck_result_based/
└── pure_skill/
```

Each subfolder contains the same outputs:

1. `first_second_win_pct.csv`  
2. `spearman_first_second_by_league_season.csv`  
3. `spearman_first_second_correlations_by_league.csv`  
4. Four league-specific scatterplot PNGs  
   (e.g., `bundesliga_correlation.png`, `la_liga_correlation.png`, etc.)

---

## 1. `first_second_win_pct.csv` — Win Percentage Split (First Half vs Second Half)

This file contains, for every **team–season**, the team's:

- **Win % in the first half**
- **Win % in the second half**
- **League and season identifiers**

### Schema

| Column | Description |
|--------|-------------|
| `team` | Team identifier (standardized code) |
| `season` | Season year |
| `first_half_win_pct` | Win percentage in first half |
| `second_half_win_pct` | Win percentage in second half |
| `league` | League name |

---

## 2. `spearman_first_second_by_league_season.csv` — Per-Season Correlation

For each **league × season**, we compute:

- number of teams  
- Spearman correlation between first-half and second-half win rates  
- p-value  

### Schema

| Column | Description |
|--------|-------------|
| `league` | League name |
| `season` | Season year |
| `n_teams` | Number of participating teams |
| `spearman_r` | Spearman rank correlation |
| `spearman_p` | p-value |

---

## 3. `spearman_first_second_correlations_by_league.csv` — Overall League Correlation

This file aggregates all seasons into a **single Spearman correlation per league**.

### Schema

| Column | Description |
|--------|-------------|
| `league` | League name |
| `spearman_r` | Correlation coefficient |
| `spearman_p` | Significance p-value |

---

## 4. Correlation Scatterplots (PNG)

Each subfolder contains **four** PNG scatterplots (one per league), e.g.:

- `bundesliga_correlation.png`
- `la_liga_correlation.png`
- `premier_league_correlation.png`
- `serie_a_correlation.png`

Plots show:

- **X-axis:** First-half win percentage  
- **Y-axis:** Second-half win percentage  
- **Red dashed line:** reference line (y = x)  
- **Title:** league name + Spearman correlation  

These visualizations illustrate performance consistency within a season.

---

## Relationship Between the Four Subfolders

| Folder | Meaning |
|--------|---------|
| **actual** | Real match data, actual consistency patterns |
| **pure_luck_goals_based** | Consistency if goals are drawn independently from empirical goal distributions |
| **pure_luck_result_based** | Consistency if match *results* (H/D/A) are randomly drawn based on league-wise outcome rates |
| **pure_skill** | Consistency if stronger teams always win (maximal predictive consistency) |

Together, these allow comparisons of:

- True seasonal stability  
- Stability under randomness  
- Stability under pure skill  

---

## Summary

This directory contains all correlation-related outputs for the Skill-vs-Luck project, including:

- First/second-half win percentage splits  
- Season-by-season Spearman correlations  
- Overall league-level Spearman correlations  
- Scatterplot visualizations  
- Outputs for **actual, goals-based luck, results-based luck, and pure-skill models**

These results form the **correlation decomposition**, one of the three core components of the project.
