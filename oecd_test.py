from pyjstat import pyjstat
import requests
import os
import json
from datetime import datetime
import locale
import io
import pandas as pd
os.makedirs('data', exist_ok=True)
access_token = os.getenv('DW_TOKEN')

#ODA Grant Equivalent Measure, Total from 1960 (69Npy)
oecd_url='http://stats.oecd.org/SDMX-JSON/data/TABLE1/20001.1.11010.1160.D/all?startTime=2018'
response = requests.get(oecd_url)
data=response.json()

