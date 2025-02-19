from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api')
def index():
    print("Hello from Flask!")
    return "Hello from Flask!"
