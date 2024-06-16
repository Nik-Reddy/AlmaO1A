# AlmaO1A
Welcome to our FastAPI application for CV (Curriculum Vitae) analysis! This project is designed to help you analyze CVs using OpenAI's powerful GPT models, extracting and interpreting text from uploaded PDF files. Whether you're looking to implement this as a part of a larger project or just want to explore AI capabilities, this application provides a robust starting point.

Features
## PDF Upload: 
Users can upload PDF files, which the system will process to extract text.

## Text Analysis: 
The extracted text is analyzed by OpenAI's GPT models, providing insights based on predefined criteria.

## Responsive Web Interface: 
The application includes a basic but functional web interface for easy interaction with the API.

## Secure Secret Management: 
API keys and other sensitive data are managed securely via environment variables.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
Before you can run this application, you'll need to have the following installed:

#### Python 3.8 or higher
#### Pip (Python package installer)
#### Installation
#### Clone the Repository

Start by cloning this repository to your local machine:

git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
Set Up a Virtual Environment

It's good practice to use a virtual environment to manage dependencies for your project:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies mentioned on "requirements.txt"
pip install -r requirements.txt

Set Environment Variables
You'll need to set the OPENAI_API_KEY environment variable to use the OpenAI services:


export OPENAI_API_KEY='your_openai_api_key_here'
Running the Application
To run the application, execute:

uvicorn main:app --host <IPV4 Address> --port 8000
Navigate to http://localhost:8000 in your web browser to see the application in action.

Usage
Upload a CV: Use the web interface to upload a PDF file containing a CV.
Review Analysis: After the CV is processed, the analysis will be displayed on the web page.

If you have suggestions for improvements, please fork the repo and submit a pull request, or open an issue with the tag "enhancement".

License
This project is licensed under the MIT License - see the LICENSE file for details.
