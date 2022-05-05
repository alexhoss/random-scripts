# make a post on an fb group, offering a product

import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

login = 'env'
pwd = 'env'
image_0 = 'x'
image_1  = 'y'
image_2 = 'z'
postDiscussion = 'message'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2} 
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com/')
driver.set_page_load_timeout(500)

def waitForLoad(id):
    try:
        myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id)))
        print ("Page is ready!")
        time.sleep(3)
    except TimeoutException:
        print ("Loading took too much time")
        
def makePost():
    waitForLoad('pagelet_pinned_posts')
    driver.find_element_by_class_name('fbReactComposerAttachmentSelector_STATUS').click()
    time.sleep(3)
    driver.find_element_by_xpath("//textarea[@name='xhpc_message_text']").send_keys(postDiscussion)
  
    driver.find_element_by_css_selector('._n._5f0v').send_keys(image_0)
    time.sleep(3)
    driver.find_element_by_css_selector('._n._5f0v').send_keys(image_1)
    time.sleep(3)
    driver.find_element_by_css_selector('._n._5f0v').send_keys(image_2)
    time.sleep(10)
    postButton = driver.find_element_by_xpath("//span[text()='Post']")
    driver.execute_script("window.scrollTo(0, 200)")
    postButton.click()

loginBar = driver.find_element_by_id('email')
loginBar.send_keys(login)

pwdBar = driver.find_element_by_id('pass')
pwdBar.send_keys(pwd)

time.sleep(0.5)
driver.find_element_by_xpath("//input[@value='Log In']").click()


driver.get('https://www.facebook.com/groups/x/')
makePost()



