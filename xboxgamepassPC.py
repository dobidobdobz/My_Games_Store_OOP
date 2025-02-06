from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import selenium


class Search_Xbox:

    def __init__(self):
        super().__init__()

    def search_xbox(self, user_input):
        # initialize the driver in GUI mode with UC enabled
        driver = Driver(uc=True, headless=False)

        # set the target URL
        url = "https://www.xbox.com/en-GB/xbox-game-pass/games"

        # open URL with a 6-second reconnect time to bypass the initial JS challenge
        driver.uc_open_with_reconnect(url, reconnect_time=6)
        sleep(1)
        driver.set_window_size(1700, 1200)
        sleep(1)
        # Scroll down by a certain number of pixels
        driver.execute_script("window.scrollBy(0, 4100);")
        sleep(3)

        PC_games_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[3]/div/div/div/div[7]/section/div[1]/div[1]/a[2]")
        sleep(2)
        PC_games_button.click()
        sleep(1)
        PC_games_button.click()
        sleep(1)
        PC_games_button.click()
        sleep(1)
        PC_games_button.click()
        sleep(1)
        PC_games_button.click()
        search_bar = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[3]/div/div/div/div[7]/section/div[1]/div[2]/form/input")
        search_bar.click()
        sleep(1.5)
        search_bar.send_keys(f"{user_input}")
        search_bar.send_keys(Keys.ENTER)
        sleep(3)
        sleep(2)

        try:
            sleep(6)
            game_name = driver.find_elements(By.CLASS_NAME, value="gameDivLink")
            game_images = driver.find_elements(By.CLASS_NAME, value="c-image")

            game_info = []

            for x in range(83, 88):
                try:
                    game_data = game_name[x].text
                    game_info.append(game_data)
                except:
                    pass

            print(game_info)

            game_image_urls = []

            for x in range(87, 96, 2):
                try:
                    img_url = game_images[x].get_attribute('src')
                    game_image_urls.append(img_url)
                except:
                    pass

            print(game_image_urls)
            games_data = []

            for x in range(0, len(game_info)):
                url = game_image_urls[x]
                games_data.append(url)
                details = game_info[x]
                games_data.append(details)

            print(games_data)

            driver.close()

            return games_data

        except:
            no_game = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[3]/div/div/div/div[7]/section/div[2]/div[11]/p").text
            driver.close()

            if no_game:
                return no_game
