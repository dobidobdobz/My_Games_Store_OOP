from seleniumbase import Driver
from selenium.webdriver.common.by import By
from time import sleep
import selenium


class Search_steamdb:

    def __init__(self):
        super().__init__()
        self.steamdb_game_data = []

    def search_steamdb(self, user_input):
        self.steamdb_game_data = []

        # open chrome + navigate to target website!
        driver = Driver(uc=True, headless=False)
        url = "https://steamdb.info/"
        driver.uc_open_with_reconnect(url, reconnect_time=1)

        # commands to open steam & find game price
        steam_db_search_bar = driver.find_element(by=By.NAME, value='q')
        steam_db_search_bar.click()
        sleep(1)
        steam_db_search_bar.send_keys(f"{user_input}")
        sleep(1)
        first_result_in_dropdown_bar = driver.find_element(By.CSS_SELECTOR, value="#js-search-suggestions a")
        first_result_in_dropdown_bar.click()

        # Game Name
        app_name = driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text

        # Current Price in Euro (if available) extract from element
        try:
            current_price = driver.find_element(By.CSS_SELECTOR, 'td[data-sort]').text  # Find the correct CSS selector
        except selenium.common.exceptions.NoSuchElementException:
            current_price = "Price not found"

        # find element image
        image_steam_game_url = driver.find_element(By.CSS_SELECTOR, "img[itemprop='image']")

        # extract url of img from element
        img_url_STEAM = image_steam_game_url.get_attribute("src")

        # retrieve current url for purchase link
        link_to_purchase_steam_game = driver.get_current_url()

        self.steamdb_game_data.append(img_url_STEAM)
        self.steamdb_game_data.append(app_name)
        self.steamdb_game_data.append(current_price)
        self.steamdb_game_data.append(link_to_purchase_steam_game)

        driver.close()

        return self.steamdb_game_data
