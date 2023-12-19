import requests

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ
from requests import JSONDecodeError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Flat(db.Model):
    __tablename__ = "flats"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "<Flat %r>" % self.title


@app.cli.command("seed_db")
def seed_db():
    url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"
    res = requests.get(url)
    try:
        res_json = res.json()

        for estate in res_json["_embedded"]["estates"]:
            flat = Flat(
                title=estate["name"],
                location=estate["locality"],
                image_url=estate["_links"]["images"][0]["href"],
            )

            db.session.add(flat)
            db.session.commit()
    except JSONDecodeError:
        print("The response is not a valid JSON.")


@app.route("/")
def index():
    flats = Flat.query.all()
    return render_template("index.html", flats=flats)


if __name__ == "__main__":
    app.run(port=8080)
