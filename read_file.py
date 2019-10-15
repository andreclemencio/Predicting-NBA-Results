from datetime import date

class Game:
	def __init__(self, date_, home_id, away_id, home_players, away_players, home_stats, away_stats, hometeam_stats, awayteam_stats, playoffs, division, conference, home_score, away_score):
		#Date of the game
		self.date_ = date_

		#Teams in play
		self.home_id = home_id
		self.away_id = away_id

		#Players used
		self.home_players = home_players
		self.away_players = away_players

		#Stats
		self.home_stats = home_stats
		self.away_stats = away_stats

		#Team stats
		self.hometeam_stats = hometeam_stats
		self.awayteam_stats = awayteam_stats

		#If 0 - Regular season, if 1 - playoffs
		self.playoffs = playoffs

		#Division and conference
		self.division = division
		self.conference = conference

		#Final result
		self.home_score = home_score
		self.away_score = away_score


#Read season file
def read_file(season_file):
	games = []

	with open(season_file,'r') as file:
		for line in file:
			line = line.split('\t')

			#Data
			date_ = line[0]
			date_ = date_.split("-")
			month = int(date_[1])
			day = int(date_[2])
			year = int(date_[0])
			date_ = date(year,month,day)

			#Team id's
			home_id = int(line[1])
			away_id = int(line[2])

			#Players
			line[3] = line[3].replace("[","")
			line[3] = line[3].replace("]",'')
			line[3] = line[3].replace("\'",'')
			line[3] = line[3].split(', ')
			home_players = line[3]

			line[4] = line[4].replace("[","")
			line[4] = line[4].replace("]",'')
			line[4] = line[4].replace("\'",'')
			line[4] = line[4].split(', ')
			away_players = line[4]

			#Player Stats
			home_stats = []
			for i in range(5,16):
				aux = []

				line[i] = line[i].replace("[","")
				line[i] = line[i].replace("]",'')
				line[i] = line[i].replace("\'",'')
				line[i] = line[i].replace(",",'')

				line[i] = line[i].split(' ')

				for j in range(len(line[i])-1):
					if line[i][j] != 'nan':
						aux.append(float(line[i][j]))
					else:
						aux.append(0)

				home_stats.append(aux)

			away_stats = []
			for i in range(16,27):
				aux = []

				line[i] = line[i].replace("[","")
				line[i] = line[i].replace("]",'')
				line[i] = line[i].replace("\'",'')
				line[i] = line[i].replace(",",'')

				line[i] = line[i].split(' ')

				for j in range(len(line[i])-1):
					if line[i][j] != 'nan':
						aux.append(float(line[i][j]))
					else:
						aux.append(0)

				away_stats.append(aux)

			#Team Stats
			line[27] = line[27].replace("[","")
			line[27] = line[27].replace("]",'')
			line[27] = line[27].replace("\'",'')
			line[27] = line[27].split(', ')
			
			hometeam_stats = []
			hometeam_stats.append(float(line[27][0]))
			hometeam_stats.append(float(line[27][3]))
			hometeam_stats.append(float(line[27][5]))
			hometeam_stats.append(float(line[27][7]))
			hometeam_stats.append(float(line[27][9]))
			hometeam_stats.append(float(line[27][11]))

			awayteam_stats = []
			awayteam_stats.append(float(line[27][0]))
			awayteam_stats.append(float(line[27][2]))
			awayteam_stats.append(float(line[27][4]))
			awayteam_stats.append(float(line[27][6]))
			awayteam_stats.append(float(line[27][8]))
			awayteam_stats.append(float(line[27][10]))

			#Playoffs
			playoffs = int(line[28])

			#Conference and Division
			if line[29] == line[31]:
				division = 1
			else:
				division = 0

			if line[30] == line[32]:
				conference = 1
			else:
				conference = 0

			#Scores
			home_score = float(line[33])
			away_score = float(line[34].replace("\n",""))

			games.append(Game(date_,home_id,away_id,home_players,away_players,home_stats,away_stats,hometeam_stats,awayteam_stats,playoffs,division,conference,home_score,away_score))

	return games
