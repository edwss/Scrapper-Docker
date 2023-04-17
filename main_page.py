import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.arguments.extend(["--headless"])     # << this
driver = uc.Chrome(options)

URL = 'https://vizer.tv/'
driver.get(URL)
time.sleep(2)

response = {
    'response': '',
    'items': []
}
try:
    items = driver.find_elements(By.CLASS_NAME, 'bslider-item')
    for item in items:
        search_name = item.find_element(By.TAG_NAME, 'a').get_attribute('href').replace('https://vizer.tv/', '')
        name = item.find_element(By.CLASS_NAME, 'infos').find_element(By.TAG_NAME, 'span').text
        image = item.find_element(By.TAG_NAME, 'picture').find_element(By.CLASS_NAME, 'img').get_attribute('src')
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
