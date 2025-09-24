from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://the-internet.herokuapp.com/dynamic_controls"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)

wait = WebDriverWait(driver, 10)

enable_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='input-example']/button")))
enable_button.click()
sleep(5)

disable_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='input-example']/button")))
disable_button.click()
sleep(5)

remove_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='checkbox-example']/button")))
remove_button.click()
sleep(3)

add_Button = wait.until(EC.element_to_be_clickable((By.XPATH,"//form[@id='checkbox-example']/button")))
add_Button.click()
sleep(5)

checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='checkbox']")))
checkbox.click()
sleep(5)

driver.quit()









