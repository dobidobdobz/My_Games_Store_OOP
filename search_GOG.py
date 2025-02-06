import selenium
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class Search_gog:

    def __init__(self):
        super().__init__()

    def search_gog(self, user_input):
        # initialize the driver in GUI mode with UC enabled
        driver = Driver(uc=True, headless=False)
        url = 'https://www.gog.com/en/'
        driver.uc_open_with_reconnect(url, reconnect_time=1)

        # commands to open gog site & find data relevant to game
        sleep(2)
        gog_search_bar_icon = driver.find_element(By.CLASS_NAME, value='js-menu-search')
        gog_search_bar_icon.click()
        sleep(1)
        gog_search_bar = driver.find_element(By.CSS_SELECTOR, value='input[type="text"]')
        gog_search_bar.click()
        gog_search_bar.send_keys(f"{user_input}")
        sleep(1)
        gog_search_bar.send_keys(Keys.ENTER)
        sleep(4)

        # try to find no game found element
        try:
            no_game = driver.find_element(By.XPATH, value="/html/body/div[2]/app-root/div/div/app-page/catalog/div/catalog-content/div/div[2]/div[2]/h2").text
            driver.close()

            if no_game:
                print(no_game)
                return no_game

        # find relevant game elements and extract data
        except selenium.common.exceptions.NoSuchElementException:
            # game element for url image + text's
            five_GOG_games_images = driver.find_elements(By.CSS_SELECTOR, value='source.ng-star-inserted')
            five_GOG_games_links = driver.find_elements(By.CSS_SELECTOR, value="product-tile a")

            urls = []

            for x in range(0, len(five_GOG_games_links)):
                print(five_GOG_games_links)
                print(five_GOG_games_links[0])

            # process data for desired order in returned list
            for x in range(0, len(five_GOG_games_images), 4):
                url = five_GOG_games_images[x].get_attribute("srcset").split()
                urls.append(url)

            gog_games_data = []

            for x in range(0, len(urls)):
                url = urls[x]
                gog_games_data.append(url)
                game_data = five_GOG_games_links[x].text
                gog_games_data.append(game_data)
                game_link = five_GOG_games_links[x].get_attribute("href")
                gog_games_data.append(game_link)

            # close driver
            driver.close()

            return gog_games_data
