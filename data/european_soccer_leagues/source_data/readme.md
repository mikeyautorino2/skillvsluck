# About this directory: `data/european_soccer/data/original/`

## Purpose

This folder stores the original soccer dataset used for exploration and cross-checks.  
These files are kept **as-downloaded** so that downstream scripts can reproduce our processing steps and compare against the source.

---

## Files in this folder

- `Original_Matches.csv` — match-level records (multi-league, multi-season) as provided by the the github repo (mentioned below).  
- `Original_EloRatings.csv` — team Elo ratings snapshot from the same project (if present in your copy).

## General
Import Soccer League data from https://github.com/xgabora/Club-Football-Match-Data-2000-2025
---

"Division", "MatchDate", "HomeTeam", "AwayTeam", "FTHome", "FTAway", "FTResult", "
|Column | Data Type | Description |
| --- | --- |---|
| **🏆 `Division`**| *enum*|League that the match was played in - country code + division number (*I1 for Italian First Division*). For countries where we only have one league, we use 3-letter country code (*ARG for Argentina*). |
| **📆 `MatchDate`**| *date* |Match date in the classic YYYY-MM-DD format. |
| **🕘 `MatchTime`**| *time* |Match time in the HH:MM:SS format. CET-1 timezone. |
| **🏠 `HomeTeam`**| *string* |Home team's club name in English, abbreviated if needed. |
| **🚗 `AwayTeam`**| *string*|Home team's club name in English, abbreviated if needed. |
| **📊 `HomeElo`**| *float* |Home team's most recent Elo rating. |
| **📊 `AwayElo`**| *float* |Away team's most recent Elo rating. |
| **📉 `Form3Home`**| *int* |Number of points gathered by home team in the last 3 matches (*Win = 3 points, Draw = 1 point, Loss = 0 points, so this value is between 0 and 9*). |
| **📈 `Form5Home`**| *int*|Number of points gathered by home team in the last 5 matches (*Win = 3 points, Draw = 1 point, Loss = 0 points, so this value is between 0 and 15*). |
| **📉 `Form3Away`**| *int* |Number of points gathered by away team in the last 3 matches (*Win = 3 points, Draw = 1 point, Loss = 0 points, so this value is between 0 and 9*). |
| **📈 `Form5Away`**| *int* |Number of points gathered by away team in the last 5 matches (*Win = 3 points, Draw = 1 point, Loss = 0 points, so this value is between 0 and 15*). |
| **⚽ `FTHome`**| *int* |Full-time goals scored by home team. |
| **⚽ `FTAway`**| *int*|Full-time goals scored by away team. |
| **🏁 `FTResult`**| *enum* |Full-time result (*H for Home win, D for Draw and A for Away win*). |
| **⚽ `HTHome`**| *int* |Half-time goals scored by home team. |
| **⚽ `HTAway`**| *int* |Half-time goals scored by away team. |
| **⏱️ `HTResult`**| *enum*|Half-time result (*H for Home win, D for Draw and A for Away win*). |
| **🏹 `HomeShots`**| *int* |Total shots (*goal, saved, blocked, off-target*) by home team. |
| **🏹 `AwayShots`**| *int* |Total shots (*goal, saved, blocked, off-target*) by away team. |
| **🎯 `HomeTarget`**| *int* |Total shots on target (*goal, saved*) by home team. |
| **🎯 `AwayTarget`**| *int* |Total shots on target (*goal, saved*) by away team. |
| **🤕 `HomeFouls`**| *int* |Total fouls by home team. |
| **🤕 `AwayFouls`**| *int* |Total fouls by away team. |
| **🚩 `HomeCorners`**| *int* |Total corners taken by home team. |
| **🚩 `AwayCorners`**| *int* |Total corners taken by away team. |
| **🟨 `HomeYellow`**| *int* |Total yellow cards awarded to home team players (*excl. staff*). |
| **🟨 `AwayYellow`**| *int* |Total yellow cards awarded to away team players (*excl. staff*). |
| **🟥 `HomeRed`**| *int* |Total red cards awarded to home team players (*excl. staff*). |
| **🟥 `AwayRed`**| *int* |Total red cards awarded to away team players (*excl. staff*). |
| **1️⃣ `OddHome`**| *float* |Bet365's Home Team Win Odd. |
| **0️⃣ `OddDraw`**| *float* |Bet365's Draw Odd. |
| **2️⃣ `OddAway`**| *float* |Bet365's Away Team Win Odd. |
| **1️⃣ `MaxHome`**| *float* |Maximum Home Team Win Odd from ~17 European bookmakers. |
| **0️⃣ `MaxDraw`**| *float* |Maximum Draw Odd from ~17 European bookmakers. |
| **2️⃣ `MaxAway`**| *float* |Maximum Away Team Win Odd from ~17 European bookmakers. |
| **⬆️ `Over25`**| *float* |Bet365's Over 2.5 Total Goals Scored Odd. |
| **⬇️ `Under25`**| *float* |Bet365's Under 2.5 Total Goals Scored Odd. |
| **⬆️ `MaxOver25`**| *float* |Maximum Over 2.5 Total Goals Scored Odd from ~17 European bookmakers. |
| **⬇️ `MaxUnder25`**| *float* |Maximum Under 2.5 Total Goals Scored Odd from ~17 European bookmakers. |
| **🟰 `HandiSize`**| *float* |Asian handicap size for home team (*negative number indicating stronger home team*) . |
| **➕️ `HandiHome`**| *float* |Bet365's Home Team Win Odd with the given handicap size for Home team. |
| **➖️ `HandiAway`**| *float* |Bet365's Away Team Win Odd with the given handicap size for Home team. |
| **📦 `C_LTH`**| *float* |Likeliness of match falling into the Low Tempo Home-oriented match cluster. |
| **📦 `C_LTA`**| *float* |Likeliness of match falling into the Low Tempo Away-oriented match cluster. |
| **📦 `C_VHD`**| *float* |Likeliness of match falling into the Visibly Home Dominated match cluster. |
| **📦 `C_VAD`**| *float* |Likeliness of match falling into the Visibly Away Dominated match cluster. |
| **📦 `C_HTB`**| *float* |Likeliness of match falling into the High Tempo Balanced match cluster. |
| **📦 `C_PHB`**| *float* |Likeliness of match falling into the Highly Physical Balanced match cluster. |

Description provided by the author of the repository.
