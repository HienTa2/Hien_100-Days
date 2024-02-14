from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Convert a Cafe object into a dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read random Record
@app.route("/random")
def get_random_cafe():
    random_cafe = Cafe.query.order_by(func.random()).first()
    if random_cafe:
        return jsonify(cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price
        })
    else:
        return jsonify(error="No cafes available"), 404


# HTTP GET - Read all Record

@app.route("/all")
def get_all_cafes():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    # usage http://127.0.0.1:5000/all?page=1&per_page=30
    cafes_page = Cafe.query.order_by(Cafe.name).paginate(page=page, per_page=per_page, error_out=False)
    cafes = [cafe.to_dict() for cafe in cafes_page.items]
    return jsonify(cafes=cafes)


# HTTP GET - search a record

# search usage http://127.0.0.1:5000/search?loc=Peckham
@app.route("/search")
def get_search_cafes():
    location_query = request.args.get('loc', type=str)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if location_query:
        cafes_search = Cafe.query.filter(Cafe.location.contains(location_query)).order_by(Cafe.location).paginate(
            page=page, per_page=per_page, error_out=False)
        if cafes_search.items:
            cafes = [cafe.to_dict() for cafe in cafes_search.items]
            return jsonify(cafes=cafes)
        else:
            # Return a structured error message
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    else:
        # Return all cafes if no specific location is queried
        cafes_search = Cafe.query.order_by(Cafe.location).paginate(page=page, per_page=per_page, error_out=False)
        cafes = [cafe.to_dict() for cafe in cafes_search.items]
        return jsonify(cafes=cafes)


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        id=request.form.get("id"),
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
