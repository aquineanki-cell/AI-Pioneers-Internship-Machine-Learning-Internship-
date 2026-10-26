from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize the Flask web app
app = Flask(__name__)

# Load the saved model from Step 1
model = joblib.load('fraud_model.pkl')

# Create an API endpoint that listens for POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get the transaction data sent by the user
    data = request.json
    
    # 2. Convert it into a Pandas DataFrame so the model can read it
    input_data = pd.DataFrame([data])
    
    # 3. Ask the model to make a prediction (0 for Normal, 1 for Fraud)
    prediction = model.predict(input_data)
    
    # 4. Return the result back to the user
    if prediction[0] == 1:
        result = "Warning: Fraudulent Transaction Detected!"
    else:
        result = "Safe: Normal Transaction."
        
    return jsonify({'prediction': result})

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
