import io
import base64

from PIL import Image


def image_to_base64(image: Image.Image) -> str:
    """
    Convert a PIL image to a base64 string.
    Args:
        image (Image.Image): The image to convert.
    Returns:
        str: The base64-encoded image
    """
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
