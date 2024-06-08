from lib.cfl_api import get_from_api
from lib.player_db import PlayerDB

SEASON = 2024
CATEGORIES = ['passing', 'rushing', 'receiving', 'defence', 'field_goals']

if __name__ == '__main__':
	db = PlayerDB()
	for category in CATEGORIES:
		player_rows = get_from_api(category, SEASON)
		for player in player_rows:
			db.upsert(category, player)
	print(f'Added {db.size()} players to the database')
	db.print_all()
