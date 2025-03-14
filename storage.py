import os

from PIL import Image
from datetime import datetime


class StorageHandler:
    """
    Handles saving inputs, outputs, and errors to session-specific directories.
    """

    def __init__(self, session_timestamp: str):
        """
        Initialize the StorageHandler with a session-specific directory.
        Args:
            session_timestamp (str): The timestamp of the session start.
        """
        self.base_dir = os.path.join("saved_data", session_timestamp)
        os.makedirs(self.base_dir, exist_ok=True)

    def save_image(self, image: Image.Image, identifier: str) -> str:
        """
        Save the uploaded image to a local file.
        Args:
            image (Image.Image): The image to save.
            identifier (str): A unique identifier for the image.
        Returns:
            str: The path to the saved image.
        """
        image_path = os.path.join(self.base_dir, f"{identifier}_image.jpg")
        image.save(image_path, format="JPEG")
        return image_path

    def save_result(self, result: str, identifier: str) -> str:
        """
        Save the analysis result to a local file.
        Args:
            result (str): The result to save.
            identifier (str): A unique identifier for the result.
        Returns:
            str: The path to the saved result.
        """
        result_path = os.path.join(self.base_dir, f"{identifier}_result.txt")
        with open(result_path, "w", encoding="utf-8") as file:
            file.write(result)
        return result_path

    def save_error(self, error: str, identifier: str) -> str:
        """
        Save an error message to a local file.
        Args:
            error (str): The error message to save.
            identifier (str): A unique identifier for the error.
        Returns:
            str: The path to the saved error.
        """
        error_path = os.path.join(self.base_dir, f"{identifier}_error.txt")
        with open(error_path, "w", encoding="utf-8") as file:
            file.write(error)
        return error_path
