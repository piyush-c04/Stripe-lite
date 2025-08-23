# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
from typing import List

# Import your modules (make sure these files exist)
# import models 
# import schemas
import uvicorn

app = FastAPI()

# Add CORS middleware if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use @app.get decorator (not app.get)
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Changed to port 8000 (FastAPI default)