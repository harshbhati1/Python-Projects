from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
USERGMAIL = os.getenv("MYGMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTPADDRESS = os.getenv("SMTPADDRESS")

# Set up SMTP connection
CONNECTION = smtplib.SMTP(SMTPADDRESS, 587)
CONNECTION.starttls()
CONNECTION.login(USERGMAIL, PASSWORD)

# Amazon WebScraping setup
header = {
    "sec-ch-ua-platform": "Windows",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}
TARGETPRICE = 100.00
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Fetch the page and parse the price
response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.select("#centerCol .aok-offscreen")[0].get_text().split("$")[1]

# Send email if the price is below the target
if float(price) < TARGETPRICE:
    message = f"Subject: Your item is available at a cheaper price\n\nThe item you were looking at is now available for ${price}."
    CONNECTION.sendmail(from_addr=USERGMAIL, to_addrs="harshbhati10216@gmail.com", msg=message)
