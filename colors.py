import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(options=webdriver.ChromeOptions())
driver.get(r"https://www.arealme.com/colors/ru/")
driver.refresh()
driver.find_element(By.XPATH, "//button[@id='start']").click()

indexes = []
time.sleep(2)
try:
    while True:
        element = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/span[1]")
        (driver.find_element(By.XPATH,
                             f"/html/body/div[4]/div[1]/div[2]/div/span[@style!='{element.get_attribute('style')}']")
         .click())
        try:
            element.click()
        except Exception as e:
            pass

except Exception as e:
    time.sleep(20)

