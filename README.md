# 🧠 Smart Task Planner

Smart Task Planner is an intelligent task management API built with **FastAPI** and integrated with the **OpenAI API** to help users organize, prioritize, and manage tasks efficiently. 
The project aims to automate task recommendations, deadlines, and productivity tips using AI.

## Execution Steps

### 1.	Clone the repository
git clone https://github.com/NVHarikaVIT/Smart-Task-Planner.git

cd Smart_Task_Planner

### 2. ✅ Create Virtual Environment
python -m venv venv

source venv/bin/activate        ### For Linux/macOS

venv\Scripts\activate           # For Windows

### 3. ✅ Install Dependencies
pip install fastapi pydantic jinja2 python-dotenv uvicorn openai==0.28.1

### 4. ✅ Set Up Environment Variables
Create a .env file in the root with the following:

OPENAI_API_KEY=your-openai-api-key

### 5. ▶️ Run the API Server

uvicorn file:app --reload

---

## 🚀 Features

- ✅ Add, update, and delete tasks
- 🧠 AI-based task prioritization (via OpenAI API)
- 🔐 Secure environment variable handling
- 📦 RESTful API built using FastAPI

---

---
## 🛠️ Tech Stack

### FastAPI → creates the web API

### Uvicorn → runs the FastAPI app

### OpenAI → talks to ChatGPT models

### Pydantic → handles request/response data

### dotenv → loads your secret API key safely

| Layer          | Technology              |
|----------------|--------------------------|
| **Backend**     | FastAPI (Python 3.10+)   |
| **AI Integration** | OpenAI API (GPT-4)       |
| **Frontend**    | HTML, CSS, JavaScript |
| **Auth (optional)** | API key |
| **Version Control**       | Uvicorn, Pydantic, GitHub |

---

<details> 
  <summary>
    <h2> 📁 <b> Project Structure </b> </h2>
  </summary>
Smart_Task_Planner/
  
├── templates/

│ └── index.html

├── .env # Secret keys and configs

├── .gitignore

├── README.md

└── file.py # FastAPI entry point
</details>


## 📌 GitHub Workflow Followed
### Step 1: Initialize Git
git init

### Step 2: Add files and commit
git add .

git commit -m "Initial commit"

### Step 3: Connect to GitHub
git remote add origin https://github.com/NVHarikaVIT/Smart-Task-Planner.git

### Step 4: Protect secrets
echo ".env" >> .gitignore

git rm --cached .env

git commit -m "Removed .env and added to .gitignore"

### Step 5: Push securely
git push -u origin main

- If secrets were accidentally pushed:

git filter-repo --path .env --invert-paths

git push origin main --force


### 📬 Contact

### Author: Harika Nune
📧 Email: nunevenkataharikaic@gmail.com
🌐 GitHub: https://github.com/NVHarikaVIT
