import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import re

pd.options.display.float_format = "{:.2f}".format


def scrape_to_df(url: str, id: str, multilevel=False):
    res = requests.get(url)
    if res.ok:
        soup = bs(res.content, "html.parser")
        table = soup.find("table", {"id": f"{id}"})
        df = pd.read_html(str(table))[0]
    else:
        print("oops something didn't work right", res.status_code)
    if multilevel:
        df.columns = df.columns.droplevel(level=0)
    return df


def apply_regex(regex: str, string: str):
    match = re.search(regex, string)
    if match:
        return match.group()
    else:
        return np.nan
