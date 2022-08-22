import time
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import  sleep
import os
folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)
def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)

i=0



driver = webdriver.Chrome()
driver.get('https://www.rawpixel.com/search/art?page=1&sort=curated&tags=%24publicdomain%2C%24noneditorial&topic_group=%24publicdomain')
driver.maximize_window()
img= driver.find_elements(By.XPATH,'//*[@itemprop="contentUrl"]')
time.sleep(2)
for name in img:
    i+=1
    imgurl = name.get_attribute('src')
    try:
        download_image(imgurl, folder_name, str(i))
        print(str(i)+'The download is complete')
    except:
        print(str(i)+'Download failed')

elment=driver.find_element(By.XPATH,'//*[@class="next activePath"]')
time.sleep(2)
elment.click()
img.clear()
for j in range(250):
    time.sleep(4)
    img = driver.find_elements(By.XPATH, '//*[@itemprop="contentUrl"]')
    time.sleep(2)
    for name in img:
        i += 1
        imgurl = name.get_attribute('src')
        try:
            download_image(imgurl, folder_name, str(i))
            print(str(i)+'The download is complete')
        except:
            print(str(i) + 'Download failed')
    elment = driver.find_element(By.XPATH, '//*[@class="next activePath"]')
    time.sleep(2)
    elment.click()
    img.clear()