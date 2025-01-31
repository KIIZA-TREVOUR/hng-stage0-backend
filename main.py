from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define the root endpoint
@app.get("/")
async def get_info():
    # Return data in JSON
    return {
        "email": "kiizatrevour@gmail.com",
        "current_datetime": datetime.now().isoformat() + "Z",
        "github_url": "https://github.com/KIIZA-TREVOUR/hng-stage0-backend",
    }