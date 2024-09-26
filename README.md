OCR and Document Search Web Application
Overview
This is a web-based prototype that performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. The application also supports a basic keyword search functionality to find and highlight matching text in the extracted content.

Features
Upload an image (JPEG, PNG) with text in Hindi and/or English.
Extract text from the image using the OCR model.
Keyword search within the extracted text.
Display search results with matching sections highlighted.
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/pk612004/ocr-web-app.git
cd ocr-web-app
2. Set up a Python Virtual Environment
bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
3. Install the Required Libraries
bash
Copy code
pip install -r requirements.txt
Usage
Run the application:

bash
Copy code
python app.py
The application will launch and be accessible at:

arduino
Copy code
http://127.0.0.1:7860
Upload an image containing Hindi or English text, and the OCR model will extract the text. You can also enter keywords to search for within the extracted text.

Deployment
This app can be deployed on platforms like Hugging Face Spaces or Streamlit Cloud for live accessibility.

For deployment on Streamlit Cloud, follow these steps:

Create an account on Streamlit.
Link your GitHub repository to Streamlit.
Deploy the web application directly from the repository.
Files in the Project
app.py: The main application script.
requirements.txt: A list of required Python libraries for the project.
README.md: Documentation for the project.
Libraries Used
Gradio: To build the web interface.
Transformers: For using the OCR model (trocr-base-printed).
Pillow: To handle image processing.
Torch: For the model backend.
Live Demo
You can access the live demo of this application here (Replace with your live URL).

Assumptions Made
The images uploaded will be in either Hindi or English.
The application focuses on simple keyword search and does not handle advanced query matching.
Limitations
This prototype is limited to extracting text from a single image at a time.
Performance may vary depending on the complexity of the image and the amount of text.
