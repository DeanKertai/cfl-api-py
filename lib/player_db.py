from typing import List, TypedDict, Dict, Any
from lib import config
from lib.config import Category, Stat, StatType, output_csv_cols, column_types
from lib.player import get_id_from_url

class DbItem(TypedDict):
	player_id: int
	category: Category
	name: str
	team: str
	stats: Dict[Stat, Any]

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
	
	def get_stat(self, player_id: int, stat: Stat) -> Any:
		"""
		Returns the value of the specified stat for the player.
		"""
		player = self.get_by_id(player_id)
		if player is not None:
			return player['stats'].get(stat)
		return None
	
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
	
	def save_csv(self, category: Category, filename: str) -> None:
		"""
		Saves a CSV file in a format compatible with our family pool points
		spreadsheet, including all players for the specified category.
		"""
		filtered = [player for player in self.list if player['category'] == category]
		filtered.sort(key=lambda x: (x['team'], x['name']))
		output_columns = output_csv_cols[category]
		with open(filename, 'w') as file:

			for stat in output_columns:
				column_name = stat.value
				file.write(f"{column_name},")
			file.write("\n")
			for player in filtered:
				for stat in output_columns:
					stat_value = self.get_stat(player['id'], stat)
					stat_type = column_types[stat]
					if stat_value is not None:
						if stat_type == StatType.Str:
							file.write(f"\"{stat_value}\",")
						else:
							file.write(f"{stat_value},")
					else:
						file.write(",")
				file.write("\n")
	
	def upsert(self, category: Category, column_values: List) -> None:
		"""
		Takes a player's name, the raw values from the CFL api (simple list) and
		adds the player to the database. This will add the player if they do not
		exist, and add the stats if the player already exists
		:param category: e.g. 'passing'
		:param column_values: e.g. ['HARRIS, Trevor', 'CGY', 5000, ...]
		"""
		column_names = config.cfl_api_columns[category]

		if len(column_names) != len(column_values):
			raise ValueError('Column names and values must be the same length')
		name_index = column_names.index(Stat.Name)
		url_index = column_names.index(Stat.Url)
		team_index = column_names.index(Stat.Team)

		name = column_values[name_index]
		team = column_values[team_index]

		# Parsing the URL is the only way to get the player ID
		player_id = get_id_from_url(column_values[url_index])

		existing = self.get_by_id(player_id)
		if existing is not None:
			stats = existing['stats']
			for i, col in enumerate(column_names):
				stats[col] = column_values[i]
		else:
			stats = dict(zip(column_names, column_values))
			self.list.append({
				'id': player_id,
				'category': category,
				'name': name,
				'team': team,
				'stats': stats
			})
