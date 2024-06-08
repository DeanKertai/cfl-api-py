import requests
import time
import json
from typing import List
import lib.config as config


def get_from_api(category: str, season: int) -> List[List]:
	"""
	Gets player statistics from the CFL API for the specified category and season.
	:param category: 'passing', 'rushing', 'receiving', etc.
	:param season: The year to retrieve statistics for (e.g. 2024)
	:return: A list of lists representing the rows (players) and columns (stats)
	"""
	print(f'Getting {category} stats for {season}...')
	if category not in config.cfl_api_columns:
		raise ValueError(f'Invalid category: {category}')
	
	time.sleep(config.rate_limit_interval) # Prevent rate limiting
	req = requests.get(f'{config.base_url}&stat_category={category}&season={season}')

	if req.status_code != 200:
		raise ValueError(f'Failed to get data for {category} and {season}. Status code: {req.status_code}')

	# Response should be `{data: [[...]...]}`
	res_str = req.text
	data: List[List] = json.loads(res_str)['data']

	# Validate the response format
	if type(data) != list:
		raise ValueError(f'Expected a list, but got {type(data)}')

	# Validate the number of columns for each player
	if len(data) == 0:
		return []
	column_count = len(data[0])
	if column_count != len(config.cfl_api_columns[category]):
		expected = len(config.cfl_api_columns[category])
		raise ValueError(f'Expected {expected} columns, but got {column_count}')

	for player in data:
		if len(player) != column_count:
			raise ValueError(f'Player has {len(player)} columns, but expected {column_count}')
		for i, column in enumerate(player):
			column_name = config.cfl_api_columns[category][i]
			data_type = config.column_description[column_name]['type']
			if type(column) == str and data_type == 'int':
				player[i] = int(column)
			if type(column) == str and data_type == 'float':
				player[i] = float(column)

	return data
