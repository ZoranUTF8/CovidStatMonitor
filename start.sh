#!/bin/bash

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
npm start