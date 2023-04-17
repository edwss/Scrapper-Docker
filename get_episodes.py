import requests
import sys
import json
import re


search_parameter = ' '.join(sys.argv[1:])
URL = 'https://vizer.tv/includes/ajax/publicFunctions.php'
data = {'getEpisodes': '{}'.format(search_parameter)}
episodes = requests.post(URL, data)

response = {
    'response': '',
    'items': []
}

episodes_json = json.loads(episodes.text)

for episode in episodes_json['list']:
	response['items'].append({
		'name': re.sub(r"[^a-zA-Z0-9 ]", "", episodes_json['list'][episode]['title']),
		'image': 'https://image.tmdb.org/t/p/w185' + episodes_json['list'][episode]['img'],
		'search_name': episodes_json['list'][episode]['id']
	})
response['response'] = 'ok'

print(response)
