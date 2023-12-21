from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wiktionary.org/wiki/Wiktionary:Main_Page")  # target url

# x_path = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/table/tbody/tr[1]/td/table/tbody/tr['
#                                        '1]/td[1]/p/b/a')
# print(search.text)

# find by search
search = driver.find_element(By.NAME, value='search')
# type in search box and press ENTER
search.send_keys("Python", Keys.ENTER)

