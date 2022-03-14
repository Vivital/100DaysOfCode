from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Games\PyCharm Community Edition 2021.3/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

search_name = driver.find_element_by_name("fName")
search_name.send_keys("Dima")
search_surname = driver.find_element_by_name("lName")
search_surname.send_keys("Ivanov")
search_email = driver.find_element_by_name("email")
search_email.send_keys("dima@mail.com")

button = driver.find_element_by_class_name("btn-primary")
button.send_keys(Keys.ENTER)

