from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

EMAIL ="inda4894@gmail.com"
PASSWORD = "pointer3"

chrome_driver_path = "D:\Games\PyCharm Community Edition 2021.3/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

sleep(1)
# enter_button = driver.find_element_by_partial_link_text("Войдите")
enter_button = driver.find_element_by_xpath("//*[@id='u131058078']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
enter_button.click()

sleep(2)
enter_google = driver.find_element_by_xpath("//*[@id='u-1597322998']/div/div/div[1]/div/div[3]/span/div/div/button")
enter_google.click()

# Получаем список вкладок для работы
base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
# Переключаемся на нужное окно
driver.switch_to.window(google_login_window)

google_login = driver.find_element_by_id("identifierId")
google_login.send_keys(EMAIL)
google_login.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
