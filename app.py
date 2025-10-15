from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
# from transformers import pipeline
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI(title="Smart Task Planner 🚀")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")
# planner = pipeline("text-generation", model="gpt2")

class GoalRequest(BaseModel):
    goal: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/generate_plan")
# async def generate_plan(request: GoalRequest):
#     goal = request.goal
    

#     prompt = f"""
#     You are a professional project planner.
#     Break this goal into actionable tasks with dependencies and timelines.
#     Format output as JSON with fields:
#     - task (string)
#     - depends_on (list)
#     - duration_days (integer)

#     Example output:
#     [
#       {{ "task": "Research", "depends_on": [], "duration_days": 1 }},
#       {{ "task": "Design", "depends_on": ["Research"], "duration_days": 2 }}
#     ]

#     Goal: {goal}
#     """

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7
#         )
#         plan = response.choices[0].message.content
#         return JSONResponse({"goal": goal, "plan": plan})

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)


@app.post("/generate_plan")
async def generate_plan(request: GoalRequest):
    goal = request.goal
    prompt = f"Break down this goal into actionable tasks: {goal}"
    response = planner(prompt, max_length=200)
    return JSONResponse({"goal": goal, "plan": response[0]['generated_text']})


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")  # Or hardcode for testing

@app.post("/generate_plan")
async def generate_plan(request: Request):
    try:
        payload = await request.json()
        user_prompt = payload.get("prompt", "Create a one-year academic plan for a CSE student.")

        # Use the new OpenAI client structure
        client = openai.OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful academic planner."},
                {"role": "user", "content": user_prompt}
            ]
        )

        plan_text = response.choices[0].message.content.strip()

        return JSONResponse(content={"plan": plan_text})

    except Exception as e:
        print(f"Error in /generate_plan: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
