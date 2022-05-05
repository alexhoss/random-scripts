# What page is my amazon product on for search_term? 

from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

search_term = 'x'
exact_title = 'y'

driver = webdriver.Chrome()
driver.get('https://www.amazon.ca/')
#driver.set_page_load_timeout(250)
i = 1

def check_exists_by_xpath(xpath):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath)
    except Exception as e:
        print(e)
        return False
    return True

#Enter Search Bar
searchBar = driver.find_element_by_id('twotabsearchtextbox')
searchBar.send_keys(search_term)

submitButton = driver.find_element_by_class_name('nav-input')
submitButton.click()

driver.set_page_load_timeout(500)

nextPage = driver.find_element_by_id('pagnNextString')

#Start Searching
while not check_exists_by_xpath("//*[@data-attribute='" + exact_title + "']"):
    time.sleep(0.5)
    nextPage = driver.find_element_by_id('pagnNextString')
    nextPage.click()
    i+=1

#Found product, now set into focus    
found = driver.find_element_by_xpath("//*[@data-attribute='" + exact_title + "']")
driver.execute_script("arguments[0].scrollIntoView(true);", found)

driver.execute_script("alert('Product found on page: " + str(i) + "')")

