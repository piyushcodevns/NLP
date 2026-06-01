from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://finance.yahoo.com/quote/RELIANCE.NS/history/")
page_source = driver.page_source
driver.quit()
print(page_source)