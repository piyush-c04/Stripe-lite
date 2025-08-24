# main.py
from fastapi import FastAPI, Depends, HTTPException, status  # ✅ Fixed: HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ Fixed: middleware.cors
import uvicorn 
import models
from database import engine, Base, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multi-Tenant Billing API",
    description="A billing and subscription management system",
    version="1.0.0")

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

@app.get('/greet/{name}')
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}

from routes.tenants import router as tenant_router
app.include_router(tenant_router,tags=["Tenants"])

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Changed to port 8000 (FastAPI default)