# European Soccer Data – Descriptive Statistics

This report presents descriptive statistics for European soccer match data across four major leagues:
- **Premier League** (England)  
- **Serie A** (Italy)  
- **Bundesliga** (Germany)  
- **La Liga** (Spain)

---

## Dataset Overview
The analysis covers **34,952 matches** across the four leagues from 2000–2024:  
- **Time span**: Seasons 2000–2024  
- **Odds data availability**: 98.9% of matches  
- **Countries represented**: England, Italy, Germany, Spain

### League Match Counts
- **Premier League**: 9,410 matches  
- **Serie A**: 9,012 matches  
- **Bundesliga**: 7,522 matches  
- **La Liga**: 9,008 matches  

---

## 1. Match Results

### Result Distribution by League

| League | Total Matches | Home Wins (%) | Draws (%) | Away Wins (%) |
|--------|---------------|---------------|-----------|---------------|
| Premier League | 9,410 | 45.8 | 24.6 | 29.6 |
| Serie A | 9,012 | 44.6 | 27.1 | 28.3 |
| Bundesliga | 7,522 | 45.7 | 24.7 | 29.7 |
| La Liga | 9,008 | 47.1 | 25.2 | 27.7 |

### All Leagues Combined
- **Total matches**: 34,952  
- **Home-win percentage**: 45.8%  
- **Draw percentage**: 25.4%  
- **Away-win percentage**: 28.8%  

**Highlights**
- Home teams won more often than away teams in all leagues (45.8% vs 28.8%).  
- Away-win percentage was highest in the Bundesliga (29.7%).  
- Home-win percentage was highest in La Liga (47.1%).  
- Draw percentage was highest in Serie A (27.1%).

---

## 2. Goals Scored

### Average Goals by League (Mean ± SD)

| League | Home Goals | Away Goals | Total Goals |
|--------|------------|------------|-------------|
| Premier League | 1.53 ± 1.30 | 1.18 ± 1.16 | 2.72 ± 1.67 |
| Serie A | 1.50 ± 1.23 | 1.17 ± 1.11 | 2.68 ± 1.65 |
| Bundesliga | 1.67 ± 1.36 | 1.28 ± 1.20 | 2.95 ± 1.72 |
| La Liga | 1.55 ± 1.31 | 1.13 ± 1.11 | 2.67 ± 1.68 |

### Median Goals

| League | Median Home | Median Away | Median Total |
|--------|-------------|-------------|--------------|
| Premier League | 1.0 | 1.0 | 3.0 |
| Serie A | 1.0 | 1.0 | 3.0 |
| Bundesliga | 1.0 | 1.0 | 3.0 |
| La Liga | 1.0 | 1.0 | 2.0 |

### Goal Skewness

| League | Home Skew | Away Skew | Total Skew |
|--------|-----------|-----------|------------|
| Premier League | 0.971 | 1.073 | 0.605 |
| Serie A | 0.803 | 0.992 | 0.570 |
| Bundesliga | 0.896 | 1.001 | 0.491 |
| La Liga | 0.982 | 1.171 | 0.661 |

---

## 3. Betting Odds

### Average Odds by League (Mean ± SD)

| League | Home Odds | Draw Odds | Away Odds |
|--------|-----------|-----------|-----------|
| Premier League | 2.74 ± 1.91 | 3.97 ± 1.17 | 4.73 ± 3.95 |
| Serie A | 2.61 ± 1.60 | 3.69 ± 0.93 | 4.56 ± 3.23 |
| Bundesliga | 2.54 ± 1.68 | 3.92 ± 1.18 | 4.31 ± 3.37 |
| La Liga | 2.57 ± 1.89 | 3.87 ± 1.41 | 4.71 ± 4.11 |

### Median Odds

| League | Median Home | Median Draw | Median Away |
|--------|------------|------------|------------|
| Premier League | 2.18 | 3.51 | 3.40 |
| Serie A | 2.15 | 3.40 | 3.50 |
| Bundesliga | 2.10 | 3.50 | 3.30 |
| La Liga | 2.10 | 3.40 | 3.50 |

### Odds Skewness

| League | Home Skew | Draw Skew | Away Skew |
|--------|-----------|-----------|-----------|
| Premier League | 3.166 | 3.078 | 2.622 |
| Serie A | 3.003 | 2.497 | 2.212 |
| Bundesliga | 4.063 | 4.079 | 3.663 |
| La Liga | 4.407 | 4.128 | 3.637 |

---

## 4. League Comparisons (by Statistics)

- **Away-win percentage**:  
  - Bundesliga: 29.7%  
  - Premier League: 29.6%  
  - Serie A: 28.3%  
  - La Liga: 27.7%

- **Mean total goals per match**:  
  - Bundesliga: 2.95  
  - Premier League: 2.72  
  - Serie A: 2.68  
  - La Liga: 2.67

- **Home-win percentage**:  
  - La Liga: 47.1%  
  - Premier League: 45.8%  
  - Bundesliga: 45.7%  
  - Serie A: 44.6%

- **Median total goals**:  
  - Premier League / Serie A / Bundesliga: 3.0  
  - La Liga: 2.0

- **Goal skewness**: All positive, ranging from 0.491 to 1.171  
- **Odds skewness**: All positive, ranging from 2.212 to 4.407

---

## 5. Statistical Summary

- **Sample size**: 34,952 matches  
- **Time span**: 2000–2024 seasons  
- **Odds data availability**: 98.9%  
- **Countries represented**: England, Italy, Germany, Spain  

**Key Points**
1. Home teams won more often than away teams in every league.  
2. Away-win percentages ranged between 27.7% and 29.7%.  
3. League-level mean total goals per match ranged from 2.67 to 2.95.  
4. Median total goals per match ranged from 2.0 to 3.0.  
5. Goal distributions were positively skewed (0.491–1.171).  
6. Odds distributions were more positively skewed (2.212–4.407).  
7. Odds data were available for nearly all matches.

---

## Method Notes
- **Source**: Football-Data.co.uk processed CSV files  
- **Period analyzed**: Seasons 2000–2024  
- **Measures used**: Mean, standard deviation, median, skewness  
- **Matches lacking odds data**: Excluded from odds-related calculations  
- **Results expressed from the home-team perspective**
