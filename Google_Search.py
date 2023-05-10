from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.google.com")

search_box = browser.find_element(By.CLASS_NAME, "gLFyf")
search_box.send_keys("Hello World")
search_box.submit()

browser.implicitly_wait(10)

search_result = browser.find_element(By.XPATH, "(//a/h3)[1]")
search_result.click()

input("")

# test
# test
# test
# test
# test
# test
# test
# test
# test
# test
# test
# test
# test
# test
