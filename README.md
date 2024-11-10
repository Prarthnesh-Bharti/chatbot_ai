# planetAi
This web application allow users to interact with their documents like pdfs by asking questions and getting respones related to their questions. 

## Features
- Uploading PDF files.
- Asking questions


## Architecture
The project contains the following folders and services
- ```planet```: Frontend developed using React.js
- ```backend```: Backend developed using FASTAPI
- ```NLP Processing```: NLP processings are handled using LLamaIndex
- ```Storage```:Used Local file system to store pdfs


**Tech used to make scalable architecture -**
- **React.js** - React's component-based structure promotes reusability and modularity, making the codebase easier to maintain and scale.
- **FASTAPI** - Built on top of Starlette for the web parts and Pydantic for the data parts, FastAPI is designed to be one of the fastest Python web frameworks.
- **LLamaIndex** - Provides sophisticated natural language processing tools, facilitating the development of intelligent applications that understand and process human language.

## Setup Guide
1. Run ```npm install``` in planet and ```pip install``` in Backend.
2. Make .env file in Backend.
    - ```backend``` :OPENAI_API_KEY

4. Run ```npm start``` in planet and ```fastapi dev main.py``` in backend

At this point following service would be up and running: 
|Service|PORT|
|------|------|
|caretaker|:3000|
|backend|:8000|

## Demo Video 
[Watch the demo video](https://drive.google.com/file/d/1yNrfGfc_vL9xrsuLVNhGoGtfSUMwTe41/view?usp=sharing) 

