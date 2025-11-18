# Dispersion Analysis  
`output/european_soccer_leagues/dispersion/`

## Overview

This directory contains the **dispersion analysis outputs** for the four major European soccer leagues (Bundesliga, La Liga, Premier League, Serie A).  
Dispersion measures the **spread in team performance within a league**, typically using the standard deviation of **final win percentages** or **total points**.

High dispersion → highly unequal league (big gap between top and bottom teams).  
Low dispersion → more parity (teams end closer together).

The analysis is computed for:

- **Actual league results**
- **Pure luck – goals-based simulation**
- **Pure luck – result-based simulation**
- **Pure skill model**

Each model appears as its own subfolder and contains **one dispersion output file**.

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

Each subfolder contains a **single CSV file** summarizing dispersion across all leagues and all seasons.

---

## Summary CSV Included in Each Subfolder

Each model’s subfolder contains one CSV. 

### **Schema**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `season` | Season identifier |
| `std_win_pct` or `std_points` | Dispersion within that season, computed from simulated or actual standings |
| `n_teams` | Number of teams used in computation |

### **Interpretation**

- `std_win_pct` measures the spread of team win-rates in that season.  
- Higher values → competitive imbalance  
- Lower values → more evenly matched teams  

The same structure is repeated in:

- `actual/` – dispersion from real leagues  
- `pure_luck_goals_based/` – dispersion under random scoring distributions  
- `pure_luck_result_based/` – dispersion under random match results  
- `pure_skill/` – dispersion when the stronger team always wins the matchup  

This allows **direct comparison** across all four models.

---

## Summary

This directory provides model-consistent dispersion metrics across 20 years of European soccer:

- One CSV per model  
- Comparisons across actual, luck-driven, and skill-driven worlds  
- Measures the competitive balance of each league  
- Supports downstream analysis of parity and predictability  