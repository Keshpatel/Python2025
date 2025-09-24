from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = "https://practice.expandtesting.com/drag-and-drop"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)
sleep(5)

source = driver.find_element(By.ID, "column-a")
destination = driver.find_element(By.ID,"column-b")

action = ActionChains(driver)
action.drag_and_drop(source, destination).perform()

    
assert driver.find_element(By.ID, "column-a").text == "B"
assert driver.find_element(By.ID, "column-b").text == "A"

driver.quit()
