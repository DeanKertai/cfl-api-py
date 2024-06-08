from typing import List
from lib import config

class PlayerDB:
	def __init__(self) -> None:
		# List of players and their stats.
		# Each player is a dictionary in this format:
		# {
		#   'name': 'HARRIS, Trevor',
		#   'team': 'SSK',
		#   'stats': {
		#     'yds': 5000,
		#     'tds': 30,
		#     ...
		#   },
		# }
		self.players = []

	def get_player(self, name: str, team: str) -> dict:
		"""
		Returns the player with the specified name and team.
		:param name: e.g. "HARRIS, Trevor"
		:param team: e.g. "SSK"
		:return: The player's dictionary
		"""
		for player in self.players:
			if player['name'] == name and player['team'] == team:
				return player
		return None
	
	def size(self) -> int:
		"""
		Returns the number of players in the database.
		"""
		return len(self.players)
	
	def print_all(self) -> None:
		"""
		Prints all players in the database.
		"""
		for player in self.players:
			print(player['name'], player['team'])
			
			for stat, value in player['stats'].items():
				is_pertinent = config.column_description[stat]['pertinent']
				if is_pertinent:
					print(f'  {stat}: {value}')

			print()
	
	def upsert(self, category: str, column_values: List) -> None:
		"""
		Takes a player's name, the raw values from the CFL api (simply list), and a list
		of column names indicating what each value is, and adds the player to the database.
		This will add the player if they do not exist, and add the stats if the player
		already exists
		:param player_name: e.g. "HARRIS, Trevor"
		:param column_names: e.g. ['name', 'team', 'yds', ...]
		:param column_values: e.g. ['HARRIS, Trevor', 'CGY', 5000, ...]
		"""
		if category not in config.cfl_api_columns:
			raise ValueError(f'Invalid category: {category}')
		
		column_names = config.cfl_api_columns[category]

		if len(column_names) != len(column_values):
			raise ValueError('Column names and values must be the same length')
		name_index = column_names.index('name')
		team_index = column_names.index('team')

		name = column_values[name_index]
		team = column_values[team_index]

		existing = self.get_player(name, team)
		if existing is not None:
			print(f'Updating record for {name} ({team})')
			stats = existing['stats']
			for i, col in enumerate(column_names):
				if col not in ['name', 'team']:
					stats[col] = column_values[i]
		else:
			print(f'Adding record for {name} ({team})')
			stats = dict(zip(column_names, column_values))
			self.players.append({'name': name, 'team': team, 'stats': stats})

