from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fetch and parse the webpage
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")
items = soup.select("ul li.ListItem-c11n-8-84-3-StyledListCardWrapper")

# Initialize lists to store data
prices = []
addresses = []
links = []

# Extract data
for item in items:
    price_element = item.select_one(".PropertyCardWrapper span")
    address_element = item.select_one(".StyledPropertyCardDataWrapper address")
    link_element = item.select_one(".StyledPropertyCardDataWrapper a")
    
    # Process price
    price = price_element.text.split("$")[1]
    if "+" in price:
        price = price.split("+")[0]
    if "/" in price:
        price = price.split("/")[0]
    price = int(price.replace(',', ''))
    
    # Extract data and append to lists
    prices.append(price)
    addresses.append(address_element.text.strip())
    links.append(link_element.get("href"))

# Print the number of entries
print(len(prices))

# Fill out the form using Selenium
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

for i in range(len(prices)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScwEdAVL0K8h8n94wUON4dLhq10wVgGCaS35V-vGOFZKu2Y6A/viewform?usp=sf_link")
    time.sleep(1)

    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    time.sleep(1)
    address_field.send_keys(addresses[i])
    price_field.send_keys(f"{prices[i]}")
    link_field.send_keys(links[i])
    submit_button.click()
    time.sleep(1)  # Optional: Add a delay to avoid rapid form submissions
