from typing import TypedDict, Literal, Dict, List

base_url = 'https://www.cfl.ca/wp-content/themes/cfl.ca/inc/admin-ajax.php?action=get_league_stats'
rate_limit_interval = 1  # seconds

class ColumnDescription(TypedDict):
	description: str
	type: Literal['int', 'float', 'str']

	# Whether or not this column is needed for our family pool
	pertinent: bool

# This dictionary describes all of the different statistics that are returned
# by the API. The CFL API returns everything as simple lists of values, so we
# have to define this manually
column_description: Dict[str, ColumnDescription] = {
	# Global
	'date': {
		'description': 'The season/year of the statistic',
		'type': 'int',
		'pertinent': False
	},
	'name': {
		'description': 'Player name',
		'type': 'str',
		'pertinent': True
	},
	'url': {
		'description': 'Link to the player profile on cfl.ca',
		'type': 'str',
		'pertinent': False
	},
	'team': {
		'description': 'Team name',
		'type': 'str',
		'pertinent': True
	},
	'gp': {
		'description': 'Games played',
		'type': 'int',
		'pertinent': True
	},

	# Passing
	'passing_comp': {
		'description': 'Number of complete passes',
		'type': 'int',
		'pertinent': True
	},
	'passing_att': {
		'description': 'Number of attempted passes',
		'type': 'int',
		'pertinent': True
	},
	'passing_pct': {
		'description': 'Percent of completed passes',
		'type': 'float',
		'pertinent': False
	},
	'passing_yds': {
		'description': 'Passing yards',
		'type': 'float',
		'pertinent': True
	},
	'passing_td': {
		'description': 'Passing touchdowns',
		'type': 'int',
		'pertinent': True
	},
	'passing_int': {
		'description': 'Interceptions',
		'type': 'int',
		'pertinent': True
	},
	'passing_effic': {
		'description': 'Passer rating',
		'type': 'float',
		'pertinent': False
	},
	'passing_int_pct': {
		'description': 'Interception percentage',
		'type': 'float',
		'pertinent': False
	},
	'passing_avg': {
		'description': 'Average passing yards',
		'type': 'float',
		'pertinent': False
	},

	# Rushing
	'rushing_car': {
		'description': 'Number of carries',
		'type': 'int',
		'pertinent': True
	},
	'rushing_yds': {
		'description': 'Rushing yards',
		'type': 'int',
		'pertinent': True
	},
	'rushing_avg': {
		'description': 'Average rushing yards',
		'type': 'float',
		'pertinent': False
	},
	'rushing_lg': {
		'description': 'Longest rush',
		'type': 'int',
		'pertinent': False
	},
	'rushing_td': {
		'description': 'Rushing touchdowns',
		'type': 'int',
		'pertinent': True
	},
	'rushing_ten': {
		'description': 'Rushing first downs',
		'type': 'int',
		'pertinent': False
	},
	'rushing_twenty': {
		'description': 'Rushing plays of 20+ yards',
		'type': 'int',
		'pertinent': False
	},

	# Receiving
	'receiving_rec': {
		'description': 'Receptions',
		'type': 'int',
		'pertinent': True
	},
	'receiving_yds': {
		'description': 'Receiving yards',
		'type': 'int',
		'pertinent': True
	},
	'receiving_yac': {
		'description': 'Yards after catch',
		'type': 'int',
		'pertinent': False
	},
	'receiving_avg': {
		'description': 'Average receiving yards',
		'type': 'float',
		'pertinent': False
	},
	'receiving_lg': {
		'description': 'Longest reception',
		'type': 'int',
		'pertinent': False
	},
	'receiving_td': {
		'description': 'Receiving touchdowns',
		'type': 'int',
		'pertinent': True
	},
	'receiving_thirty': {
		'description': 'Receptions of 30+ yards',
		'type': 'int',
		'pertinent': False
	},
	'receiving_tgts': {
		'description': 'Targets',
		'type': 'int',
		'pertinent': True
	},

	# Defence
	'defence_tt': {
		'description': 'Total tackles',
		'type': 'int',
		'pertinent': False
	},
	'defence_dt': {
		'description': 'Defensive tackles',
		'type': 'int',
		'pertinent': True
	},
	'defence_st': {
		'description': 'Special teams tackles',
		'type': 'int',
		'pertinent': False
	},
	'defence_tlf': {
		'description': 'Tackles for loss',
		'type': 'int',
		'pertinent': False
	},
	'defence_qs': {
		'description': 'Quarterback sacks',
		'type': 'int',
		'pertinent': True
	},
	'defence_int': {
		'description': 'Interceptions',
		'type': 'int',
		'pertinent': True
	},
	'defence_int_yds': {
		'description': 'Interception yards',
		'type': 'int',
		'pertinent': False
	},
	'defence_int_lg': {
		'description': 'Longest interception return',
		'type': 'int',
		'pertinent': False
	},
	'defence_int_td': {
		'description': 'Interception touchdowns',
		'type': 'int',
		'pertinent': True
	},
	'defence_ff': {
		'description': 'Forced fumbles',
		'type': 'int',
		'pertinent': True
	},
	'defence_fr': {
		'description': 'Fumble recoveries',
		'type': 'int',
		'pertinent': False
	},
	'defence_fr_yds': {
		'description': 'Fumble recovery yards',
		'type': 'int',
		'pertinent': False
	},
	'defence_fr_lg': {
		'description': 'Longest fumble recovery',
		'type': 'int',
		'pertinent': False
	},
	'defence_fr_td': {
		'description': 'Fumble recovery touchdowns',
		'type': 'int',
		'pertinent': True
	},

	# Kickers
	'field_goals_fga': {
		'description': 'Field goals attempted',
		'type': 'int',
		'pertinent': False
	},
	'field_goals_md': {
		'description': 'Field goals made',
		'type': 'int',
		'pertinent': True
	},
	'field_goals_pct': {
		'description': 'Field goal percentage',
		'type': 'float',
		'pertinent': False
	},
	'field_goals_lg': {
		'description': 'Longest field goal',
		'type': 'int',
		'pertinent': False
	},
	'field_goals_s': {
		'description': 'Singles',
		'type': 'int',
		'pertinent': True
	},
	'field_goals_c1_att': {
		'description': 'Convert 1-point attempts',
		'type': 'int',
		'pertinent': False
	},
	'field_goals_c1_md': {
		'description': 'Convert 1-point made',
		'type': 'int',
		'pertinent': True
	},
}

# This dictionary contains the columns (and their order) as they are returned by the
# CFL API for each category. Unfortunately the CFL API returns data as a simple list
# of values, so this will need to be updated if they ever add/remove columns or change
# the order in which they are returned.
# The column names listed must match the keys in the `column_description` dictionary
cfl_api_columns: Dict[str, List[str]] = {
	'passing': [
		'date',
		'name',
		'url',
		'team',
		'gp',
		'passing_comp',
		'passing_att',
		'passing_pct',
		'passing_yds',
		'passing_td',
		'passing_int',
		'passing_effic',
		'passing_int_pct',
		'passing_avg',
	],
	'rushing': [
		'date',
		'name',
		'url',
		'team',
		'gp',
		'rushing_car',
		'rushing_yds',
		'rushing_avg',
		'rushing_lg',
		'rushing_td',
		'rushing_ten',
		'rushing_twenty',
	],
	'receiving': [
		'date',
		'name',
		'url',
		'team',
		'gp',
		'receiving_rec',
		'receiving_yds',
		'receiving_yac',
		'receiving_avg',
		'receiving_lg',
		'receiving_td',
		'receiving_thirty',
		'receiving_tgts',
	],
	'defence': [
		'date',
		'name',
		'url',
		'team',
		'gp',
		'defence_tt',
		'defence_dt',
		'defence_st',
		'defence_tlf',
		'defence_qs',
		'defence_int',
		'defence_int_yds',
		'defence_int_lg',
		'defence_int_td',
		'defence_ff',
		'defence_fr',
		'defence_fr_yds',
		'defence_fr_lg',
		'defence_fr_td',
	],
	'field_goals': [
		'date',
		'name',
		'url',
		'team',
		'gp',
		'field_goals_fga',
		'field_goals_md',
		'field_goals_pct',
		'field_goals_lg',
		'field_goals_s',
		'field_goals_c1_att',
		'field_goals_c1_md',
	],
}
