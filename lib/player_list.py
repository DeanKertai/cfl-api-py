from typing import List
from lib.config import Category
from lib.player import Player


def load_all_players() -> List[Player]:
	"""
	Loads all players from the player list.
	"""
	qb = load_player_list('picks/qb.txt', Category.Passing)
	rb = load_player_list('picks/rb.txt', Category.Rushing)
	wr = load_player_list('picks/wr.txt', Category.Receiving)
	kickers = load_player_list('picks/kickers.txt', Category.FieldGoals)
	defence = load_player_list('picks/defence.txt', Category.Defence)
	return qb + rb + wr + kickers + defence

def load_player_list(file_path: str, category: Category) -> List[Player]:
	"""
	Loads the player list from the specified file.
	"""
	players: List[Player] = []
	with open(file_path, 'r') as file:
		for line in file:
			# Expect 3 columns (two tabs)
			if not line or line.count('\t') != 2:
				continue
			id, team, name = line.strip().split('\t')
			player: Player = {
				'id': int(id),
				'team': team,
				'name': name,
				'category': category
			}
			players.append(player)
	return players
