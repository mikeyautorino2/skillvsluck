# Upset Frequency Analysis  
`output/european_soccer_leagues/upset_frequency/`

## Overview

This directory contains the **upset–frequency analysis outputs** for the four major European soccer leagues (Bundesliga, La Liga, Premier League, Serie A).  
The analysis is computed for:

- **Actual historical results**
- **Pure luck – goals-based model**
- **Pure luck – result-based model**
- **Pure skill model**

Each model appears as its own subfolder, containing the same set of summary CSV files and visualisations.

Upset frequency measures **how often weaker teams defeat stronger teams**, based on end-of-season standings.

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

Each subfolder includes:

- Two summary CSV files:
  - `season_upset_frequency_summary.csv`
  - `league_upset_frequency_summary.csv`
- Three visualisation PNGs:
  - Boxplot of upset frequency by league
  - Bar chart of overall upset frequency across leagues
  - Line plot of upset frequency by season for each league
- A notebook (`upset_frequency_plots.ipynb`) generating all outputs

---

## Summary CSV Files

### 1. `season_upset_frequency_summary.csv`

This file reports upset frequencies **season by season**, for each league.

**Schema:**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `season` | Season identifier |
| `total_matches` | Number of matches in that season |
| `total_upsets` | Total number of matches classified as upsets |
| `upset_frequency` | Share of matches in that season that were upsets |

This allows longitudinal comparison of upset rates across ~20 seasons.

---

### 2. `league_upset_frequency_summary.csv`

This file aggregates results across **all seasons** for each league.

**Schema:**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `total_matches` | Total number of matches across all seasons |
| `total_upsets` | Total number of upsets across all seasons |
| `upset_frequency` | Overall upset rate for the league |

These values provide the **average upset rate** for each league across ~20 years.

---

## Visualisations

Each subfolder contains three core visualisations:

### **1. Boxplot — upset frequency distribution (per league, across seasons)**  
Shows the season-to-season variation in upset rates.  
Useful for comparing the *spread* of unpredictability across leagues.

### **2. Bar chart — overall upset frequency (across all seasons)**  
Summarises each league’s long-run upset rate.  
Useful for comparing which leagues are more “upset-prone” on average.

### **3. Line plot — upset frequency over time (20-year trend)**  
Plots each league’s upset frequency season by season.  
Useful for detecting long-term changes in parity/unpredictability.

---

## Consistency Across Models

All four subfolders contain:

- The same CSV schemas  
- The same three plots  
- Upset frequencies computed using the same method  
- Differences arising only from the underlying model:

| Folder | Meaning |
|--------|---------|
| `actual` | True match outcomes |
| `pure_luck_goals_based` | Luck model based on goal distributions |
| `pure_luck_result_based` | Luck model based on outcome-probability simulation |
| `pure_skill` | Deterministic model where stronger team always wins |

This ensures **direct comparability** between actual football, pure randomness, and pure determinism.

---

## Summary

This folder provides a complete, model-consistent breakdown of upset rates in European football:

- Season-level and league-level CSV summaries  
- Three standard visualisations per model  
- Identical structure across *actual*, *pure luck (goals)*, *pure luck (results)*, and *pure skill*  
- Ready for downstream statistical and visual analysis  
