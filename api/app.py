from flask import Flask, render_template
from flask_cors import CORS  # We'll add this to handle CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

#@app.route('/api', methods=['POST'])
@app.route('/api')


#def process_text():
#    data = request.data.decode('utf-8')

#    if data:
#        return data
#    else:
#        # Return an error as plain text
#        return 400

def index():
    print('bimbi')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#cool push it again
