from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from ascii import image_to_highres_ascii_image

app = FastAPI()

# CORS setup to allow frontend to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://asciigenerator.netlify.app"],  # Change this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Generate ASCII image in memory
    ascii_buffer = image_to_highres_ascii_image(image_bytes)

    return StreamingResponse(ascii_buffer, media_type="image/png")