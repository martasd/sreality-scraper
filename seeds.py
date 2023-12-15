import requests

from requests import JSONDecodeError
from app import app, db, Flat

url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"
res = requests.get(url)
with app.app_context():
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
