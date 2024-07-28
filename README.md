# Fish Weight Predictor

This application has been deployed: https://fish-weight-predictor.onrender.com

This project is a Fish Weight Predictor web application. It allows users to predict the weight of a fish based on its species and various length measurements. The application is built using Flask for the backend and HTML/CSS with Bootstrap for the frontend. The machine learning model is trained using a dataset from Kaggle.

## Features

- Input fish species and measurements to get a weight prediction.
- Web interface for easy input of data.
- Deployed on Render for easy access.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- scikit-learn
- pandas
- joblib
- gunicorn

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fish-weight-predictor.git
    cd fish-weight-predictor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000` to see the application running.


## Files

- `app.py`: The main Flask application file.
- `index.html`: The main HTML file for user input.
- `predict.html`: The HTML file for displaying predictions.
- `Regression_model_lab_5.ipynb`: The Jupyter Notebook used for training the model.
- `requirements.txt`: The required packages for the application.

## License

This project is licensed under the MIT License.

