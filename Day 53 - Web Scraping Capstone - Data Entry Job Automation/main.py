from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from time import sleep
from selenium.webdriver.chrome.options import Options

GOOGLE_FORM_URL = "https://forms.gle/MgdVAJgS8E4nqWtBA"
CHROME_DRIVER_PATH = "D:\Games\PyCharm Community Edition 2021.3\chromedriver.exe"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6"
}

response = requests.get(ZILLOW_URL, headers=header)
zillow_html = response.text

soup = BeautifulSoup(zillow_html, "html.parser")
all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]

    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_price_elements = soup.select(".list-card-price")
all_prices = [price.text.split("+")[0].split("/")[0] for price in all_price_elements if "$" in price.text]

all_address_element = soup.select(".list-card-addr")
all_addresses = [address.text.split(" | ")[-1] for address in all_address_element]


chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chr_options)
driver.get(GOOGLE_FORM_URL)

for n in range(len(all_links)):
    input_address = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_price = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_link = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    input_address.send_keys(all_addresses[n])
    input_price.send_keys(all_prices[n])
    input_link.send_keys(all_links[n])
    submit_button.click()
    sleep(1)

    next_answer = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    next_answer.click()
    sleep(1)

