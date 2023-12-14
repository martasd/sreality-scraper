from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# TODO:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost/dbname"


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return "<Flat %r>" % self.title


@app.route("/")
def index():
    flats = Flat.query.all()
    return render_template("index.html", flats=flats)
