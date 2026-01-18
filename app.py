from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model from the best_model.pkl file using joblib
with open('models/best_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

@app.route('/')
def home():
    return render_template('user.html')  # You can render this if you want a welcome page

@app.route('/index', methods=["POST"])
def index():
    return render_template('index.html')  # Render the index page with the form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data from the POST request and convert it to the necessary types
        age = int(request.form['age'])
        cholesterol = int(request.form['cholesterol'])
        smoking = int(request.form['smoking'])
        diabetes = int(request.form['diabetes'])
        blood_pressure = int(request.form['bloodPressure'])
        stress_level = int(request.form['stressLevel'])
        obesity = int(request.form['obesity'])
        heart_rate = int(request.form['heartRate'])
        bmi = float(request.form['bmi'])
        physical_activity = int(request.form['physicalActivity'])
        sleep_hours = int(request.form['sleepHours'])
        triglycerides = int(request.form['triglycerides'])
        family_history = int(request.form['familyHistory'])
        exercise_hours = int(request.form['exerciseHours'])
        sedentary_hours = int(request.form['sedentaryHours'])

        # Prepare the data in the format expected by the model (a 2D array)
        input_data = np.array([[age, cholesterol, smoking, diabetes, blood_pressure, stress_level,
                                obesity, heart_rate, bmi, physical_activity, sleep_hours, triglycerides,
                                family_history, exercise_hours, sedentary_hours]])

        # Predict the risk using the trained model
        prediction = model.predict(input_data)

        # Map the prediction to a more readable result (e.g., 'High Risk' or 'Low Risk')
        predicted_risk = 'High Risk' if prediction[0] == 1 else 'Low Risk'

        # Return the prediction result as a JSON response
        return jsonify({'predicted_risk': predicted_risk})

    except Exception as e:
        # Handle errors and return an error message as JSON
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
