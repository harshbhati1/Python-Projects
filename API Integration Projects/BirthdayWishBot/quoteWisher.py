import smtplib
import datetime as dt
import random

#loading quotes
with open(file="Projects/Birthday Wisher/quotes.txt", mode='r') as file:
    quotes = file.readlines()

# choosing random quote
quote = random.choice(quotes)

# checking the day of the week
today = dt.datetime.now().weekday()

if today == 3:
    my_gmail = "harshbhati10217@gmail.com"
    password = "lsdt wsmk pqes fovp"
    
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_gmail, password=password)
    connection.sendmail(from_addr=my_gmail, to_addrs="harshbhati10216@gmail.com", msg=f"Subject:Motivational Quote \n\n {quote}")
    connection.close()