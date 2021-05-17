from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

successful_test = 0

# create a new Firefox session
driver = webdriver.Edge()
driver.implicitly_wait(2)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://127.0.0.1:5000/")

# get the login button
login_in_button = driver.find_element_by_id("login-register")
login_in_button.click()

# login the user

#Test for login page
driver.implicitly_wait(2)
login_page_title = driver.title
successful_test += 1

assert login_page_title == "Login Page"
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login   = driver.find_element_by_id("submit")
username.send_keys("testuser")
password.send_keys("1111")
login.click()

# move to profile
time.sleep(1)
profile_page_title = driver.title
assert profile_page_title == "testuser's Profile"
successful_test += 1

print("All " + str(successful_test) +  " out of " + str(successful_test) + " tests successful")

# close the browser window
driver.quit()