from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():
    """Sets up and returns a Chrome WebDriver with options."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def get_store_items(driver):
    """Returns a list of store item IDs."""
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    return [item.get_attribute("id") for item in items]


def get_upgrade_costs(driver):
    """Extracts and returns a dictionary of upgrade costs and corresponding IDs."""
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    item_prices = []
    for price in all_prices:
        if price.text != "":
            cost = int(price.text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    return dict(zip(item_prices, get_store_items(driver)))


def get_cookie_count(driver):
    """Returns the current number of cookies."""
    money_element = driver.find_element(by=By.ID, value="money").text.replace(",", "")
    return int(money_element)


def buy_upgrade(driver, cookie_upgrades, cookie_count):
    """Buys the most expensive affordable upgrade."""
    affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost}
    if affordable_upgrades:
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(by=By.ID, value=to_purchase_id).click()


def main():
    driver = setup_driver()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # Wait for the cookie element to be clickable before starting
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie")))

    cookie = driver.find_element(by=By.ID, value="cookie")
    check_interval = 5  # seconds
    game_duration = 100  # seconds (5 minutes)
    five_min = time.time() + 60 * 1  # 5 minutes

    start_time = time.time()
    next_check = start_time + check_interval

    while time.time() - start_time < game_duration:
        cookie.click()

        if time.time() > next_check:
            try:
                cookie_upgrades = get_upgrade_costs(driver)
                cookie_count = get_cookie_count(driver)
                buy_upgrade(driver, cookie_upgrades, cookie_count)
                next_check = time.time() + check_interval
            except Exception as e:
                print(f"An error occurred: {e}")

    # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break


if __name__ == "__main__":
    main()
