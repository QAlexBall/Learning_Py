from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/home/alex/Downloads/SoftWare/chromedriver/chromedriver")
# driver = webdriver.Chrome()
driver.get('https://python.org')
