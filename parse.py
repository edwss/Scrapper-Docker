import sys
import urllib.parse
import requests
import json

search_parameter = ' '.join(sys.argv[1:])
URL = 'https://vizer.tv/{}'.format(search_parameter)
options = uc.ChromeOptions()
options.arguments.extend(["--headless"])     # << this
driver = uc.Chrome(options)

driver.get(URL)
time.sleep(2)

response = {
    'response': '',
    'items': []
}
try:
    main_page = driver.find_element(By.TAG_NAME, 'body')
    seasons = main_page.find_element(By.CLASS_NAME, 'bslider-outer').find_elements(By.CLASS_NAME, 'bslider-item')
    for season in seasons:
        item = season.find_element(By.CLASS_NAME, 'item')
        season_number = item.text
        season_id = item.get_attribute('data-season-id')
        response['items'].append(
            {
                'name': season_number,
                'image': '',
                'search_name': season_id
            }
        )
    response['response'] = 'ok'
except Exception as e:
    response = {'response': e}

print(response)
driver.quit()
