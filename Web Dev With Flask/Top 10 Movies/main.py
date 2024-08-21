from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv
load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


#IMDB setup:
API_TOKEN = os.getenv('API_TOKEN')
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

#creating a form for update
class updateForm(FlaskForm):
    rating = FloatField(label='Your Rating out of 10', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Submit", render_kw={"class": "btn btn-primary btn-lg"})

class addForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Submit", render_kw={"class": "btn btn-primary btn-lg"})

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/harsh/OneDrive/Desktop/Python/Working With Flask/Projects/Top 10 Movies/movies.db"


db.init_app(app)

# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable= False)
    year: Mapped[int] = mapped_column(nullable= False)
    description: Mapped[str] = mapped_column(nullable= False)
    rating:Mapped[float] = mapped_column(nullable= False)
    ranking: Mapped[int] = mapped_column(nullable= False)
    review: Mapped[str] = mapped_column(nullable= False)
    img_url: Mapped[str] = mapped_column(nullable= False)
    
with app.app_context():
    db.create_all()
    


# with app.app_context():
#         second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#         db.session.add(second_movie)
#         db.session.commit()

@app.route("/")
def home():
      with app.app_context():
        # Query the database to get all movies ordered by rating
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = result.scalars().all()
        
        for i in range(len(all_movies)):
            all_movies[i].ranking = len(all_movies) - i
            db.session.commit()
            
        return render_template("index.html", data = all_movies)


@app.route("/edit/<int:number>", methods = ['GET','POST'])
def edit(number):
    form = updateForm()
    movie_id = number
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    
    if form.validate_on_submit():
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    else:
        return render_template('edit.html', form = form, movie = movie_to_update)
@app.route('/delete/<int:number>')
def delete(number):
    movieId = number
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movieId)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
              
@app.route('/add', methods = ['GET','POST'])
def add():
    form = addForm()
    if request.method == 'GET':
        return render_template('add.html', form = form)
    else:
        name = form.title.data
        parameters = {
            'query': name,
        }
        endpoint = 'https://api.themoviedb.org/3/search/movie'
        response = requests.get(endpoint, params= parameters,headers=headers)
        data = response.json()['results']
        return render_template('select.html', data = data)
@app.route('/selected/<int:number>')
def selected(number):
    id = number
    parameters = {
        "movie_id" : id,
    }   
    endpoint = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(endpoint, params= parameters,headers=headers)
    data = response.json()
    # now adding the data to the database
    title = data["original_title"]
    year = data["release_date"]
    description = data["overview"]
    img_url = f"https://image.tmdb.org/t/p/original{data['poster_path']}"
    with app.app_context():
        newMovie = Movie(
        id = id,
        title= title,
        year=year,
        description=description,
        rating=0.0,
        ranking=0,
        review="",
        img_url=img_url
        )
        db.session.add(newMovie)
        db.session.commit()
        return redirect(url_for('edit', number=id))
    
if __name__ == '__main__':
    app.run(debug=True)
