import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from datetime import date

class Game:
	def __init__(self, date_, home_id, away_id, players, home_stats, away_stats, four_factors, playoffs, home_division, away_division, home_conference, away_conference, home_score, away_score):
		#Date of the game
		self.date_ = date_

		#Teams in play
		self.home_id = home_id
		self.away_id = away_id

		#Players used
		self.players = players

		#Stats
		self.home_stats = home_stats
		self.away_stats = away_stats

		#Four factors
		self.four_factors = four_factors

		#If 0 - Regular season, if 1 - playoffs
		self.playoffs = playoffs

		#Division and conference
		self.home_division = home_division
		self.away_division = away_division
		self.home_conference = home_conference
		self.away_conference = away_conference

		#Final result
		self.home_score = home_score
		self.away_score = away_score

	def writefile(self):
		with open(season_file,'a') as file:
			file.write(str(self.date_))
			file.write('\t')
			file.write(str(self.home_id))
			file.write('\t')
			file.write(str(self.away_id))
			file.write('\t')

			for i in range(len(self.players)):
				file.write(str(self.players[i]))
				file.write('\t')

			for i in range(len(self.home_stats)):
				file.write(str(self.home_stats[i]))
				file.write('\t')

			for i in range(len(self.away_stats)):
				file.write(str(self.away_stats[i]))
				file.write('\t')

			file.write(str(self.four_factors))
			file.write('\t')

			file.write(str(self.playoffs))
			file.write('\t')

			file.write(str(self.home_division))
			file.write('\t')
			file.write(str(self.home_conference))
			file.write('\t')
			file.write(str(self.away_division))
			file.write('\t')
			file.write(str(self.away_conference))
			file.write('\t')

			file.write(str(self.home_score))
			file.write('\t')
			file.write(str(self.away_score))
			file.write('\n')

def get_stats(pts,fg,fga,ft,fta,oR,dR,stl,ast,blk,tov):
	stats = []

	pts_ = []
	for k in range(len(pts[0])):
		if pts[0][k] != 'PTS' and pts[0][k] != 'Team Totals':
			str_ = str(pts[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			pts_.append(str_)

	fg_ = []
	for k in range(len(fg[0])):
		if fg[0][k] != 'FG' and fg[0][k] != 'Team Totals':
			str_ = str(fg[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			fg_.append(str_)

	fga_ = []
	for k in range(len(fga[0])):
		if fga[0][k] != 'FGA' and fga[0][k] != 'Team Totals':
			str_ = str(fga[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			fga_.append(str_)

	ft_ = []
	for k in range(len(ft[0])):
		if ft[0][k] != 'FT' and ft[0][k] != 'Team Totals':
			str_ = str(ft[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			ft_.append(str_)

	fta_ = []
	for k in range(len(fta[0])):
		if fta[0][k] != 'FTA' and fta[0][k] != 'Team Totals':
			str_ = str(fta[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			fta_.append(str_)

	oR_ = []
	for k in range(len(oR[0])):
		if oR[0][k] != 'ORB' and oR[0][k] != 'Team Totals':
			str_ = str(oR[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			oR_.append(str_)

	dR_ = []
	for k in range(len(dR[0])):
		if dR[0][k] != 'DRB' and dR[0][k] != 'Team Totals':
			str_ = str(dR[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			dR_.append(str_)

	stl_ = []
	for k in range(len(stl[0])):
		if stl[0][k] != 'STL' and stl[0][k] != 'Team Totals':
			str_ = str(stl[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			stl_.append(str_)

	ast_ = []
	for k in range(len(ast[0])):
		if ast[0][k] != 'AST' and ast[0][k] != 'Team Totals':
			str_ = str(ast[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			ast_.append(str_)

	blk_ = []
	for k in range(len(blk[0])):
		if blk[0][k] != 'BLK' and blk[0][k] != 'Team Totals':
			str_ = str(blk[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			blk_.append(str_)

	tov_ = []
	for k in range(len(tov[0])):
		if tov[0][k] != 'TOV' and tov[0][k] != 'Team Totals':
			str_ = str(tov[0][k]).replace('\'','')
			str_ = str_.replace('[','')
			str_ = str_.replace(']','')
			str_ = str_.replace('"','')

			tov_.append(str_)

	stats.append(pts_)
	stats.append(fg_)
	stats.append(fga_)
	stats.append(ft_)
	stats.append(fta_)
	stats.append(oR_)
	stats.append(dR_)
	stats.append(stl_)
	stats.append(ast_)
	stats.append(blk_)
	stats.append(tov_)
	
	return stats

def scrap_data(year):
	base_url = 'https://www.basketball-reference.com/leagues/NBA_'
	base_url = base_url+year+'_games-{}.html'
	
	box_score_url = 'https://www.basketball-reference.com{}'

	index = -1
	for i in range (len(months)):
		print ("Scraping ", months[i])
		url = base_url.format(months[i])

		response = requests.get(url)	

		soup = BeautifulSoup(response.content, 'html.parser')

		table = soup.find(name='table',attrs={'id':'schedule'})
		df = pd.read_html(str(table))[0]

		for k in range(len(df.index)):
			if df.iloc[k].isnull().sum() == len(df.columns)-1:
				index = k

		games = []

		away_teams = [df['Visitor/Neutral'].values]
		home_teams = [df['Home/Neutral'].values]
		away_pts = [df['PTS'].values]
		home_pts = [df['PTS.1'].values]
		date_ = [df['Date'].values]

		#Check if playoff or regular season (pre ant post all star game)
		if index == -1:
			
			for j in range(len(away_teams[0])):
				game = []
				game.append(away_teams[0][j])
				game.append(home_teams[0][j])
				game.append(away_pts[0][j])
				game.append(home_pts[0][j])
				game.append(0)
				game.append(date_[0][j])
				games.append(game)
		else:
			if months[i] == 'april':
				for j in range(len(away_teams[0])):
					if j == index:
						continue
					elif j < index:
						game = []
						game.append(away_teams[0][j])
						game.append(home_teams[0][j])
						game.append(away_pts[0][j])
						game.append(home_pts[0][j])
						game.append(0)
						game.append(date_[0][j])
						games.append(game)
					elif j > index:
						game = []
						game.append(away_teams[0][j])
						game.append(home_teams[0][j])
						game.append(away_pts[0][j])
						game.append(home_pts[0][j])
						game.append(1)
						game.append(date_[0][j])
						games.append(game)
			else:
				for j in range(len(away_teams[0])):
					game = []
					game.append(away_teams[0][j])
					game.append(home_teams[0][j])
					game.append(away_pts[0][j])
					game.append(home_pts[0][j])
					game.append(1)
					game.append(date_[0][j])
					games.append(game)

		links = []
		for link in soup.findAll('a', attrs={'href': re.compile("^/boxscores/")}):
			if '.html' in link.get('href'):
				links.append(link.get('href'))

		for j in range(len(games)):
			games[j].append(links[j])

		for j in range(len(games)):
			print ("Scraping ",games[j][0],games[j][1])

			box_score_url = box_score_url.format(games[j][6])

			response = requests.get(box_score_url)
			soup = BeautifulSoup(response.content, 'html.parser')

			if int(year) == 2019 and (months[i] == 'january' or months[i] == 'february' or months[i] == 'march' or months[i] == 'april' or months[i] == 'may' or months[i] == 'june'):
				id_away = 'box_'+team_name[games[j][0]][0].lower()+'_basic'
				id_home = 'box_'+team_name[games[j][1]][0].lower()+'_basic'
			else:
				id_away = 'box-'+team_name[games[j][0]][0]+'-game-basic'
				id_home = 'box-'+team_name[games[j][1]][0]+'-game-basic'

			print (id_home)
			#Date
			month = month_to_nr[(games[j][5].split(' '))[1]]
			day = int((games[j][5].split(' '))[2].replace(',',''))
			year = int((games[j][5].split(' '))[3])
			todays_game = date(year,month,day)

			#Division and conference of the teams in play
			home_division = team_name[games[j][1]][2]
			home_conference = team_name[games[j][1]][3]
			away_division = team_name[games[j][0]][2]
			away_conference = team_name[games[j][0]][3]

			#Teams id
			home_id = team_name[games[j][1]][1]
			away_id = team_name[games[j][0]][1]

			#Playoffs or regular season
			playoffs = games[j][4]

			#Final result
			home_score = games[j][3]
			away_score = games[j][2]
			
			box_stats = soup.find(name='table',attrs={'id':id_away})
			df = pd.read_html(str(box_stats))
			df = df[0]

			players_away = [df['Unnamed: 0_level_0'].values]
			#Stats (points, assists, offensive and defensive rebounds, etc for each player)
			pts_away = [df['Unnamed: 19_level_0'].values]
			fg_away = [df['Unnamed: 2_level_0'].values]
			fga_away = [df['Unnamed: 3_level_0'].values]
			ft_away = [df['Unnamed: 8_level_0'].values]
			fta_away = [df['Unnamed: 9_level_0'].values]
			or_away = [df['Unnamed: 11_level_0'].values]
			dr_away = [df['Unnamed: 12_level_0'].values]
			stl_away = [df['Unnamed: 15_level_0'].values]
			ast_away = [df['Unnamed: 14_level_0'].values]
			blk_away = [df['Unnamed: 16_level_0'].values]
			tov_away = [df['Unnamed: 17_level_0'].values]

			away_stats = get_stats(pts_away,fg_away,fga_away,ft_away,fta_away,or_away,dr_away,stl_away,ast_away,blk_away,tov_away)

			box_stats = soup.find(name='table',attrs={'id':id_home})
			df = pd.read_html(str(box_stats))
			df = df[0]

			players_home = [df['Unnamed: 0_level_0'].values]

			pts_home = [df['Unnamed: 19_level_0'].values]
			fg_home = [df['Unnamed: 2_level_0'].values]
			fga_home = [df['Unnamed: 3_level_0'].values]
			ft_home = [df['Unnamed: 8_level_0'].values]
			fta_home = [df['Unnamed: 9_level_0'].values]
			or_home = [df['Unnamed: 11_level_0'].values]
			dr_home = [df['Unnamed: 12_level_0'].values]
			stl_home = [df['Unnamed: 15_level_0'].values]
			ast_home = [df['Unnamed: 14_level_0'].values]
			blk_home = [df['Unnamed: 16_level_0'].values]
			tov_home = [df['Unnamed: 17_level_0'].values]

			home_stats = get_stats(pts_home,fg_home,fga_home,ft_home,fta_home,or_home,dr_home,stl_home,ast_home,blk_home,tov_home)

			#Get players used in the game
			home_players = []
			away_players = []

			for k in range(len(players_away[0])):
				if players_away[0][k] != 'Reserves' and players_away[0][k] != 'Team Totals':
					str_ = str(players_away[0][k]).replace('\'','')
					str_ = str_.replace('[','')
					str_ = str_.replace(']','')
					str_ = str_.replace('"','')

					away_players.append(str_)

			for k in range(len(players_home[0])):
				if players_home[0][k] != 'Reserves' and players_home[0][k] != 'Team Totals':
					str_ = str(players_home[0][k]).replace('\'','')
					str_ = str_.replace('[','')
					str_ = str_.replace(']','')
					str_ = str_.replace('"','')

					home_players.append(str_)

			players = []
			players.append(home_players)
			players.append(away_players)

			box_stats = soup.find(name='div',attrs={'id':'all_four_factors'})
			for el in box_stats:
				if str(type(el)) == '<class \'bs4.element.Comment\'>':
					Dsoup = BeautifulSoup(el,features='html.parser')
					factors = Dsoup.find(name='table',attrs={'id':'four_factors'})
					df = pd.read_html(str(factors))[0]


			four_factors = []

			#Pace
			four_factors.append(df[1][2])
			four_factors.append(df[1][3])
			#eFG%
			four_factors.append(df[2][2])
			four_factors.append(df[2][3])
			#tov%
			four_factors.append(df[3][2])
			four_factors.append(df[3][3])
			#orb%
			four_factors.append(df[4][2])
			four_factors.append(df[4][3])
			#ft/fga
			four_factors.append(df[5][2])
			four_factors.append(df[5][3])
			#ortg
			four_factors.append(df[6][2])
			four_factors.append(df[6][3])

			box_score_url = 'https://www.basketball-reference.com{}'

			g = Game(todays_game,home_id,away_id,players,home_stats,away_stats,four_factors,playoffs,home_division,away_division,home_conference,away_conference,home_score,away_score)
			g.writefile()

if __name__ == "__main__":
	months = ['october','november','december','january','february','march','april','may','june']
	month_to_nr = {'Oct':10,'Nov':11,'Dec':12,'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6}

	''' Contains acronym, team_id, division and conference
	Atlantic - 0 
	Central - 1
	Southeast - 2
	Northwest - 3
	Pacific - 4
	Southwest - 5

	East - 0
	West - 1

	wins
	losses
	results [] (1-win, 0-loss)
	'''
	team_name ={'Atlanta Hawks':['ATL',1,2,0,0,0,[]], 'Boston Celtics':['BOS',2,0,0,0,0,[]], 'Brooklyn Nets':['BRK',3,0,0,0,0,[]], 'Charlotte Hornets':['CHO',4,2,0,0,0,[]],
	'Chicago Bulls':['CHI',5,1,0,0,0,[]],'Cleveland Cavaliers':['CLE',6,1,0,0,0,[]],'Dallas Mavericks':['DAL',7,5,1,0,0,[]],'Denver Nuggets':['DEN',8,3,1,0,0,[]],
	'Detroit Pistons':['DET',9,1,0,0,0,[]],'Golden State Warriors':['GSW',10,4,1,0,0,[]],'Houston Rockets':['HOU',11,5,1,0,0,[]], 'Indiana Pacers':['IND',12,1,0,0,0,[]],
	'Los Angeles Clippers':['LAC',13,4,1,0,0,[]],'Los Angeles Lakers':['LAL',14,4,1,0,0,[]],'Memphis Grizzlies':['MEM',15,5,1,0,0,[]],'Miami Heat':['MIA',16,2,0,0,0,[]],
	'Milwaukee Bucks':['MIL',17,1,0,0,0,[]],'Minnesota Timberwolves':['MIN',18,3,1,0,0,[]],'New Orleans Pelicans':['NOP',19,5,1,0,0,[]],'New York Knicks':['NYK',20,0,0,0,0,[]],
	'Oklahoma City Thunder':['OKC',21,3,1,0,0,[]],'Orlando Magic':['ORL',22,2,0,0,0,[]],'Philadelphia 76ers':['PHI',23,0,0,0,0,[]],'Phoenix Suns':['PHO',24,4,1,0,0,[]], 
	'Portland Trail Blazers':['POR',25,3,1,0,0,[]],'Sacramento Kings':['SAC',26,4,1,0,0,[]],'San Antonio Spurs':['SAS',27,5,1,0,0,[]],'Toronto Raptors':['TOR',28,0,0,0,0,[]],
	'Utah Jazz':['UTA',29,3,1,0,0,[]],'Washington Wizards':['WAS',30,2,0,0,0,[]]}

	season_file = 'Data/Seasons/season1819.txt'
	
	scrap_data('2019')





















