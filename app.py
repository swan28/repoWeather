from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/") # https://yellow-waitress-zkuif.pwskills.app:5000 => hit this url to get the weather form
def showWeatherForm():
    return render_template('weatherForm.html') 

@app.route("/weatherapp", methods=['POST', 'GET'])
def takeWeatherData(): # bind this  func to the "/weatherapp" route
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # request => to get data from form
    parameter = {
        'q' : request.form.get('city'),
        'units' : request.form.get('units'),
        'appid' : request.form.get('appid')
    }

    # requests => to get data from URL
    response = requests.get(url, params=parameter)
    data = response.json()
    city = data['name']
    return f"data : {data}, city : {city}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")