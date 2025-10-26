import csv
import re

def load_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        
        fields = next(csvreader)

        for row in csvreader:
            result.append(row)

    return result

def is_away_team(away_team, current_team):
    return away_team == current_team

def analyse_nba_game(play_by_play_moves):
    results = {"home_team": {"name": "", "players_data": {}}, "away_team": {"name": "otherteam", "players_data":{}}}
    for play in play_by_play_moves:
        current_team = play[2]
        home_team = play[3]
        away_team = play[4]
        current_action = play[7]

        three_pts_regexp = re.compile(r'(.*) makes 3-pt jump shot from')
        data = three_pts_regexp.search(current_action)

        if data:

            player_name = data[1]
            print(current_action)
            print(player_name)

        if is_away_team(away_team, current_team):
            team_key = "away_team"
    else:
        team_key = "home_team"

    if player_name not in results[team_key]["players_data"]:
        results[team_key]["players_data"][player_name] = {"3P": 0}

    results[team_key]["players_data"][player_name]["3P"] += 1
    return results

def _main():
    play_by_play_moves = load_data("nba_game_warriors_thunder_20181016.txt")
    analyse_nba_game(play_by_play_moves)

_main()