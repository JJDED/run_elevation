import requests
import pandas as pd

year = 2020
params = dict(
    offset=0,
    start="2020-01-01T00:00",
    end="2020-12-31T00:00",
    sort="Minutes5UTC€DESC",
    limit=0
)

url = 'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime'
response = requests.get(
    url=url,
    params=params
)

result = response.json()

print(response.status_code)
print(response.)

records = result.get('records', [])

print('records:')

