import gradio as gr
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Load the OCR model and processor
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")

# Function to perform OCR
def perform_ocr(image):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    with torch.no_grad():
        output = model.generate(pixel_values)
    return processor.decode(output[0], skip_special_tokens=True)

# Function to perform keyword search in the extracted text
def search_keyword(text, keyword):
    if keyword.lower() in text.lower():
        return f"Keyword '{keyword}' found in the text."
    else:
        return f"Keyword '{keyword}' not found."

# Create the Gradio interface
def main():
    with gr.Blocks() as demo:
        gr.Markdown("## OCR and Document Search Web Application")
        with gr.Row():
            image_input = gr.Image(type="pil", label="Upload an Image")
            output_text = gr.Textbox(label="Extracted Text")
            keyword_input = gr.Textbox(label="Enter Keyword to Search")
            search_result = gr.Textbox(label="Search Result")
        
        submit_btn = gr.Button("Extract Text")
        search_btn = gr.Button("Search Keyword")
        
        submit_btn.click(fn=perform_ocr, inputs=image_input, outputs=output_text)
        search_btn.click(fn=search_keyword, inputs=[output_text, keyword_input], outputs=search_result)
    
    # Set share=True to create a public link
    demo.launch(share=True)

if __name__ == "__main__":
    main()
