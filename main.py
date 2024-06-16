import os
import pdfplumber
import openai
import traceback
import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

# Initialize the FastAPI app
app = FastAPI()

# Set up Jinja2 for HTML templating, pointing to the directory where templates are stored
templates = Jinja2Templates(directory="templates")


# Endpoint to serve the main HTML page with the file upload form
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    # Render the upload form template with the current request context
    return templates.TemplateResponse("upload_form.html", {"request": request})


# Endpoint to handle the file upload and process it through GPT model
@app.post("/upload-cv/", response_class=HTMLResponse)
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    # Ensure the uploaded file is a PDF
    if file.content_type != 'application/pdf':
        return JSONResponse(status_code=400, content={"message": "Invalid file type. Please upload a PDF file."})

    try:
        # Extract text from the PDF using pdfplumber
        with pdfplumber.open(file.file) as pdf:
            text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
    except Exception as e:
        # Return an error response if PDF processing fails
        return JSONResponse(status_code=500, content={"message": f"Error processing PDF file: {str(e)}",
                                                      "details": traceback.format_exc()})

    try:
        # Load the prompt template from a text file
        with open('prompt_file.txt', 'r') as file:
            prompt_template = file.read()
        prompt = prompt_template.format(text=text)
    except Exception as e:
        # Return an error if loading the prompt template fails
        return JSONResponse(status_code=500, content={"message": f"Error loading prompt template: {e}"})

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key is not set")
    
    try:
        # Call the OpenAI API with the extracted text and configured prompt
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500  # Can adjust this as per requirement - concise answers give easily understandable response
        )
        # Since it's a probabilistic model, it will get a response differently every request but the context remain the same on the results
        result = response.choices[0].message['content']
    except Exception as e:
        # Return an error if the API call fails
        return JSONResponse(status_code=500, content={"message": f"Error calling OpenAI API: {str(e)}",
                                                      "details": traceback.format_exc()})

    return templates.TemplateResponse("results.html", {"request": request, "result": result})

# # Start the Uvicorn server with live reloading enabled - for Local run during development
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="10.0.0.82", port=8000, reload=True)
