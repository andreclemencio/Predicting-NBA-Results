from predict import *
import time

class Game:
	def __init__(self,home_team,away_team,home_odd,away_odd,date_):
		self.home_team = home_team
		self.away_team = away_team

		self.home_odd = home_odd
		self.away_odd = away_odd

		self.home_prob = 0
		self.away_prob = 0

		self.outcome = 0

		self.date_ = date_


def get_games(odds_file):
	games =[] 
	with open(odds_file,'r') as file:
		for line in file:
			line = line.split('\t')

			away_odd = float(line[0])
			home_odd = float(line[1])

			away_team = line[2]
			home_team = line[3]	

			date_ = line[4].replace('\n','')

			game = Game(home_team,away_team,home_odd,away_odd,date_)
			games.append(game)

	return games

def simulate_season(games,bankroll):
	date_ = ''
	won = 0
	spent = 0

	w = 0
	l = 0

	for g in games:
		print (g.home_team,g.away_team)
		print ("Odds:",g.home_odd,g.away_odd)
		print ("Probs:",g.home_prob,g.away_prob)

		fair_home_odd = 1/g.home_prob
		fair_away_odd = 1/g.away_prob

		if g.home_prob > g.away_prob:
			if fair_home_odd < g.home_odd:
				bet_amount = 0.1 * bankroll
				print ("Betting",bet_amount,"€ on",g.home_team)

				if g.outcome == 1:
					w += 1
					print (g.home_team,"won!")
					profit = (bet_amount * g.home_odd) - bet_amount
					bankroll += profit
					won += profit
					spent += bet_amount
				else:
					l += 1
					print (g.away_team,"won!")
					bankroll -= bet_amount
					spent += bet_amount
			else:
				print ("No Bets made!")
		else:
			if fair_away_odd < g.away_odd:
				bet_amount = 0.1 * bankroll
				print ("Betting",bet_amount,"€ on",g.away_team)

				if g.outcome == 2:
					w += 1
					print (g.away_team,"won!")
					profit = (bet_amount * g.away_odd) - bet_amount
					bankroll += profit
					won += profit
					spent += bet_amount
				else:
					l += 1
					print (g.home_team,"won!")
					bankroll -= bet_amount
					spent += bet_amount
			else:
				print ("No Bets made!")

		print ("Bankroll:",bankroll)
		print ("----------------------------------------------------")
		#time.sleep(10)

	print (w/(w+l))
	print (won,spent)



if __name__ == "__main__":
	odds_file = 'Data/Odds/1819gameodds.txt'

	games = get_games(odds_file)
	probs, outcomes = classification()

	for i in range (len(probs)):
		games[i].home_prob = probs[i][0]
		games[i].away_prob = probs[i][1]

		games[i].outcome = outcomes[i][0]


	bankroll = 100
	simulate_season(games,bankroll)