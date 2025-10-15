# 🧠 Smart Task Planner

Smart Task Planner is an intelligent task management API built with **FastAPI** and integrated with the **OpenAI API** to help users organize, prioritize, and manage tasks efficiently. 
The project aims to automate task recommendations, deadlines, and productivity tips using AI.

---

## 🚀 Features

- ✅ Add, update, and delete tasks
- 🧠 AI-based task prioritization (via OpenAI API)
- 🕒 Due date and time parsing
- 🔄 Task completion tracking
- 🔐 Secure environment variable handling
- 📦 RESTful API built using FastAPI

---

## 🛠️ Tech Stack

| Layer          | Technology              |
|----------------|--------------------------|
| **Backend**     | FastAPI (Python 3.10+)   |
| **AI Integration** | OpenAI API (GPT-4)       |
| **Database**    | JSON / SQLite (optional) |
| **Auth (optional)** | API key / token-based  |
| **Other**       | Uvicorn, Pydantic, GitHub |

---

## 📁 Project Structure

Smart_Task_Planner/
│
├── templates/
│ ├── index.html 
├── .env # Secret keys and configs
├── .gitignore
├── README.md
└── file.py # FastAPI entry point

# 1. ✅ Create Virtual Environment
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows

# 2. ✅ Install Dependencies
pip install fastapi openai pydantic jinja2 python-dotenv

# 3. ✅ Set Up Environment Variables
Create a .env file in the root with the following:

OPENAI_API_KEY=your-openai-api-key

# 4. ▶️ Run the API Server
uvicorn app.main:app --reload

## 📌 GitHub Workflow Followed
# Step 1: Initialize Git
git init

# Step 2: Add files and commit
git add .
git commit -m "Initial commit"

# Step 3: Connect to GitHub
git remote add origin https://github.com/NVHarikaVIT/Smart-Task-Planner.git

# Step 4: Protect secrets
echo ".env" >> .gitignore
git rm --cached .env
git commit -m "Removed .env and added to .gitignore"

# Step 5: Push securely
git push -u origin main

- If secrets were accidentally pushed:

git filter-repo --path .env --invert-paths
git push origin main --force


# 📬 Contact

# Author: Harika Nune
📧 Email: nunevenkataharikaic@gmail.com
🌐 GitHub: https://github.com/NVHarikaVIT
