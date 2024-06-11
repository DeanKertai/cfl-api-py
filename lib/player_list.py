from typing import List
from lib.player import Player, Position


def load_all_players() -> List[Player]:
	"""
	Loads all players from the player list.
	:return: A list of players.
	"""
	qb = load_player_list('picks/qb.txt', Position.QB)
	rb = load_player_list('picks/rb.txt', Position.RB)
	wr = load_player_list('picks/wr.txt', Position.WR)
	kickers = load_player_list('picks/kickers.txt', Position.KICKER)
	defence = load_player_list('picks/defence.txt', Position.DEFENCE)
	return qb + rb + wr + kickers + defence

def load_player_list(file_path: str, pos: Position) -> List[Player]:
	"""
	Loads the player list from the specified file.
	:param file_path: The path to the file containing the player list.
	:return: A list of players.
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
				'position': pos
			}
			players.append(player)
	return players
