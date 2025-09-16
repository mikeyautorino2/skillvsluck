# About this directory: `data/us_leagues`

## MLB Data
# MLB Data Dictionary

| Variable   | Definition/Description                        | Data Type  | Allowed Values / Coding Conventions | Periodicity  | Notes                                                                 |
|------------|-----------------------------------------------|------------|-------------------------------------|--------------|----------------------------------------------------------------------|
| season     | Year of the season                            | Integer    | YYYY                                | Season-level | If a season includes 2 years, use the earlier year (e.g., Season 2024-25 uses 2024) |
| date       | Date of the game                              | Date       | YYYY-MM-DD                          | Game-level   | Regular season only (no playoffs)                                    |
| team1      | Abbreviation for the home team                | String     | e.g., SEA                           | Game-level   |                                                                      |
| team2      | Abbreviation for the away team                | String     | e.g., SEA                           | Game-level   |                                                                      |
| result     | Outcome of the game from team1 perspective    | Categorical| W, L, T                             | Game-level   | Based on score1 and score2                                           |
| score1     | Score for the first team                      | Integer    | Non-negative                        | Game-level   | Matches official box score                                           |
| score2     | Score for the second team                     | Integer    | Non-negative                        | Game-level   | Matches official box score                                           |
| home_away  | Indicates whether team1 is Home or Away       | Categorical| {Home, Away}                                | Game-level   | Always home                                                   |


## NFL Data
*Add Data description here*

## NBA Data
# NBA Data Dictionary

| Variable   | Definition/Description                        | Data Type  | Allowed Values / Coding Conventions | Periodicity  | Notes                                                                 |
|------------|-----------------------------------------------|------------|-------------------------------------|--------------|----------------------------------------------------------------------|
| season     | Year of the season                            | Integer    | YYYY                                | Season-level | If a season includes 2 years, use the earlier year (e.g., Season 2024-25 uses 2024) |
| date       | Date of the game                              | Date       | YYYY-MM-DD                          | Game-level   | Regular season only (no playoffs)                                    |
| team1      | Abbreviation for the home team                | String     | e.g., INJ, FWP, WSC                 | Game-level   |                                                                      |
| team2      | Abbreviation for the away team                | String     | e.g., SLB, NYK, PHA                 | Game-level   |                                                                      |
| result     | Outcome of the game from team1 perspective    | Categorical| W = Win, L = Loss                   | Game-level   | Based on score1 and score2                                           |
| score1     | Points scored by team1                        | Integer    | Non-negative integers               | Game-level   | Matches official box score                                           |
| score2     | Points scored by team2                        | Integer    | Non-negative integers               | Game-level   | Matches official box score                                           |
| home_away  | Indicates whether team1 is Home or Away       | Categorical| {Home, Away}                        | Game-level   | Always home                                                          |
