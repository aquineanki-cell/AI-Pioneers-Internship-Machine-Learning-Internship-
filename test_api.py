import requests

# The URL of your running Flask app
url = 'http://127.0.0.1:5000/predict'

# A suspicious transaction to test fraud detection
sample_transaction = {
    'amount': -0.7793744255120085, 
    'transaction_hour': -0.08570774013247712,
    'foreign_transaction': 1,          
    'location_mismatch': 1,             
    'device_trust_score': -1.293815890247523,
    'velocity_last_24h':0.6918733426373468,
    'cardholder_age':0.9033876378472397,
    'merchant_category_Electronics': 1, 
    'merchant_category_Food': 0,
    'merchant_category_Grocery': 0,
    'merchant_category_Travel': 0
}

# Send the data to the API
response = requests.post(url, json=sample_transaction)
print(response.json())