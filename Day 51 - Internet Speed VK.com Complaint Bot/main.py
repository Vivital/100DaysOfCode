from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 25
CHROME_DRIVER_PATH = "D:\Games\PyCharm Community Edition 2021.3/chromedriver.exe"
PHONE_NUM = "89951157546"
PASSWORD = "qwerty1991"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        time.sleep(50)
        down = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(down)
        up = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        print(up)
        return [float(up), float(down)]

    def vk_at_provider(self):
        self.driver.get("https://vk.com/")

        time.sleep(2)
        email = self.driver.find_element_by_xpath("//*[@id='index_email']")
        email.send_keys(PHONE_NUM)
        password = self.driver.find_element_by_xpath("//*[@id='index_pass']")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        post_news = self.driver.find_element_by_xpath("//*[@id='post_field']")
        post_news.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")

        publish_button = self.driver.find_element_by_xpath("//*[@id='send_post']/span/span")
        publish_button.click()

        time.sleep(2)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speed = bot.get_internet_speed()

if speed[0] < PROMISED_UP or speed[1] < PROMISED_DOWN:
    bot.vk_at_provider()
