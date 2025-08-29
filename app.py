import requests
import secrets
import sqlite3
from flask import Flask, flash, redirect, render_template, request, jsonify

app = Flask(__name__)
API_KEY = "9f44049fcbe24e75b3b160827252108"
custom_id = secrets.token_hex(16)
public_ip = requests.get("https://api.ipify.org").text

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/', methods=['GET', 'POST'])
def new():
    conn = sqlite3.connect('public_ip.db')
    cursor = conn.cursor()
    info = cursor.execute('SELECT id, traffic FROM ip WHERE ip = ?', (public_ip,)).fetchall()
    if info:
        traffic = int(info[0][1])+1
        cursor.execute('UPDATE ip SET traffic = ? WHERE id = ?', (traffic, info[0][0]))
    else:
        cursor.execute('INSERT INTO ip (ip) VALUES(?)', (public_ip,))
    conn.commit()
    if request.method == 'POST':
        data = request.get_json()
        lat = data.get("lat")
        lon = data.get("lon")
        return jsonify({"redirect": f"/{lat}/{lon}"})
    else:
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={public_ip}&custom_id={custom_id}"
        response = requests.get(url)
        data = response.json()
        CITY = data["location"]["name"]
        temp = float(data["current"]["temp_c"])
        wind_s = float(data["current"]["wind_kph"])
        rain = float(data["current"]["humidity"])
        like = float(data["current"]["feelslike_c"])
        windchill = float(data["current"]["windchill_c"])
        pressure = float(data["current"]["pressure_in"])
        cloud = float(data["current"]["cloud"])
        day = int(data["current"]["is_day"])
        difference = abs(like-temp)
        result = [temp, like, wind_s, rain, windchill, pressure, cloud, day]
        final = ''
        text = data["current"]["condition"]["text"]
        if temp > 35:
            final = "very hot"
        elif temp < 5:
            final = "very cold"
        elif wind_s > 30:
            final = "very windy"
        elif rain > 95:
            final = "very wet"
        elif difference > 6:
            final = "very uncomfortable"
        
        if final:
            final = final.capitalize()
        else:
            final = "Good For Outings"
        
        #------------------------
        #----------Main----------
        #------------------------

        avaleb = ['Blowing snow', 'Clear', 'Cloudy', 'Heavy freezing drizzle', 'Heavy rain',
                'Mist', 'Moderate or heavy rain with thunder', 'Sunny','Patchy rain possible','Partly cloudy','Overcast']
        if text in avaleb:
            if result[7] == 1:
                if text == "Clear":
                    text = "Sun Set"
                back = f"./static/img/{text}.jpg"
            elif result[7] != 1:
                back = f"./static/img/{text}-night.jpg"
        else:
            back = f"./static/img/bad-weather-2772933_1280.jpg"
        return render_template("main.html", result=result, final =final, background=back, text=text, city=CITY) 


@app.route('/<lat>/<lon>', methods=['GET'])
def main(lat, lon):
    conn = sqlite3.connect('public_ip.db')
    cursor = conn.cursor()
    info = cursor.execute('SELECT id, traffic FROM ip WHERE ip = ?', (public_ip,)).fetchall()
    if info:
        traffic = int(info[0][1])+1
        cursor.execute('UPDATE ip SET traffic = ? WHERE id = ?', (traffic, info[0][0]))
    else:
        cursor.execute('INSERT INTO ip (ip) VALUES(?)', (public_ip,))
    conn.commit()
    if request.method == 'GET':
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&custom_id={custom_id}"
        response = requests.get(url)
        data = response.json()
        if "error" not in data:
            CITY = data["location"]["name"]
            temp = float(data["current"]["temp_c"])
            wind_s = float(data["current"]["wind_kph"])
            rain = float(data["current"]["humidity"])
            like = float(data["current"]["feelslike_c"])
            windchill = float(data["current"]["windchill_c"])
            pressure = float(data["current"]["pressure_in"])
            cloud = float(data["current"]["cloud"])
            day = int(data["current"]["is_day"])
            difference = abs(like-temp)
            result = [temp, like, wind_s, rain, windchill, pressure, cloud, day]
            final = ''
            text = data["current"]["condition"]["text"]
            if temp > 35:
                final = "very hot"
            elif temp < 5:
                final = "very cold"
            elif wind_s > 30:
                final = "very windy"
            elif rain > 95:
                final = "very wet"
            elif difference > 6:
                final = "very uncomfortable"
            
            if final:
                final = final.capitalize()
            else:
                final = "Good For Outings"
            
            #------------------------
            #----------Main----------
            #------------------------

            avaleb = ['Blowing snow', 'Clear', 'Cloudy', 'Heavy freezing drizzle', 'Heavy rain',
                    'Mist', 'Moderate or heavy rain with thunder', 'Sunny','Patchy rain possible','Partly cloudy','Overcast']
            if text in avaleb:
                if result[7] == 1:
                    if text == "Clear":
                        text = "Sun Set"
                    back = f"../static/img/{text}.jpg"
                elif result[7] != 1:
                    back = f"../static/img/{text}-night.jpg"
            else:
                back = f"./static/img/bad-weather-2772933_1280.jpg"
            return render_template("main copy.html", result=result, final =final, background=back, text=text, city=CITY)
        else:
            return render_template("error.html", message= data['error']['message'])





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5006,debug=True)
