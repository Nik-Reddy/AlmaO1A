# AlmaO1A
Welcome to our FastAPI application for CV (Curriculum Vitae) analysis! This project is designed to help you analyze CVs using OpenAI's powerful GPT models, extracting and interpreting text from uploaded PDF files. Whether you're looking to implement this as a part of a larger project or just want to explore AI capabilities, this application provides a robust starting point.


## Site is  live at:
https://nik-reddy.github.io/AlmaO1A/

## Docuemnts Walkhtough:
### Design and Evaluation_Present Scope.pdf: 
Explains the current working solution I developed using GPT-4 and other LLMs 
### System Design for Large Scale.pdf:
Future scope and enhancement can be made to the current system to handle a large user base.
### main.py: 
Python Script that contains the FAST API development and use of LLM  model to respond to a given USER CV as text input.
### Prompt_file.txt: 
This file contains the prompting approach used in the process of understanding the input CV text and provides a systematic approach to analyze and provide results based on the given 8 criteria to classify a user into a [LOW, MEDIUM, HIGH] qualified category.

### Prompt Engineering: Leveraged various prompting techniques like:
##### Chain of Thought (CoT) Prompting: mimic a step-by-step reasoning process
##### Contextual Embedding: setting the stage for the kind of analysis required
##### Explicit Instruction: instructs the model on the format and depth of the analysis required
##### Simulated Role-Playing: sets up a role for the language model to adopt—that of an immigration consultant—which is a form of role-playing:
##### Iterative Refinement: An iterative approach to evaluating the CV, where each criterion is assessed independently before a final judgment is made.

## Features
### PDF Upload: 
Users can upload PDF files, which the system will process to extract text.

### Text Analysis: 
The extracted text is analyzed by OpenAI's GPT models or other LLMs (Used GPT 4 and GPT 3.5 Turbo as part of the implementation for now), providing insights based on predefined criteria.

### Responsive Web Interface: 
The application includes a basic but functional web interface for easy interaction with the API.

### Secure Secret Management: 
API keys and other sensitive data are managed securely via environment variables.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Before you can run this application, you'll need to have the following installed:
#### Python 3.8 or higher
#### Pip (Python package installer)


## Installation
#### Clone the Repository
##### Start by cloning this repository to your local machine:
git clone https://github.com/<yourusername>/<your-repository-name.git>

##### Install Dependencies mentioned on "requirements.txt"
pip install -r requirements.txt

##### Set Environment Variables
You'll need to set the OPENAI_API_KEY environment variable to use the OpenAI services:


export OPENAI_API_KEY='your_openai_api_key_here'


### Running the Application
##### To run the application, execute:
uvicorn main:app --host <IPV4 Address> --port 8000
Navigate to http://localhost:8000 in your web browser to see the application in action.

## Usage
##### Upload a CV: Use the web interface to upload a PDF file containing a CV.
![image](https://github.com/Nik-Reddy/AlmaO1A/assets/41942071/c8e4afcc-10e6-4e79-af19-071186b8e6c6)


##### Review Analysis: After the CV is processed, the analysis will be displayed on the web page.
![image](https://github.com/Nik-Reddy/AlmaO1A/assets/41942071/e8c5b93d-7056-439b-84ae-23fb388bad51)

##### Click GoBack to redirect to the home page to upload other documents to evaluate another document
If you have suggestions for improvements, please fork the repo and submit a pull request, or open an issue with the tag "enhancement".
