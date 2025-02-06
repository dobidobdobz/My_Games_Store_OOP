import selenium
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class Search_epic:

    def __init__(self):
        super().__init__()
        self.epic_games_data_list = []

    def search_epic(self, user_input):

        # open chrome + navigate to website & search for game
        driver = Driver(uc=True, headless=False)
        url = 'https://store.epicgames.com/en-US/'
        driver.uc_open_with_reconnect(url, reconnect_time=1)

        sleep(2)
        epic_search_bar = driver.find_element(By.CLASS_NAME, value='css-mrdxwd')
        epic_search_bar.click()
        sleep(1)
        epic_search_bar.send_keys(f"{user_input}")
        sleep(1)
        epic_search_bar.send_keys(Keys.ENTER)
        sleep(3)

        # try see if you find game not found element if not there is games!
        try:
            no_game = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[4]/main/div[3]/div/div/div/div/div/div[2]/p").text
            driver.close()

            if no_game:
                return no_game

        # find elements with images of games & game price + title
        except selenium.common.exceptions.NoSuchElementException:
            five_epic_games_found = driver.find_elements(By.CLASS_NAME, value='css-g3jcms')
            five_epic_games_found_images = driver.find_elements(By.CLASS_NAME, value="css-1ae5wog")
            sleep(1)

            five_games_url_list = []

            # according to num of elements in between 0-5 extract imgs + links + text
            for x in range(0, 5):
                try:
                    url = five_epic_games_found_images[x].get_attribute("src")
                    purchase_url = five_epic_games_found[x].get_attribute("href")
                    text = five_epic_games_found[x].text
                    five_games_url_list.append(url)
                    five_games_url_list.append(text)
                    five_games_url_list.append(purchase_url)
                except:
                    pass

            # close webpage and return list of all data
            driver.close()
            return five_games_url_list
