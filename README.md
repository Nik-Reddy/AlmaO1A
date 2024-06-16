# AlmaO1A
Welcome to our FastAPI application for CV (Curriculum Vitae) analysis! This project is designed to help you analyze CVs using OpenAI's powerful GPT models, extracting and interpreting text from uploaded PDF files. Whether you're looking to implement this as a part of a larger project or just want to explore AI capabilities, this application provides a robust starting point.


## Site is  live at:
https://nik-reddy.github.io/AlmaO1A/

## Documents Walkhtough:
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


#### Review Analysis: After the CV is processed, the analysis will be displayed on the web page.
![image](https://github.com/Nik-Reddy/AlmaO1A/assets/41942071/e8c5b93d-7056-439b-84ae-23fb388bad51)

##### Structure of the Analysis Results: For a given sample Resume. (Attached in Sample Resumes Folder)
Criterion-Based Evaluation: Each of the eight criteria necessary for the O-1A visa has been individually assessed. The results are presented in a list format, with each criterion followed by a rating (Low, Medium, High) and a brief explanation justifying the rating:
Awards: The candidate's CV did not mention any nationally or internationally recognized awards, resulting in a "Low" rating.
Membership: No memberships requiring outstanding achievements were noted, thus a "Low" rating.
Press: The absence of significant publications also leads to a "Low" rating.
Judging: Lack of evidence regarding participation as a judge in the field results in a "Low" rating.
Original Contribution: This category received a "High" rating, indicating significant contributions such as innovative algorithms or models noted in the CV.
Scholarly Articles: Despite some publications, the lack of articles in professional journals resulted in a "Low" rating.
Critical Employment: The candidate has held important roles in reputable organizations, meriting a "Medium" rating.
High Remuneration: With insufficient information on salary or remuneration compared to peers, this criterion also received a "Low" rating.
Overall Evaluation:
The summary compiles the ratings across all criteria, providing an overall evaluation of the candidate's qualifications for an O-1A visa:
High: The candidate meets high standards in original contributions.
Medium: Significant employment roles are acknowledged.
Low: Most criteria including awards, membership, press, judging, scholarly articles, and high remuneration did not meet the high standards required.

#### Click GoBack to redirect to the home page to upload other documents to start evaluating another document
If you have suggestions for improvements, please fork the repo and submit a pull request, or open an issue with the tag "enhancement".
