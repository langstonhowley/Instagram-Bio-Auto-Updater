#    Copyright 2020 Langston Howley

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from skylive_requester import planet_location
import datetime
import random
from decouple import config


USRN = config('INSTAGRAM_USERNAME')
PASS = config('INSTAGRAM_PASSWORD')
FIRST_UPDATE = True


#Setting up the webdriver
options = webdriver.ChromeOptions()
'''
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
'''


chrome_driver_path = '/Users/langston/Library/Application Support/Google/chromedriver'
driver = webdriver.Chrome(chrome_driver_path, options=options)

driver.implicitly_wait(6)
driver.get('https://www.instagram.com/')


#Login
username_feild = WebDriverWait(driver,3).until(lambda d: d.find_element_by_css_selector('input[name="username"]')) #driver.find_element_by_css_selector('input[name="username"]') #driver.find_element_by_name('username')
password_field = driver.find_element_by_css_selector('input[name="password"]') #driver.find_element_by_name('password')
form = driver.find_element_by_id('loginForm')

username_feild.send_keys(USRN)
password_field.send_keys(PASS)
form.submit()

WebDriverWait(driver,5).until(EC.staleness_of(username_feild))
#Getting passed the "save login info"
not_now_button = driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF') #WebDriverWait(driver,3).until(lambda d: d.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF')) 
not_now_button.click()

#Getting passed the notifications
not_now_button2 = driver.find_element_by_css_selector('button.aOOlW.HoLwm') #WebDriverWait(driver,3).until(lambda d: d.find_element_by_css_selector('button.aOOlW.HoLwm')) 
not_now_button2.click()

#Now in the home page
profile_link = driver.find_element_by_link_text(USRN)
profile_link.click()


#Now in the profile page
edit_profile = driver.find_element_by_link_text('Edit Profile') #WebDriverWait(driver,3).until(lambda d:  d.find_element_by_link_text('Edit Profile'))
edit_profile.click()

#Now in the Edit Profile page
while True:
    if(not FIRST_UPDATE):
        time.sleep(60*10)

    planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    bio_textarea = driver.find_element_by_id('pepBio')

    planet_info = planet_location(random.choice(planet_list))
    new_bio = '{} RA|DEC|CO: {} | {} | {}\nWhen: {}'.format(planet_info[1],planet_info[2],planet_info[3], planet_info[7],datetime.datetime.now().strftime("%Y-%m-%d @ %H:%M:%S"))

    if(len(new_bio) < 150):
        bio_textarea.clear()
        bio_textarea.send_keys(new_bio)

    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.sqdOP.L3NKy.y3zKF')))
    bio_submit_button = driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
    driver.execute_script("arguments[0].scrollIntoView(true);", bio_submit_button)
    bio_submit_button.click()

    FIRST_UPDATE = False
#driver.close()



