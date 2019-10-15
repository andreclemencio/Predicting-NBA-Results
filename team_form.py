def get_team_form(teams,team_id):	
	team_id -= 1

	if len(teams[team_id].form) == 0:
		form = 0

	elif len(teams[team_id].form) < 5:
		wins = 0
		for i in range (len(teams[team_id].form)):
			if teams[team_id].form[i] == 1:
				wins += 1

		form = wins / len(teams[team_id].form)

	else:
		wins = 0
		for i in range (len(teams[team_id].form) - 5, len(teams[team_id].form)):
			if teams[team_id].form[i] == 1:
				wins += 1

		form = wins / 5

	return form