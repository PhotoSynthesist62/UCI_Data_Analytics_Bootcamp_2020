## 10 - SQLAlchemy Challenge

### Climate Analysis and Exploration (Part 1)

Within a Jupyter Notebook, Conduct climate analysis and data exploration of the provided database (hawaii.sqlite) using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Choose a start and end date (approx. 3-15 days) for the proposed trip  analysis. 

* Connect to sqlite database with SQLAlchemy `create_engine`.

* Reflect tables into classes with SQLAlchemy `automap_base()`. Save references to those classes - Station and Measurement.

#### Precipitation Analysis
1. Design a query retrieving the last 12 months of precipitation data, selecting only `date` and `prcp` values.

2. Load query results into a Pandas DataFrame, setting the index to the Date column and sort values by Date.

3. Plot the results (using Matplotlib) as a bar chart. Print Summary Statistics (Pandas).

#### Station Analysis
1. Design queries calculating the total number of stations and the most active stations.
    * List station and observation counts (descending order).
    * Which station has the highest number of observations?
2. Design a query retrieving the last 12 months of temperature observation (`tobs`) data.
    * Filter by station with the highest number of observations
    * Plot results as a histogram (`bins=12`).

### Climate Application (Part 2)

Design a Flask API [app.py] to illustrate the queries from Part 1.

1. Create the following Routes:
    * `/` Home Page, listing all available routes
    * `/api/v1.0/precipitation` Returns a JSON representation of the Precipitation Analysis above, where `date` is the key and `prcp` the value. 
    * `/api/v1.0/stations` Returns a JSON list of stations from the dataset.
    * `/api/v1.0/tobs` Returns a JSON representation of temperature observations (`tobs`) for the previous year
    * `/api/v1.0/<start>` Returns a JSON list of the minimum temperature, ave temperature, and max temperature results for all dates greater than and/or equal to the start date.
    * `/api/v1.0/<start>/<end>` Returns a JSON list of the minimum temperature, ave temperature, and max temperature results for all dates between the start and end date, inclusively.