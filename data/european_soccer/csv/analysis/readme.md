# Analysis: Upset Frequency

This directory contains our first-pass measurements of **how often favorites lose** across Europe’s top soccer leagues.

We computed upset frequency rates in two ways and store results in two subfolders with identical output files:

- `standings_upset/` — favorites defined by **end-of-season standings** (lower final rank = stronger team). This was calculated based on the end of the previous season's rankings. 
- `betting_upset/` — favorites defined by **Bet365 pre-match odds** (lower decimal odd = higher implied win probability).

- Both subfolders contain the **same two outputs per league**; only the favorite-definition (“predictor”) differs.

---

## Key definitions

- **Match outcome encoding (`hometeamresult`)**
  - `+1` = home win  
  - `-1` = home loss (away win)  
  - `0`  = draw

- **Predictors (who is favored?)**
  - **Season-Ranking predictor:** look up each team’s *final* rank for that season and mark the club with the better (smaller) rank as the favorite. If either rank is missing, we skip the match.
  - **Betting-Odds predictor:** compare `OddHome` vs `OddAway`. The smaller odd is favored. If either odd is missing/non-positive, we skip the match. (Draw odds are not used to determine the favorite.)

- **Upset**
  - A match is an *upset* when the **actual non-draw result** disagrees with the favorite predicted by the chosen predictor.
  - Draws are **excluded** from upset calculations.

- **Accuracy**
  - Share of (predicted) matches where the predictor picked the actual winner.

- **Total predictions**
  - Number of matches where we *could* make a favorite call (i.e., predictor returned ±1).  
  - This can be less than total matches if odds/ranks were missing.

---

## What the code does (high level)


For each league and season:

1. **Load data**
   - Matches: standardized files (e.g., `bundesliga_std.csv`, `premier_league1_std.csv`) with columns like `season`, `home_team`, `away_team`, `hometeamresult`, `OddHome`, `OddAway`.
   - Standings: season-end tables with `season`, `team_name`, `rank` (used only by the standings predictor).

2. **Predict a favorite per match**
   - **Standings mode:** compare `rank(home)` vs `rank(away)`.
   - **Betting mode:** compare `OddHome` vs `OddAway`.

3. **Score each match**
   - Keep matches where the predictor returns ±1.
   - Count an **upset** if (prediction ≠ actual `hometeamresult`) **and** the actual is not a draw (0).
   - Count a **correct prediction** if (prediction = actual).

4. **Aggregate**
   - By **season** (league-season row).
   - By **team** (home, away, and overall rows across all seasons).

---

## Outputs per league (same schema in both subfolders)

### 1) Seasonal upset frequency  
**File pattern:** `[league]_seasonal_upset_frequency.csv`  
**Example:** `bundesliga_seasonal_upset_frequency.csv`

| Column              | Type   | Meaning                                                                                 |
|---------------------|--------|-----------------------------------------------------------------------------------------|
| `league`            | string | League name (“Bundesliga”, “La Liga”, “Premier League”, “Serie A”).                    |
| `season`            | int    | Season start year (e.g., 2017 for 2017/18).                                            |
| `upset_frequency`   | float  | Upsets ÷ **non-draw matches with a favorite** (0.0–1.0).                                |
| `total_predictions` | int    | Matches where a favorite could be identified (predictor returned ±1).                  |
| `total_upsets`      | int    | Number of upsets in those predicted matches (draws excluded).                          |
| `accuracy`          | float  | Correct favorite picks ÷ total_predictions (0.0–1.0).                                   |
| `non_draw_matches`  | int    | Count of non-draw matches among those predicted (denominator for `upset_frequency`).   |

**Formulas**
- `upset_frequency = total_upsets / non_draw_matches`
- `accuracy = correct_predictions / total_predictions`

> Note: `non_draw_matches ≤ total_predictions` because total_predictions includes both draws and decisive results, but we explicitly exclude draws from the upset rate.

---

### 2) Team upset frequency  
**File pattern:** `[league]_team_upset_frequency.csv`  
**Example:** `bundesliga_team_upset_frequency.csv`

| Column                     | Type   | Meaning                                                                                   |
|---------------------------|--------|-------------------------------------------------------------------------------------------|
| `league`                  | string | League name.                                                                              |
| `team`                    | string | Standardized team code (e.g., `BAY`, `RBL`, `M'G`).                                       |
| `upset_frequency_home`    | float  | Team’s upset rate **in home matches** (as favorite/underdog vs actual non-draw result).   |
| `upset_frequency_away`    | float  | Team’s upset rate **in away matches**.                                                    |
| `upset_frequency_overall` | float  | Upset rate across **all** matches for this team.                                          |
| `total_upsets_home`       | int    | Upsets when this team played at home.                                                     |
| `total_upsets_away`       | int    | Upsets when this team played away.                                                        |
| `total_upsets`            | int    | `total_upsets_home + total_upsets_away`.                                                  |
| `total_predictions_home`  | int    | Predicted home matches (favorite could be identified).                                    |
| `total_predictions_away`  | int    | Predicted away matches.                                                                    |
| `total_predictions`       | int    | `total_predictions_home + total_predictions_away`.                                        |
| `accuracy_home`           | float  | Favorite-pick accuracy in home matches.                                                   |
| `accuracy_away`           | float  | Favorite-pick accuracy in away matches.                                                   |
| `accuracy_overall`        | float  | Favorite-pick accuracy across all matches.                                                |

**Formulas (home/away/overall)**
- `upset_frequency = upsets_non_draw / non_draw_predicted`
- `accuracy = correct_predictions / total_predictions`

---

## Folder layout

analysis/
├── betting_upset/
│ ├── bundesliga_seasonal_upset_frequency.csv
│ ├── bundesliga_team_upset_frequency.csv
│ ├── la_liga_seasonal_upset_frequency.csv
│ ├── la_liga_team_upset_frequency.csv
│ ├── premier_league_seasonal_upset_frequency.csv
│ ├── premier_league_team_upset_frequency.csv
│ ├── serie_a_seasonal_upset_frequency.csv
│ └── serie_a_team_upset_frequency.csv
├── standings_upset/
│ └── (same filenames & schemas as above, computed with the standings predictor)

---

## General Notes

- Higher `upset_frequency` ⇒ more **surprises** (favorites losing) under the chosen predictor.
- Higher `accuracy` ⇒ the predictor’s favorites aligned with actual winners more often.
- Compare `standings_upset` vs `betting_upset` to see how **market favorites** differ from **table-strength favorites** by league, season, or team.
