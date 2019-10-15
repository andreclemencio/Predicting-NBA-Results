def get_win_percentage(teams,team_id):
	team_id -= 1

	if teams[team_id].nr_games == 0:
		return 0
	else:
		win_p = teams[team_id].nr_wins / teams[team_id].nr_games
		return win_p