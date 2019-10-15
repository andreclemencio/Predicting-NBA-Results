def find_player(players, p):
	for i in range (len(players)):
		if players[i].name == p:
			index = i
			break

	return index


def get_game_score(team_players,players):	
		index = 0
		game_score_starters = 0 
		game_score_reserves = 0

		for p in team_players:
			player = find_player(players,p)

			if index < 5:

				game_score_starters += players[player].pts + (0.4 * players[player].fg) - (0.7 * players[player].fga) - (0.4 * (players[player].fta - players[player].ft)) + \
				(0.7 * players[player].orb) + (0.3 * players[player].drb) + players[player].stl + (0.7 * players[player].ast) + (0.7 * players[player].blk) - \
				players[player].tov

			else:
				game_score_reserves += players[player].pts + (0.4 * players[player].fg) - (0.7 * players[player].fga) - (0.4 * (players[player].fta - players[player].ft)) + \
				(0.7 * players[player].orb) + (0.3 * players[player].drb) + players[player].stl + (0.7 * players[player].ast) + (0.7 * players[player].blk) - \
				players[player].tov
				
			index +=1

		avg_game_score_starters = game_score_starters / 5
		avg_game_score_reserves = game_score_reserves / (index - 5)

		return avg_game_score_starters,avg_game_score_reserves


def get_threes_percentage(team_players,players):
	threes_made = 0
	threes_attempted = 0

	for p in team_players:
		player = find_player(players,p)

		threes_made += players[player].threes_m
		threes_attempted += players[player].threes_a


	avg_threes_made = threes_made / len(team_players)
	avg_threes_attempted = threes_attempted / len(team_players)

	print (avg_threes_made,avg_threes_attempted)

	return avg_threes_made, avg_threes_attempted