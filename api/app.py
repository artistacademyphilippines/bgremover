from flask import Flask, request, jsonify
from flask_cors import CORS
from rembg import remove
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api')
def index():
    return "Hello from Sir Ozy!"
        
if __name__ == '__main__':
    app.run()
