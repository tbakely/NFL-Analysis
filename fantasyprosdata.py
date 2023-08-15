from scrapetools import *


class FantasyProsData:
    def __init__(self, scoring: str):
        self.scoring = scoring

        if not self.scoring in ["STD", "PPR", "HALF"]:
            raise ValueError("Scoring system must be STD, PPR, or HALF.")

    def pull_adp(self):
        scoring_map = {
            "STD": "overall",
            "PPR": "ppr-overall",
            "HALF": "half-point-ppr-overall",
        }

        df = scrape_to_df(
            f"https://www.fantasypros.com/nfl/adp/{scoring_map[self.scoring]}.php",
            "data",
        )

        df["Player"] = df["Player Team (Bye)"].apply(
            lambda x: apply_regex(r"^([a-zA-Z'-.]+\s[a-zA-Z'-]+)(\s(IV|I{2,3}))?", x)
        )
        df["Team"] = df["Player Team (Bye)"].apply(
            lambda x: apply_regex(r"(?!IV|I{1,3})([A-Z]{2,3})", x)
        )
        df["Bye"] = df["Player Team (Bye)"].apply(lambda x: apply_regex(r"\d+", x))
        df["Position"] = df["POS"].apply(lambda x: apply_regex(r"\D+", x))
        df.rename(columns={"AVG": "ADP"}, inplace=True)

        df = df[["Rank", "Player", "Team", "Bye", "Position", "ADP"]]
        return df

    def projected_points(self, week: str = "draft"):
        """Scrapes projected points from fantasypros.com

        Args:
            scoring (str, optional): 'STD', 'PPR', or 'HALF'. Defaults to 'STD'.
            week (str, optional): _description_. Defaults to 'draft'.

        Returns:
            pd.DataFrame: Finalized dataframe with projected points for the week.
        """
        data = []
        for position in ["qb", "wr", "rb", "te"]:
            df = scrape_to_df(
                f"https://www.fantasypros.com/nfl/projections/{position}.php?week={week}&scoring={self.scoring}",
                "data",
                multilevel=True,
            )
            df["Team"] = df["Player"].apply(
                lambda x: apply_regex(r"(?!IV|I{1,3})([A-Z]{2,3})", x)
            )
            df["Player"] = df["Player"].apply(
                lambda x: apply_regex(
                    r"^([a-zA-Z'-.]+\s[a-zA-Z'-]+)(\s(IV|I{2,3}))?", x
                )
            )
            df["Position"] = position.upper()
            df = df[["Player", "Position", "Team", "FPTS"]]
            data.append(df)
        data = pd.concat(data)

        data = data.sort_values("FPTS", ascending=False).reset_index(drop=True)

        return data
