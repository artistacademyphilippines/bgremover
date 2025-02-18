from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def index():
    return "Hello from Flask!"

# Add this line at the end of the file
api = app.wsgi_app
