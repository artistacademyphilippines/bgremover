from flask import Flask, request, jsonify
from flask_cors import CORS
from rembg import remove
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/rembg', methods=['POST'])
def remove_background():
    try:
        # Get the base64 string from the request
        data = request.json
        base64_string = data['image']

        # Decode the base64 string to image
        img_data = base64.b64decode(base64_string.split(',')[1])
        img = Image.open(io.BytesIO(img_data))

        # Remove background
        output = remove(img)

        # Convert the output image to base64
        buffered = io.BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({'image': f'data:image/png;base64,{img_str}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
