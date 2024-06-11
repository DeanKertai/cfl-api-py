from lib.cfl_api import get_from_api
from lib.player_db import PlayerDB
from lib.player_list import load_all_players

SEASON = 2024
CATEGORIES = ['passing', 'rushing', 'receiving', 'defence', 'field_goals']


if __name__ == '__main__':
	picked_players = load_all_players()

	db = PlayerDB()
	for category in CATEGORIES:
		player_rows = get_from_api(category, SEASON)
		for player_cols in player_rows:
			db.upsert(category, player_cols)
	print(f'Added {db.size()} players to the database')

	# Find players that are picked, but not in the CFL player list. This
	# could be due to an incorrect player ID, or a problem with the pick
	not_found = []
	for player in picked_players:
		if not db.has_player(player['id']):
			not_found.append(player)
	
	# Sort by team, then position, then name
	not_found.sort(key=lambda x: (x['team'], x['position'].value, x['name']))

	if len(not_found) > 0:
		print(f'WARNING! {len(not_found)} picked players were not found in the API response')
		for player in not_found:
			id = player['id']
			team = player['team']
			name = player['name']
			pos = player['position'].value
			print(f'{id} - {team} - {pos} - {name}')
