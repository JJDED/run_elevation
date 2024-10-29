import requests
import pandas as pd

# https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime?offset=0&start=2020-01-01T00:00&end=2020-12-31T00:00&sort=Minutes5UTC%20DESC

year = 2020
params = dict(
    offset=0,
    start=f"{year}-01-01T00:00",
    end=f"{year}-12-31T00:00",
    sort="Minutes5UTC DESC",
    # limit=100,
    limit=0
)
url = 'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime'
response = requests.get(
    url=url,
    params=params
)

if response.status_code != 200:
    print(response.status_code)
    print(response.text)

result = response.json()

records = result.get('records', [])

print('records:')
print(len(records))

# gem som ... csv eller json eller ?

energy_df = pd.DataFrame(records)
print(energy_df)

energy_df.to_csv(f'energi_{year}.csv')
energy_df.to_json(f'energi_{year}.json')

