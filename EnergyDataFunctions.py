import requests
import pandas as pd

def extractFunc(year):
    params = dict(
    offset=0,
    start=f"{year}-01-01T00:00",
    end=f"{year}-12-31T00:00",
    sort="Minutes5UTC DESC",
    limit=0
    )
    url = 'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime'
    response = requests.get(url=url,params=params) #
    records = response.json().get('records', [])
    return pd.DataFrame(records)
    
def loadFunc(energy_df,year):
    print('Load data to csv...')
    filename = f'energi_{year}.csv'
    print(f'energi_{year}.csv')
    energy_df.to_csv(filename, index=False)
    print('Data loaded to csv...')
    return filename

def transformFunc(filename):
    print('Transform data...')
    df = pd.read_csv(filename)

    exportGermanyDK1 = df[df['PriceArea'] == 'DK1']["ExchangeGermany"].sum()
    exportGermanyDK2 = df[df['PriceArea'] == 'DK2']["ExchangeGermany"].sum()
    #totalExportGermany = exportGermanyDK1 + exportGermanyDK2

    return {
        "Net Export DK1 (MW)": exportGermanyDK1,
        "Net Export DK2 (MW)": exportGermanyDK2
    }

def run():
    # Extract
    input_year = input('Enter year: ')
    df = extractFunc(input_year)

    #Load
    filename = loadFunc(df, input_year)
    
    #Transform
    result = transformFunc(filename)

    for key, value in result.items():
        print(f"{key}: {value}")