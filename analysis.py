import nfl_data_py as nfl
import pandas as pd
import numpy as np
import re
import configparser
import json
from config import *
from sqlalchemy import create_engine

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
    def __init__(self, years: list[int] = None, chunk: bool = True):
        if chunk:
            if len(years) > 1:
                raise ValueError("Enter only one year when chunk = True")
        for year in years:
            if len(str(year)) != 4:
                raise ValueError("Please enter years in YYYY format.")
        self.years = years
        self.pbp = nfl.import_pbp_data(self.years)
        self.id_table = nfl.import_ids()

    def get_ids(self):
        ids = self.id_table[ID_COLS]
        return ids.melt(
            id_vars=["name"], var_name="id_source", value_name="id"
        ).drop_duplicates(subset=["id"])

    def get_full_pbp(self):
        return self.pbp.drop_duplicates(subset=KEY_COLS)

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
        if self.years[0] < 2016:
            cols = [
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
            keep_cols = KEY_COLS + PLAY_DATA_COLS
            for col in cols:
                if col in keep_cols:
                    keep_cols.remove(col)
            data = self.pbp[keep_cols].drop_duplicates(subset=KEY_COLS)
            for col in cols:
                data[col] = np.nan
            return data
        else:
            return self.pbp[KEY_COLS + PLAY_DATA_COLS].drop_duplicates(subset=KEY_COLS)

    def get_result_data(self):
        return self.pbp[KEY_COLS + RESULT_COLS].drop_duplicates(subset=KEY_COLS)

    def get_passing_data(self):
        if self.years[0] < 2016:
            cols = ["number_of_pass_rushers"]
            keep_cols = KEY_COLS + PASSING_COLS
            for col in cols:
                if col in keep_cols:
                    keep_cols.remove(col)
            data = (
                self.pbp[keep_cols]
                .loc[self.pbp["pass"] == 1]
                .reset_index(drop=True)
                .drop_duplicates(subset=KEY_COLS)
            )
            data[cols] = np.nan
            return data
        return (
            self.pbp[KEY_COLS + PASSING_COLS]
            .loc[self.pbp["pass"] == 1]
            .reset_index(drop=True)
            .drop_duplicates(subset=KEY_COLS)
        )

    def get_rushing_data(self):
        if self.years[0] < 2016:
            cols = ["defenders_in_box"]
            keep_cols = KEY_COLS + RUSHING_COLS
            for col in cols:
                if col in keep_cols:
                    keep_cols.remove(col)
            return (
                self.pbp[keep_cols]
                .loc[self.pbp["rush"] == 1]
                .reset_index(drop=True)
                .drop_duplicates(subset=KEY_COLS)
            )
        else:
            return (
                self.pbp[KEY_COLS + RUSHING_COLS]
                .loc[self.pbp["rush"] == 1]
                .reset_index(drop=True)
                .drop_duplicates(subset=KEY_COLS)
            )

    def get_receiving_data(self):
        return (
            self.pbp[KEY_COLS + RECEIVING_COLS]
            .loc[self.pbp["pass"] == 1]
            .reset_index(drop=True)
            .drop_duplicates(subset=KEY_COLS)
        )

    def get_epa_data(self):
        return self.pbp[KEY_COLS + EPA_COLS].drop_duplicates(subset=KEY_COLS)

    def get_punting_data(self):
        return self.pbp[KEY_COLS + PUNTING_COLS].drop_duplicates(subset=KEY_COLS)

    def get_kicking_data(self):
        return self.pbp[KEY_COLS + KICKING_COLS].drop_duplicates(subset=KEY_COLS)

    def get_drive_data(self):
        return self.pbp[KEY_COLS + DRIVE_COLS].drop_duplicates(subset=KEY_COLS)

    def get_defense_data(self):
        if self.years[0] < 2016:
            cols = ["defense_personnel", "defense_players", "n_defense"]
            keep_cols = KEY_COLS + DEFENSE_COLS
            for col in cols:
                if col in keep_cols:
                    keep_cols.remove(col)
            data = self.pbp[keep_cols].drop_duplicates(subset=KEY_COLS)
            for col in cols:
                data[col] = np.nan
            return data
        else:
            return self.pbp[KEY_COLS + DEFENSE_COLS].drop_duplicates(subset=KEY_COLS)

    def get_special_data(self):
        return self.pbp[KEY_COLS + SPECIAL_COLS].drop_duplicates(subset=KEY_COLS)

    def get_penalty_data(self):
        return self.pbp[KEY_COLS + PENALTY_COLS].drop_duplicates(subset=KEY_COLS)

    def get_injuries(self):
        return nfl.import_injuries(self.years).drop_duplicates(
            subset=["season", "week", "gsis_id"]
        )

    def load_sql(self, append: bool = False):
        engine = create_engine(
            "postgresql+psycopg2://tbakely@localhost:5432/thefantasybot"
        )

        if not append:
            if_exists = "replace"
        else:
            if_exists = "append"

        self.get_full_pbp().to_sql("full_pbp", engine, if_exists=if_exists, index=False)
        self.get_ids().to_sql("ids", engine, if_exists=if_exists, index=False)
        self.get_game_data().to_sql(
            "game_data", engine, if_exists=if_exists, index=False
        )
        self.get_result_data().to_sql(
            "result_data", engine, if_exists=if_exists, index=False
        )
        self.get_play_data().to_sql(
            "play_data", engine, if_exists=if_exists, index=False
        )
        self.get_passing_data().to_sql(
            "passing_data", engine, if_exists=if_exists, index=False
        )
        self.get_rushing_data().to_sql(
            "rushing_data", engine, if_exists=if_exists, index=False
        )
        self.get_receiving_data().to_sql(
            "receiving_data", engine, if_exists=if_exists, index=False
        )
        self.get_epa_data().to_sql("epa_data", engine, if_exists=if_exists, index=False)
        self.get_punting_data().to_sql(
            "punting_data", engine, if_exists=if_exists, index=False
        )
        self.get_kicking_data().to_sql(
            "kicking_data", engine, if_exists=if_exists, index=False
        )
        self.get_drive_data().to_sql(
            "drive_data", engine, if_exists=if_exists, index=False
        )
        self.get_defense_data().to_sql(
            "defense_data", engine, if_exists=if_exists, index=False
        )
        self.get_special_data().to_sql(
            "special_data", engine, if_exists=if_exists, index=False
        )
        self.get_penalty_data().to_sql(
            "penalty_data", engine, if_exists=if_exists, index=False
        )
        if self.years[0] == 2009:
            self.get_injuries().to_sql(
                "injuries", engine, if_exists="replace", index=False
            )
        if self.years[0] > 2009:
            self.get_injuries().to_sql(
                "injuries", engine, if_exists="append", index=False
            )
