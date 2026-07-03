def get_meal_plan(goal):

    meal_plans = {

        "Build Muscle": {

            "Breakfast": [
                "4 Eggs",
                "100g Oats",
                "1 Banana",
                "250ml Milk"
            ],

            "Lunch": [
                "200g Chicken Breast",
                "150g Rice",
                "Mixed Salad"
            ],

            "Snack": [
                "Peanut Butter Sandwich",
                "Greek Yogurt"
            ],

            "Dinner": [
                "200g Chicken",
                "2 Chapatis",
                "Vegetables"
            ]

        },

        "Bodybuilder": {

            "Breakfast": [
                "6 Eggs",
                "150g Oats",
                "Banana",
                "Milk"
            ],

            "Lunch": [
                "250g Chicken",
                "200g Rice",
                "Salad"
            ],

            "Snack": [
                "Protein Shake",
                "Almonds",
                "Apple"
            ],

            "Dinner": [
                "250g Fish",
                "Sweet Potato",
                "Broccoli"
            ]

        },

        "Lose Fat": {

            "Breakfast": [
                "Oats",
                "Apple",
                "Green Tea"
            ],

            "Lunch": [
                "150g Grilled Chicken",
                "Salad"
            ],

            "Snack": [
                "Handful of Almonds"
            ],

            "Dinner": [
                "Paneer",
                "Vegetables"
            ]

        },

        "Maintain": {

            "Breakfast": [
                "Oats",
                "Eggs",
                "Milk"
            ],

            "Lunch": [
                "Rice",
                "Dal",
                "Chicken"
            ],

            "Snack": [
                "Fruit"
            ],

            "Dinner": [
                "Chapati",
                "Paneer",
                "Vegetables"
            ]

        },

        "Lean Athlete": {

            "Breakfast": [
                "Eggs",
                "Oats",
                "Banana"
            ],

            "Lunch": [
                "Chicken",
                "Rice",
                "Vegetables"
            ],

            "Snack": [
                "Greek Yogurt"
            ],

            "Dinner": [
                "Fish",
                "Sweet Potato"
            ]

        }

    }

    return meal_plans.get(goal, meal_plans["Maintain"])