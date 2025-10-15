# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from dotenv import load_dotenv
# from pydantic import BaseModel
# import openai
# import os

# load_dotenv()
# app = FastAPI()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# # Allow frontend connections
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# templates = Jinja2Templates(directory="templates")
# # # ✅ Correct OpenAI client usage
# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Goal or Task input
# class GoalInput(BaseModel):
#     goal: str


# @app.get("/", response_class=HTMLResponse)
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request,"message": "Welcome to AI Powered Smart Task Planner 🚀"})

# @app.post("/generate_plan")
# async def generate_plan(request: GoalInput):
#     goal = request.goal
#     if not goal:
#         return {"error": "No goal provided"}

#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are an AI Task Planner."},
#             {"role": "user", "content": f"Break down this goal into actionable steps with timelines: {goal}"}
#         ]
#     )
#     return {"plan": response.choices[0].message.content}



from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import openai
import os

load_dotenv()

app = FastAPI()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Template directory
templates = Jinja2Templates(directory="templates")

# Request model
class GoalInput(BaseModel):
    goal: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to AI Powered Smart Task Planner 🚀"})

@app.post("/generate_plan")
async def generate_plan(request: GoalInput):
    goal = request.goal

    if not goal:
        return {"error": "No goal provided"}

    try:
        # ✅ Use this syntax for OpenAI Python v1.10.0
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # ✅ Use a valid model
            messages=[
                {"role": "system", "content": "You are an AI Task Planner."},
                {"role": "user", "content": f"Break down this goal into actionable steps with timelines: {goal}"}
            ]
        )
        return {"plan": response['choices'][0]['message']['content']}

    except Exception as e:
        return {"error": str(e)}
