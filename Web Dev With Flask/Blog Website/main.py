from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# adding the data to the file
response = requests.get('https://api.npoint.io/77c5921fad0691be3b31')
data = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data = data)

@app.route('/contact', methods=["POST", "GET"])
def helper():
    if request.method == 'POST':
        formData = request.form
        sendData(formData)
        return render_template("contact.html", isSent = True)
    else:
        return render_template("contact.html", isSent = False)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:number>')
def post(number):
    return render_template("post.html",data = data[number])

@app.route('/form-entry', methods=["POST", "GET"])


def sendData(data):
     myGmail = os.getenv('myGmail')
     password = os.getenv('password')
      # Set up the SMTP connection
     connection = smtplib.SMTP("smtp.gmail.com", 587)
     connection.starttls()
     connection.login(user=myGmail, password=password)
     connection.sendmail(
        from_addr=myGmail,
        to_addrs=os.getenv('to_addrs'),
        msg=f"Subject: Contact Form Query \n\n Name:{data['name']} \n Email Address: {data['email']} \n Phone Number: {data['phone']} \n Message: {data['message']}"
    )
    

if __name__ == "__main__":
    app.run(debug=True)