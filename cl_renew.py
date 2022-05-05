# renew all my craigslist classfields

from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

usr = 'env'
pwd = 'env'

selectLinkOpeninNewTab = (Keys.CONTROL + Keys.ENTER)

driver = webdriver.Chrome()
driver.get('https://accounts.craigslist.org/login?rt=L&rp=%2Flogin%2Fhome')
driver.set_page_load_timeout(30)

usr_box = driver.find_element_by_id('inputEmailHandle')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_id('inputPassword')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_class_name('accountform-btn')
login_button.submit()

time.sleep(3)

driver.find_element(By.XPATH, '//input[@name = "go" and @value = "renew"]').send_keys(selectLinkOpeninNewTab)
