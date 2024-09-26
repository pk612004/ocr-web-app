OCR and Document Search Web Application
Overview
A web-based prototype for Optical Character Recognition (OCR) on uploaded images with Hindi and English text. It also supports keyword search functionality to find matching text in the extracted content.

Features
Upload an image (JPEG, PNG) with text in Hindi and/or English.
Extract text using OCR.
Search keywords within the extracted text.
Deployment
To deploy on platforms like Hugging Face Spaces or Streamlit Cloud:


Files in the Project
app.py: The main application script.
requirements.txt: Python libraries for the project.
README.md: Documentation.
Libraries Used
Gradio: For the web interface.
Transformers: OCR model (trocr-base-printed).
Pillow: Image processing.
Torch: Model backend.
Assumptions
Images uploaded will contain text in Hindi or English
