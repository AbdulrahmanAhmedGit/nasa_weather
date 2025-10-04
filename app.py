import requests
import secrets
import sqlite3
from flask import Flask, flash, redirect, render_template, request, jsonify
import xarray as xr
import requests
import numpy as np

app = Flask(__name__)
API_KEY = "e4f9d234b1694596a74194334252909"
custom_id = secrets.token_hex(16)
public_ip = requests.get("https://api.ipify.org").text

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

def weth(inlat, inlon, month, day):
    token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImFiZG9uZXduYXNhIiwiZXhwIjoxNzY0NzQyNTIxLCJpYXQiOjE3NTk1NTg1MjEsImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiIsImlkZW50aXR5X3Byb3ZpZGVyIjoiZWRsX29wcyIsImFjciI6ImVkbCIsImFzc3VyYW5jZV9sZXZlbCI6M30.xbNoLWyB0ocWHvJ6TeZdJFiFvW3uOsesSG7v9N5rSqM5l_ZFDR4lbJXq4zoh6PbTJYh9Cv7NpuO6TyM3QXWkHd9WVJRkT1czg4v44FnDySrD_n5z_EVtEmG8gX_egiBgAdMzE-mPg_lg7dwjHXTOzGXp-oLKd0xWuYas2y7DLt2Wr0r4ytt4iuDWpfmiDC_yEXMOhVZwmRvRM0rfP5hwaHRB6W0HW5DlbOKObJH8v0Qtg_oAJPWc2izyxHe9pczQzmTQKZgaY4N33LGFmCk_lNCXJuSL8Wio2UHUtOzYaZclT_klWgI0YpZ2AmMCKnxq5V_GYYQhlW-wODidgqTk4g"
    values = []
    years = range(2001, 2025)
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    count = 0
    for i in years:
        url = f"https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3IMERGDF.07/{i}/{month}/3B-DAY.MS.MRG.3IMERG.{i}{month}{day}-S000000-E235959.V07B.nc4"
        ds = xr.open_dataset(url, engine="pydap", backend_kwargs={"session": session})
        precip_point = ds["precipitation"].sel(
            lat=inlat,
            lon=inlon,
            method="nearest"
        )

        if precip_point.size > 0:
            values.append(float(precip_point.values))
        else:
            values.append(np.nan)
        print(f'Level {count} From {len(years)}')
        count += 1

    avg_precip = np.nanmean(values)
    return avg_precip

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
        if data:
            lat = data.get("lat")
            lon = data.get("lon")
            return jsonify({"redirect": f"/{lat}/{lon}"})
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
    else:
        return render_template('main.html', result="result", final ="final", background="back", text="text", city="CITY")


@app.route('/<lat>/<lon>', methods=['GET'])
def main(lat, lon):
    day = request.args.get('day')
    month = request.args.get('month')
    year = request.args.get('year')
    spec = False
    rsult = ' '
    if day and month and year:
        if len(str(month)) >= 2:
            if len(str(day)) >= 2:
                rsult = round(weth(lat, lon, month, day), 3)
            elif len(str(day)) < 2:
                day = f'0{day}'
                rsult = round(weth(lat, lon, month, day), 3)
        elif len(str(month)) < 2:
            month = f'0{month}'
            if len(str(day)) >= 2:
                rsult = round(weth(lat, lon, month, day), 3)
            elif len(str(day)) < 2:
                day = f'0{day}'
                rsult = round(weth(lat, lon, month, day), 3)
        spec = True
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
                back = f"../static/img/bad-weather-2772933_1280.jpg"
            return render_template("main copy.html", rsult=rsult,spec=spec,result=result, final =final, background=back, text=text, city=CITY, lat=lat, lon=lon)
        else:
            return render_template("error.html", message= data['error']['message'])





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5006,debug=True)
