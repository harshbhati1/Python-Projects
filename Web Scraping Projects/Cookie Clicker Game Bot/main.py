from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time


# tuning the chrome browser
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

# setting the driver 
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# intro page 
time.sleep(5)
language = driver.find_element(By.ID, value="langSelect-EN")
language.click()
# now the game starts 
time.sleep(3)

#game variables
bigCookie = driver.find_element(By.ID, value="bigCookie")
score = driver.find_element(By.ID, value= "cookies")
# list = driver.find_elements(By.CSS_SELECTOR, "#products .product.unlocked.enabled")

# print(len(list))

# game 
while True:
    bigCookie.click()
    list = driver.find_elements(By.CLASS_NAME, value="product.unlocked.enabled")
    num = 0
    if len(list) > 1:
        num = random.randint(0,len(list)-1)
    elementScore = driver.find_element(By.XPATH, value= f'//*[@id="productPrice{num}"]') 
    if int(score.text.split(" ")[0]) > int(elementScore.text):
        element = driver.find_element(By.XPATH, value= f'//*[@id="product{num}"]')
        element.click()