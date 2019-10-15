from datetime import date

def get_rest_days(date_,team_id,teams):
	todays_game = date_
	team_id -= 1

	if teams[team_id].last_game == 0:
		return 10
	else:
		team_rest_days = todays_game - teams[team_id].last_game
		return team_rest_days.days