# import libraries
from flask import Flask, render_template
import pymongo

# Create Flask Instance
app = Flask(__name__)

# Create Connection Var
conn = 'mongodb://localhost:27017'

# Pass connection to pymongo instance
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Set route
@app.route("/")
def echo():
    
        # Store the entire team collection in a list
    mars_news = list(db.latest_news.find())
    print(mars_news)

    # Return the template with the teams list passed in
    return render_template("index.html", mars_news=mars_news, text="This is a Test")

if __name__ == "__main__":
    app.run(debug=True)
