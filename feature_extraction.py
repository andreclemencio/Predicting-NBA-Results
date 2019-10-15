import csv
import pandas as pd
from datetime import date

from read_file import *
from overall_values import *
from player_stats import *
from team_stats import *
from rest_days import *
from win_percentage import *
from update_stats import *
from team_form import *

class Team:
	def __init__(self,team_id,pace,ortg,efg_p,tov_p,orb_p,shooting_p,efg_p_defense,tov_p_defense,orb_p_defense,shooting_p_defense):
		self.team_id = team_id

		self.last_game = 0

		self.nr_games = 0
		self.nr_wins = 0
		self.nr_losses = 0
		self.points_scored = 0
		self.points_conceded = 0
		self.form = []

		self.pace = pace
		self.ortg = ortg

		self.efg_p = efg_p
		self.tov_p = tov_p
		self.orb_p = orb_p
		self.shooting_p = shooting_p

		self.efg_p_defense = efg_p_defense
		self.tov_p_defense = tov_p_defense
		self.orb_p_defense = orb_p_defense
		self.shooting_p_defense = shooting_p_defense

class Player:
	def __init__(self,name,overall,pts,fg,fga,ft,fta,orb,drb,stl,ast,blk,tov):
		self.name = name
		self.overall = overall
		
		self.pts = pts
		self.fg = fg
		self.fga = fga
		self.ft = ft
		self.fta = fta
		self.orb = orb
		self.drb = drb
		self.stl = stl
		self.ast = ast
		self.blk = blk
		self.tov = tov

		self.nr_games = 0


def write_features_file(features,features_file):

	with open(features_file,'a') as file:

		for i in range (len(features)):
			for j in range (len(features[i])):
				file.write(str(features[i][j]))
				file.write('\t')
			file.write('\n')

def get_features(season_games,teams,players):
	features = []  
	#Iterate for every game of the season
	for i in range (len(season_games)):
		game_features = []

		#Team Id's
		home_team_id = season_games[i].home_id
		away_team_id = season_games[i].away_id

		#Overall
		avg_home_starters_overall, avg_home_reserves_overall = get_overall_values(players_ratings,season_games[i].home_players)
		avg_away_starters_overall, avg_away_reserves_overall = get_overall_values(players_ratings,season_games[i].away_players)

		#GameScore
		avg_game_score_home_starters, avg_game_score_home_reserves = get_game_score(season_games[i].home_players,players)
		avg_game_score_away_starters, avg_game_score_away_reserves = get_game_score(season_games[i].away_players,players)

		#Four factors 
		home_team_stats = get_team_stats(season_games[i].home_id,teams)
		away_team_stats = get_team_stats(season_games[i].away_id,teams) 

		#Rest Days
		home_rest_days = get_rest_days(season_games[i].date_,season_games[i].home_id,teams)
		away_rest_days = get_rest_days(season_games[i].date_,season_games[i].away_id,teams)

		#Win Percentage
		home_win_percentage = get_win_percentage(teams,season_games[i].home_id)
		away_win_percentage = get_win_percentage(teams,season_games[i].away_id)

		#Team Form (Win Percentage in the last 5 games)
		home_team_form = get_team_form(teams,season_games[i].home_id)
		away_team_form = get_team_form(teams,season_games[i].away_id)

		#Playoff or Reg Season
		playoff = season_games[i].playoffs

		#Final Score
		home_score = season_games[i].home_score
		away_score = season_games[i].away_score

		#UPDATE STATS

		#Player Stats
		update_player_stats(players, season_games[i].home_players, season_games[i].home_stats)
		update_player_stats(players, season_games[i].away_players, season_games[i].away_stats)

		#Team Stats
		update_team_stats(teams, season_games[i].home_id, season_games[i].hometeam_stats, season_games[i].awayteam_stats)
		update_team_stats(teams, season_games[i].away_id, season_games[i].awayteam_stats, season_games[i].hometeam_stats)

		#Date of last game
		teams[season_games[i].home_id-1].last_game = season_games[i].date_
		teams[season_games[i].away_id-1].last_game = season_games[i].date_

		#Results
		teams[season_games[i].home_id-1].nr_games += 1
		teams[season_games[i].away_id-1].nr_games += 1

		if season_games[i].home_score > season_games[i].away_score:
			teams[season_games[i].home_id-1].nr_wins += 1
			teams[season_games[i].home_id-1].form.append(1)
			teams[season_games[i].away_id-1].form.append(0)

		else:
			teams[season_games[i].away_id-1].nr_wins += 1
			teams[season_games[i].away_id-1].form.append(1)
			teams[season_games[i].home_id-1].form.append(0)

		game_features.append(home_team_id)
		game_features.append(away_team_id)

		game_features.append(avg_home_starters_overall)
		game_features.append(avg_home_reserves_overall)
		game_features.append(avg_away_starters_overall)
		game_features.append(avg_away_reserves_overall)

		game_features.append(avg_game_score_home_starters)
		game_features.append(avg_game_score_home_reserves)
		game_features.append(avg_game_score_away_starters)
		game_features.append(avg_game_score_away_reserves)

		for i in range (len(home_team_stats)):
			game_features.append(home_team_stats[i])
		for i in range (len(away_team_stats)):
			game_features.append(away_team_stats[i])

		game_features.append(home_rest_days)
		game_features.append(away_rest_days)

		game_features.append(home_win_percentage)
		game_features.append(away_win_percentage)

		game_features.append(home_team_form)
		game_features.append(away_team_form)

		game_features.append(playoff)

		if (home_score > away_score):
			game_features.append(1)
		else:
			game_features.append(2)
		
		#game_features.append(home_score)
		#game_features.append(away_score)

		features.append(game_features)
		
	return features

if __name__ == "__main__":
	season_file = 'Data/Seasons/season1819.txt'
	file_ratings = 'Data/Ratings/1819ratings.txt'

	stats_file = 'Data/Stats/1718stats.csv'
	team_stats = 'Data/Stats/1718teamstats.csv'

	features_file = 'Data/Features/1819features_binary.txt'

	players_ratings = dict()
	with open(file_ratings,'r') as ratings:
		for line in ratings:
			line = line.split('*')
			line[2] = line[2].replace('\n','')
			players_ratings[line[1]] = [line[0]]
			players_ratings[line[1]].append(line[2])

	teams = []
	for i in range (1,31):
		df = pd.read_csv(team_stats)

		pace = float(df['Unnamed: 13'][i])
		ortg = float(df['Unnamed: 10'][i])

		efg_p = float(df['Offense Four Factors'][i])
		tov_p = float(df['Offense Four Factors.1'][i])
		orb_p = float(df['Offense Four Factors.2'][i])
		shooting_p = float(df['Offense Four Factors.3'][i])

		efg_p_defense = float(df['Defense Four Factors'][i])
		tov_p_defense = float(df['Defense Four Factors.1'][i])
		orb_p_defense = float(df['Defense Four Factors.2'][i])
		shooting_p_defense = float(df['Defense Four Factors.3'][i])

		team = Team(i,pace,ortg,efg_p,tov_p,orb_p,shooting_p,efg_p_defense,tov_p_defense,orb_p_defense,shooting_p_defense)

		teams.append(team)

	players = []
	for p in players_ratings:
		df = pd.read_csv(stats_file)

		if p in df['Player'].values:
			pts = float(df[df.Player == p].PTS.values[0])
			fg = float(df[df.Player == p].FG.values[0])
			fga = float(df[df.Player == p].FGA.values[0])
			ft = float(df[df.Player == p].FT.values[0])
			fta = float(df[df.Player == p].FTA.values[0])
			orb = float(df[df.Player == p].ORB.values[0])
			drb = float(df[df.Player == p].DRB.values[0])
			stl = float(df[df.Player == p].STL.values[0])
			ast = float(df[df.Player == p].AST.values[0])
			blk = float(df[df.Player == p].BLK.values[0])
			tov = float(df[df.Player == p].TOV.values[0])

			player = Player(p,players_ratings[p][0],pts,fg,fga,ft,fta,orb,drb,stl,ast,blk,tov)
		else:
			player = Player(p,players_ratings[p][0],0,0,0,0,0,0,0,0,0,0,0)
		
		players.append(player)

	season_games = []
	season_games = read_file(season_file)

	features = get_features(season_games,teams,players)

	write_features_file(features,features_file)






