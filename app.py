from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost/sreality_dev"
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


@app.route("/")
def index():
    flats = Flat.query.all()
    return render_template("index.html", flats=flats)


if __name__ == "__main__":
    app.run()
