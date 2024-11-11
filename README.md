<<<<<<< HEAD
# Planet AI Web Application
=======

This web application allow users to interact with their documents like pdfs by asking questions and getting respones related to their questions. 
>>>>>>> ce3353a98c121de81f789cc555593af5b76c5a1b

## Overview

The Planet AI web application empowers users to interact with their PDF documents by asking questions and receiving relevant answers. This innovative solution leverages advanced natural language processing techniques to enhance document accessibility and understanding.

## Key Features

- **PDF Uploading**: Seamlessly upload PDF files for interaction.
- **Interactive Q&A**: Pose questions related to the content of your PDFs and receive instant responses.

## Architecture

The project is organized into several components, each serving a specific purpose:

- **Frontend (`planet`)**: Developed using **React.js**, providing a dynamic and responsive user interface.
- **Backend (`backend`)**: Built with **FastAPI**, ensuring high performance and rapid response times.
- **NLP Processing**: Utilizes **LLamaIndex** for sophisticated natural language processing capabilities.
- **Storage**: Employs the local file system for efficient PDF storage.

### Technologies for Scalable Architecture

- **React.js**: Its component-based architecture promotes reusability and modularity, making the codebase easier to maintain and scale.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python, built on Starlette and Pydantic.
- **LLamaIndex**: Offers advanced natural language processing tools to facilitate the development of intelligent applications that comprehend and process human language.

## Setup Guide

Follow these steps to set up the application locally:

1. **Install Dependencies**:

<<<<<<< HEAD
   - Navigate to the `planet` directory and run:
     ```bash
     npm install
     ```
   - Then, navigate to the `backend` directory and run:
     ```bash
     pip install -r requirements.txt
     ```
=======
## Demo Video 
[Watch the demo video](https://drive.google.com/file/d/1AXV1_8Bwvm18hIjAwnK8ljZYt9lfqADi/view?usp=drive_link) 
>>>>>>> ce3353a98c121de81f789cc555593af5b76c5a1b

2. **Configure Environment Variables**:

   - Create a `.env` file in the `backend` directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Start the Services**:
   - In the `planet` directory, run:
     ```bash
     npm start
     ```
   - In the `backend` directory, run:
     ```bash
     uvicorn main:app --reload
     ```

At this point, the following services will be operational:

| Service  | Port  |
| -------- | ----- |
| Frontend | :3000 |
| Backend  | :8000 |

## Demo Video

For a visual demonstration of the application, please watch the following video:  
[Watch the demo video](https://drive.google.com/file/d/1AXV1_8Bwvm18hIjAwnK8ljZYt9lfqADi/view?usp=drive_link)
