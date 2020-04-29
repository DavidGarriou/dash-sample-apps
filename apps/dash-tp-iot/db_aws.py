import requests
import pandas as pd
from datetime import datetime, timezone
import time

ENTRY_POINT = '<url>'
API_PATH = '<path>'
ID_STATION = '{id}'

def get_aws_data(start, stop):
    hstart = datetime.fromtimestamp(start, tz=timezone.utc).isoformat()
    hstop = datetime.fromtimestamp(stop, tz=timezone.utc).isoformat()
    url = ENTRY_POINT + API_PATH + ID_STATION + '?' + 'start=' + hstart + '&' + 'stop=' + hstop
    response = requests.get(url)
    data = []
    for val in response.json()['Items']:
        data.append(float(val['Temperature']['S']))
    serie = pd.Series(data[-200:])
    return serie
