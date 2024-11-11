from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from pydantic import BaseModel

# Initiating an app to handle routes
app = FastAPI()

# Load environment variables
load_dotenv()

# Setting OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Setting origins for CORS
origins = [
    "http://localhost:3000"
]

# Setting CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

# Directory for persistent storage
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # Loading the documents data from uploaded_files folder
    documents = SimpleDirectoryReader("uploaded_files").load_data()
    # Indexing the documents data
    index = VectorStoreIndex.from_documents(documents)
    # Storing the index for later use
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # Loading the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Setting a query engine to query through indexes
query_engine = index.as_query_engine()

# Ensure the uploaded_files directory exists
if not os.path.exists("uploaded_files"):
    os.makedirs("uploaded_files")

# PDF upload route
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        # Read contents of the file and store it in uploaded_files folder
        contents = await file.read()
        with open(f'uploaded_files/{file.filename}', 'wb') as f:
            f.write(contents)
        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

# Model for query
class Query(BaseModel):
    text: str

# Post route for getting queries from frontend
@app.post("/messages")
async def query(q: Query):
    if not q.text:
        raise HTTPException(status_code=422, detail="Message text cannot be empty")
    
    # Getting response from query engine related to the query 
    response = query_engine.query(q.text)
    return {"response": response}