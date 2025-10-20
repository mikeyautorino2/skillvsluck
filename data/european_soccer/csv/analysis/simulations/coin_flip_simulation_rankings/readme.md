# Simulated League Rankings

End-of-season tables generated from the simulated match files in the **[matches](../matches/)** folder.  
Each table aggregates simulated results for every season and ranks teams by **points**; if two or more teams finish on the same points, they are ordered **alphabetically by the team standardised name**.

## Files
One CSV per league, e.g.:
- `bundesliga_simulated_standings_all_seasons.csv`
- `la_liga_simulated_standings_all_seasons.csv`
- `premier_league_simulated_standings_all_seasons.csv`
- `serie_a_simulated_standings_all_seasons.csv`

## Schema
| column  | description |
|---|---|
| `season` | Season year (YYYY) |
| `team` | Standardized team code |
| `points` | Total points from simulated results (win=3, draw=1, loss=0) |
| `wins` | Simulated wins |
| `draws` | Simulated draws |
| `losses` | Simulated losses |
| `rank` | Final position (points ↓, then **alphabetical** by `team`) |
