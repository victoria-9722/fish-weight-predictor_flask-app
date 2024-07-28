from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('fish_weight_predictor.pkl')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    species = float(request.form.get('Species'))
    length1 = float(request.form.get('Length1'))
    length2 = float(request.form.get('Length2'))
    length3 = float(request.form.get('Length3'))
    height = float(request.form.get('Height'))
    width = float(request.form.get('Width'))

    fish_data = [[species, length1, length2, length3, height, width]]

    prediction = model.predict(fish_data)

    prediction = prediction[0]
    return render_template("predict.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)