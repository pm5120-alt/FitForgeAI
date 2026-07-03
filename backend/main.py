from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from calculation import calculate_fitness
from mealplanner import get_meal_plan
from database import save_user

app = FastAPI(title="FitForge AI")


# -----------------------------
# Enable CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# User Model
# -----------------------------

class User(BaseModel):

    name: str
    age: int
    gender: str
    height: float
    weight: float
    activity: float
    goal: str


# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():

    return {

        "message": "Welcome to FitForge AI Backend 🚀"

    }


# -----------------------------
# Calculate Route
# -----------------------------

@app.post("/calculate")
def calculate(user: User):

    user_data = user.dict()

    result = calculate_fitness(user_data)

    meal = get_meal_plan(user.goal)

    save_data = {

        **user_data,

        **result

    }

    save_user(save_data)

    return {

        "success": True,

        "result": result,

        "meal_plan": meal

    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health():

    return {

        "status": "Server Running"

    }