from flask import Flask, request
from flask_cors import CORS
from rembg import remove
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5503", "https://artistacademyphilippines.github.io"])

@app.route('/', methods=['GET','POST'])

def index():
    return "Hello from Boss Ozy!"

def remove_background():
    try:
        # Get the base64 string from the request
        data = request.data.decode('utf-8')
        base64_string = data

        # Decode the base64 string to image
        img_data = base64.b64decode(base64_string.split(',')[1])
        img = Image.open(io.BytesIO(img_data))

        # Remove background
        output = remove(img)

        # Convert the output image to base64
        buffered = io.BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return f'data:image/png;base64,{img_str}'
    except Exception as e:
        return {'error': str(e)}, 500
        
if __name__ == '__main__':
    app.run()
