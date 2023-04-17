import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import urllib.parse

search_parameter = ' '.join(sys.argv[1:])
#URL = 'https://vizer.tv/pesquisar/{}'.format(urllib.parse.quote(search_parameter.encode('utf8')))
URL = 'https://vizer.tv/pesquisar/{}'.format(search_parameter)
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
    main_page = driver.find_element(By.CLASS_NAME, 'searchPageFixed')
    cards = main_page.find_element(By.CLASS_NAME, 'listItems').find_elements(By.TAG_NAME, 'a')
    for card in cards:
        search_name = card.get_attribute('href').replace('https://vizer.tv/', '')
        name = card.find_element(By.CLASS_NAME, 'infos').find_element(By.TAG_NAME, 'span').text
        image = card.find_element(By.TAG_NAME, 'picture').find_element(By.CLASS_NAME, 'img').get_attribute('src')
        response['items'].append(
            {
                'name': name,
                'image': image,
                'search_name': search_name
            }
        )
    response['response'] = 'ok'
except Exception as e:
    response = {'response': e}

print(response)

driver.quit()
