## Stage 0 Backend API - HNG12

This is a public API developed for HNG12 Stage 0 Backend task. The API provides basic information including the developer's registered email, current datetime, and the GitHub URL of the project's codebase.

## Features

Public API: Accessible via a single GET endpoint.
Dynamically Generated Data: Returns the current datetime in ISO 8601 format (UTC).
CORS Support: Handles Cross-Origin Resource Sharing (CORS).
JSON Response: All responses are in JSON format.

## Technology Stack

Framework: FastAPI
Programming Language: Python
Deployment: Railway
Dependency Management: pip

## Installation

Clone the repository: git clone https://github.com/KIIZA-TREVOUR/hng-stage0-backend.git

Install Dependencies: pip install -r requirements.txt

Run the app: uvicorn main:app --reload

Open in browser: http://127.0.0.1:8000

## API Documentation

## Endpoint

Base URL:
https://hng-stage0-backend-ae6g.onrender.com/

## GET /

GET /hire/python-developers

## Response Format

HTTP 200 OK
{
"email": "your-email@example.com",
"current_datetime": "2025-01-30T09:30:00Z",
"github_url": "https://github.com/yourusername/your-repo"
}

## Deployment

The API is deployed on https://hng-stage0-backend-ae6g.onrender.com/

## Useful Links

Hire Python Developers
Hire C# Developers
Hire Golang Developers
Hire PHP Developers
Hire Java Developers
Hire Node.js Developers
