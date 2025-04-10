from flask import Flask, request, send_file
from ascii import image_to_highres_ascii_image  # Import your image processing logic

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16MB


@app.route('/upload/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    # Check if the user has selected a file
    if file.filename == '':
        return "No selected file", 400

    image_bytes = file.read()

    ascii_buffer = image_to_highres_ascii_image(image_bytes)

    return send_file(ascii_buffer, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)