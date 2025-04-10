from bottle import Bottle, request, response, run
from ascii import image_to_highres_ascii_image

app = Bottle()

# Manually add CORS headers to enable cross-origin requests
@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins, can change this to specific domains
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, X-Requested-With, Accept'

@app.post('/upload/')
def upload_image():
    # Get the uploaded file from the request
    file = request.files.get('file')

    # Read the image bytes from the file
    image_bytes = file.file.read()

    # Generate ASCII image in memory
    ascii_buffer = image_to_highres_ascii_image(image_bytes)

    # Send the generated ASCII image as a response
    response.content_type = 'image/png'
    return ascii_buffer  # Return the image directly from memory

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000, debug=True)