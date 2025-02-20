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
    #try:
        # Get the base64 string from the request
        data = request.data.decode('utf-8')
        base64_string = data

        #return "Hello from Boss Ozy!" + data
    
        # Decode the base64 string to image
        img_data = base64.b64decode(base64_string.split(',')[1])
        img = Image.open(io.BytesIO(img_data))

        # Remove background
        output = remove(img)

        # Convert the output image to base64
        buffered = io.BytesIO()
        output.save(buffered, format="PNG")
        buffered.seek(0)

        # Encode the image in base64
        img_base64 = base64.b64encode(buffered.read()).decode('utf-8')

        print('BOSS! data:image/png;base64,' + img_base64)
        
    #except Exception as e:
    #    return {'error': str(e)}, 500
        
if __name__ == '__main__':
    app.run()
