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
