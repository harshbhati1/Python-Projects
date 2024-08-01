from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
load_dotenv()
import os
import time

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
LINK = os.getenv('LINK')
# setting the driver 

class InstaFollower:
    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.chromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chromeOptions)
    
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        # loging in 
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.click()
        email.send_keys(USERNAME, Keys.ENTER)

        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.click()
        password.send_keys(PASSWORD, Keys.ENTER)

        time.sleep(5)
        notNow = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notNow.click()
        time.sleep(2)
    
    def findFollowersAndFollow(self, username):
        link = f'https://www.instagram.com/{username}/'
        self.driver.get(link)
        time.sleep(2)
        
        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers_link.click()
        time.sleep(2)
        
        list = self.driver.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3 button')
        for item in list:
            try:
                item.click()
                time.sleep(1)
            except:
                try:
                    cancel = self.driver.find_element(By.CSS_SELECTOR, value='._a9--._ap36._a9_1')
                    cancel.click()
                    print("cancelled")
                except:
                    ok = self.driver.find_element(By.CSS_SELECTOR, value='._a9--._ap36._a9_1')
                    ok.click()
                    print("Ok")
    
                    
       

bot = InstaFollower()
bot.login()
bot.findFollowersAndFollow('narendramodi')


        
        