from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI app
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["GET"],  # Allows only GET requests
    allow_headers=["*"],  # Allows all headers
)

# Define the API endpoint
@app.get("/api")
def get_info():
    # Replace with your registered email
    email = "kiizatrevour@gmail.com"
    
    # Get current datetime in ISO 8601 format (UTC)
    current_datetime = datetime.utcnow().isoformat() + "Z"
    
    # Replace with your GitHub repository URL
    github_url = "https://github.com/yourusername/your-repo"
    
    # Return JSON response
    return {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }