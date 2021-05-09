import os
from flask import Flask, render_template, request
import psycopg2
from datetime import datetime
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Database access via psycopg2

# Accessing the data for the selection menues

app = Flask(__name__)
conn = psycopg2.connect(host=os.environ.get("HOST"), database=os.environ.get("DATABASE"), user=os.environ.get("USER"), password=os.environ.get("PASSWORD"))
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT \"Drivers\" FROM f1data ORDER BY 1")
drivers = cursor.fetchall()
actualdrivers = ["Driver"]

for i in drivers:
    actualdrivers.append(i[0])

cursor.execute("SELECT DISTINCT LEFT(\"TRACK\", 3) FROM f1data ORDER BY 1")
tracks = cursor.fetchall()
currenttracks = ["Track"]

for i in tracks:
    currenttracks.append(i[0])

cursor = conn.cursor()
cursor.execute("SELECT DISTINCT \"SESSION\" FROM f1data ORDER BY 1")
session = cursor.fetchall()
currentsession = ["Session"]

for i in session:
    currentsession.append(i[0])

cursor = conn.cursor()
cursor.execute("SELECT DISTINCT RIGHT(\"TRACK\", 4) FROM f1data ORDER BY 1")
year = cursor.fetchall()
currentyear = ["Year"]

for i in year:
    currentyear.append(i[0])

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

# Route section

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

    # Function that cuts right name part in order to bypass a query request error
    def right(s, amount):
        return s[-amount:]

    driverreplace = driver1.replace(" ", "")
    driverreplace2 = driver2.replace(" ", "")

    drivershort=right(driverreplace,5)
    drivershort2=right(driverreplace2,5)

    # SQL-Statements for the request of the output
  
    SQL1="SELECT f1data.\"TRACK\", f1data.\"TIME\",f1data.\"LAPS\", f1data.\"POS\" FROM f1data WHERE RIGHT(REPLACE(f1data.\"Drivers\", ' ',''),5) = '"+drivershort+"' AND f1data.\"TRACK\" = '"+track+year+"' AND f1data.\"SESSION\" = '"+session+"'"
    SQL2="SELECT f1data.\"TRACK\", f1data.\"TIME\",f1data.\"LAPS\", f1data.\"POS\" FROM f1data WHERE RIGHT(REPLACE(f1data.\"Drivers\", ' ',''),5) = '"+drivershort2+"' AND f1data.\"TRACK\" = '"+track+year+"' AND f1data.\"SESSION\" = '"+session+"'"
    
    # Connecting to the DB to get the data

    conn = psycopg2.connect(host=os.environ.get("HOST"), database=os.environ.get("DATABASE"), user=os.environ.get("USER"), password=os.environ.get("PASSWORD"))
    cursor = conn.cursor()
    cursor.execute(SQL1)
    dbdata1= cursor.fetchall()
    if len(dbdata1) == 0:
        return ("Your driver/-s have not attended on this Race weekend. Try choosing a different one!")

    outTrack1 =  (dbdata1[0][0])
    outTime1 =  (dbdata1[0][1])
    outLaps1 =  (dbdata1[0][2])
    outPos1 =  (dbdata1[0][3])
    
    cursor = conn.cursor()
    cursor.execute(SQL2)
    dbdata2 = cursor.fetchall()
    if len(dbdata2) == 0:
        return ("Your driver/-s have not attended on this Race weekend. Try choosing a different one!")

    outTrack2 =  (dbdata2[0][0])
    outTime2 =  (dbdata2[0][1])
    outLaps2 =  (dbdata2[0][2])
    outPos2 =  (dbdata2[0][3])

    return render_template('results.html', driver1 = driver1, driver2 = driver2, track = track, year = year, session = session, dbdata1 = dbdata1, dbdata2 = dbdata2, outTrack1 = outTrack1, outTime1 = outTime1, outLaps1 = outLaps1, outPos1 = outPos1, outTrack2 = outTrack2, outTime2 = outTime2, outLaps2 = outLaps2, outPos2 = outPos2)


if __name__ == "__main__":
    port=os.environ.get("PORT")
    app.run(host="localhost", port=port, debug=True)




 