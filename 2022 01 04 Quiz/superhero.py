import requests
from pprint import pprint


url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
params = {"feature": "intelligence"}
headers = {"Authorization": "2619421814940190"}
response = requests.get(url, params=params, headers=headers, timeout=5)
resp = response.json()
int_Hulk = int(resp['results'][0]['powerstats']['intelligence'])
pprint(int_Hulk)

url = "https://superheroapi.com/api/2619421814940190/search/Captain America"
params = {"feature": "intelligence"}
headers = {"Authorization": "2619421814940190"}
response = requests.get(url, params=params, headers=headers, timeout=5)
resp = response.json()
int_Cap = int(resp['results'][0]['powerstats']['intelligence'])
pprint(int_Cap)

url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
params = {"feature": "intelligence"}
headers = {"Authorization": "2619421814940190"}
response = requests.get(url, params=params, headers=headers, timeout=5)
resp = response.json()
int_Thanos = int(resp['results'][0]['powerstats']['intelligence'])
pprint(int_Thanos)

if int_Cap < int_Hulk > int_Thanos:
    print('Капитан Америка самый умный')
elif int_Hulk < int_Cap > int_Thanos:
    print('Халк самый умный')
else:
    print('Танос самый умный')