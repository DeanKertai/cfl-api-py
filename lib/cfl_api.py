import requests
import time
import json
from typing import List
from lib.config import Category, StatType, cfl_api_columns, column_types, category_api_names

base_url = 'https://www.cfl.ca/wp-content/themes/cfl.ca/inc/admin-ajax.php?action=get_league_stats'
rate_limit_interval = 1  # seconds


def get_from_api(category: Category, year: int) -> List[List]:
	"""
	Gets player statistics from the CFL API for the specified category and season.
	:return: A list of lists representing the rows (players) and columns (stats)
	"""
	print(f'Getting {category.value} stats for {year}...')
	
	time.sleep(rate_limit_interval) # Prevent rate limiting
	api_category_str = category_api_names[category]
	req = requests.get(f'{base_url}&stat_category={api_category_str}&season={year}')

	if req.status_code != 200:
		raise ValueError(f'Failed to get data. Status code: {req.status_code}')

	# Response should be `{data: [[...]...]}`
	res_str = req.json()
	data: List[List] = res_str['data']

	# Validate the response format
	if type(data) != list:
		raise ValueError(f'Expected a list, but got {type(data)}')

	# Validate the number of columns for each player
	if len(data) == 0:
		return []
	column_count = len(data[0])
	api_columns = cfl_api_columns[category]
	expected_col_count = len(api_columns)
	if column_count != expected_col_count:
		raise ValueError(f'Expected {expected_col_count} columns, but got {column_count}')

	for player_cols in data:
		if len(player_cols) != column_count:
			raise ValueError(f'Player has {len(player_cols)} columns, but expected {column_count}')
		for i, column in enumerate(player_cols):
			column_stat = api_columns[i]
			data_type = column_types[column_stat]
			if type(column) == str and data_type == StatType.Int:
				player_cols[i] = int(column)
			if type(column) == str and data_type == StatType.Float:
				player_cols[i] = float(column)

	return data
