from flask import Flask,render_template,request,redirect,url_for,flash
import requests

app = Flask(__name__)
app.secret_key = "MasterPrem"

cities =[]

Api_Key = "e7b60f5833602e4505a5891074b408c1"

@app.route('/')
def index():
    return render_template('index.html',cities=cities)

@app.route('/add_city',methods =['POST'])
def add_city():
    city_name = request.form.get('city')
    if city_name and city_name not in cities :
        cities.append(city_name)
        flash(f"City name {city_name} added sucesssfully","success")
    else:
        flash(f"City name{city_name}already exist","error")
    return redirect(url_for('index'))


weather_conditions = {
    "clear": "sunny",
    "clouds": "cloudy",
    "rain": "rainy",
    "drizzle": "rainy",
    "thunderstorm": "stormy",
    "snow": "snowy",
    "default": "default-bg"
}

@app.route('/weather/<city_name>')
def get_weather(city_name):
    if city_name not in cities:
        flash(f"City '{city_name}' not found", "error")
        return redirect(url_for('index'))
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_Key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        weather_condition = data['weather'][0]['main'].lower()
        bg_class = weather_conditions.get(weather_condition, "default")

        weather_info = {
            "city": data["name"],
            "country": data['sys']['country'],
            "temperature": data['main']['temp'],
            "humidity": data["main"]["humidity"],
            "weather_cond": data['weather'][0]['description']
        }
        return render_template('weather.html', weather_info=weather_info, bg_class=bg_class)
    except requests.exceptions.RequestException:
        flash("Error occurred ")
    return redirect(url_for('index'))

@app.route('/delete_city/<city_name>')
def delete_city(city_name):
    if city_name in cities:
        cities.remove(city_name)
        flash(f"City '{city_name}' removed successfully", "success")
    else:
        flash(f"City '{city_name}' not found", "error")
    return redirect(url_for('index'))

@app.route('/update_city/<old_name>', methods=['GET', 'POST'])
def update_city(old_name):
    if old_name not in cities:
        flash(f"City '{old_name}' not found", "error")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        new_name = request.form.get('city').strip()
        if new_name and new_name.lower() not in [city.lower() for city in cities]:
            cities[cities.index(old_name)] = new_name
            flash(f"City '{old_name}' updated to '{new_name}' successfully", "success")
            return redirect(url_for('index'))
        else:
            flash(f"City '{new_name}' already exists or invalid", "error")
    
    return render_template('update_city.html', old_name=old_name)

if __name__ == "__main__":
    app.run(debug=True)