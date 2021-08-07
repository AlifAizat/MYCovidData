import pandas as pd
from io import StringIO
import requests
import collections

STATE_VAX_URL = "https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main/vaccination/vax_state.csv"
MAS_VAX_URL = "https://github.com/CITF-Malaysia/citf-public/raw/main/vaccination/vax_malaysia.csv"
STATE_CASE_URL = "https://github.com/AlifAizat/covid19-public/raw/main/epidemic/cases_state.csv"


def fetch_data_csv(data_url) -> pd.DataFrame:
    return pd.read_csv(StringIO(requests.get(data_url).text))


def csv_to_array(data_url: str, _columns=None):
    if _columns is None:
        _columns = []
    data_by_dates = {}
    csv_read = fetch_data_csv(data_url)

    for row in csv_read.iterrows():
        index = row[0]
        state_buffer = {}
        for col in columns:
            state_buffer[col] = csv_read.iloc[index][col]
        date = csv_read.iloc[index]['date']
        if date in data_by_dates:
            data_by_dates[date].append(state_buffer)
        else:
            data_by_dates[date] = [state_buffer]

    return data_by_dates


columns = ['date', 'state', 'dose1_daily', 'dose2_daily', 'total_daily', 'dose1_cumul', 'dose2_cumul', 'total_cumul']

states_vaccinations = csv_to_array(STATE_VAX_URL, columns)


print("hoho")

for state in states_vaccinations['2021-02-24']:
    print(state)
