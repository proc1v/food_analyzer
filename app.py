import os

from datetime import datetime
from dotenv import load_dotenv
from PIL import Image

import gradio as gr

from openai import OpenAI

from storage import StorageHandler
from utils import image_to_base64
from configs import SYSTEM_PROMPT, MODEL_NAME


# Load environment variables from .env file
load_dotenv()
# Initialize the OpenAI API client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
session_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
storage_handler = StorageHandler(session_timestamp)


def analyze_food_image(image: Image.Image) -> str:
    """
    Analyze the food image and return details such as portion size,
    calorie estimates, and warnings for unhealthy foods.
    Args:
        image (Image.Image): The food image to analyze.
    Returns:
        str: The analysis result in Markdown format.
    """
    # Generate a unique identifier for this operation
    identifier = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    try:
        # Save the uploaded image locally
        storage_handler.save_image(image, identifier)

        # Convert image to base64
        b64_image = image_to_base64(image)

        # Send the image to the model
        response = client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": SYSTEM_PROMPT},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{b64_image}",
                        },
                    ],
                }
            ],
        )
        reply_content = response.output[0].content[0].text.strip()

        # Save the result locally
        storage_handler.save_result(reply_content, identifier)

        return reply_content

    except Exception as e:
        # Save the error locally
        error_message = f"Error occurred: {e}"
        storage_handler.save_error(error_message, identifier)
        print(error_message)
        return "An error occurred while analyzing the image. Please try again with a different image."


# Set up Gradio interface components
with gr.Blocks() as demo:
    # Add a description at the top of the interface
    gr.Markdown(
        "### 🥗 Food Image Analyzer\nUpload a food image to estimate portion sizes and calories. The app will also flag unhealthy items (high sugar, etc.)."
    )

    # Create a row layout with two columns
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Food Image")
        with gr.Column():
            analysis_output = gr.Markdown(label="Food Analysis")

    # Clear the output when the image changes
    image_input.change(fn=lambda x: "", inputs=image_input, outputs=analysis_output)

    # Add a button to trigger analysis (optional)
    analyze_btn = gr.Button("Analyze")
    analyze_btn.click(
        fn=analyze_food_image, inputs=image_input, outputs=analysis_output
    )


if __name__ == "__main__":
    demo.launch()
