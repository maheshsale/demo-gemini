from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-3.8-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Allow specified domains
    allow_credentials=True,          # Allow cookies and headers
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all headers
)

class PromptRequest(BaseModel):
    prompt: str

@app.get('/')
def home():
    return {'message': 'FastAPI Gemini API Backend Running'}

@app.post('/generate')
def generate_text(request: PromptRequest):
    response = model.generate_content(request.prompt)
    return {'response': response.text}

