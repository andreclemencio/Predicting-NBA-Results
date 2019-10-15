def get_team_stats(team_id, teams):
	team_stats = []
	team_id -= 1
	
	#Pace
	pace = teams[team_id].pace

	#Offensive Rating
	ortg = teams[team_id].ortg

	#Four Factors Offense
	efg_p = teams[team_id].efg_p
	tov_p = teams[team_id].tov_p
	orb_p = teams[team_id].orb_p
	shooting_p = teams[team_id].shooting_p

	#Four Factors Defense
	efg_p_defense = teams[team_id].efg_p_defense
	tov_p_defense = teams[team_id].tov_p_defense
	orb_p_defense = teams[team_id].orb_p_defense
	shooting_p_defense = teams[team_id].shooting_p_defense

	team_stats.append(pace)
	team_stats.append(ortg)
	team_stats.append(efg_p)
	team_stats.append(tov_p)
	team_stats.append(orb_p)
	team_stats.append(shooting_p)

	team_stats.append(efg_p_defense)
	team_stats.append(tov_p_defense)
	team_stats.append(orb_p_defense)
	team_stats.append(shooting_p_defense)

	return team_stats