# Welcome to  NBA Game Analysis poject
Welcome to the NBA Game Analysis project! This project aims to analyze NBA game data to extract player statistics, team performances, and predict game outcomes. In this README, you'll find an overview of the project, how to use it, and the key components involved.

# Overview
The NBA Game Analysis project provides a set of Python scripts to analyze NBA game data, extract player statistics, and predict game outcomes. It includes functions to load game data, preprocess it, analyze player performances, visualize statistics, and predict game results.

# How I solve the problem?
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

# Install the required dependencies:
```python
pip install pandas
```
# Run the main script to perform NBA game analysis:
```python
python main.py
```

# Installation
To use this project, follow these steps:

1. Clone the repository to your local machine:
   
```python
   git clone https://github.com/your-username/nba-game-analysis.git
```


apart from downloading the txt file and importing several useful liberies no instalations were made
# Usage
How does it work?
The project consists of several key components:
## 1. Loading NBA Game Data
   The 'load_nba_game_data' function is used to load NBA game data from a text file
``` 
# Load NBA game data
play_by_play_moves = load_nba_game_data("nba_game_warriors_thunder_20181016.txt")

```
## 2. Analyzing NBA Game Data
  The new_analyze_game_nba function extracts player names from the game data.
  ```
  # Analyze NBA game and extract player names
  player_names = new_analyze_game_nba(play_by_play_moves)
  ```
The call_players_statz function calculates player statistics based on the game data and player names.
```
# Calculate player statistics
player_statistics = call_players_statz(play_by_play_moves, player_names)
```
## 3. Mapping Players to Teams
The assign_player_to_teams function maps players to their respective teams and aggregates team statistics.
```
# Map players to their respective teams
team_mappings = assign_player_to_teams(play_by_play_moves, player_names, player_statistics)
```
## 4. Preprocessing Data
 preprocess NBA game data using the preprocess_nba_game_data function.
 ```
# Preprocess NBA game data
preprocessed_data = preprocess_nba_game_data(game_data)
```
## 5. Visualization
  Visualize NBA game statistics using the 'visualize_nba_stats' function.
```
# Visualize NBA game statistics
visualize_nba_stats(player_statistics)
```
## 6. Prediction
  Predict NBA game outcomes using the 'predict_game_outcome' function.
  ```
# Predict NBA game outcomes
predicted_outcomes = predict_game_outcome(preprocessed_data)
  ```
## 7. Saving and Exporting Results
  Save and export analysis results using the following functions:
  ```
  # Save analysis results
save_analysis_results(results, "analysis_results.txt")

# Export analysis to CSV
export_to_csv(results, "analysis_results.csv")
  ```
##  Conclusion
The NBA Game Analysis project provides a comprehensive toolkit for analyzing NBA game data, extracting player statistics, and predicting game outcomes. Whether you're a sports enthusiast, data analyst, or machine learning practitioner, this project offers valuable insights into NBA game dynamics. Start exploring and analyzing NBA game data today!
 
## License

This project is licensed under the [MIT License](LICENSE).
  
### The Core Team
[Mbah Rawling Mukhen](https://github.com/Rawlingsofficial)

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
