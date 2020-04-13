import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Saheed Obitayo's SQLAlchemy Project Home Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"       
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/<start><br/>"
        f"/api/v1.0/temp/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session 
    session = Session(engine)

    """Return dates and precipitation"""
    # Query all dates and precipitation
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary and append to a list of all_passengers
    precipitation = []
    for date, prcp in results:
        row = {}
        row["date"] = date
        row["prcp"] = prcp
        precipitation.append(row)

    return jsonify(precipitation)

######################################################################

@app.route("/api/v1.0/stations")
def stations():
    # Create our session 
    session = Session(engine)

    """Return list of stations"""
    # Query all station
    results = session.query(Station.station, Station.name).all()

    session.close()

    #  # Convert list of tuples into normal list
    all_stations = [item for t in results for item in t]
    return jsonify(all_stations)

#######################################################################

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session 
    session = Session(engine)

    """Return a list of temperatures for the last year"""
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query all dates and prcp measurements
    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > query_date).all()

    session.close()
    # Create a list of dicts with `date` and `tobs` as the keys and values
    temperature = []
    for date, tobs in results:
        row = {}
        row["date"] = date
        row["tobs"] = tobs
        temperature.append(row)
    return jsonify(temperature)

##########################################################################

@app.route("/api/v1.0/temp/<start>")
def start_1(start):
    # Create our session 
    session = Session(engine)
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""
     # Take date and convert to yyyy-mm-dd 
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    trip_data_1 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    trip_1 = list(np.ravel(trip_data_1))
    return jsonify(trip_1)

############################################################
@app.route("/api/v1.0/temp/<start>/<end>")
def start_2(start, end):
    # Create our session 
    session = Session(engine)
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start and end dates."""
    # Get start and end dates and convert to yyyy-mm-dd format for the query
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    trip_data_2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    trip_2 = list(np.ravel(trip_data_2))
    return jsonify(trip_2)

##################################################################

    
if __name__ == "__main__":
    app.run(debug=True)