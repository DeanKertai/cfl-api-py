from enum import Enum
from typing import Dict, List


class Category(Enum):
	Passing = 'passing'
	Rushing = 'rushing'
	Receiving = 'receiving'
	Defence = 'defence'
	FieldGoals = 'field_goals'

# Map of Category to the query param name in the CFL stats API
category_api_names: Dict[Category, str] = {
	Category.Passing: 'passing',
	Category.Rushing: 'rushing',
	Category.Receiving: 'receiving',
	Category.Defence: 'defence',
	Category.FieldGoals: 'field_goals',
}

class StatType(Enum):
	Str = 'str'
	Int = 'int'
	Float = 'float'

class Stat(Enum):
	NoOp = 'noop'  # For columns we don't care about
	Date = 'date'
	Name = 'name'
	Url = 'url'
	Team = 'team'
	Position = 'position'
	PassingCompletions = 'passing_comp'
	PassingYards = 'passing_yds'
	PassingTD = 'passing_td'
	RushingYards = 'rushing_yds'
	RushingTD = 'rushing_td'
	ReceivingYards = 'receiving_yds'
	ReceivingTD = 'receiving_td'
	FieldGoalsMade = 'field_goals_md'
	FieldGoalsSingles = 'field_goals_s'
	FieldGoalsConvert1Point = 'field_goals_c1_md'
	DefenceTackles = 'defence_dt'
	DefenceSacks = 'defence_qs'
	DefenceInterceptions = 'defence_int'
	DefenceForcedFumbles = 'defence_ff'


column_types: Dict[Stat, StatType] = {
	Stat.NoOp: StatType.Str,
	Stat.Date: StatType.Int,
	Stat.Name: StatType.Str,
	Stat.Url: StatType.Str,
	Stat.Team: StatType.Str,
	Stat.PassingCompletions: StatType.Int,
	Stat.PassingYards: StatType.Float,
	Stat.PassingTD: StatType.Int,
	Stat.RushingYards: StatType.Float,
	Stat.RushingTD: StatType.Int,
	Stat.ReceivingYards: StatType.Int,
	Stat.ReceivingTD: StatType.Int,
	Stat.FieldGoalsMade: StatType.Int,
	Stat.FieldGoalsConvert1Point: StatType.Int,
	Stat.DefenceTackles: StatType.Int,
	Stat.DefenceSacks: StatType.Int,
	Stat.DefenceInterceptions: StatType.Int,
	Stat.DefenceForcedFumbles: StatType.Int,
}

# This dictionary contains the columns (and their order) as they are returned by the
# CFL API for each category. Unfortunately the CFL API returns data as a simple list
# of values, so this will need to be updated if they ever add/remove columns or change
# the order in which they are returned.
cfl_api_columns: Dict[Category, List[Stat]] = {
	Category.Passing: [
		Stat.Date,
		Stat.Name,
		Stat.Url,
		Stat.Team,
		Stat.NoOp, # gp
		Stat.PassingCompletions,
		Stat.NoOp, # passing_att
		Stat.NoOp, # passing_pct
		Stat.PassingYards,
		Stat.PassingTD,
		Stat.NoOp, # passing_int
		Stat.NoOp, # passing_effic
		Stat.NoOp, # passing_int_pct
		Stat.NoOp, # passing_avg
	],
	Category.Rushing: [
		Stat.Date,
		Stat.Name,
		Stat.Url,
		Stat.Team,
		Stat.NoOp, # gp
		Stat.NoOp, # rushing_car
		Stat.RushingYards,
		Stat.NoOp, # rushing_avg
		Stat.NoOp, # rushing_lg
		Stat.RushingTD,
		Stat.NoOp, # rushing_ten
		Stat.NoOp, # rushing_twenty
	],
	Category.Receiving: [
		Stat.Date,
		Stat.Name,
		Stat.Url,
		Stat.Team,
		Stat.NoOp, # gp
		Stat.NoOp, # receiving_rec
		Stat.ReceivingYards,
		Stat.NoOp, # receiving_yac
		Stat.NoOp, # receiving_avg
		Stat.NoOp, # receiving_lg
		Stat.ReceivingTD,
		Stat.NoOp, # receiving_thirty
		Stat.NoOp, # receiving_tgts
	],
	Category.Defence: [
		Stat.Date,
		Stat.Name,
		Stat.Url,
		Stat.Team,
		Stat.NoOp, # gp
		Stat.NoOp, # defence_tt
		Stat.DefenceTackles,
		Stat.NoOp, # defence_st
		Stat.NoOp, # defence_tlf
		Stat.DefenceSacks,
		Stat.DefenceInterceptions,
		Stat.NoOp, # defence_int_yds
		Stat.NoOp, # defence_int_lg
		Stat.NoOp, # defence_int_td
		Stat.DefenceForcedFumbles,
		Stat.NoOp, # defence_fr
		Stat.NoOp, # defence_fr_yds
		Stat.NoOp, # defence_fr_lg
		Stat.NoOp, # defence_fr_td
	],
	Category.FieldGoals: [
		Stat.Date,
		Stat.Name,
		Stat.Url,
		Stat.Team,
		Stat.NoOp, # gp
		Stat.NoOp, # field_goals_fga
		Stat.FieldGoalsMade,
		Stat.NoOp, # field_goals_pct
		Stat.NoOp, # field_goals_lg
		Stat.NoOp, # field_goals_s
		Stat.NoOp, # field_goals_c1_att
		Stat.FieldGoalsConvert1Point,
	],
}

# Map of Category to the columns we care about for our output CSV
output_csv_cols: Dict[Category, List[Stat]] = {
	Category.Passing: [
		Stat.Name,
		Stat.Team,
		Stat.Position,
		Stat.PassingYards,
		Stat.PassingTD,
		Stat.ReceivingYards,
		Stat.ReceivingTD,
		Stat.RushingYards,
		Stat.RushingTD,
	],
	Category.Rushing: [
		Stat.Name,
		Stat.Team,
		Stat.Position,
		Stat.PassingYards,
		Stat.PassingTD,
		Stat.ReceivingYards,
		Stat.ReceivingTD,
		Stat.RushingYards,
		Stat.RushingTD,
	],
	Category.Receiving: [
		Stat.Name,
		Stat.Team,
		Stat.Position,
		Stat.PassingYards,
		Stat.PassingTD,
		Stat.ReceivingYards,
		Stat.ReceivingTD,
		Stat.RushingYards,
		Stat.RushingTD,
	],
	Category.FieldGoals: [
		Stat.Name,
		Stat.Team,
		Stat.Position,
		Stat.FieldGoalsMade,
		Stat.FieldGoalsConvert1Point,
	],
	Category.Defence: [
		Stat.Name,
		Stat.Team,
		Stat.Position,
		Stat.DefenceTackles,
		Stat.DefenceSacks,
		Stat.DefenceInterceptions,
		Stat.DefenceForcedFumbles,
	],
}
