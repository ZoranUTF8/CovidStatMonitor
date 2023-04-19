#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi


# Change directory to the backend folder
cd backend

# Install backend dependencies
pip install -r requirements.txt

# Start backend server
uvicorn main:app --reload &

# Change directory to the frontend folder
cd ../frontend

# Install frontend dependencies
npm install

# Start frontend server
npm run serve