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
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/20001.1.11010.1160.D/all?startTime=2018'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Year', columns='Donor', values='Value')
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/20001.1.1010.1140.D/all?startTime=1960&endTime=2017&dimensionAtObservation=allDimension'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df_pre18=pd.read_csv(io.StringIO(resultat.text))
df_new_pre18 = df_pre18.pivot(index='Year', columns='Donor', values='Value')
df_new_1 = pd.concat([df_new_pre18,df_new])
df_new_1.to_csv('data/OECD_ODA_Total.csv', index=True)

#ODA Gross National Income from 1960 (Ptm3T)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/20001.1.11002+2.1140+1160.A+D+N/all?startTime=1960&endTime=2021&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Year', columns='Donor', values='Value')
df_new.to_csv('data/OECD_ODA_GNI_Total.csv', index=True)

#ODA Last avaliable year Grant Equivivalent (hHpUJ) and GNI 
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.11002+11010.1160.A/all?startTime=2021&endTime=2021&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Donor', columns='Unit', values='Value')
df_new.to_csv('data/OECD_ODA_GRANT_GNI_recent_y.csv', index=True)

#ODA Pct change last year (ECLuA)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.11010.1140+1160.D/all?startTime=2020&endTime=2021&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Donor', columns='Year', values='Value')
df_new['change_pct'] = ((df_new.iloc[:,1] - df_new.iloc[:,0]) / df_new.iloc[:,0]*100)
df_new.to_csv('data/OECD_ODA_pct_change_last_year.csv', index=True)

#ODA Gross National Income from 1960, by Country (L4Dln)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.11002.1140+1160.A+D+N/all?startTime=2018&dimensionAtObservation=allDimensions&pid=c0dcdd50-2d08-440b-94d7-8aa50471b7ff'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Year', columns='Donor', values='Value')
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.2.1140+1160.A+D+N/all?startTime=1960&endTime=2017&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df_pre18=pd.read_csv(io.StringIO(resultat.text))
df_new_pre18 = df_pre18.pivot(index='Year', columns='Donor', values='Value')
df_new_1 = pd.concat([df_new_pre18,df_new])
df_new_1.to_csv('data/OECD_ODA_GNI_Total_Country.csv', index=True)

#ODA Grant Equivalent Measure, Total from 1960, by country (aPS1l)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.11010.1160.D/all?startTime=2018&endTime=2021&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='Year', columns='Donor', values='Value')
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/801+1+2+301+68+3+18+4+5+40+75+20+21+6+701+742+22+7+820+8+76+9+69+61+50+10+11+12+302+918.1.1010.1140.D/all?startTime=1960&endTime=2017&dimensionAtObservation=allDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df_pre18=pd.read_csv(io.StringIO(resultat.text))
df_new_pre18 = df_pre18.pivot(index='Year', columns='Donor', values='Value')
df_new_1 = pd.concat([df_new_pre18,df_new])
df_new_1.to_csv('data/OECD_ODA_Total_Country.csv', index=True)