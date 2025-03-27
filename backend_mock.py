from flask import Flask, request, jsonify

app = Flask(__name__)

# Root endpoint (handles GET requests to '/')
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

# Endpoint to verify data sent from your app
@app.route('/verify', methods=['POST'])
def verify_data():
    # Get the data sent by the app (from the request body)
    data = request.get_json()

    # Print the data to the console (for debugging)
    if data:
        print("Received data:", data)  # Logs the data to the console
        return jsonify({"message": "Data received successfully", "received": data}), 200
    else:
        return jsonify({"message": "No data received"}), 400

if __name__ == '__main__':
    app.run(debug=True)
