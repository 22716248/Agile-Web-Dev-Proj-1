"""
This set of tests check the majority of basic functions on our site,
simulating how a user would interact with our web application.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


successful_test = 0

# create a new browser session
driver = webdriver.Edge()
driver.implicitly_wait(2)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://127.0.0.1:5000/")

# get the login/register button
login_in_button = driver.find_element_by_id("login-register")
login_in_button.click()


#Test for login page
time.sleep(2)
login_page_title = driver.title
assert login_page_title == "User Login"
successful_test += 1


#register the user

register_button = driver.find_element_by_id("register")
register_button.click()

time.sleep(2)
login_page_title = driver.title
assert login_page_title == "User Register"
successful_test += 1

#register
username = driver.find_element_by_id("username")
password1 = driver.find_element_by_id("password")
password2 = driver.find_element_by_id("password2")
register   = driver.find_element_by_id("submit")
username.send_keys("sel-test-user01") # CHANGE USER HERE (could also implement random user, or delete this one.)
password1.send_keys("1111")
password2.send_keys("1111")
register.click()

time.sleep(2)
login_page_title = driver.title
assert login_page_title == "User Login"
successful_test += 1

#login the user

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login   = driver.find_element_by_id("submit")
username.send_keys("sel-test-user01")
password.send_keys("1111")
login.click()

# move to profile
time.sleep(2)
profile_page_title = driver.title
assert profile_page_title == "sel-test-user01's Profile"
successful_test += 1

# move to quiz
quiz_button = driver.find_element_by_id("take-quiz")
quiz_button.click()

# Test if successfully moved to Quiz Page
time.sleep(2)
profile_page_title = driver.title
assert profile_page_title == "Quiz"
successful_test += 1
q1 = driver.find_element_by_id("question1")
q2 = driver.find_element_by_id("question2")
q3 = driver.find_element_by_id("question3")
q4 = driver.find_element_by_id("question4")
q5 = driver.find_element_by_id("question5")
q6 = driver.find_element_by_id("question6")
q7 = driver.find_element_by_id("question7")
q8 = driver.find_element_by_id("question8")
q9 = driver.find_element_by_id("question9")
q10 = driver.find_element_by_id("question10")

q1.send_keys("crux")
q2.send_keys("aquarius")
q3.send_keys("centaurus")
q4.send_keys("scorpius")
q5.send_keys("sagittarius")
q6.send_keys("lupus")
q7.send_keys("puppis")
q8.send_keys("vela")
q9.send_keys("centaurus")
q10.send_keys("orion")

finish_quiz   = driver.find_element_by_id("submit")
finish_quiz.click()

# check if succesfully routed to profile page
time.sleep(2)
profile_page_title = driver.title
assert profile_page_title == "sel-test-user01's Profile"
successful_test += 1

# Answers validation and attempt checks will be done in unit tests to
# complement this set of tests


print("All " + str(successful_test) +  " out of " + str(successful_test) + " tests successful")

# close the browser window
driver.quit()