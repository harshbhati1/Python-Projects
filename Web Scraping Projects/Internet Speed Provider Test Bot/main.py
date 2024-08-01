from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
load_dotenv() 

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.chromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chromeOptions)
        self.PhoneNumber = os.getenv('PHONENUMBER')
        self.UP = 100
        self.DOWN = 200
        self.XUSERNAME = os.getenv('XUSERNAME')
        self.PASSWORD = os.getenv('PASSWORD')
        
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        # go button 
        goButton = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        goButton.click()
        time.sleep(40)
        
        # extracting details
        downloadSpeed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        uploadSpeed = self.driver.find_element(By.XPATH, value= '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        #print(f"The download speed is {downloadSpeed.text} and the upload speed is {uploadSpeed.text}")
        if (float(downloadSpeed.text) < self.DOWN or float(uploadSpeed.text) < self.UP):
            self.tweet_at_provider(downloadSpeed.text, uploadSpeed.text)
        self.driver.close()
        
        
    
    def tweet_at_provider(self, down, up):
        self.driver.get("https://x.com/home")
        time.sleep(4)

        #loging in 
        signIn = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
        signIn.click()
        time.sleep(1)

        # entering username and password 
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label')
        email.click()
        email.send_keys(self.XUSERNAME, Keys.ENTER)
        time.sleep(1)
        
        # #phone number 
        # phoneNumber = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label')
        # phoneNumber.send_keys('harshbhati10217@gmail.com', Keys.ENTER)
        # time.sleep(1)
        
        #password
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label')
        password.send_keys(self.PASSWORD, Keys.ENTER)

        time.sleep(3)
        
        # typing the message 
        bar = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        bar.click()
        bar.send_keys(f"Hey internet provider, why is my interent speed {down}down/{up}up when I pay for {self.DOWN}down/{self.UP}up?")
        time.sleep(10)
        self.driver.close()
                
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()