import os
from flask import Flask, render_template, request
import psycopg2
import sqlalchemy 
from os import environ
app = Flask(__name__)
if os.environ.get('DATABASE_URL'):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)  

conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT \"Drivers\" FROM f1stage.f1data ORDER BY 1")
drivers = cursor.fetchall()
actualdrivers = ["Driver"]

for i in drivers:
    actualdrivers.append(i[0])

conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT LEFT(\"TRACK\", 3) FROM f1stage.f1data ORDER BY 1")
tracks = cursor.fetchall()
currenttracks = ["Track"]

for i in tracks:
    currenttracks.append(i[0])

conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT \"SESSION\" FROM f1stage.f1data ORDER BY 1")
session = cursor.fetchall()
currentsession = ["Session"]

for i in session:
    currentsession.append(i[0])


conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT RIGHT(\"TRACK\", 4) FROM f1stage.f1data ORDER BY 1")
year = cursor.fetchall()
currentyear = ["Year"]

for i in year:
    currentyear.append(i[0])



	   



app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

@app.route('/')
def index():
    return render_template('index.html', page_title="f1stats")

@app.route('/comparison.html')
def comparison():
    return render_template('comparison.html', page_title="f1stats", drivers = actualdrivers, session = currentsession, tracks = currenttracks, year = currentyear)

@app.route('/driverdata', methods = ["POST"])
def driverdata():
    driver1 = request.form.get('driver1')
    driver2 = request.form.get('driver2')
    track = request.form.get('track_type')
    year = request.form.get('year')
    year[3:]
    session = request.form.get('session')
    
    #conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
    #cursor = conn.cursor()
    #print("SELECT f1data.\"TRACK\", f1data.\"TIME\",f1data.\"LAPS\", f1data.\"POS\" FROM f1stage.f1data WHERE f1data.\"Drivers\" = '"+ driver1+"' AND f1data.\"TRACK\" = '"+track+year+"' AND f1data.\"SESSION\" = '"+session+"')
    #print("SELECT f1data.\"TRACK\", f1data.\"TIME\",f1data.\"LAPS\", f1data.\"POS\" FROM f1stage.f1data WHERE f1data.\"Drivers\" = '"+ driver2+"' AND f1data.\"TRACK\" = '"+track+year+"' AND f1data.\"SESSION\" = '"+session+"')
    #cursor.execute("SELECT  f1data.\"TIME\" FROM f1stage.f1data WHERE f1data.\"Drivers\" = '"||driver1||"' AND f1data.\"TRACK\" = ('"||track||year||"') AND f1data.\"SESSION\" = '"||session||"')
    #data = cursor.fetchall()
    #data = [""]

    for i in data:

        currentdata.append(i[0])
    


    return render_template('results.html', driver1 = driver1, driver2 = driver2, track = track, year = year, session = session)




if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)




 