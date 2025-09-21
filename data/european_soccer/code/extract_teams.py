import pandas as pd
import numpy as np
from pathlib import Path

def create_standardized_name(team_name):
    """Create standardized team names (abbreviations) for common teams."""

    # Common team name mappings to standard abbreviations
    team_mappings = {
        # Premier League
        'Arsenal': 'ARS',
        'Aston Villa': 'AVL',
        'Chelsea': 'CHE',
        'Liverpool': 'LIV',
        'Manchester City': 'MCI',
        'Manchester United': 'MUN',
        'Tottenham': 'TOT',
        'Newcastle': 'NEW',
        'West Ham': 'WHU',
        'Brighton': 'BHA',
        'Crystal Palace': 'CRY',
        'Everton': 'EVE',
        'Fulham': 'FUL',
        'Leeds': 'LEE',
        'Leicester': 'LEI',
        'Norwich': 'NOR',
        'Southampton': 'SOU',
        'Watford': 'WAT',
        'Wolves': 'WOL',
        'Burnley': 'BUR',
        'Sheffield United': 'SHU',
        'West Brom': 'WBA',

        # Serie A
        'Juventus': 'JUV',
        'AC Milan': 'MIL',
        'Inter': 'INT',
        'Napoli': 'NAP',
        'Roma': 'ROM',
        'Lazio': 'LAZ',
        'Atalanta': 'ATA',
        'Fiorentina': 'FIO',
        'Torino': 'TOR',
        'Bologna': 'BOL',
        'Genoa': 'GEN',
        'Sampdoria': 'SAM',
        'Udinese': 'UDI',
        'Cagliari': 'CAG',
        'Parma': 'PAR',
        'Sassuolo': 'SAS',
        'Verona': 'VER',
        'Spezia': 'SPE',

        # Bundesliga
        'Bayern Munich': 'BAY',
        'Borussia Dortmund': 'DOR',
        'RB Leipzig': 'LEI',
        'Bayer Leverkusen': 'LEV',
        'Borussia Monchengladbach': 'MON',
        'Wolfsburg': 'WOL',
        'Eintracht Frankfurt': 'FRA',
        'Union Berlin': 'UNI',
        'SC Freiburg': 'FRE',
        'Hoffenheim': 'HOF',
        'FC Koln': 'KOL',
        'Mainz': 'MAI',
        'Hertha Berlin': 'HER',
        'Augsburg': 'AUG',
        'Stuttgart': 'STU',
        'Schalke 04': 'SCH',

        # La Liga
        'Real Madrid': 'RMA',
        'Barcelona': 'BAR',
        'Atletico Madrid': 'ATM',
        'Sevilla': 'SEV',
        'Real Sociedad': 'RSO',
        'Villarreal': 'VIL',
        'Real Betis': 'BET',
        'Athletic Bilbao': 'ATH',
        'Valencia': 'VAL',
        'Espanyol': 'ESP',
        'Getafe': 'GET',
        'Osasuna': 'OSA',
        'Mallorca': 'MAL',
        'Celta Vigo': 'CEL',
        'Cadiz': 'CAD',
        'Granada': 'GRA',
        'Levante': 'LEV',
        'Elche': 'ELC',
    }

    # First try exact match
    if team_name in team_mappings:
        return team_mappings[team_name]

    # Try partial matches for slight variations
    for full_name, abbrev in team_mappings.items():
        if full_name.lower() in team_name.lower() or team_name.lower() in full_name.lower():
            return abbrev

    # Fallback: create abbreviation from team name
    # Remove common words and take first 3 letters of significant words
    words = team_name.replace("FC", "").replace("CF", "").replace("AC", "").replace("SC", "").split()
    if len(words) >= 2:
        return (words[0][:3] + words[1][:1]).upper()
    else:
        return team_name[:3].upper()

def extract_teams_by_season():
    # Load the league datasets
    data_dir = Path('data/european_soccer/data/processed')

    leagues = {
        'Premier League': pd.read_csv(data_dir / 'premier_league.csv'),
        'Serie A': pd.read_csv(data_dir / 'serie_a.csv'),
        'Bundesliga': pd.read_csv(data_dir / 'bundesliga.csv'),
        'La Liga': pd.read_csv(data_dir / 'la_liga.csv')
    }

    # Standardize column names for consistent processing
    standardized_leagues = {}

    for name, df in leagues.items():
        df_std = df.copy()

        if name in ['Premier League', 'Serie A']:
            # Already have correct column names
            standardized_leagues[name] = df_std
        else:
            # Bundesliga and La Liga need column mapping
            column_mapping = {
                'MatchDate': 'date',
                'HomeTeam': 'home_team',
                'AwayTeam': 'away_team'
            }

            # Rename columns
            df_std = df_std.rename(columns=column_mapping)
            standardized_leagues[name] = df_std

    # Extract teams by season for each league
    output_dir = Path('data/european_soccer/data/processed')

    for league_name, df in standardized_leagues.items():
        teams_by_season = []

        # Get unique combinations of season and teams
        for season in sorted(df['season'].unique()):
            season_data = df[df['season'] == season]

            # Get all teams that played in this season
            home_teams = set(season_data['home_team'].unique())
            away_teams = set(season_data['away_team'].unique())
            all_teams = home_teams.union(away_teams)

            for team in sorted(all_teams):
                # Create standardized team name (common abbreviations/short forms)
                team_standardized = create_standardized_name(team)

                teams_by_season.append({
                    'Season': int(season),
                    'Team_Standardized': team_standardized,
                    'Team_Full_Name': team
                })

        # Create DataFrame and save to CSV
        teams_df = pd.DataFrame(teams_by_season)

        # Generate filename
        league_filename = league_name.lower().replace(' ', '_') + '_teams.csv'
        output_file = output_dir / league_filename

        teams_df.to_csv(output_file, index=False)

        print(f"Created {output_file}")
        print(f"  {len(teams_df)} team-season combinations")
        print(f"  {teams_df['Season'].nunique()} seasons")
        print(f"  {teams_df['Team_Standardized'].nunique()} unique teams")
        print()

if __name__ == "__main__":
    extract_teams_by_season()