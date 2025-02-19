from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api')
def index():
    return "Hello from Flask!"