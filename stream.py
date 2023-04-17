import requests
import sys
import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

search_parameter = ' '.join(sys.argv[1:])
URL = 'https://vizer.tv/includes/ajax/publicFunctions.php'
data = {'getEpisodeLanguages': search_parameter}
streaming = requests.post(URL, data)

response = {
    'response': '',
    'items': []
}
streams = []

streaming_json = json.loads(streaming.text)
for stream in streaming_json['list']:
    streams.append(streaming_json['list'][stream]['id'])
    
URL = 'https://vizer.tv/embed/getPlay.php?id={}&sv=streamtape'.format(streams[0])
episode = requests.get(URL)


href_start = episode.text.find('href')
href_end = episode.text[href_start:].find(";")

URL = episode.text[href_start:][6:href_end - 1]
video = requests.get(URL)

tag = "document.getElementById('robotlink').innerHTML"
video_start = video.text.find(tag)
video_end = video.text.find(';', video_start)
video = video.text[video_start + len(tag):video_end]
parameters = 'https://streamtape.com/get_video?{}&stream=1'.format(video.split('?')[1].split("'")[0])

response['items'].append({
    'name': '',
    'image': '',
    'search_name': parameters
    })
response['response'] = 'ok'

print(response)
