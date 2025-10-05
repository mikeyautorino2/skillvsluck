# Code Directory 

## Purpose

This folder stores the code we wrote to process and analyze the data.

---

## Files in this folder

- `cleaning.ipynb` — Cleaning and retrieving the soccer data from the GitHub source.
- `descriptive_statistics.ipynb` — Exploratory data analysis of the soccer data we collected.
- `end_of_season_tables.ipynb`  — Finding the standings of each team within each league and season. 
- `extract_teams.py`  — Creating a dictionary of full team names and their abbreviated names.
- `master_team_names_cleaning.ipynb`  — Finalizing the abbreviated team names, making sure there are no duplicates and abbreviations are unique
- `upset_frequencies.ipynb`  — Match result simulations based on rankings and betting odds

## In Depth Step by Step Walkthrough of Each Code File

### cleaning.ipynb
<!-- add step by step -->

---

### descriptive_statistics.ipynb
<!-- add step by step -->

---

### end_of_season_tables.ipynb
<!-- add step by step -->

---

### master_team_names_cleaning.ipynb
<!-- add step by step -->

---

### upset_frequencies.ipynb
<!-- add step by step -->

---

### correlation.ipynb
# Step-by-Step Summary of the Code

## 1. Load All League Data
- The code starts by calling `load_all_league_data()`, which reads match data and standings for multiple soccer leagues: Premier League, Serie A, Bundesliga, and La Liga.
- The data is stored in two dictionaries:
  - `league_data` → match information per league
  - `standings_data` → team standings per league

## 2. Prepare for Results Collection
- An empty list `results` is created to store the calculated statistics for every team, season, and league.

## 3. Define a Helper Function to Calculate Total Points/Goals
- `goal_calculation(team, games)` takes a subset of matches for a team and calculates:
  - Points/goals scored in home matches
  - Points/goals scored in away matches
- Returns the total points/goals for that subset of matches.

## 4. Define a Function to Compute First-Half and Second-Half Totals
- `correlation(team, season, matches_played)` performs the following steps:
  1. Filters the DataFrame to include only matches for the given team in the given season.
  2. Sorts matches by date to ensure chronological order.
  3. Splits the season into first half and second half using the midpoint of the total number of matches.
  4. Calls `goal_calculation()` on each half to compute total points/goals.
  5. Returns a dictionary containing:
     - `team`
     - `season`
     - `first_half_goals`
     - `second_half_goals`

## 5. Loop Through Every League
- For each league in `league_data`:
  - Extract the matches DataFrame.
  - Create a set of unique `(season, home_team)` pairs so that each team-season combination is processed exactly once.

## 6. Loop Through Every Team-Season Pair
- For each `(season, team)` pair:
  1. Call `correlation()` to calculate first-half and second-half points/goals.
  2. Add the league information to the result dictionary.
  3. Append the dictionary to the `results` list.

## 7. Convert Results to a DataFrame
- After processing all leagues, teams, and seasons:
  - Convert the `results` list of dictionaries into a pandas DataFrame called `allleagues`.
  - Sort the DataFrame by `league`, `season`, and `team` for easier reading and analysis.

## 8. Export the Results
- Save the DataFrame to `correlation_metrics.csv`.
- The CSV contains all teams, seasons, leagues, and their first-half and second-half totals.
