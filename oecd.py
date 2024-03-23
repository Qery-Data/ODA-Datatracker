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

rename_columns = {"AUS": "Australia", "AUT": "Austria", "BEL": "Belgium", "CAN": "Canada", "CHE": "Switerland", "CHL": "Chile", "COL": "Colombia", "CRI": "Costa Rica", "CZE": "Czechia", "DNK": "Denmark", "EST": "Estonia", "EA20": "Euro area", "EU27_2020": "EU27", "FIN": "Finland", "FRA": "France", "DEU": "Germany", "GRC": "Greece", "HUN": "Hungary", "ISL": "Iceland", "IRL": "Ireland", "ISR": "Israel", "ITA": "Italy", "JPN": "Japan", "KOR": "Korea", "LVA": "Latvia", "LTU": "Lithuania", "LUX": "Luxembourg", "MEX": "Mexico", "NLD": "Netherlands", "NZL": "New Zealand", "NOR": "Norway", "POL": "Poland", "PRT": "Portugal", "SVK": "Slovak Republic", "SVN": "Slovenia", "ESP": "Spain", "SWE": "Sweden", "TUR": "Türkiye", "GBR": "United Kingdom", "USA": "United States", "4EU001": "EU Institutions"}

#ODA Grant Equivalent Measure, Total from 1990 (69Npy)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/DAC.1010..1140+1160..Q.?startPeriod=1990&endPeriod=2017&dimensionAtObservation=AllDimensions'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/DAC.11010..1140+1160..Q.?startPeriod=2018&dimensionAtObservation=AllDimensions'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df_pre18=pd.read_csv(io.StringIO(result.text))
df_new_pre18 = df_pre18.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
df_new_1 = pd.concat([df_new_pre18,df_new])
df_new_1.index = df_new_1.index.astype(int)
df_new_1.sort_index(inplace=True)
df_new_1.rename(columns={'DAC': 'DAC Countries, Total'}, inplace=True)
df_new_1.index.name = 'Year'
df_new_1.to_csv('data/OECD_ODA_Total.csv', index=True)

#ODA Gross National Income from 1990 (Ptm3T)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/DAC.2+11002.....?startPeriod=1990&dimensionAtObservation=AllDimensions'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
df_new.rename(columns={'DAC': 'DAC Countries, Total'}, inplace=True)
df_new.to_csv('data/OECD_ODA_GNI_Total.csv', index=True)

#ODA Last avaliable year Grant Equivivalent (hHpUJ) and GNI 
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.2+11010...USD.V.?startPeriod=2022&dimensionAtObservation=AllDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='DONOR', columns='TIME_PERIOD', values='OBS_VALUE')
df_new = df_new.rename(index=rename_columns)
df_new.rename(columns={df_new.columns[0]: 'US Dollar'}, inplace=True)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.11002+2...PT_B5G..?startPeriod=2022&dimensionAtObservation=AllDimensions'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df_gni=pd.read_csv(io.StringIO(result.text))
df_new_gni = df_gni.pivot(index='DONOR', columns='TIME_PERIOD', values='OBS_VALUE')
df_new_gni = df_new_gni.rename(index=rename_columns)
df_new_gni.rename(columns={df_new_gni.columns[0]: 'Percentage'}, inplace=True)
df_new_1 = pd.concat([df_new_gni,df_new], axis=1)
df_new_1.index.name = 'Donor'
df_new_1.to_csv('data/OECD_ODA_GRANT_GNI_recent_y.csv', index=True)


#ODA Pct change last year (ECLuA)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.11010+2...USD.Q.?startPeriod=2021&endPeriod=2022&dimensionAtObservation=AllDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='DONOR', columns='TIME_PERIOD', values='OBS_VALUE')
df_new['change_pct'] = ((df_new.iloc[:,1] - df_new.iloc[:,0]) / df_new.iloc[:,0]*100)
df_new = df_new.rename(index=rename_columns)
df_new.index.name = 'Donor'
df_new.to_csv('data/OECD_ODA_pct_change_last_year.csv', index=True)

#ODA Gross National Income from 1990, by Country (L4Dln)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.11002+2.....?startPeriod=1990&dimensionAtObservation=AllDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
df_new = df_new.rename(columns=rename_columns)
df_new.index.name = 'Year'
df_new.to_csv('data/OECD_ODA_GNI_Total_Country.csv', index=True)

#ODA Grant Equivalent Measure, Total from 1990, by country (aPS1l)
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.11010+2...USD.Q.?startPeriod=2018&dimensionAtObservation=AllDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new = df.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
df_new = df_new.rename(columns=rename_columns)
df_new.index.name = 'Year'
oecd_url='https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,1.0/CAN+JPN+GBR+USA+AUS+ISL+KOR+NZL+NOR+CHE+AUT+BEL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+LTU+LUX+NLD+POL+PRT+SVK+SVN+ESP+SWE+4EU001.1010+2..1140.USD.Q.?startPeriod=1990&endPeriod=2017&dimensionAtObservation=AllDimensions'
resultat = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(resultat.text))
df_new_1 = df.pivot(index='TIME_PERIOD', columns='DONOR', values='OBS_VALUE')
df_new_1 = df_new_1.rename(columns=rename_columns)
df_new_1.index.name = 'Year'
df_final = pd.concat([df_new_1, df_new])
df_new.to_csv('data/OECD_ODA_Total_Country.csv', index=True)