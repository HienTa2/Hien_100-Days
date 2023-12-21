from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")  # target url

# find element
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cent.text}")

# find element by NAME
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)

# documentation link searching CSS anchor tag
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# find element by XPATH
# x_path = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[3]/div[2]')
# print(x_path.)

# # find elements
# upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
#
# for n in range(len(upcoming_events)):
#     events[n] = {
#         "time": upcoming_events[n].text,
#         "name": event_names[n].text
#     }
# print(events)

# Find elements
upcoming_event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Check if lengths of lists are equal
if len(upcoming_event_times) != len(event_names):
    raise ValueError("Mismatch in number of events and event names")

# Create a list of events using list comprehension and zip
events = [
    {"time": event_time.text, "name": event_name.text}
    for event_time, event_name in zip(upcoming_event_times, event_names)
]

# Print events
print(events)


# driver.quit()
