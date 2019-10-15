def find_player(players, p):
	for i in range (len(players)):
		if players[i].name == p:
			index = i
			break

	return index

def update_player_stats(players, players_used, players_stats):	
	i = 0
	for p in players_used:
		player = find_player(players,p)

		if players[player].nr_games == 0:
			players[player].pts = players_stats[0][i]
			players[player].fg = players_stats[1][i]
			players[player].fga = players_stats[2][i]
			players[player].ft = players_stats[3][i]
			players[player].fta = players_stats[4][i]
			players[player].orb = players_stats[5][i]
			players[player].drb = players_stats[6][i]
			players[player].stl = players_stats[7][i]
			players[player].ast = players_stats[8][i]
			players[player].blk = players_stats[9][i]
			players[player].tov = players_stats[10][i]

		else:
			players[player].pts = ((players[player].pts * players[player].nr_games) + players_stats[0][i])/ (players[player].nr_games + 1)
			players[player].fg = ((players[player].fg * players[player].nr_games) + players_stats[1][i])/ (players[player].nr_games + 1)
			players[player].fga = ((players[player].fga * players[player].nr_games) + players_stats[2][i])/ (players[player].nr_games + 1)
			players[player].ft = ((players[player].ft * players[player].nr_games) + players_stats[3][i])/ (players[player].nr_games + 1)
			players[player].fta = ((players[player].fta * players[player].nr_games) + players_stats[4][i])/ (players[player].nr_games + 1)
			players[player].orb = ((players[player].orb * players[player].nr_games) + players_stats[5][i])/ (players[player].nr_games + 1)
			players[player].drb = ((players[player].drb * players[player].nr_games) + players_stats[6][i])/ (players[player].nr_games + 1)
			players[player].stl = ((players[player].stl * players[player].nr_games) + players_stats[7][i])/ (players[player].nr_games + 1)
			players[player].ast = ((players[player].ast * players[player].nr_games) + players_stats[8][i])/ (players[player].nr_games + 1)
			players[player].blk = ((players[player].blk * players[player].nr_games) + players_stats[9][i])/ (players[player].nr_games + 1)
			players[player].tov = ((players[player].tov * players[player].nr_games) + players_stats[10][i])/ (players[player].nr_games + 1)

		players[player].nr_games += 1
		i += 1

def update_team_stats(teams, team_id, team_stats, opponent_stats):
	team_id -= 1

	if teams[team_id].nr_games == 0:
		teams[team_id].pace = team_stats[0]
		teams[team_id].ortg = team_stats[5]

		teams[team_id].efg_p = team_stats[1]
		teams[team_id].tov_p = team_stats[2]
		teams[team_id].orb_p = team_stats[3]
		teams[team_id].shooting_p = team_stats[4]

		teams[team_id].efg_p_defense = opponent_stats[1]
		teams[team_id].tov_p_defense = opponent_stats[2]
		teams[team_id].orb_p_defense = opponent_stats[3]
		teams[team_id].shooting_p_defense = opponent_stats[4]

	else:
		teams[team_id].pace = ((teams[team_id].pace * teams[team_id].nr_games) + team_stats[0])/ (teams[team_id].nr_games+1)
		teams[team_id].ortg = ((teams[team_id].ortg * teams[team_id].nr_games) + team_stats[5])/ (teams[team_id].nr_games+1)

		teams[team_id].efg_p = ((teams[team_id].efg_p * teams[team_id].nr_games) + team_stats[1])/ (teams[team_id].nr_games+1)
		teams[team_id].tov_p = ((teams[team_id].tov_p * teams[team_id].nr_games) + team_stats[2])/ (teams[team_id].nr_games+1)
		teams[team_id].orb_p = ((teams[team_id].orb_p * teams[team_id].nr_games) + team_stats[3])/ (teams[team_id].nr_games+1)
		teams[team_id].shooting_p = ((teams[team_id].shooting_p * teams[team_id].nr_games) + team_stats[4])/ (teams[team_id].nr_games+1)

		teams[team_id].efg_p_defense = ((teams[team_id].efg_p_defense * teams[team_id].nr_games) + opponent_stats[1])/ (teams[team_id].nr_games+1)
		teams[team_id].tov_p_defense = ((teams[team_id].tov_p_defense * teams[team_id].nr_games) + opponent_stats[2])/ (teams[team_id].nr_games+1)
		teams[team_id].orb_p_defense = ((teams[team_id].orb_p_defense * teams[team_id].nr_games) + opponent_stats[3])/ (teams[team_id].nr_games+1)
		teams[team_id].shooting_p_defense = ((teams[team_id].shooting_p_defense * teams[team_id].nr_games) + opponent_stats[4])/ (teams[team_id].nr_games+1)






