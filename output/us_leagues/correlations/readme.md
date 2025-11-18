# Predictive Persistence (NBA / NFL / MLB)
## Main Conclusions:
- **NBA**: The first-half win percentage is a pretty good predictor of second-half win percentage across seasons, since the NBA data plot is tight and diagonally alligned.

-  **MLB**: The MLB points form a compact oval around .500 with a less harsh diagonal, meaning first-half win percentage is a predictor of second-half win percentage, but weaker than it is for the NBA. The strong pull towards .500 also means that extremely poor or extremely high-performing teams in the first-half tend to perform more average in the second half. 
 
-  **NFL**: The first-half win percentage tells you very little about the second-half win percentage, which could be because there are fewer games per season. 

- Across **pure luck leagues**, first-half performance does not predict second-half performance. 


## How to read the visuals
- **Scatterplots:** A cloud around y = x with no slope → independence
- **ρ histograms:** Centered near 0 → no relationship


## Deeper Explanation

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

The title also shows **Spearman r** (rank correlation) and **p-value** for that season. See what Spearman r means below.

---

### 2) Combined scatterplot (all seasons overlaid)
This chart overlays all per-team datapoints from all seasons. The title shows the **lowest** and **highest** seasons present in the data. It’s useful for seeing the overall relationship and whether it thr data is broadly near the y=x line across many seasons.

---

### 3) Histogram of Spearman r across seasons
We compute one **Spearman r** per season (comparing teams’ first-half and second-half win % ranks in that season). The histogram shows how those seasonal r values are **distributed** across years.

**Interpretation:**
- If values cluster around **0.7**, then **most seasons** show **strong** persistence: early ranks tend to predict later ranks.
- If values cluster near **0.0**, then persistence is **weak**: early ranks don’t tell you much about later ranks.
- Negative values (rare) would indicate **reversal** (high early → low later, and vice versa).

---


## How “win %” is computed (including ties)

- **NBA:** `win = 1` for win, `0` for loss
- **NFL / MLB (with ties):**  
  We encode ties as **0.5**, so:
  - win = 1  
  - tie = 0 
  - loss = -1  
  Then the **mean** of these values over a half equals the win % that includes ties.

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
   - Combined scatterplot over all seasons  
   - Histogram of per-season Spearman r values

---

## How to run

1. Place your league dataset CSV in the files of the google colab notebook for the datatype you want. Put them in mnt/data.
   - `nba_data.csv`  
   - `nfl_data.csv`  
   - `mlb_data.csv`

2. Run the Spearman code (first code block) three times: once with league = nba, and then nfl, and then mlb.
3. Run the second code block and obtain your first half versus second half win percentage CSV, and your spearman csv for that data type and all leagues.
