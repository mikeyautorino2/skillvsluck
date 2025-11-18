# Skill–Luck Decomposition  
`output/european_soccer_leagues/skill_luck_decomposition/`

## Overview

This directory contains **three decomposition analyses** that quantify how much of each league’s behavior can be attributed to **skill** versus **luck**:

- **Upset Frequency decomposition**
- **Correlation (First-half vs Second-half) decomposition**
- **Dispersion decomposition**

For each metric, the directory includes:

- **One CSV file** containing the final decomposition values  
- **One Jupyter Notebook** showing the full computation pipeline  

Together, these provide a unified skill–luck framework across all four major European leagues.

---

## Methodology Summary

Each decomposition compares the *actual* league metric to three simulated benchmark worlds:

1. **Pure Skill Model**  
   The stronger team always wins (deterministic).

2. **Pure Luck – Result-Based Model**  
   Outcomes drawn randomly using real home/draw/away rates.

3. **Pure Luck – Goals-Based Model**  
   Goals generated from league-wide scoring distributions.

For each season and metric, we compute:

- The actual league value  
- The average across 10 result-based luck simulations  
- The average across 10 goals-based luck simulations  

Then we form **Q-values**, which measure how close the real world is to skill or luck.

---

## Q-Value Definitions

For each metric \( M \):

- \( M_{\text{actual}} \) — real-world value  
- \( M_{\text{skill}} \) — pure skill model value  
- \( M_{\text{luck}} \) — pure luck model value (averaged over seeds)

Two Q-values are reported:

### **Q-results**
Using result-based luck:
\[
Q_{\text{results}} = 
\frac{M_{\text{actual}} - M_{\text{luck-results}}}
     {M_{\text{skill}} - M_{\text{luck-results}}}
\]

### **Q-goals**
Using goals-based luck:
\[
Q_{\text{goals}} = 
\frac{M_{\text{actual}} - M_{\text{luck-goals}}}
     {M_{\text{skill}} - M_{\text{luck-goals}}}
\]

Interpretation:
- Values near **1** → close to pure **skill**
- Values near **0** → close to pure **luck**
- Intermediate values → a mix of both

---

# File Descriptions

The folder contains **three pairs** of files:

```text
correlations_skill_luck_decomposition.csv
correlations_skill_luck.ipynb

dispersion_skill_luck_decomposition.csv
dispersion_skill_luck_decomposition.ipynb

upset_frequency_skill_luck_decomposition.csv
upset_frequency_skill_luck.ipynb
```

Below are the schemas and explanations for each.

---

# 1. Correlation Skill–Luck Decomposition

### **File:**
`correlations_skill_luck_decomposition.csv`

### **Purpose**
Measures how much **first-half vs second-half win-percentage correlation** is driven by inherent team strength vs randomness.

### **Schema**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `season` | Season identifier |
| `n_teams` | Number of teams used in the correlation |
| `spearman_r_actual` | Actual Spearman correlation between halves |
| `spearman_r_skill` | Correlation under the pure skill model |
| `spearman_r_luck_results_avg` | Average correlation under result-based luck |
| `spearman_r_luck_goals_avg` | Average correlation under goals-based luck |
| `q_results` | Q-value using result-based simulations |
| `q_goals` | Q-value using goals-based simulations |

---

# 2. Dispersion Skill–Luck Decomposition

### **File:**
`dispersion_skill_luck_decomposition.csv`

### **Purpose**
Assesses how much of the **spread of win percentages** within a league is due to skill vs randomness.

### **Schema**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `num_data_points` | Number of team-season observations |
| `std_win_pct_actual` | Dispersion of actual win percentages |
| `std_win_pct_skill` | Dispersion under pure skill |
| `std_win_pct_luck_results_avg` | Average dispersion under result-based luck |
| `std_win_pct_luck_goals_avg` | Average dispersion under goals-based luck |
| `q_results` | Q-value using result-based luck |
| `q_goals` | Q-value using goals-based luck |

---

# 3. Upset Frequency Skill–Luck Decomposition

### **File:**
`upset_frequency_skill_luck_decomposition.csv`

### **Purpose**
Decomposes the frequency of upsets (lower-ranked team beating higher-ranked team).

### **Schema**

| Column | Meaning |
|--------|---------|
| `league` | League name |
| `season` | Season identifier |
| `upset_frequency_actual` | Actual upset frequency |
| `upset_frequency_skill` | Upset frequency under pure skill (typically 0) |
| `upset_frequency_luck_results_avg` | Average upset frequency under result-based luck |
| `upset_frequency_luck_goals_avg` | Average upset frequency under goals-based luck |
| `q_results` | Q-value using result-based luck |
| `q_goals` | Q-value using goals-based luck |

---

# Summary

This folder provides the decomposition of **skill vs luck** for the three core metrics of league behavior:

- **Consistency (correlation)**
- **Parity (dispersion)**
- **Unpredictability (upsets)**

Each CSV gives season-by-season numbers and Q-values, allowing precise comparison of:

- How much randomness drives each metric  
- Whether leagues behave closer to pure skill or pure chance  
- Differences across the four leagues  
- Differences across luck models (goals vs results)  

These are final, ready-to-use outputs for analysis, visualization, and reporting within the Skill-vs-Luck project.
