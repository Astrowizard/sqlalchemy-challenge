import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import functions

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = (__name__)

@app.route("/")
def welcome():
    def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation:
    session = Session(engine)
    q = session.query(Measurement.date).order_by(Measurement.date.desc())\
        .first()
    session.close()
    last_day = q[0]
    last_day = dt.datetime.strptime(last_day, '%Y-%m-%d')
    one_year = last_day - dt.timedelta(days=365)
    session = Session(engine)
    q1 = session.query(Measurement.prcp,Measurement.date).\
       filter(Measurement.date >= one_year.date().strftime('%Y-%m-%d')) 
    session.close()

    precipitation = {}
    for prcp, date in q1:
        precipitation.append({date:prcp})

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations:
    session = Session(engine)
    q = session.query(Station.name)
    session.close()

    stations = list(np.unravel(q))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs:
    session = Session(engine)
    q = session.query(Measurement.date).order_by(Measurement.date.desc())\
        .first()
    session.close()
    last_day = q[0]
    last_day = dt.datetime.strptime(last_day, '%Y-%m-%d')
    one_year = last_day - dt.timedelta(days=365)
    session = Session(engine)
    q1 = session.query(Measurement.prcp,Measurement.date).\
       filter(Measurement.date >= one_year.date().strftime('%Y-%m-%d')) 
    session.close()

    precipitation = {}
    for prcp, date in q1:
        precipitation.append({date:prcp})

    return jsonify(precipitation)

@app.route("/api/v1.0/<start>")
def start:
    def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    q = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date)
    session.close()

    for i in q:
        print(f"Minimum temperature: {i[0]}")
        print(f"Maximum temperature: {i[2]}")
        print(f"Average temperature: {i[1]}")

@app.route("/api/v1.0/<start>/<end>")
def startend:
    def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    q = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()

    for i in q:
        print(f"Minimum temperature: {i[0]}")
        print(f"Maximum temperature: {i[2]}")
        print(f"Average temperature: {i[1]}")


if __name__ = "__main__":
    app.run(debug=true)