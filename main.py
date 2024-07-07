from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .pdfapp.routes import pdf


app = FastAPI(title="centPDF", description="A comprehensive API for manipulating and extracting data from PDF files.")

origins = [
    "https://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins = ["*"],
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(pdf)

@app.get("/")
async def home():
    return {"message": "Welcome to centPDF"}
