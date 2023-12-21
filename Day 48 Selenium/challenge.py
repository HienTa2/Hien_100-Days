from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")  # target url

# type in fname, lastname, email and press ENTER
first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

# send the keys
first_name.send_keys("Samuel")
last_name.send_keys("Test")
email.send_keys("Samuel.Test@test.com")

# submit button
submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()

