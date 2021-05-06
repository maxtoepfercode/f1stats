from flask import Flask, render_template, request
import psycopg2
from os import environ

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

conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT \"POS\" FROM f1stage.f1data")
position = cursor.fetchall()
currentpos = [""]

for i in year:
    currentpos.append(i[0])



# LOGIC

# SELECT "POS", "Drivers", "NO", "CAR", "SESSION", "TIME", "LAPS", "TRACK"
# FROM f1stage.f1data WHERE "Drivers" = 'Sebastian Vettel                                  ' AND "TRACK" = 'RUS'|'2020' AND "SESSION" = 'FP'
	   



app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

@app.route('/')
def index():
    return render_template('index.html', page_title="f1stats")

@app.route('/comparison.html')
def comparison():
    return render_template('comparison.html', page_title="f1stats", drivers = actualdrivers, session = currentsession, tracks = currenttracks, year = currentyear, position = currentpos)

@app.route('/driverdata', methods = ["POST"])
def driverdata():
    driver1 = request.form.get('driver1')
    driver2 = request.form.get('driver2')
    track = request.form.get('track_type')
    year = request.form.get('year')
    year[3:]
    session = request.form.get('session')
    position = currentpos
    


    return render_template('results.html', driver1 = driver1, driver2 = driver2, track = track, year = year, session = session)
 
 
 
 
 #   conn = psycopg2.connect(host="35.242.233.91", database="f1data", user="postgres", password=environ.get('DB_PASSWORD'))
 #  cursor = conn.cursor()
 #   cursor.execute("SELECT" "POS", "Drivers", "NO", "CAR", "SESSION", "TIME", "LAPS", "TRACK"
 #   FROM f1stage.f1data WHERE "Drivers" = 'Sebastian Vettel                                  ' AND "TRACK" = 'RUS'|'2020' AND "SESSION" = 'FP'")
 #   year = cursor.fetchall()
 #   currentyear = [""]





 #   return (drivers = actualdrivers, session = currentsession, tracks = currenttracks, year = currentyear)





if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)




# SELECT "POS", "Drivers", "NO", "CAR", "SESSION", "TIME", "LAPS", "TRACK"
# FROM f1stage.f1data WHERE "Drivers" = 'Sebastian Vettel                                  ' AND "TRACK" = 'RUS'|'2020' AND "SESSION" = 'FP'
	   