import unidecode

#Get overall values for players in the game
def get_overall_values(ratings, players):
	starters = 0
	reserves = 0
	nr_reserves = 0

	for i in range (len(players)):
		players[i] = unidecode.unidecode(players[i])

		if i < 5:
			starters += int(ratings[players[i]][0])
		else:
			nr_reserves += 1
			reserves += int(ratings[players[i]][0])

	avg_starters_overall = starters/5	
	avg_reserves_overall = reserves/nr_reserves

	return avg_starters_overall,avg_reserves_overall