import requests
import json

hakusana = input('Syötä paikkakunnan nimi: ')
api_key = '83ccf1b063522f573de42a5e6f1fc24e'
units = 'metric'
pyyntö = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}&units={units}'

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus['weather']:
            print('Sää: ')
            print(a['description'])
        print('Lämpötila: ')
        print(json_vastaus['main']['temp'])
except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa')
