from typing import Union

from fastapi import FastAPI,File,UploadFile
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

# inititating an app to handle routes
app = FastAPI()

# to load evnironment variables
load_dotenv()

# setting OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# setting origins for cors
origins=[
    "http://localhost:3000"
]

# setting cors 
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET","POST"],
    allow_headers =["*"]
)

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # loading the documents data from uploaded_files folder
    documents = SimpleDirectoryReader("uploaded_files").load_data()
    # indexing the documents data
    index = VectorStoreIndex.from_documents(documents)
    # storing the index for later use
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # loading the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# setting a query engine to query through indexes
query_engine = index.as_query_engine()

#  pdf upload route
@app.post("/upload")
async def upload(file:UploadFile = File(...)):
    try:
        # contents of the file are read and file is stored in uploaded_files folder
        contents = await file.read()
        with open(f'uploaded_files/{file.filename}','wb') as f:
            f.write(contents)
        return JSONResponse(content={"message":"File uploaded Successfully"})
    except Exception as e:
        return JSONResponse(content={"message":str(e)},status_code=500)

# model for query
class Query(BaseModel):
    text:str

# post route for getting queries from frontend
@app.post("/messages")
async def query(q:Query):
    if not q.text:
        raise HTTPException(status_code=422, detail="Message text cannot be empty")
    print(q)
    # getting response from query engine related to the query 
    response = query_engine.query(q.text)
    return {"response":response}
