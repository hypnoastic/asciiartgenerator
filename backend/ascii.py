import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def image_to_highres_ascii_image(
    image_bytes,
    font_path="font/couriernew.ttf",
    font_size=20,
    scale=0.6
):
    # Read image from bytes
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Failed to decode image from bytes.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_gray = cv2.resize(gray, (new_width, new_height))

    chars = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    num_chars = len(chars)

    ascii_image = [
        ''.join([chars[int(pixel) * num_chars // 256] for pixel in row])
        for row in resized_gray
    ]

    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        font = ImageFont.load_default()

    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]

    img_width = char_width * new_width
    img_height = char_height * new_height
    output_img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(output_img)

    for i, line in enumerate(ascii_image):
        draw.text((0, i * char_height), line, fill="black", font=font)

    # Save to temporary storage instead of a file
    output_buffer = BytesIO()
    output_img.save(output_buffer, format="PNG")
    output_buffer.seek(0)
    return output_buffer