# Predictive Persistence (NBA / NFL / MLB)


## What the graphs show

### 1) Season scatter plots (per-season)
Each chart plots **teams in one season**:

- **X-axis:** First-half win %  
- **Y-axis:** Second-half win %  
- **Dashed red line (y = x):** If points lie near this line, teams performed similarly in both halves (“persistence”).

**Interpretation:**
- Points **near the line** → similar first/second half performance.
- Points **above** the line → teams improved in the second half.
- Points **below** the line → teams declined in the second half.

The title also shows **Spearman r** (rank correlation) and **p-value** for that season. See “What Spearman r means” below.

---

### 2) Combined scatter (all seasons overlaid)
This chart overlays all per-team points from all seasons. The title shows the **lowest** and **highest** seasons present in the data. It’s useful for seeing the overall cloud and whether the relationship is broadly near the y=x line across many seasons.

---

### 3) Histogram of Spearman r across seasons
We compute one **Spearman r** per season (comparing teams’ first-half and second-half win % ranks in that season). The histogram shows how those seasonal r values are **distributed** across years.
- We rank teams by **first-half** win % and by **second-half** win %, then correlate those ranks.

**Interpretation:**
- If values cluster around **0.7**, then **most seasons** show **strong** persistence: early ranks tend to predict later ranks.
- If values cluster near **0.0**, then persistence is **weak**: early ranks don’t tell you much about later ranks.
- Negative values (rare) would indicate **reversal** (high early → low later, and vice versa).

---


## How “win %” is computed (including ties)

- **NBA:** `win = 1` for win, `0` for loss (ties don’t occur).
- **NFL / MLB (with ties):**  
  We encode ties as **0.5**, so:
  - win = 1  
  - tie = 0.5  
  - loss = 0  
  Then the **mean** of these values over a half equals the “effective” win % that includes ties.

This lets first-half and second-half averages fairly represent teams that recorded ties.

---

## Methodology 

1. **Convert to team-game rows:** Each game appears twice—once from each team’s perspective—with:
   - season, date, team, opponent, points_for, points_against, home/away
   - margin = points_for − points_against
   - win flag (1, 0.5 if tie, 0)

2. **Split each (season, team) in half by date:**  
   First ⌊n/2⌋ games → first half; remaining games → second half.

3. **Compute per-team summaries:**  
   First-half win % and second-half win % for each (season, team).

4. **Analyze per-season persistence:**  
   For each season, compute **Spearman r** between first-half and second-half win % **across teams**.

5. **Visualize:**  
   - Per-season scatter plots  
   - Combined scatter over all seasons  
   - Histogram of per-season Spearman r values

---

## How to run

1. Place your league dataset CSV in the files of the google colab notebook:  
   - `nba_data.csv`  
   - `nfl_data.csv`  
   - `mlb_data.csv`

2. In the script, set:
   ```python
   DATA_PATH = 'nba_data.csv'   # or 'nfl_data.csv', 'mlb_data.csv'
