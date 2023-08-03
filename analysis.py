import nfl_data_py as nfl
import pandas as pd
import numpy as np
import re
import configparser
import json
from config import *

import warnings

warnings.filterwarnings("ignore")

# config = configparser.ConfigParser()
# config.read(r"config.txt")

# # Current season
# current_season = int(config.get("global", "current_season"))

# # Column selectors
# game_data_cols = config.get("column-settings", "game_data").split(",")


def apply_regex(regex: str, string: str):
    try:
        match = re.search(regex, string)
        if match:
            return match.group()
        else:
            return np.nan
    except:
        return np.nan


class NFLVerseData:
    def __init__(self, years: list[int] = None, all_years: bool = False):
        if not all_years:
            self.years = years
            for year in years:
                if len(str(year)) != 4:
                    raise ValueError("Please enter years in YYYY format.")
        else:
            if years is not None:
                raise TypeError("Can not pass a list of years when all_years is True.")
            self.years = range(2000, CURRENT_SEASON + 1)

        self.pbp = nfl.import_pbp_data(self.years)
        self.id_table = nfl.import_ids()

    def get_ids(self):
        ids = self.id_table[ID_COLS]
        return ids.melt(id_vars=["name"], var_name="id_source", value_name="id")

    def get_full_pbp(self):
        return self.pbp

    def get_game_data(self):
        def clean_weather(row):
            try:
                if "RAIN" in row.upper():
                    return "RAIN"
                elif "SNOW" in row.upper():
                    return "SNOW"
                elif "COLD" in row.upper() or "FRIGID" in row.upper():
                    return "COLD"
                elif "FOG" in row.upper() or "HAZEY" in row.upper():
                    return "HAZE"
                else:
                    return "NONE"
            except:
                return None

        game_data = self.pbp[GAME_DATA_COLS]
        game_data["weather_hazards"] = game_data["weather"].apply(clean_weather)
        game_data["temp"] = (
            game_data["weather"]
            .apply(lambda x: apply_regex(r"\d+(?=°)", x))
            .astype(float)
        )
        game_data["humidity"] = (
            game_data["weather"]
            .apply(lambda x: apply_regex(r"\d+(?=%)", x))
            .astype(float)
            / 100
        )
        game_data["wind_speed"] = (
            game_data["weather"]
            .apply(lambda x: apply_regex(r"\d+(?=\s)", x))
            .astype(float)
        )
        game_data.drop(columns="weather", inplace=True)
        game_data.drop_duplicates(subset=["game_id"], inplace=True)
        game_data.reset_index(drop=True, inplace=True)

        return game_data

    def get_play_data(self):
        return self.pbp[KEY_COLS + PLAY_DATA_COLS]

    def get_result_data(self):
        return self.pbp[KEY_COLS + RESULT_COLS]

    def get_passing_data(self):
        return (
            self.pbp[KEY_COLS + PASSING_COLS]
            .loc[self.pbp["pass"] == 1]
            .reset_index(drop=True)
        )

    def get_rushing_data(self):
        return self.pbp[KEY_COLS + PASSING_COLS]

    def get_receiving_data(self):
        return self.pbp[KEY_COLS + RECEIVING_COLS]

    def get_epa_data(self):
        return self.pbp[KEY_COLS + EPA_COLS]

    def get_punting_data(self):
        return self.pbp[KEY_COLS + PUNTING_COLS]

    def get_kicking_data(self):
        return self.pbp[KEY_COLS + KICKING_COLS]

    def get_drive_data(self):
        return self.pbp[KEY_COLS + DRIVE_COLS]

    def get_defense_data(self):
        return self.pbp[KEY_COLS + DEFENSE_COLS]

    def get_special_data(self):
        return self.pbp[KEY_COLS + SPECIAL_COLS]

    def get_penalty_data(self):
        return self.pbp[KEY_COLS + PENALTY_COLS]
