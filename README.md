Heart Attack Prediction Web App

This is a Flask web application that predicts the risk of a heart attack using a trained machine learning model (best_model.pkl).
The app collects user input through a form, processes it, and returns a prediction as either High Risk or Low Risk.

Features

User-friendly form for entering health parameters

Predicts heart attack risk using a trained ML model

Returns results in JSON format

Built using Flask and joblib

Model

The trained model is stored in:

models/best_model.pkl

Model output:

1 → High Risk

0 → Low Risk

Project Structure
.
├── app.py
├── models/
│   └── best_model.pkl
├── templates/
│   ├── user.html
│   └── index.html
└── README.md

Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/heart-attack-prediction.git
cd heart-attack-prediction

2. Create a virtual environment (recommended)
python -m venv venv

3. Activate the virtual environment

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

4. Install required packages
pip install flask joblib numpy

Running the App
python app.py


Open your browser and go to:

http://127.0.0.1:5000/

API Endpoints
/ (GET)

Returns the welcome page.

/index (POST)

Renders the form page.

/predict (POST)

Receives form data and returns the prediction result as JSON.

Example Input Data
{
  "age": 55,
  "cholesterol": 200,
  "smoking": 0,
  "diabetes": 0,
  "bloodPressure": 120,
  "stressLevel": 2,
  "obesity": 1,
  "heartRate": 80,
  "bmi": 24.5,
  "physicalActivity": 3,
  "sleepHours": 7,
  "triglycerides": 150,
  "familyHistory": 0,
  "exerciseHours": 2,
  "sedentaryHours": 6
}

Notes

Ensure models/best_model.pkl exists.

Input values must be sent in the same order as in the code.

Make sure templates/ folder contains user.html and index.html.
