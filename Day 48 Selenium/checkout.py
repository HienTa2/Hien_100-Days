from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT = 'MED4114'
ACCOUNT_PASSWORD = '###'

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
)

# # Click Sign in Button
# time.sleep(2)
# med_login = driver.find_element(by=By.LINK_TEXT, value="Sign in")
# med_login.click()

# Sign in
time.sleep(5)
med_login = driver.find_element(by=By.ID, value="username")
med_login.send_keys(ACCOUNT)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
