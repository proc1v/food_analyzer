# Food Image Analyzer

The **Food Image Analyzer** is a Python-based application that uses OpenAI's API to analyze food images. It provides details such as portion size, calorie estimates, and warnings for unhealthy foods. The application uses a Gradio interface for user interaction.

---

## Features

- Upload a food image to analyze portion sizes and calorie estimates.
- Flags unhealthy items (e.g., high sugar content).
- Saves uploaded images, analysis results, and errors in session-specific directories for easy management.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.11 or higher installed on your system.
2. **OpenAI API Key**: You need an API key from OpenAI to use this application.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/proc1v/food_analyzer.git
cd food_analyzer
```

### 2. Create a Virtual Environment
Create a virtual environment to isolate dependencies:
```bash
python -m venv .venv
```

Activate the virtual environment:
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Create a .env File
The application requires a .env file to store your OpenAI API key. Use the provided .env.example file as a template.

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Open the .env file and replace the placeholder with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## Usage

### 1. Run the Application
To start the application, use the following command:
```bash
python app.py
```

This will launch the Gradio interface and provide a URL in the terminal, such as:
```
Running on local URL:  http://127.0.0.1:7860
```

### 2. Access the Application
Open your web browser and navigate to the provided URL (e.g., `http://127.0.0.1:7860`). You can upload a food image and view the analysis results directly in the browser.

### 3. Interactive Mode with Auto-Reload
Gradio supports an interactive mode that detects changes in the code and automatically reloads the application. To enable this, run the app with command:
```bash
gradio app.py
```

This is especially useful during development, as it allows you to see changes in real-time without restarting the application manually.


## Notes

- All uploaded images, analysis results, and errors are saved in the saved_data directory under session-specific subdirectories.
- The application uses OpenAI's API, so ensure your API key has sufficient permissions and quota.

---

## Troubleshooting

- **Missing Dependencies**: Ensure you have installed all dependencies using the requirements.txt file.
- **Invalid API Key**: Double-check your .env file to ensure the API key is correct.
- **Environment Activation Issues**: Ensure you are activating the virtual environment before running the application.

---
