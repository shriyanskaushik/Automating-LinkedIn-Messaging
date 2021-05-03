from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "Path to your webdriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/")
time.sleep(2)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("Your email ID")
password.send_keys("Your linkedin Password")
time.sleep(2)
submit = driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(2)

driver.get("Link to your webpage of connections")
time.sleep(4)

all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
driver.execute_script("arguments[0].click();", message_buttons[0])
time.sleep(2)

main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
driver.execute_script("arguments[0].click();", main_div)

time.sleep(2)
paragraphs = driver.find_elements_by_tag_name("p")

paragraphs[-5].send_keys("testing")
