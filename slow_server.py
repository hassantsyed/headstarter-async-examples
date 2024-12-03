from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def slow_response():
    """Simulate a slow API endpoint with a 5-second delay."""
    print("Received request, waiting 5 seconds...")
    time.sleep(5)
    return jsonify({'message': 'Slow response completed!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)