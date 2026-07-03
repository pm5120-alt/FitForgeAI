async function calculate() {

    try {

        const data = {
            name: document.getElementById("name").value.trim(),
            age: parseInt(document.getElementById("age").value),
            gender: document.getElementById("gender").value,
            height: parseFloat(document.getElementById("height").value),
            weight: parseFloat(document.getElementById("weight").value),
            activity: parseFloat(document.getElementById("activity").value),
            goal: document.getElementById("goal").value
        };

        // Validation
        if (
            !data.name ||
            isNaN(data.age) ||
            isNaN(data.height) ||
            isNaN(data.weight)
        ) {
            alert("Please fill all the fields.");
            return;
        }

        const response = await fetch("http://127.0.0.1:8000/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Server Error: " + response.status);
        }

        const result = await response.json();

        console.log(result);

        // Update Result Cards
        document.getElementById("bmi").textContent = result.result.bmi;
        document.getElementById("bmiStatus").textContent = result.result.bmi_status;
        document.getElementById("calories").textContent = result.result.calories + " kcal";
        document.getElementById("protein").textContent = result.result.protein + " g";
        document.getElementById("carbs").textContent = result.result.carbs + " g";
        document.getElementById("fats").textContent = result.result.fats + " g";
        document.getElementById("water").textContent = result.result.water + " L";

        // Meal Plan
        let mealHTML = "";

        for (const meal in result.meal_plan) {

            mealHTML += `<h3>${meal}</h3><ul>`;

            result.meal_plan[meal].forEach(food => {
                mealHTML += `<li>${food}</li>`;
            });

            mealHTML += `</ul>`;
        }

        document.getElementById("mealPlan").innerHTML = mealHTML;

        // Workout Plan (only if backend sends one)
        if (result.workout_plan) {

            let workoutHTML = "";

            for (const section in result.workout_plan) {

                workoutHTML += `<h3>${section}</h3><ul>`;

                result.workout_plan[section].forEach(exercise => {
                    workoutHTML += `<li>${exercise}</li>`;
                });

                workoutHTML += `</ul>`;
            }

            document.getElementById("workoutPlan").innerHTML = workoutHTML;

        } else {

            document.getElementById("workoutPlan").innerHTML =
                "<p>No workout plan available yet.</p>";

        }

    } catch (error) {

        console.error(error);

        alert("Error: " + error.message);

    }

}document.getElementById("analyzeBtn").addEventListener("click", calculate);