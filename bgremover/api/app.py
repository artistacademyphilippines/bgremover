from flask import Flask, request
from flask_cors import CORS  # We'll add this to handle CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api', methods=['POST'])
def process_text():
    data = request.data.decode('utf-8')

    if data:
        print(f"Received flask message: {data}")
        return f"Received: {data}", 200  # Respond with a plain text message
    else:
        return "No message provided", 400

if __name__ == '__main__':
    app.run()

#cool push it again