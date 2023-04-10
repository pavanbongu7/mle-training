import pickle

import mlflow.sklearn
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
# Load the model artifact
best_run_id = "ede37f64711845258936830791646d75"
model_path = f"runs:/{best_run_id}/model"
model = mlflow.sklearn.load_model(model_path)

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction function
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the HTML form
    longitude = float(request.form['longitude'])
    latitude = float(request.form['latitude'])
    housing_median_age = float(request.form['housing_median_age'])
    total_rooms = float(request.form['total_rooms'])
    total_bedrooms = float(request.form['total_bedrooms'])
    population = float(request.form['population'])
    households = float(request.form['households'])
    median_income = float(request.form['median_income'])
    rooms_per_household = float(request.form['rooms_per_household'])
    bedrooms_per_room = float(request.form['bedrooms_per_room'])
    population_per_household = float(request.form['population_per_household'])
    ocean_proximity_dropdown = request.form.get('ocean_proximity_dropdown')
    if ocean_proximity_dropdown == 'INLAND':
        inland = 1
        island = 0
        near_bay = 0
        near_ocean = 0
    elif ocean_proximity_dropdown == 'ISLAND':
        inland = 0
        island = 1
        near_bay = 0
        near_ocean = 0
    elif ocean_proximity_dropdown == 'NEAR BAY':
        inland = 0
        island = 0
        near_bay = 1
        near_ocean = 0
    elif ocean_proximity_dropdown == 'NEAR OCEAN':
        inland = 0
        island = 0
        near_bay = 0
        near_ocean = 1
    else:
        inland = 0
        island = 0
        near_bay = 0
        near_ocean = 0

    
    # Make a prediction using the model
    input_list = [[longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, rooms_per_household, bedrooms_per_room, population_per_household,inland,island,near_bay,near_ocean ]]
    prediction = model.predict(input_list)
    print(input_list)
    
    # Return the prediction as a string
    return render_template('prediction.html', predicted_value=str(round(prediction[0], 2)))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')