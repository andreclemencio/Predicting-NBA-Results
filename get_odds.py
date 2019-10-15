import pandas as pd
import requests
from bs4 import BeautifulSoup

def us_to_decimal_odds(us_odd):
	us_odd = float(us_odd)
	if us_odd > 0:
		decimal_odd = (us_odd/100)+1
	else:
		decimal_odd = (100/abs(us_odd))+1

	return decimal_odd

def get_games(year):
	base_url = 'https://www.basketball-reference.com/leagues/NBA_'
	base_url = base_url+year+'_games-{}.html'
	
	box_score_url = 'https://www.basketball-reference.com{}'
	
	games = []
	
	for i in range (len(months)):
		print ("Scraping ", months[i])
		url = base_url.format(months[i])

		response = requests.get(url)	

		soup = BeautifulSoup(response.content, 'html.parser')

		table = soup.find(name='table',attrs={'id':'schedule'})
		df = pd.read_html(str(table))[0]

		index = -1
		for i in range(len(df.index)):
			if df.iloc[i].isnull().sum() == len(df.columns)-1:
				index = i

		away_teams = [df['Visitor/Neutral'].values]
		home_teams = [df['Home/Neutral'].values]
		date_ = [df['Date'].values]

		if index == -1:
			for j in range(len(away_teams[0])):
				game = []
				game.append(away_teams[0][j])
				game.append(home_teams[0][j])
				
				d = date_[0][j].split(' ')
				
				month = month_to_nr[d[1]]
				day = int(d[2].replace(',',''))
				
				if day < 10:
					final_date = str(month)+'0'+str(day)
				else:
					final_date = str(month)+str(day)

				game.append(final_date)
				games.append(game)

		else:
			for j in range(len(away_teams[0])):
				if j == index:
					continue
				else:
					game = []
					game.append(away_teams[0][j])
					game.append(home_teams[0][j])

					d = date_[0][j].split(' ')
				
					month = month_to_nr[d[1]]
					day = int(d[2].replace(',',''))
				
					if day < 10:
						final_date = str(month)+'0'+str(day)
					else:
						final_date = str(month)+str(day)

					game.append(final_date)
					games.append(game)
	return games

def get_odds():
	odds = []
	for i in range(0,len(df['Sheet1']['Team'].values),2):
		game = []
		game.append(df['Sheet1']['Team'][i])
		game.append(df['Sheet1']['Team'][i+1])

		game.append(us_to_decimal_odds(df['Sheet1']['ML'][i]))
		game.append(us_to_decimal_odds(df['Sheet1']['ML'][i+1]))

		game.append(df['Sheet1']['Date'][i])
		
		odds.append(game)

	return odds


def odds_to_games(target_file):
	with open(target_file,'a') as file: 
		for i in range (len(games)):
			for j in range (len(odds)):
				if (odds[j][0] == games[i][0]) and (odds[j][1] == games[i][1]) and (odds[j][4] == int(games[i][2])):
					file.write(str(odds[j][2]))
					file.write('\t')
					file.write(str(odds[j][3]))	
					file.write('\t')
					file.write(str(games[i][0]))	
					file.write('\t')
					file.write(str(games[i][1]))	
					file.write('\t')
					file.write(str(odds[i][4]))
					file.write('\n')


if __name__ == "__main__":
	months = ['october','november','december','january','february','march','april','may','june']
	month_to_nr = {'Oct':10,'Nov':11,'Dec':12,'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6}

	target_file = 'Data/Odds/1819gameodds.txt'

	df = pd.read_excel("Data/Odds/1819odds.xlsx", sheet_name=None)

	odds = get_odds()
	games = get_games('2019')

	print (games)

	odds_to_games(target_file)






