from transformers import pipeline

planner = pipeline("text-generation", model="gpt2")

@app.post("/generate_plan")
async def generate_plan(request: GoalRequest):
    goal = request.goal
    prompt = f"Break down this goal into actionable tasks: {goal}"
    response = planner(prompt, max_length=200)
    return JSONResponse({"goal": goal, "plan": response[0]['generated_text']})
