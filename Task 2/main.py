import requests
from bs4 import BeautifulSoup
import lxml

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
chrome_driver_path = '/Users/ernest/Learn/driver/chromedriver'


TITLES = ['data engineer', 'data analyst', 'data scientist', 'python', 'machine learning']
DATA_ENGINEER_URL = 'https://www.indeed.com/jobs?q=data+engineer&l=&vjk=d23f1d1057a4cae2'
DATA_ANALYST_URL = 'https://www.indeed.com/jobs?q=DATA+analyst&l=&vjk=bc97e559fccbb4ee'
DATA_SCIENTIST_URL = 'https://www.indeed.com/jobs?q=data+scientist&l=&vjk=3b1b1d1b5b1b1b1b'
PYTHON_URL = 'https://www.indeed.com/jobs?q=python&l=&vjk=3b1b1d1b5b1b1b1b'
MACHINE_LEARNING_URL = 'https://www.indeed.com/jobs?q=machine+learning&l=&vjk=3b1b1d1b5b1b1b1b'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url=DATA_ENGINEER_URL)
time.sleep(5)

titles = driver.find_elements(By.CLASS_NAME,"resultContent")[0]
titles.find_element(By.TAG_NAME, "a")
print(titles.text)

titles = driver.find_elements(By.CLASS_NAME,"resultContent")
job_list = []
for title in titles:
    jobs = title.find_elements(By.TAG_NAME, "a")
    for job in jobs:
        job_text = job.text
        print(job_text)
        # print()
        # job_list.append(job_text)
 



# print(job_list)




