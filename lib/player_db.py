from typing import List, TypedDict
from lib import config
from lib.player import get_id_from_url

class DbItem(TypedDict):
	id: int
	name: str
	team: str
	stats: dict

class PlayerDB:
	def __init__(self) -> None:
		self.list: List[DbItem] = []

	def get_by_id(self, player_id: int) -> DbItem:
		"""
		Returns the player with the specified ID
		"""
		for player in self.list:
			if player['id'] == player_id:
				return player
		return None

	def get_by_name(self, name: str) -> List[DbItem]:
		"""
		Returns the players with the specified name
		"""
		result = []
		compare_name = name.lower().strip()
		for player in self.list:
			player_name = player['name'].lower().strip()
			if player_name == compare_name:
				result.append(player)
		return result
	
	def get_all(self) -> List[DbItem]:
		"""
		Returns all players in the database.
		"""
		return self.list
	
	def has_player(self, id: int) -> bool:
		"""
		Returns True if the player is in the database, False otherwise.
		"""
		return self.get_by_id(id) is not None
	
	def size(self) -> int:
		"""
		Returns the number of players in the database.
		"""
		return len(self.list)
	
	def upsert(self, category: str, column_values: List) -> None:
		"""
		Takes a player's name, the raw values from the CFL api (simple list) and
		adds the player to the database. This will add the player if they do not
		exist, and add the stats if the player already exists
		:param category: e.g. 'passing'
		:param column_values: e.g. ['HARRIS, Trevor', 'CGY', 5000, ...]
		"""
		if category not in config.cfl_api_columns:
			raise ValueError(f'Invalid category: {category}')
		
		column_names = config.cfl_api_columns[category]

		if len(column_names) != len(column_values):
			raise ValueError('Column names and values must be the same length')
		name_index = column_names.index('name')
		url_index = column_names.index('url')
		team_index = column_names.index('team')

		name = column_values[name_index]
		team = column_values[team_index]

		# Parsing the URL is the only way to get the player ID
		player_id = get_id_from_url(column_values[url_index])

		existing = self.get_by_id(player_id)
		if existing is not None:
			stats = existing['stats']
			for i, col in enumerate(column_names):
				if col not in ['name', 'team', 'url']:
					stats[col] = column_values[i]
		else:
			stats = dict(zip(column_names, column_values))
			self.list.append({'id': player_id, 'name': name, 'team': team, 'stats': stats})
