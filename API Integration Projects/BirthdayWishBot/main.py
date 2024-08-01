# Importing necessary libraries
import pandas as pd  # For handling data in dataframes
import random  # For generating random numbers
import datetime as dt  # For working with dates and times
import smtplib  # For sending emails
import os  # For interacting with the operating system
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Loading environment variables from a .env file
load_dotenv()

# Setting up the SMTP connection for sending emails
myGmail = os.getenv('myGmail')  # Retrieving the Gmail address from environment variables
password = os.getenv('password')  # Retrieving the email password from environment variables
connection = smtplib.SMTP("smtp.gmail.com", 587)  # Connecting to the Gmail SMTP server
connection.starttls()  # Starting TLS encryption for the connection
connection.login(user=myGmail, password=password)  # Logging in to the email account

# Getting today's date and month
date = dt.datetime.now()  # Getting the current date and time
day = date.day  # Extracting the day from the current date
month = date.month  # Extracting the month from the current date

# Loading birthday data from a CSV file
data = pd.read_csv('API Integration Projects/BirthdayWishBot/birthdays.csv')  # Reading the CSV file into a DataFrame
matching_rows = data[(data['month'] == month) & (data['day'] == day)]  # Filtering the DataFrame for today's birthdays

# For each person whose birthday is today, send a birthday email
for index, row in matching_rows.iterrows():
    # Randomly select a letter template for the birthday message
    message = ""  # Initializing an empty message string
    letter_number = random.randint(1, 3)  # Choosing a random letter template number between 1 and 3
    with open(file=f'API Integration Projects/BirthdayWishBot/letter_templates/letter_{letter_number}.txt', mode='r') as file:
        answer = file.read()  # Reading the selected letter template
        answer = answer.replace("[NAME]", row['name'])  # Replacing [NAME] placeholder with the recipient's name
        
        # Sending the birthday email to the recipient
        sendingTo = row['email']  # Getting the recipient's email address
        connection.sendmail(from_addr=myGmail, to_addrs=sendingTo, msg=f"Subject: Happy Birthday {row['name']} \n\n {answer}")

# Closing the SMTP connection
connection.close()
