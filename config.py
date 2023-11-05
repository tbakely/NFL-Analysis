# Current season
CURRENT_SEASON = 2022

### Column selectors

# ID Data
ID_COLS = [
    "name",
    "mfl_id",
    "sportradar_id",
    "fantasypros_id",
    "gsis_id",
    "pff_id",
    "sleeper_id",
    "nfl_id",
    "espn_id",
    "yahoo_id",
    "fleaflicker_id",
    "cbs_id",
    "rotowire_id",
    "rotoworld_id",
    "ktc_id",
    "pfr_id",
    "cfbref_id",
    "stats_id",
    "stats_global_id",
    "fantasy_data_id",
    "swish_id",
]

# Player misc data (Draft pick, Age, Etc.)
# PLAYER_MISC_COLS = []

## PLAY BY PLAY

# Base columns needed to join play by data
KEY_COLS = ["play_id", "game_id", "drive_play_id_started", "drive_play_id_ended"]

# Game data
GAME_DATA_COLS = [
    "game_id",
    "old_game_id",
    "home_team",
    "away_team",
    "season_type",
    "div_game",
    "roof",
    "surface",
    "home_coach",
    "away_coach",
    "stadium_id",
    "game_stadium",
    "game_date",
    "start_time",
    "stadium",
    "weather",
]

# Play data, add base cols
PLAY_DATA_COLS = [
    "yardline_100",
    "quarter_seconds_remaining",
    "half_seconds_remaining",
    "game_seconds_remaining",
    "game_half",
    "qtr",
    "down",
    "ydstogo",
    "goal_to_go",
    "time",
    "play_type",
    "run_location",
    "run_gap",
    "offense_formation",
    "offense_personnel",
    "defenders_in_box",
    "defense_personnel",
    "number_of_pass_rushers",
    "players_on_play",
    "offense_players",
    "defense_players",
    "n_offense",
    "n_defense",
]

# Result of play data, add base cols
RESULT_COLS = [
    "touchdown",
    "first_down",
    "interception",
    "fumble",
    "third_down_converted",
    "third_down_failed",
    "fourth_down_converted",
    "fourth_down_failed",
]

# Passing data, add base cols
PASSING_COLS = [
    "qb_dropback",
    "qb_kneel",
    "qb_spike",
    "qb_scramble",
    "pass_length",
    "pass_location",
    "air_yards",
    "yards_after_catch",
    "total_home_pass_epa",
    "total_away_pass_epa",
    "air_epa",
    "comp_air_epa",
    "total_home_comp_air_epa",
    "total_away_comp_air_epa",
    "total_home_raw_air_epa",
    "total_away_raw_air_epa",
    "total_home_pass_wpa",
    "total_away_pass_wpa",
    "air_wpa",
    "comp_air_wpa",
    "total_home_comp_air_wpa",
    "total_away_comp_air_wpa",
    "total_home_raw_air_wpa",
    "total_away_raw_air_wpa",
    "first_down_pass",
    "incomplete_pass",
    "punt_fair_catch",
    "kickoff_fair_catch",
    "qb_hit",
    "pass_attempt",
    "pass_touchdown",
    "complete_pass",
    "passer_player_id",
    "passer_player_name",
    "passing_yards",
    "qb_hit_1_player_id",
    "qb_hit_1_player_name",
    "qb_hit_2_player_id",
    "qb_hit_2_player_name",
    "pass_defense_1_player_id",
    "pass_defense_1_player_name",
    "pass_defense_2_player_id",
    "pass_defense_2_player_name",
    "passer",
    "passer_jersey_number",
    "pass",
    "passer_id",
    "qb_epa",
    "xpass",
    "pass_oe",
    "number_of_pass_rushers",
]

# Rushing data, add base cols
RUSHING_COLS = [
    "total_home_rush_epa",
    "total_away_rush_epa",
    "total_home_rush_wpa",
    "total_away_rush_wpa",
    "first_down_rush",
    "rush_attempt",
    "rush_touchdown",
    "lateral_rush",
    "rusher_player_id",
    "rusher_player_name",
    "rushing_yards",
    "lateral_rusher_player_id",
    "lateral_rusher_player_name",
    "lateral_rushing_yards",
    "rusher",
    "rusher_jersey_number",
    "rush",
    "rusher_id",
    "defenders_in_box",
]

# Receiving stats, add base cols
RECEIVING_COLS = [
    "yards_after_catch",
    "yac_epa",
    "comp_yac_epa",
    "total_home_comp_yac_epa",
    "total_away_comp_yac_epa",
    "total_home_raw_yac_epa",
    "total_away_raw_yac_epa",
    "yac_wpa",
    "comp_yac_wpa",
    "total_home_comp_yac_wpa",
    "total_away_comp_yac_wpa",
    "total_home_raw_yac_wpa",
    "total_away_raw_yac_wpa",
    "incomplete_pass",
    "punt_fair_catch",
    "kickoff_fair_catch",
    "complete_pass",
    "receiver_player_id",
    "receiver_player_name",
    "receiving_yards",
    "lateral_receiver_player_id",
    "lateral_receiver_player_name",
    "lateral_receiving_yards",
    "receiver",
    "receiver_jersey_number",
    "receiver_id",
    "xyac_epa",
    "xyac_mean_yardage",
    "xyac_median_yardage",
    "xyac_success",
    "xyac_fd",
]

# EPA stats, add base cols
EPA_COLS = [
    "epa",
    "total_home_epa",
    "total_away_epa",
    "total_home_rush_epa",
    "total_away_rush_epa",
    "total_home_pass_epa",
    "total_away_pass_epa",
    "air_epa",
    "yac_epa",
    "comp_air_epa",
    "comp_yac_epa",
    "total_home_comp_air_epa",
    "total_away_comp_air_epa",
    "total_home_comp_yac_epa",
    "total_away_comp_yac_epa",
    "total_home_raw_air_epa",
    "total_away_raw_air_epa",
    "total_home_raw_yac_epa",
    "total_away_raw_yac_epa",
    "qb_epa",
    "xyac_epa",
]

# Punting stats, add base cols
PUNTING_COLS = [
    "punt_blocked",
    "punt_inside_twenty",
    "punt_in_endzone",
    "punt_out_of_bounds",
    "punt_downed",
    "punt_fair_catch",
    "punt_attempt",
    "punt_returner_player_id",
    "punt_returner_player_name",
    "lateral_punt_returner_player_id",
    "lateral_punt_returner_player_name",
    "punter_player_id",
    "punter_player_name",
]

# Kicks stats, add base cols
KICKING_COLS = [
    "goal_to_go",
    "field_goal_result",
    "kick_distance",
    "kickoff_inside_twenty",
    "kickoff_in_endzone",
    "kickoff_out_of_bounds",
    "kickoff_downed",
    "kickoff_fair_catch",
    "own_kickoff_recovery",
    "own_kickoff_recovery_td",
    "field_goal_attempt",
    "kickoff_attempt",
    "kickoff_returner_player_name",
    "kickoff_returner_player_id",
    "lateral_kickoff_returner_player_id",
    "lateral_kickoff_returner_player_name",
    "kicker_player_name",
    "kicker_player_id",
    "own_kickoff_recovery_player_id",
    "own_kickoff_recovery_player_name",
    "home_opening_kickoff",
]

# Drive stats, add base cols
DRIVE_COLS = [
    "drive",
    "fixed_drive",
    "fixed_drive_result",
    "drive_real_start_time",
    "drive_play_count",
    "drive_time_of_possession",
    "drive_first_downs",
    "drive_inside20",
    "drive_ended_with_score",
    "drive_quarter_start",
    "drive_quarter_end",
    "drive_yards_penalized",
    "drive_start_transition",
    "drive_end_transition",
    "drive_game_clock_start",
    "drive_game_clock_end",
    "drive_start_yard_line",
    "drive_end_yard_line",
]

# Defense stats, add base cols
DEFENSE_COLS = [
    "interception",
    "fumble_forced",
    "fumble_not_forced",
    "fumble_out_of_bounds",
    "solo_tackle",
    "tackled_for_loss",
    "fumble_lost",
    "qb_hit",
    "sack",
    "fumble",
    "assist_tackle",
    "lateral_sack_player_id",
    "lateral_sack_player_name",
    "interception_player_id",
    "interception_player_name",
    "lateral_interception_player_id",
    "lateral_interception_player_name",
    "tackle_for_loss_1_player_id",
    "tackle_for_loss_1_player_name",
    "tackle_for_loss_2_player_id",
    "tackle_for_loss_2_player_name",
    "qb_hit_1_player_id",
    "qb_hit_1_player_name",
    "qb_hit_2_player_id",
    "qb_hit_2_player_name",
    "forced_fumble_player_1_team",
    "forced_fumble_player_1_player_id",
    "forced_fumble_player_1_player_name",
    "forced_fumble_player_2_team",
    "forced_fumble_player_2_player_id",
    "forced_fumble_player_2_player_name",
    "solo_tackle_1_team",
    "solo_tackle_2_team",
    "solo_tackle_1_player_id",
    "solo_tackle_2_player_id",
    "solo_tackle_1_player_name",
    "solo_tackle_2_player_name",
    "assist_tackle_1_player_id",
    "assist_tackle_1_player_name",
    "assist_tackle_1_team",
    "assist_tackle_2_player_id",
    "assist_tackle_2_player_name",
    "assist_tackle_2_team",
    "assist_tackle_3_player_id",
    "assist_tackle_3_player_name",
    "assist_tackle_3_team",
    "assist_tackle_4_player_id",
    "assist_tackle_4_player_name",
    "assist_tackle_4_team",
    "tackle_with_assist",
    "tackle_with_assist_1_player_id",
    "tackle_with_assist_1_player_name",
    "tackle_with_assist_1_team",
    "tackle_with_assist_2_player_id",
    "tackle_with_assist_2_player_name",
    "tackle_with_assist_2_team",
    "pass_defense_1_player_id",
    "pass_defense_1_player_name",
    "pass_defense_2_player_id",
    "pass_defense_2_player_name",
    "fumbled_1_team",
    "fumbled_1_player_id",
    "fumbled_1_player_name",
    "fumbled_2_player_id",
    "fumbled_2_player_name",
    "fumbled_2_team",
    "fumble_recovery_1_team",
    "fumble_recovery_1_yards",
    "fumble_recovery_1_player_id",
    "fumble_recovery_1_player_name",
    "fumble_recovery_2_team",
    "fumble_recovery_2_yards",
    "fumble_recovery_2_player_id",
    "fumble_recovery_2_player_name",
    "sack_player_id",
    "sack_player_name",
    "half_sack_1_player_id",
    "half_sack_1_player_name",
    "half_sack_2_player_id",
    "half_sack_2_player_name",
    "defense_personnel",
    "defense_players",
    "n_defense",
]

# Special teams stats, add base cols
SPECIAL_COLS = [
    "kick_distance",
    "punt_blocked",
    "punt_inside_twenty",
    "punt_in_endzone",
    "punt_out_of_bounds",
    "punt_downed",
    "punt_fair_catch",
    "kickoff_inside_twenty",
    "kickoff_in_endzone",
    "kickoff_out_of_bounds",
    "kickoff_downed",
    "kickoff_fair_catch",
    "own_kickoff_recovery",
    "own_kickoff_recovery_td",
    "return_touchdown",
    "kickoff_attempt",
    "punt_attempt",
    "lateral_return",
    "punt_returner_player_id",
    "punt_returner_player_name",
    "lateral_punt_returner_player_id",
    "lateral_punt_returner_player_name",
    "kickoff_returner_player_name",
    "kickoff_returner_player_id",
    "lateral_kickoff_returner_player_id",
    "lateral_kickoff_returner_player_name",
    "punter_player_id",
    "punter_player_name",
    "kicker_player_name",
    "kicker_player_id",
    "own_kickoff_recovery_player_id",
    "own_kickoff_recovery_player_name",
    "return_team",
    "return_yards",
    "home_opening_kickoff",
]

# Penalty stats, add base cols
PENALTY_COLS = [
    "first_down_penalty",
    "penalty",
    "penalty_team",
    "penalty_player_id",
    "penalty_player_name",
    "penalty_yards",
    "penalty_type",
]

CREATE_VIEWS = """
/* snap counts */
create view current_season_data.offense_snap_counts as
select 
ids.id,
season,
week,
offense_snaps,
offense_pct
from current_season_data.snap_count_data
left join
	(select distinct name, gsis_id as id from current_season_data.full_ids) ids
on current_season_data.snap_count_data.player = ids.name;


/* weekly_qb */
create view current_season_data.weekly_qb as
select
	player_name,
	position,
	recent_team,
	wd.season,
	wd.week,
	case when wd.attempts <> 0 then cast((wd.completions/wd.attempts) as numeric(3,2)) else null end as comp_pct,
	passing_yards,
	passing_tds,
	wd.interceptions,
	sacks,
	sack_yards,
	passing_air_yards,
	passing_yards_after_catch,
	passing_first_downs,
	passing_epa,
	dakota,
	pacr,
	avg_time_to_throw,
	avg_completed_air_yards,
	avg_intended_air_yards,
	avg_air_yards_differential,
	aggressiveness,
	max_completed_air_distance,
	avg_air_yards_to_sticks,
	passer_rating,
	completion_percentage_above_expectation,
	avg_air_distance,
	carries,
	rushing_yards,
	rushing_tds,
	rushing_fumbles,
	rushing_fumbles_lost,
	rushing_first_downs,
	rushing_epa,
	offense_snaps,
	offense_pct,
	(carries + wd.attempts) as total_usage,
	roof,
	surface,
	weather_hazards,
	temp,
	humidity,
	wind_speed,
	total_blitz,
	case when offense_snaps <> 0 then (total_blitz / offense_snaps) else null end as blitz_faced_pct
from current_season_data.weekly_data wd
left join current_season_data.ngs_passing_data ngs
on wd.player_id = ngs.player_gsis_id
and wd.season = ngs.season
and wd.week = ngs.week
left join current_season_data.offense_snap_counts os
on wd.player_id = os.id
and wd.season = os.season
and wd.week = os.week
left join (select distinct passer_player_id, game_id, season, week from current_season_data.full_pbp) game_id
on wd.player_id = game_id.passer_player_id
and wd.season = game_id.season
and wd.week = game_id.week
left join current_season_data.game_data
on game_data.game_id = game_id.game_id
left join (
select
	passer_player_id,
	season,
	week,
	sum(blitz) as total_blitz
from current_season_data.full_pbp
where play_type = 'pass'
and two_point_attempt = 0
group by passer_player_id, season, week
) blitz
on wd.player_id = blitz.passer_player_id
and wd.season = blitz.season
and wd.week = blitz.week
where position = 'QB'
and wd.attempts > 0;

/* weekly wr stats */
create view current_season_data.weekly_wr as
select
	player_id,
	player_name,
	position,
	recent_team,
	wd.season,
	wd.week,
	wd.receptions,
	wd.targets,
	receiving_yards,
	receiving_tds,
	receiving_fumbles,
	receiving_fumbles_lost,
	receiving_air_yards,
	receiving_yards_after_catch,
	receiving_first_downs,
	receiving_epa,
	racr,
	target_share,
	air_yards_share,
	wopr,
	offense_snaps,
	offense_pct,
	avg_cushion,
	avg_separation,
	avg_intended_air_yards,
	percent_share_of_intended_air_yards,
	catch_percentage,
	avg_yac,
	avg_yac_above_expectation,
	roof,
	surface,
	weather_hazards,
	temp,
	humidity,
	wind_speed
from current_season_data.weekly_data wd
left join current_season_data.offense_snap_counts os
on wd.player_id = os.id
and wd.season = os.season
and wd.week = os.week
left join current_season_data.ngs_receiving_data ngs
on wd.player_id = ngs.player_gsis_id
and wd.season = ngs.season
and wd.week = ngs.week
left join (select distinct receiver_player_id, game_id, season, week from current_season_data.full_pbp) game_id
on wd.player_id = game_id.receiver_player_id
and wd.season = game_id.season
and wd.week = game_id.week
left join current_season_data.game_data
on game_data.game_id = game_id.game_id
where position = 'WR';

/* weekly te stats */
create view current_season_data.weekly_te as
select
	player_id,
	player_name,
	position,
	recent_team,
	wd.season,
	wd.week,
	wd.receptions,
	wd.targets,
	receiving_yards,
	receiving_tds,
	receiving_fumbles,
	receiving_fumbles_lost,
	receiving_air_yards,
	receiving_yards_after_catch,
	receiving_first_downs,
	receiving_epa,
	racr,
	target_share,
	air_yards_share,
	wopr,
	offense_snaps,
	offense_pct,
	avg_cushion,
	avg_separation,
	avg_intended_air_yards,
	percent_share_of_intended_air_yards,
	catch_percentage,
	avg_yac,
	avg_yac_above_expectation,
	roof,
	surface,
	weather_hazards,
	temp,
	humidity,
	wind_speed
from current_season_data.weekly_data wd
left join current_season_data.offense_snap_counts os
on wd.player_id = os.id
and wd.season = os.season
and wd.week = os.week
left join current_season_data.ngs_receiving_data ngs
on wd.player_id = ngs.player_gsis_id
and wd.season = ngs.season
and wd.week = ngs.week
left join (select distinct receiver_player_id, game_id, season, week from current_season_data.full_pbp) game_id
on wd.player_id = game_id.receiver_player_id
and wd.season = game_id.season
and wd.week = game_id.week
left join current_season_data.game_data
on game_data.game_id = game_id.game_id
where position = 'TE';

/* weekly rb stats */
create view current_season_data.weekly_rb as
select
	player_id,
	player_name,
	position,
	recent_team,
	wd.season,
	wd.week,
	carries,
	rushing_yards,
	rushing_tds,
	rushing_fumbles,
	rushing_fumbles_lost,
	rushing_first_downs,
	rushing_epa,
	efficiency,
	percent_attempts_gte_eight_defenders,
	avg_time_to_los,
	rush_yards_over_expected,
	avg_rush_yards,
	rush_yards_over_expected_per_att,
	rush_pct_over_expected,
	wd.receptions,
	wd.targets,
	receiving_yards,
	receiving_tds,
	receiving_fumbles,
	receiving_fumbles_lost,
	receiving_air_yards,
	receiving_yards_after_catch,
	receiving_first_downs,
	receiving_epa,
	racr,
	target_share,
	air_yards_share,
	wopr,
	offense_snaps,
	offense_pct,
	(carries + wd.targets) as total_usage,
	roof,
	surface,
	weather_hazards,
	temp,
	humidity,
	wind_speed
from current_season_data.weekly_data wd
left join current_season_data.offense_snap_counts os
on wd.player_id = os.id
and wd.season = os.season
and wd.week = os.week
left join current_season_data.ngs_rushing_data ngsr
on wd.player_id = ngsr.player_gsis_id
and wd.season = ngsr.season
and wd.week = ngsr.week
left join (select distinct rusher_player_id, game_id, season, week from current_season_data.full_pbp) game_id
on wd.player_id = game_id.rusher_player_id
and wd.season = game_id.season
and wd.week = game_id.week
left join current_season_data.game_data
on game_data.game_id = game_id.game_id
where position = 'RB';

/* redzone snaps current season */
create view current_season_data.redzone_snaps as
select
player_id,
player_name,
season,
week,
sum(redzone) as redzone
from(
select
rusher_player_id as player_id,
rusher_player_name as player_name,
season,
week,
count(yardline_100) as redzone
from current_season_data.full_pbp
where play_type in ('run')
and two_point_attempt = 0
and yardline_100 < 20
and rusher_player_id is not null
group by rusher_player_id, rusher_player_name, season,week

UNION ALL

select
receiver_player_id as player_id,
receiver_player_name as player_name,
season,
week,
count(yardline_100) as redzone
from current_season_data.full_pbp
where play_type in ('pass')
and two_point_attempt = 0
and yardline_100 < 20
and receiver_player_id is not null
group by receiver_player_id, receiver_player_name, season, week
) as redzone_union
group by player_id, player_name, season, week
order by week desc, redzone desc;
"""

# SQL needed to create reports in PositionReport
WEEKLY_WR = """
select 
wr.player_name, 
wr.position, 
wr.season,
wr.week,
offense_snaps,
offense_pct,
target_share,
targets,
receiving_epa,
redzone
from current_season_data.weekly_wr wr
left join current_season_data.redzone_snaps rz
on wr.player_id = rz.player_id
and wr.season = rz.season
and wr.week = rz.week
"""

WEEKLY_RB = """
select
rb.player_name,
rb.position,
rb.season,
rb.week,
offense_snaps,
offense_pct,
total_usage,
rushing_epa,
rush_yards_over_expected_per_att,
rush_pct_over_expected,
target_share,
receiving_epa,
redzone
from current_season_data.weekly_rb rb
left join current_season_data.redzone_snaps rz
on rb.player_id = rz.player_id
and rb.season = rz.season
and rb.week = rz.week
"""

WEEKLY_TE = """
select 
te.player_name, 
te.position, 
te.season,
te.week,
offense_snaps,
offense_pct,
target_share,
targets,
receiving_epa,
redzone
from current_season_data.weekly_te te
left join current_season_data.redzone_snaps rz
on te.player_id = rz.player_id
and te.season = rz.season
and te.week = rz.week
"""
