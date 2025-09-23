## Data Dictionary 

For **all** end of seasons rankings datasets in `us_league`, we have the same columns, as shown below:

| Variable    | Description                                 | Data Type | Coding Conventions                       | Periodicity  | Notes                                                        |
| ----------- | ------------------------------------------- | --------- | ---------------------------------------- | ------------ | ------------------------------------------------------------ |
| `league`    | Identifies which sports league         | String   | (e.g. NFL, MLB, NBA)                         | League-level | Uses standard league codes like NBA, MLB, NFL |
| `season`    | Year of the season                          | Integer   | YYYY (e.g. 2024)                         | Season-level | If a season crosses 2 years, then use the first year. (e.g. Season 2024-25 -> 2024) |
| `team_id`    | Team identifier                        | String  | Abbreviation of the team name (e.g. SEA)   | Season-level | Identifies how the team preformed |
| `games_played`    | Total number of games played by the team                       | Integer | Non-negative   | Season-level | Regular season games only |
| `wins`    | Total number of games won by the team                       | Integer | Non-negative   | Season-level | Counts number of games where team won |
| `losses`    | Total number of games lost by the team                       | Integer | Non-negative   | Season-level | Counts number of games where team lost |
| `ties`    | Total number of games tied by the team                       | Integer | Non-negative   | Season-level | Counts number of games where team tied |
| `win_pct`    | Win percentage of the team                       | Float | 0.0 to 1.0  | Season-level | Calculated as (wins + 0.5 * ties) / games_played |
| `points_for`    | Total points scored by the team                       | Integer | Non-negative  | Season-level | Sum of all points scored across season by team |
| `points_against`    | Total points scored against the team                       | Integer | Non-negative  | Season-level | Sum of all points scored against team across season|
| `point_diff`    | Point differentail                      | Integer | can be negative  | Season-level | Calculated as points_for - points_against|
| `rank`    | Teams ranking within the league season                   | Integer | non-negative  | Season-level | Ranked by win_pct (desc), then point_diff (desc), then team_id (desc). (1 is best rank)|
