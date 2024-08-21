from flask import Flask
import random


num = random.randint(0,9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    html =   '''
    <center><h1>Guess a number from 0 to 9</h1></center>
    <center><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzZmMGd4ZGxhZm9jbDU5MGxiYXRkOWg1emlubTNtZnE3OGY5cmZteCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Fo1cy8mqGDvbjpJBB7/giphy.webp" alt="Guessing Game GIF"></center>
     '''
    return html

@app.route("/<int:number>")
def storer(number):
    if number == num:
        html = '''
        <center><h1>You found me!</h1></center>
        <center><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHlhd2JrdjBpZnpqbDg5b2tsamd6NXE0bWVyYTAwOGowYXV5NTN0ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/v65rDtklV9l6g/giphy.webp" alt="Guessing Game GIF"></center>
        '''
        return html
    elif number > num:
        html = '''
        <center><h1>Too high, try again!</h1></center>
        <center><img src="https://media2.giphy.com/media/PCvkgunX9ZbEEyfTQH/giphy.webp?cid=82a1493b7fzhqymlc9p8qxntme3xa82egcb987laliga2jnf&ep=v1_gifs_trending&rid=giphy.webp&ct=g" alt="Guessing Game GIF"></center>
        '''
        return html
    else:
        html = '''
        <center><h1>Too low, try again!</h1></center>
        <center><img src="https://media1.giphy.com/media/pynZagVcYxVUk/giphy.webp?cid=82a1493b3rcpl0s814y213fnmrimjt50cyb473t698hw2n6t&ep=v1_gifs_trending&rid=giphy.webp&ct=g" alt="Guessing Game GIF"></center>
        '''
        return html
        
        

if __name__ == "__main__":
    app.run(debug=True)
    