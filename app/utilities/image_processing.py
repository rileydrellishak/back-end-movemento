from PIL import Image
from io import BytesIO

def process_image(file):
    MAX_SIZE = (1024, 1024)
    JPEG_QUALITY = 80

    image = Image.open(file.stream)

    if image.mode in ('RGBA', 'P'):
        image = image.convert('RGB')
    
    image.thumbnail(MAX_SIZE)
    buffer = BytesIO()
    image.save(
        buffer,
        format='JPEG',
        quality=JPEG_QUALITY,
        optimize=True
    )

    buffer.seek(0)
    return buffer