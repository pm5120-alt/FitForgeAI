from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from calculation import calculate_fitness
from database import save_user
from mealplanner import get_meal_plan


app = FastAPI(title="FitForge AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    activity: float
    goal: str


@app.get("/")
def home():
    return {"message": "Welcome to FitForge AI Backend"}


@app.post("/calculate")
def calculate(user: User):
    user_data = user.model_dump()
    result = calculate_fitness(user_data)
    meal_plan = get_meal_plan(user.goal)

    save_user_data = {
        **user_data,
        **result
    }

    save_user(save_user_data)

    return {
        "success": True,
        "result": result,
        "meal_plan": meal_plan
    }


@app.get("/health")
def health():
    return {"status": "Server Running"}
