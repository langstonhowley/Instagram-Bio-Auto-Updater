#    Copyright 2024 Langston Howley

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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from skylive_requester import planet_location

import datetime
import time
import random
import os


USRN = os.environ.get("INSTAGRAM_USERNAME")
PASS = os.environ.get("INSTAGRAM_PASSWORD")
FIRST_UPDATE = True

# Setting up the webdriver
driver = webdriver.Chrome()

driver.implicitly_wait(30)
driver.get("https://www.instagram.com/")


# Login
username_feild = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, 'input[name="username"]')
)
username_feild.send_keys(USRN)

password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_field.send_keys(PASS)

form = driver.find_element(By.ID, "loginForm")
form.submit()

# Getting passed the "save login info"
not_now_button = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div",
)
not_now_button.click()

# Getting passed the notifications
not_now_button2 = driver.find_element(
    By.XPATH,
    "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
)
not_now_button2.click()

# Go to profile page
driver.get("https://www.instagram.com/accounts/edit/")

planet_list = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Now in the Edit Profile page
while True:
    try:
        # 60 minute timer
        if not FIRST_UPDATE:
            time.sleep(60 * 60)

        # Get the planet information from https://theskylive.com/
        planet = random.choice(planet_list)
        planet_info = planet_location(planet)
        new_bio = "{} RA|DEC|CO: {} | {} | {}\nWhen: {}".format(
            planet,
            planet_info[1],
            planet_info[2],
            planet_info[3],
            datetime.datetime.now().strftime("%Y-%m-%d @ %H:%M:%S"),
        )

        # Find the text area and type the planet info in it
        bio_textarea = driver.find_element(By.ID, "pepBio")

        if len(new_bio) < 150:
            bio_textarea.clear()
            bio_textarea.send_keys(new_bio)

        # Submit
        bio_submit_button = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div/form/div[4]/div",
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", bio_submit_button)
        bio_submit_button.click()

        FIRST_UPDATE = False
    except Exception:
        driver.close()
