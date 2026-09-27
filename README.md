# FitForge AI

FitForge AI is a small fitness and nutrition calculator project.

It takes basic user details and calculates:
- BMI
- BMR
- daily calorie target
- protein, carbs and fats
- water estimate
- a simple meal plan

## Project structure

- `backend/` - FastAPI backend and calculations
- `frontend/` - HTML, CSS and JavaScript frontend
- `database/` - SQLite data

## Run the backend

pip install -r requirements.txt
uvicorn backend.main:app --reload

This is a student project made while practicing Python, FastAPI, SQLite and frontend development.