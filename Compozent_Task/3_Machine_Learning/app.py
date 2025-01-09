import pickle
from flask import Flask,request, jsonify, render_template

app = Flask(__name__)
#only using linear regression model cause it has higher accuracy
with open("Compozent_Task/3_Machine_Learning/linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)
#mapping the inputs to match the labelencoded dataset
cloud_mapping = {"clear": 0, "partly cloudy": 1, "overcast": 2}
season_mapping = {"Winter": 0, "Spring": 1, "Summer": 2}
location_mapping = {"inland": 0, "coastal": 1, "mountain": 2}

#giving default values to other features
default_values = {
    "wind_speed": 5.0,  
    "precipitation": 50.0, 
    "pressure": 1013.25, 
    "uv_index": 5,  
    "visibility": 10.0, 
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
    
        data = request.form
        features = [
            float(data["humidity"]),
            default_values["wind_speed"],
            default_values["precipitation"],
            cloud_mapping[data["cloud_cover"]],
            default_values["pressure"],
            default_values["uv_index"],
            season_mapping[data["season"]],
            default_values["visibility"],
            location_mapping[data["location"]],
        ]
        
        # Predict using the trained model
        prediction = model.predict([features])[0]
        return render_template("index.html", prediction=f"The Predicted temperature is {prediction:}°C")
    #error handing to handle exceptions
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
