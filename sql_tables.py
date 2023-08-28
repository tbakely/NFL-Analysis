import psycopg2
import pandas as pd


def execute_statement(sql: str):
    with psycopg2.connect(
        host="localhost", database="thefantasybot", user="tbakely"
    ) as conn:
        df = pd.read_sql(sql, conn)
        return df


passing_with_ngs = """select
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
	ngs.avg_time_to_throw
from weekly_data wd
join ngs_passing_data ngs
on wd.player_id = ngs.player_gsis_id
and wd.season = ngs.season
and wd.week = ngs.week
where position = 'QB'
and wd.attempts > 0
order by season asc"""
