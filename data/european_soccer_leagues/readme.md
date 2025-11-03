# European Soccer Match Data (Top 5 Leagues)

> Premier League · Serie A · Bundesliga · Ligue 1 · La Liga  
> Source: Football-Data.co.uk (season-by-season CSVs)

## Overview

This repo aggregates **match-level data** for Europe’s “Top 5” leagues, downloaded **per season** from Football-Data.co.uk, then **combined and normalized** with Python/pandas into **one CSV per league**. We keep a compact format (dates, teams, full-time score/result, match week when available, and Bet365 odds) and add derived fields (season start year and per-team match points).

- **Primary source:** Football-Data.co.uk — data download page: https://www.football-data.co.uk/data.php  
- **Leagues covered:** Premier League (E0), Serie A (I1), Bundesliga (D1), Ligue 1 (F1), La Liga (SP1)  
- **Data:** One row per regular-season match

> Note: This directory has also referenced the *xgabora/Club-Football-Match-Data-2000-2025* project for exploration. Though we have also included downloads **directly** from Football-Data.co.uk as well. See **References** below.

---

## What’s inside

- `code/` — Python code that was used to load, normalize, and export league-level CSVs.  
- `data/` — includes all data gathered for the project – both raw and final.
  - `original/` — Original raw data found (pulled from github cited).
  - `processed/` — Final per-league CSVs (e.g., `premier_league.csv`, `serie_a.csv`, etc.).

---

## Fields we select (as downloaded)

These come *verbatim* from Football-Data season files before normalization:

| Column | Description |
|---|---|
| `Date` | Match date in **dd/mm/yyyy** format (string in the raw files). |
| `HomeTeam` | Home team name (string). |
| `AwayTeam` | Away team name (string). |
| `FTHG` | Full-time home goals (int). |
| `FTAG` | Full-time away goals (int). |
| `FTR` | Full-time result (enum: `H`=home win, `D`=draw, `A`=away win). |
| `MW` | Match week (int). *Not present for all seasons.* |
| `B365H` | Bet365 home-win odds (float). |
| `B365D` | Bet365 draw odds (float). |
| `B365A` | Bet365 away-win odds (float). |


---

## Normalization & derived variables

During processing we standardize names and compute extra fields:

- **Parsed date** → `date` (ISO `YYYY-MM-DD`)
- **Season start year** → `season` (e.g., **2023** means 2023/24)  
  - Rule: if `date.month >= 8` (Aug–Dec) then `season = date.year`; else (Jan–Jul) `season = date.year - 1`.
- **Team names** → `home_team`, `away_team` (renamed from `HomeTeam`, `AwayTeam`)
- **Goals** → `hometeamgoals`, `awayteamgoals` (from `FTHG`, `FTAG`)
- **Home-team result (ternary)** → `hometeamresult` ∈ {`win`, `draw`, `loss`} (derived from goals)
- **Per-match points** → `home_team_points`, `away_team_points` (3/1/0 and 0/1/3)
- **Odds (standardized names)** → `OddHome`, `OddDraw`, `OddAway` (renamed from `B365H/D/A`)
- **Match week** → `week` (renamed from `MW` when available)


**Final per-league CSV schema**

| Column | Type | Example | Notes |
|---|---|---|---|
| `season` | Int64 | `2023` | Start year of the season (e.g., 2023 → 2023/24). |
| `date` | date (YYYY-MM-DD) | `2024-04-06` | Parsed from raw `Date`. |
| `week` | Int64 (optional) | `28` | Included only if `MW` was present. |
| `home_team` | string | `Arsenal` | From `HomeTeam`. |
| `away_team` | string | `Liverpool` | From `AwayTeam`. |
| `hometeamgoals` | Int64 | `3` | From `FTHG`. |
| `awayteamgoals` | Int64 | `1` | From `FTAG`. |
| `hometeamresult` | string (`win`/`draw`/`loss`) | `win` | Derived from goals. |
| `home_team_points` | Int64 | `3` | 3 if `win`, 1 if `draw`, 0 if `loss`. |
| `away_team_points` | Int64 | `0` | Complement of home points. |
| `OddHome` | float | `1.85` | From `B365H`. |
| `OddDraw` | float | `3.60` | From `B365D`. |
| `OddAway` | float | `4.10` | From `B365A`. |

> We include **regular-season** league matches. Cups/playoffs are excluded by file selection (divisions) and, when needed, by date/league filters.
