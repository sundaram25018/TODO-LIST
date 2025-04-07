# ✅ To-Do App with FastAPI + Streamlit + SQLite

A simple full-stack To-Do list app built with:

- ⚙️ **FastAPI** – for the backend API
- 🖥️ **Streamlit** – for the frontend UI
- 💾 **SQLite** – as the database
- ☁️ **Render** and **Streamlit Cloud** – for deployment

---

## 🚀 Features

- Add, view, update, and delete tasks
- Mark tasks as completed
- Easy-to-use interface with real-time updates
- Deployed backend (FastAPI) and frontend (Streamlit)

---

## 🏗️ Project Structure

# 📦 my-todo-app/ 
├── main.py
FastAPI backend ├── ui.py 
Streamlit frontend ├── task.db 
SQLite database (optional to include) ├── models.py 
SQLAlchemy models ├── database.py 
DB session & engine ├── requirements.txt 
Python dependencies


---

## 🔧 Requirements

- Python 3.8+
- `uvicorn`, `fastapi`, `sqlalchemy`, `pydantic`, `streamlit`, `requests`

Install everything:

```bash
pip install -r requirements.txt
```
# 🧠 How It Works
✅ FastAPI Backend (main.py)
Provides RESTful endpoints:

GET /tasks/ – list tasks

POST /tasks/ – add task

PUT /tasks/{id} – update task

DELETE /tasks/{id} – delete task

Connects to task.db using SQLAlchemy

Run locally:

```base
uvicorn main:app --reload
```
Visit docs: http://localhost:8000/docs


# 🖼️ Streamlit Frontend (ui.py)
Simple interface with checkboxes, forms, and buttons

Communicates with FastAPI using requests

Run locally:

```bash
streamlit run ui.py
```
⚠️ Set the API_URL at the top of ui.py to your local or deployed FastAPI URL.


# ☁️ Deployment
1. Deploy FastAPI on Render Create a new Web Service

- Use start command:
- uvicorn main:app --host 0.0.0.0 --port 10000

# Add a requirements.txt

Optional: add env vars like DATABASE_URL=sqlite:///./task.db

2. Deploy Streamlit on Streamlit Cloud
Point to your repo and ui.py

Make sure API_URL in ui.py points to your FastAPI Render URL
