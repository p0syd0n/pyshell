from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com')