from flask import Flask, request, jsonify
from flask_cors import CORS  # We'll add this to handle CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api', methods=['POST'])
def process_text():
    data = request.json
    input_text = data.get('text', '')
    # Process the input_text here. For this example, we'll just reverse it.
    result = input_text[::-1]
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()