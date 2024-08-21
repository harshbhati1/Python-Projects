from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/harsh/OneDrive/Desktop/Python/Working With Flask/Projects/Cafe API/instance/cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods = ['GET'])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    modifiedObj = random_cafe.to_dict()
    return jsonify({'cafe': modifiedObj})

@app.route("/all", methods = ['GET'])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    storage = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes = storage)

@app.route("/search")
def find_cafe():
    query_location = request.args.get("loc")
    with app.app_context():
        cafe = db.session.execute(db.select(Cafe).where(Cafe.location ==  str(query_location))).scalar()
        if cafe == None:
            cafe = {
                "Not found": "sorry we do not have that location"
            } 
            return jsonify(error = cafe)
    return jsonify(cafes = cafe.to_dict())

# helper functions 
def convertToDict(cafe):
    storage = {
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price
    }
    return storage

@app.route("/add", methods=["GET","POST"])
def add_cafe():
    new_cafe=Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=True if request.form.get("has_scoket") == "True" else False,
        has_toilet=True if request.form.get("has_toilet") == "True" else False,
        has_wifi=True if request.form.get("has_wifi") == "True" else False,
        can_take_calls=True if request.form.get("can_take_calls") == "True" else False,
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),

    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe. "})

@app.route('/update-price/<cafe_id>',  methods=["PATCH"])
def updateCoffePrice(cafe_id):
    try:
        newPrice = request.args.get('new_price')
        with app.app_context():
            cafe= db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            cafe.coffee_price = newPrice
            db.session.commit()
            cafe = {"success": "Successfully updated the price"}
            return jsonify(cafe)
              
    except:
        cafe = {"Not found": "Sorry a cafe with this id doesn't exist"}
        return jsonify(error = cafe)
        
@app.route('/report-closed/<cafe_id>', methods = ['DELETE'])
def delete(cafe_id):
    try:
        api_key = request.args.get('api_key')
        if api_key == "TopSecretAPIKey":
            with app.app_context():
                cafe= db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
                db.session.delete(cafe)
                db.session.commit()
                db.session.commit()
                cafe = {"success": "Successfully deleted the cafe"}
                return jsonify(cafe)
              
    except:
        cafe = {"Not found": "Sorry a cafe with this id doesn't exist"}
        return jsonify(error = cafe)


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
