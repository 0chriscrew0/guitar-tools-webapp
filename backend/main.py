from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chords, practice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chords.router, prefix="/chords")
app.include_router(practice.router, prefix="/practice")

@app.get("/")
def read_root():
    return {"message": "Guitar Tools API is live!"}