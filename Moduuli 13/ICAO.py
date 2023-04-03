from flask import Flask, Response
import mysql.connector
import json

app = Flask(__name__)


@app.route('/kentta/<icao>')
def kentta(icao):
    kursori = yhteys.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident like '" + icao + "'"
    kursori.execute(query)
    tulos = kursori.fetchall()

    for rivi in tulos:
        print(rivi)
        vastaus = {
            "ICAO": icao,
            "Name": rivi[0],
            "Municipality": rivi[1]
        }
    jsonvast = json.dumps(vastaus)
    return jsonvast


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='6249',
    autocommit=True
)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
