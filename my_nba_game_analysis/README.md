# Welcome to My Nba Game Analysis
We have caught all the play_by_play happening during a NBA game so we have a flow of data and we want to create a nice array of hash which will sum everything.
Part I
Create a function analyse_nba_game(play_by_play_moves) which receives an array of play and will return a dictionary summary of the game.
Each play follow this format:
PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
They are ordered by time.
The return dictionary (hash) will have this format:
{"home_team": {"name": TEAM_NAME, "players_data": DATA}, "away_team": {"name": TEAM_NAME, "players_data": DATA}}
DATA will be an array of hashes with this format:
{"player_name": XXX, "FG": XXX, "FGA": XXX, "FG%": XXX, "3P": XXX, "3PA": XXX, "3P%": XXX, "FT": XXX, "FTA": XXX, "FT%": XXX, "ORB": XXX, "DRB": XXX, "TRB": XXX, "AST": XXX, "STL": XXX, "BLK": XXX, "TOV": XXX, "PF": XXX, "PTS": XXX}
Part II
Create a print_nba_game_stats(team_dict) function which will a dictionary with name and players_data will print it with the following format (each column is separated by a tabulation (' ')):
HEADER
FOR PLAYER IN PLAYERS
PLAYER
TOTAL
Example 00
Players	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS
Player00	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX
Totals	XX	XX	.XXX	X	XX	.XXX	XX	XX	.XXX	XX	XX	XX	XX	X	X	XX	XX	XX
## Task
What is the problem? And where is the challenge?
NBA (National Basketball Association) game data. It performs various tasks related to extracting and
processing information from an input CSV file containing play-by-play data for an NBA game.
the chalenge of this project involve 
(data loading, player name extraction, calculating the player statistics, team assingment and team statistic calculation )

## Description
How have you solved the problem?
-load_nba_game_data(nbafile)
this function is used for loding the nba data from the text file (nba_game_warriors_thunder_20181016.txt).
It takes the file path (nbafile) as an argument and reads the file line by line using the csv module. 
The data is stored in the play_info list, where each element represents a line of data from the CSV file.
-new_analyze_game_nba(plays_by_play_movez)
extract player names from the play descriptions, by taking  the plays_by_play_movez list as input,
which contains play descriptions. The function iterates through these descriptions and splits them using regular expressions to identify player names. It appends unique player names to the players_names list while filtering out common names and team names. The final list of player names is returned.
-call_players_statz(play_by_play_movez, list_data_on_players)
This function calculates player statistics based on play descriptions, play_by_play_movez (play descriptions) and list_data_on_players (list of player names)
 as inputs. The function defines patterns using regular expressions to match specific play events and increments corresponding statistics for each player.
After processing all plays, it calculates shooting percentages (FG%, 3P%, FT%) and total points (PTS) for each player. The results are stored in a list of dictionaries, where each dictionary represents a player's statistics.
-assign_player_to_teams(plays_by_plays_movez, lst_player_teams, statics)
This function assigns players to their respective teams and calculates team-level statistics.
by plays_by_plays_movez (play descriptions), lst_player_teams (list of player names), and statics
(player statistics) as inputs. It identifies the names of the two teams playing the game and maps
players to their corresponding teams based on play descriptions. The function then aggregates player statistics for each team, calculating total points, rebounds, assists, and other metrics. The results are stored in dictionaries (team_one_stats and team_two_stats) and printed.

## Installation
How to install your project? npm install? make? make re?
apart from downloading the txt file and importing several useful liberies no instalations were made
## Usage
How does it work?
``` 
have the actual NBA game data file ("nba_game_warriors_thunder_20181016.txt") available, 
as the code relies on the specific content and format of this file for parsing and analysis.
copy and past in  your code editior of choice make sure to have python installed on your pc. 
runing the code will print the statistics in the terminal.
```
### The Core Team
RAWLING MUKHEN

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
