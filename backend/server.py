from flask import Flask, request, send_file
from flask_cors import CORS
from ascii import image_to_highres_ascii_image

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)

@app.route('/upload/', methods=['POST'])
def upload_image():
    file = request.files['file']
    image_bytes = file.read()

    # Generate ASCII image in memory
    ascii_buffer = image_to_highres_ascii_image(image_bytes)

    # Send the image as a response
    # Since ascii_buffer is already a BytesIO object, we can directly use it in send_file
    return send_file(ascii_buffer, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)