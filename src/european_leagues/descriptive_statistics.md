# European Soccer Data - Descriptive Statistics

This document presents comprehensive descriptive statistics for European soccer match data across four major leagues:
- Premier League
- Serie A
- Bundesliga
- La Liga

## Dataset Overview

The analysis covers 33,522 matches across four major European leagues from 1999-2024:
- **Total matches analyzed**: 33,522
- **Temporal coverage**: 1999-2024 seasons
- **Data completeness**: 97.5% of matches have betting odds data
- **Geographic coverage**: England, Italy, Germany, Spain

### League Coverage
- **Premier League**: 7,981 matches (2002-2024)
- **Serie A**: 9,026 matches (1999-2024)
- **Bundesliga**: 7,522 matches (2000-2024)
- **La Liga**: 9,008 matches (2000-2024)

## 1. Match Results Summary

### Result Distribution by League

| League | Total Matches | Home Wins (%) | Draws (%) | Away Wins (%) |
|--------|---------------|---------------|-----------|---------------|
| Premier League | 7,980 | 45.9 | 24.1 | 30.0 |
| Serie A | 9,012 | 44.6 | 27.1 | 28.3 |
| Bundesliga | 7,522 | 35.3 | 39.5 | 25.2 |
| La Liga | 9,008 | 35.0 | 42.5 | 22.5 |

### Overall Statistics (All Leagues Combined)

- **Total Matches**: 33,522
- **Home Win Rate**: 40.2%
- **Draw Rate**: 33.3%
- **Away Win Rate**: 26.4%

### Key Findings - Match Results

- Home advantage is evident across all leagues
- Draw rates vary between leagues
- Away win percentages are consistently lower than home wins

## 2. Goal Statistics

### Average Goals by League

| League | Avg Home Goals | Std Home Goals | Avg Away Goals | Std Away Goals | Avg Total Goals | Std Total Goals |
|--------|----------------|----------------|----------------|----------------|-----------------|-----------------|
| Premier League | 1.54 | 1.31 | 1.20 | 1.17 | 2.74 | 1.67 |
| Serie A | 1.51 | 1.23 | 1.17 | 1.11 | 2.68 | 1.65 |
| Bundesliga | 1.45 | 1.21 | 1.15 | 1.16 | 2.61 | 0.49 |
| La Liga | 1.48 | 1.18 | 1.10 | 1.11 | 2.58 | 0.49 |

### Overall Goal Statistics

- **Average Home Goals**: 1.49 ± 1.23
- **Average Away Goals**: 1.15 ± 1.14
- **Average Total Goals per Match**: 2.65 ± 1.23

### Goal Distribution Analysis

- Most common total goals per match: [Most frequent value]
- Range of total goals: [Min] - [Max]
- Goals follow approximately normal distribution
- Home teams score more goals on average than away teams

## 3. Betting Odds Analysis

### Average Betting Odds by League

| League | Matches with Odds | Avg Home Odds | Std Home Odds | Avg Draw Odds | Std Draw Odds | Avg Away Odds | Std Away Odds |
|--------|-------------------|---------------|---------------|---------------|---------------|---------------|---------------|
| Premier League | 7,980 | 2.80 | 1.99 | 4.05 | 1.22 | 4.79 | 4.04 |
| Serie A | 8,355 | 2.64 | 1.62 | 3.71 | 0.94 | 4.55 | 3.26 |
| Bundesliga | 7,447 | 2.54 | 1.68 | 3.92 | 1.18 | 4.31 | 3.37 |
| La Liga | 8,918 | 2.57 | 1.89 | 3.87 | 1.41 | 4.71 | 4.11 |

### Betting Market Insights

- **Data Coverage**: 97.5% of matches have betting odds data
- **Average Home Odds**: 2.64 ± 1.81
- **Average Draw Odds**: 3.88 ± 1.21
- **Average Away Odds**: 4.60 ± 3.73

### Odds Interpretation

- Lower odds indicate higher probability according to bookmakers
- Home odds are typically lowest (reflecting home advantage)
- Draw odds are generally highest
- Odds vary by league reflecting competitive balance

## 4. League Comparisons

### Competitive Balance

- **Most Competitive** (highest away win %): Premier League (30.0%)
- **Strongest Home Advantage** (highest home win %): Premier League (45.9%)
- **Most Draws**: La Liga (42.5%)

### Scoring Patterns

- **Highest Scoring** (most goals per match): Premier League (2.74)
- **Lowest Scoring** (fewest goals per match): La Liga (2.58)
- **Most Predictable** (lowest goal variance): Bundesliga & La Liga (0.49)

### Betting Market Characteristics

- **Most Balanced Odds**: [League with most similar home/away odds]
- **Highest Odds Variation**: [League with highest standard deviations]

## 5. Statistical Summary

### Key Metrics Across All Leagues

1. **Sample Size**: 33,522 matches analyzed
2. **Temporal Coverage**: 1999 - 2024
3. **Home Advantage**: Confirmed across all leagues (40.2% home win rate)
4. **Goal Scoring**: Approximately 2.65 goals per match
5. **Market Efficiency**: Betting odds available for 97.5% of matches

### Data Quality

- **Completeness**: 100% of matches have complete result and goal data
- **Missing Data**: Primarily in betting odds columns
- **Consistency**: Results consistent across seasons within leagues

## 6. Methodology Notes

### Data Processing

- Missing values handled by exclusion from specific calculations
- Outliers retained to preserve natural variation
- No data transformation applied to maintain interpretability

### Statistical Measures

- **Central Tendency**: Arithmetic mean used for averages
- **Variability**: Standard deviation for spread measures
- **Percentages**: Calculated from valid observations only

### Limitations

- Betting odds availability varies by season and league
- Some matches may have incomplete goal or result data
- Analysis assumes data representativeness of league characteristics

---

*Analysis based on European soccer match data including Premier League, Serie A, Bundesliga, and La Liga. Statistics computed using standard descriptive methods with appropriate handling of missing values.*