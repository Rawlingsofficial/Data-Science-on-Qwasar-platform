# libs
import pandas as pd
import csv
import re

# load nba 
def load_nba_game_data(nbafile):
    play_info = []
    with open(nbafile, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter="|")
        fields = next(csvreader)
        for row in csvreader:
            play_info.append(row)
    return play_info

# analyze NBA game and extract names of players
def new_analyze_game_nba(plays_by_play_movez):
    players_names = []  # Player names
    result = []
    
    for play in plays_by_play_movez:
        result.append(re.split(r"[\s+;\(\)]", play[7]))  # Split play descriptions

    for i in range(len(result)):
        for a in range(len(result[i])):
            if result[i][a].endswith(".") and (result[i][a] + " " + result[i][a+1]) not in players_names:  # Check and append unique player names
                players_names.append(result[i][a] + " " + result[i][a+1])  # Add unique player names
                
    players_names = [name for name in players_names if not name.startswith("Team ")]  # Filter out common names

    return players_names

# Calculate player statistics
def call_players_statz(play_by_play_movez, list_data_on_players):
    statics_of_all_players = []
    field_goals = []
    field_goal_attempts = []

    for players in list_data_on_players:
        players_status = {
            "Players": '', "FG": 0, "3PA": 0, "FG%": 0, "3P": 0, "3P%": 0, "FT": 0,"FGA": 0,
            "FTA": 0, "FT%": 0, "DRB": 0, "TRB": 0,"ORB": 0,  "STL": 0, "BLK": 0, "TOV": 0,"AST": 0,
            "PF": 0, "PTS": 0
        }
        players_status['Players'] = players

        # Define regular expressions $ corresponding statistic.
        patterns = {
            r"(\w\. \w+) makes 2-pt": {'FGA': 1, 'FG': 1},
            r"(\w\. \w+) misses 2-pt": {'FGA': 1},
            r"(\w. \w+) makes 3-pt": {'3PA': 1, '3P': 1, 'FGA': 1, 'FG': 1},
            r"(\w. \w+) misses 3-pt": {'3PA': 1, 'FGA': 1},
            r"(\w\. \w+) makes free throw": {'FT': 1, 'FTA': 1},
            r"(\w\. \w+) misses free throw": {'FTA': 1},
            r"Offensive rebound by (\w\. \w+)": {'ORB': 1, 'TRB': 1},
            r"Defensive rebound by (\w\. \w+)": {'TRB': 1, 'DRB': 1},
            r"assist by (\w. \w+)": {'AST': 1},
            r"steal by (\w. \w+)": {'STL': 1},
            r"block by (\w. \w+)": {'BLK': 1},
            r"Turnover by (\w. \w+)": {'TOV': 1},
            r"foul by (\w\. \w+)": {'PF': 1},
        }

        # Loop through plays and calculate stats
        for play in play_by_play_movez:
            for pattern, increments in patterns.items():  
                match = re.search(pattern, play[-1])
                if match and match.group(1) == players:
                    for key, value in increments.items():
                        players_status[key] += value

        if players_status['FGA'] != 0:
            players_status['FG%'] = round((players_status['FG'] / players_status['FGA']), 3)
        else:
            players_status['FG%'] = 0

        if players_status['3PA'] != 0:
            players_status['3P%'] = round((players_status['3P'] / players_status['3PA']), 3)
        else:
            players_status['3P%'] = 0

        if players_status['FTA'] != 0:
            players_status['FT%'] = round((players_status['FT'] / players_status['FTA']), 3)
        else:
            players_status['FT%'] = 0

        if players_status["FG"] != 0:
            players_status["PTS"] = 2 * (players_status['FG'] - players_status['3P']) + 3 * (players_status['3P']) + players_status['FT']
        else:
            players_status["PTS"] = 0

        # Append p stats to  list
        statics_of_all_players.append(players_status)

    return statics_of_all_players

# Mapping players to their respective teams
def assign_player_to_teams(plays_by_plays_movez, lst_player_teams, statics):
    team_one_name = plays_by_plays_movez[0][2]
    team_i = 1
    while team_i != len(plays_by_plays_movez):
        if team_one_name != plays_by_plays_movez[team_i][2]:
            team_two_name = plays_by_plays_movez[team_i][2]
            break
        team_i += 1

    players_team_mappings = {name: '' for name in lst_player_teams}
    team_one_stats = {
        "total1": 'Team Totals', "PTS": 0, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
        "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0
    }
    team_two_stats = {
        "total2": 'Team Totals', "PTS": 0, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0,
        "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0
    }

    for play in plays_by_plays_movez:
        match1 = re.search(r"(\w\. \w+) makes \d-pt", play[-1])
        if match1:
            names = match1.group(1)
            players_team_mappings[names] = play[2]

        match_MISS = re.search(r"(\w\. \w+) MISSED \d-pt", play[-1])
        if match_MISS:
            names = match_MISS.group(1)
            players_team_mappings[names] = play[2]

        match_ETG = re.search(r"(\w\. \w+) ENTERS THE GAME", play[-1])
        if match_ETG:
            names = match_ETG.group(1)
            players_team_mappings[names] = play[2]

        match_drb = re.search(r"DEFENSIVE REBOUND BY (\w\. \w+)", play[-1])
        if match_drb:
            names = match_drb.group(1)
            players_team_mappings[names] = play[2]

        match_drb = re.search(r"DEFENSIVE REBOUND BY (\w\. \w+-\w+)", play[-1])
        if match_drb:
            names = match_drb.group(1)
            players_team_mappings[names] = play[2]

    teamone = []
    teams_two = []
    print(*statics[0].keys(), sep='\t')
    for k, v in players_team_mappings.items():
        if v == team_two_name:
            for event in statics:
                if event['Players'] == k:
                    teamone.append(event)
                    print(*event.values(), sep='\t')
                    break

    for event in teamone:
        for k, v in event.items():
            for key, value in team_one_stats.items():
                if key == k:
                    try:
                        team_one_stats[k] += v
                    except:
                        continue
            try:
                team_one_stats["FG%"] = round((team_one_stats["FG"] / team_one_stats["FGA"]), 3)
            except:
                continue
            try:
                team_one_stats["3P%"] = round((team_one_stats["3P"] / team_one_stats["3PA"]), 3)
            except:
                continue
            try:
                team_one_stats["FT%"] = round((team_one_stats["FT"] / team_one_stats["FTA"]), 3)
            except:
                continue

    print(*team_one_stats.values(), sep='\t')
    print("\n\n")

    print(*statics[0].keys(), sep='\t')
    for k, v in players_team_mappings.items():
        if v == team_one_name:
            for event in statics:
                if event['Players'] == k:
                    teams_two.append(event)
                    print(*event.values(), sep='\t')
                    break
    for event in teams_two:
        for k, v in event.items():
            for key, value in team_two_stats.items():
                if key == k:
                    try:
                        team_two_stats[k] += v
                    except:
                        continue

    print(*team_two_stats.values(), sep='\t')
    return players_team_mappings

# M
def main():
    play_by_play_moves = load_nba_game_data("nba_game_warriors_thunder_20181016.txt")
    lst_of_players = new_analyze_game_nba(play_by_play_moves)
    statics = call_players_statz(play_by_play_moves, lst_of_players)
    TEAMS = assign_player_to_teams(play_by_play_moves, lst_of_players, statics)


if __name__ == "__main__":
    main()

    


    