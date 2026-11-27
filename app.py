from flask import Flask, request, jsonify
import joblib
import pandas as pd


# Create Flask application
app = Flask(__name__)


# Load trained model
model = joblib.load("model.pkl")


# Home route
@app.route("/", methods=["GET"])
def home():


    return jsonify({
        "message": "House Price Prediction API is running"
    })


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():


    try:


        data = request.get_json()


        # Extract input values
        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        age = float(data["age"])


        # Create input DataFrame
        input_data = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "age": [age]
        })


        # Generate prediction
        prediction = model.predict(input_data)


        return jsonify({
            "area": area,
            "bedrooms": bedrooms,
            "age": age,
            "predicted_price": round(
                float(prediction[0]), 2
            )
        })


    except (KeyError, TypeError, ValueError) as e:


        return jsonify({
            "error": str(e)
        }), 400


# Run Flask server
if __name__ == "__main__":


    app.run(host="127.0.0.1", port=5000, debug=False)
