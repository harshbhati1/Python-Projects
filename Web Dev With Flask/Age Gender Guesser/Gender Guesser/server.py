from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/<name>') #accessing the name
def program(name):
    # calling Api
    agifyApi = requests.get(f"https://api.agify.io?name={name}")
    genderizeApi = requests.get(f"https://api.genderize.io?name={name}")
    
    #storing the data
    age = agifyApi.json()['age']
    gender = genderizeApi.json()['gender']

    return render_template("index.html", age = age, gender = gender, name = name)

if __name__ == "__main__":
    app.run(debug=True)