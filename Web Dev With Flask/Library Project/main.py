from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



#creating a db object
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/harsh/OneDrive/Desktop/Python/Working With Flask/Projects/Library Project/new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable= False)
    author: Mapped[str] = mapped_column(nullable= False)
    rating:Mapped[float] = mapped_column(nullable= False)
    
with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
     with app.app_context():
    # Query the database to get all books ordered by title
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(all_books)
        return render_template("index.html", data = all_books)


@app.route("/add", methods = ["GET", "POST"])
def add():
    
    if request.method == "POST":
        formData = request.form
        with app.app_context():
            newBook = Book(id = 1, title =  formData.get("title"), author = formData.get("author"), rating = formData.get("rating"))
        db.session.add(newBook)
        db.session.commit()
        print("Added successfully")
        return redirect(url_for('home'))
    
    return render_template("add.html")

@app.route('/edit/<int:number>', methods=['GET', 'POST'])
def edit(number):
    if request.method == 'GET':
        with app.app_context():
            # Retrieve the book based on its ID
            book = db.session.execute(db.select(Book).where(Book.id == number)).scalar()
            if book:
                # Render the update template with the book's current details
                return render_template('update.html', data=book)
            else:
                # Handle the case where the book is not found
                return "Book not found", 404
    else:
        # Handle form submission to update book details
        rating = float(request.form.get('rating'))
        
        # Retrieve the book based on its ID
        book = db.session.get(Book, number)
        if book:
            # Update book details
            book.rating = rating
            db.session.commit()
            return redirect(url_for('home'))
        else:
            # Handle the case where the book is not found
            return "Book not found", 404

@app.route('/delete/<int:number>')
def delete(number):
    book_id = number
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

