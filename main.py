from lib.cfl_api import get_from_api
from lib.player_db import PlayerDB
from lib.player_list import load_all_players
from lib.config import Category

SEASON_YEAR = 2024

if __name__ == '__main__':
	picked_players = load_all_players()

	db = PlayerDB()
	for category in Category:
		player_rows = get_from_api(category, SEASON_YEAR)
		for player_cols in player_rows:
			db.upsert(category, player_cols)
	print(f'Added {db.size()} players to the database')

	db.save_csv(Category.Passing, 'output/passing.csv')
	db.save_csv(Category.Rushing, 'output/rushing.csv')
	db.save_csv(Category.Receiving, 'output/receiving.csv')
	db.save_csv(Category.FieldGoals, 'output/kickers.csv')
	db.save_csv(Category.Defence, 'output/defence.csv')

	# Find players that are picked, but not in the CFL player list. This
	# could be due to an incorrect player ID, or a problem with the pick
	not_found = []
	for player in picked_players:
		if not db.has_player(player['id']):
			not_found.append(player)
	
	# Sort by team, then category, then name
	not_found.sort(key=lambda x: (x['team'], x['category'].value, x['name']))

	if len(not_found) > 0:
		print(f'WARNING! {len(not_found)} picked players were not found in the API response')
		for player in not_found:
			id = player['id']
			team = player['team']
			name = player['name']
			category = player['category'].value
			print(f'{id} - {team} - {category} - {name}')

