from flask import Flask, request, jsonify
from flask_cors import CORS  # We'll add this to handle CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api', methods=['POST'])
def process_text():
    data = request.get_json()

    if 'message' in data:
        message = data['message']
        # Process the message (e.g., print, save, etc.)
        #print(f"Received message: {message}")
        return jsonify({"status": "success", "message": message}), 200
    else:
        return jsonify({"status": "error", "message": "No message provided"}), 400

if __name__ == '__main__':
    app.run()

#cool push it again