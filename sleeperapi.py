import pandas as pd
from pandas import json_normalize
import psycopg2
import requests
import json
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def execute_statement(sql: str):
    with psycopg2.connect(
        host="localhost", database="thefantasybot", user="tbakely"
    ) as conn:
        df = pd.read_sql(sql, conn)
        return df


class SleeperLeague:
    # remember to incorporate json_normalize when rosters are set
    def __init__(
        self, league_id: int, year: int = None, json: bool = False, dynasty=False
    ):
        self.league_id = str(league_id)
        self.year = year
        self.json = json
        self.dynasty = dynasty
        self.sleeper_ids = execute_statement(
            "select sleeper_id as id, name from full_ids"
        )
        self.sleeper_ids["id"] = (
            self.sleeper_ids["id"].astype(str).apply(lambda x: x[:-2])
        )

    def get_data(self, url):
        response = requests.get(url)
        if not self.json:
            data = json.dumps(response.json())
            return pd.read_json(data)
        else:
            return response.json()

    def users(self):
        url = f"https://api.sleeper.app/v1/league/{self.league_id}/users"
        users = self.get_data(url)
        users = pd.concat([users, json_normalize(users["metadata"])], axis=1).drop(
            columns="metadata"
        )
        return users

    def rosters(self):
        url = f"https://api.sleeper.app/v1/league/{self.league_id}/rosters"
        rosters = self.get_data(url)
        rosters = pd.concat(
            [rosters, json_normalize(rosters["metadata"])], axis=1
        ).drop(columns="metadata")
        temp = json_normalize(rosters["settings"])
        rosters = pd.concat([rosters, temp], axis=1).drop("settings", axis=1)

        sleeper_ids_dict = (
            self.sleeper_ids[["id", "name"]].set_index("id").to_dict()["name"]
        )

        df_rows = []
        if self.dynasty:
            rosters["starters_mapped"] = rosters["starters"].apply(
                lambda x: [sleeper_ids_dict[k] for k in x]
            )
            start_positions = [
                "QB",
                "RB1",
                "RB2",
                "WR1",
                "WR2",
                "WR3",
                "TE",
                "FLEX1",
                "FLEX2",
                "SFLEX",
            ]
        else:
            rosters["starters_mapped"] = rosters["starters"].apply(
                lambda x: [sleeper_ids_dict[k] if not len(k) < 4 else k for k in x]
            )
            start_positions = [
                "QB",
                "RB1",
                "RB2",
                "WR1",
                "WR2",
                "TE",
                "FLEX1",
                "FLEX2",
                "FLEX3",
                "DEF",
            ]
        for i, row in enumerate(rosters["starters_mapped"]):
            data = dict(zip(start_positions, row))
            df = pd.DataFrame(data, index=[i])
            df_rows.append(df)
        temp = pd.concat(df_rows)
        rosters = pd.concat([rosters, temp], axis=1)

        return rosters

    def draft(self, draft_id):
        url = f"https://api.sleeper.app/v1/draft/{draft_id}/picks"
        draft = self.get_data(url)
        draft = pd.concat([draft, json_normalize(draft["metadata"])], axis=1).drop(
            columns="metadata"
        )
        draft["player_name"] = draft["first_name"] + " " + draft["last_name"]
        draft.drop(columns=["first_name", "last_name"], inplace=True)
        return draft

    def weekly_report(self, position: str):
        roster = self.rosters()
        not_available = list(roster["players"].explode())
        if self.year is None:
            weekly_data = execute_statement(f"select * from weekly_{position}")
        else:
            weekly_data = execute_statement(
                f"select * from weekly_{position} where season = {self.year}"
            )
        weekly_data["available"] = np.where(
            weekly_data["sleeper_id"].astype(int).astype(str).isin(not_available), 0, 1
        )
        return weekly_data.drop_duplicates()
