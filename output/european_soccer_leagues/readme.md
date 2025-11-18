# European Soccer Leagues — Output Summary  
`output/european_soccer_leagues/`

## Overview

This directory contains **all computed outputs** for the four major European soccer leagues across three key metrics:

1. **Correlations**  
   (first-half vs second-half win-percentage consistency)

2. **Dispersion**  
   (spread of win percentages within a league)

3. **Upset Frequency**  
   (rate at which weaker teams beat stronger teams)

For each metric, results are produced under four different categories:

- **Actual**  
  The real historical data.

- **Pure Luck — Results-Based**  
  Random match outcomes using empirical H/D/A probabilities.

- **Pure Luck — Goals-Based**  
  Random goals scored using season-level scoring distributions.

- **Pure Skill**  
  The stronger team always wins (deterministic).

Each metric’s folder contains:
- CSV output files  
- Plots for every league  
- The Jupyter notebook used to generate the outputs

All code needed for replication is included in the subfolders.

---

## Folder Structure

```text
correlations/
dispersion/
upset_frequency/
skill_luck_decomposition/
```

Each of the first three folders—**correlations**, **dispersion**, and **upset_frequency**—has the following standardized subfolders:

```text
actual/
pure_luck_results_based/
pure_luck_goals_based/
pure_skill/
```

Each subfolder contains identical file types:

- **Metric-specific summary CSVs**
- **Per-league or all-league visualizations (PNGs)**
- **Jupyter notebook with full computation pipeline**

This consistent structure allows direct comparison of:
- Real data vs luck simulations  
- Results-based vs goals-based luck models  
- Luck baselines vs deterministic skill model  

---

## Use of 10 Simulation Seeds

Both **luck-based worlds** (results-based and goals-based) were simulated **10 separate times** per league-season.  
Because random draws introduce variance, we compute:

- **Per-seed outputs**
- **Averaged values across all 10 seeds**, used in final analyses

These averaged outputs form the inputs to the **skill–luck decomposition**.

---

# Metric Folders

## 1. correlations/

Contains:
- First-half vs second-half win-percentage data
- Per-league correlation plots
- League-season Spearman correlations
- Supporting notebooks

---

## 2. dispersion/

Contains:
- Standard deviation of team win percentages
- League-level dispersion comparisons
- Visualizations of spread under skill vs luck vs actual
- Supporting notebooks

---

## 3. upset_frequency/

Contains:
- Season and league upset rates
- Definitions based on rank differences
- Per-league boxplots, line plots, and bar charts
- Supporting notebooks

---

# Skill–Luck Decomposition

## Folder: `skill_luck_decomposition/`

This folder combines **all three metrics** into a unified framework that measures:

- How close actual leagues are to the pure skill model  
- How close they are to luck  
- Differences across:
  - Skill baseline  
  - Result-based luck  
  - Goals-based luck  

---

# Summary

This directory provides the full analytical output for the European soccer component of the Skill-vs-Luck project.  
It includes:

- Standardized metric outputs across four worlds  
- Plots and summaries for each league  
- Reproducible notebooks  
- A final integrated skill–luck decomposition

All results are computed consistently, fully documented, and ready for downstream analysis, presentation, or publication.
