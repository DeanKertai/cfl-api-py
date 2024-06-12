from enum import Enum
from typing import TypedDict
from lib.config import Category

class Player(TypedDict):
	id: int
	team: str
	name: str
	category: Category

def get_id_from_url(url: str) -> int:
	"""
	Extracts the player ID from the URL.
	Player URLs are in this format:
	https://www.cfl.ca/players/rene-paredes/158244/
	Where the last path param is the player ID
	:param url: The URL to extract the ID from
	:return: The player ID
	"""
	if url.endswith('/'):
		url = url[:-1]
	parts = url.split('/')
	return int(parts[-1])
