from pathlib import Path
from django.conf import settings # type: ignore
from PIL import Image


# redimensionar a imagem
def resize_image(image_django, new_width=800, optimize=True, quality=60):
    """
    Resizes a Django image to a specified width while maintaining aspect ratio.

    Parameters:
    image_django: An instance of a Django image field.
    new_width (int): The desired width for the resized image. Default is 800.
    optimize (bool): Whether to optimize the image. Default is True.
    quality (int): The quality of the saved image, on a scale from 1 (worst) to 95 (best). Default is 60.

    Returns:
    Image: The resized PIL Image object.
    """
    image_path = Path(settings.MEDIA_ROOT/image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow
    
    new_height = round(new_width / original_height * original_width ) 

    new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS) # type: ignore
    new_image.save(
        image_path, 
        optimize=optimize, 
        quality=quality,
    )
    
    return new_image