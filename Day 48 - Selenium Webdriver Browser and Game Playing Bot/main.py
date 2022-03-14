from selenium import webdriver

chrome_driver_path = "D:\Games\PyCharm Community Edition 2021.3/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_class_name("price-block__final-price")
# print(price.text)

# link = driver.find_elements_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[2]/a/span')
# print(link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget .menu a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)


driver.quit()
