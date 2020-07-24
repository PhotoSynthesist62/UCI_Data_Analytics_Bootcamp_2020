# import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask Instance
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/martian_scrape")

@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    if mars_data == None:
        mars_data = scrape_mars.scrape_all()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_all()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
