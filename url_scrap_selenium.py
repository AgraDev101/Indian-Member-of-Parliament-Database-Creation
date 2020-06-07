from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import io
import time

driver = webdriver.Firefox()
driver.get("https://www.india.gov.in/my-government/indian-parliament/lok-sabha")

data = []

while True:
	time.sleep(5)
	soup = BeautifulSoup(driver.page_source, 'html.parser') 

	for info in soup.findAll("div", {"class": "views-field views-field-title"}):
		name = info.find("a")['href']
		name = "https://www.india.gov.in" + name
		print(name)
		data.append(name)

	try:
		driver.find_element_by_link_text('next ›').click()
	except NoSuchElementException:
		break

	time.sleep(5)


print(len(data))

with open("url_output.py", "w+") as f:
	f.seek(0)
	f.write("urls = " + str(data))