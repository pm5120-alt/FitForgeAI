def calculate_fitness(data):
    name = data["name"]
    age = data["age"]
    gender = data["gender"]
    height = data["height"]
    weight = data["weight"]
    activity = data["activity"]
    goal = data["goal"]

    height_m = height / 100
    bmi = round(weight / (height_m * height_m), 1)

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Healthy"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    calories = bmr * activity

    if goal == "Lose Fat":
        calories -= 500
    elif goal == "Build Muscle":
        calories += 300
    elif goal == "Bodybuilder":
        calories += 600
    elif goal == "Lean Athlete":
        calories += 150

    calories = int(calories)

    if goal == "Bodybuilder":
        protein = weight * 2.2
    elif goal in ("Lose Fat", "Build Muscle"):
        protein = weight * 2
    else:
        protein = weight * 1.6

    protein = round(protein)

    fats = round((calories * 0.25) / 9)

    carbs = round(
        (calories - (protein * 4 + fats * 9)) / 4
    )

    water = round(weight * 0.035, 1)

    return {
        "name": name,
        "bmi": bmi,
        "bmi_status": bmi_status,
        "bmr": round(bmr),
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats,
        "water": water
    }
