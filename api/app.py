from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api')
def index():
    return "Hello from Flask!"
    
if __name__ == '__main__':
    app.run()
