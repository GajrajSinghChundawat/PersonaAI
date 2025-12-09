from uvicorn import run
from fastapi import FastAPI
from src.routes import persona_ai_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(router=persona_ai_router)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port="8000")
