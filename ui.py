import streamlit as st
import requests

st.set_page_config(page_title="📝 To-Do App", layout="centered")
API_URL  = "http://fastapi:8000"


st.title("📝 To-Do List App")
st.markdown("---")

# 🎯 Add New Task
with st.expander("➕ Add a New Task", expanded=True):
    new_title = st.text_input("Task Title", placeholder="Enter task title")
    new_desc = st.text_area("Task Description", placeholder="Enter task description")

    if st.button("Add Task"):
        all_tasks = requests.get(f"{API_URL}/tasks/").json()
        new_task = {
            "id": len(all_tasks) + 1,
            "title": new_title,
            "description": new_desc,
            "completed": False
        }
        res = requests.post(f"{API_URL}/tasks/", json=new_task)
        if res.status_code == 200:
            st.success("Task added!")
            st.rerun()
        else:
            st.error("Failed to add task.")

st.markdown("---")

# 📋 View All Tasks
tasks = requests.get(f"{API_URL}/tasks/").json()
incomplete_tasks = [t for t in tasks if not t["completed"]]
complete_tasks = [t for t in tasks if t["completed"]]

def render_task(task, index):
    st.markdown(f"### {task['title']}")
    st.write(task["description"])

    new_title = st.text_input("Edit Title", value=task["title"], key=f"title_{index}")
    new_desc = st.text_area("Edit Description", value=task["description"], key=f"desc_{index}")
    new_completed = st.checkbox("Completed", value=task["completed"], key=f"check_{index}")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("💾 Update", key=f"update_{index}"):
            updated_task = {
                "id": task["id"],
                "title": new_title,
                "description": new_desc,
                "completed": new_completed
            }
            res = requests.put(f"{API_URL}/tasks/{task['id']}", json=updated_task)
            if res.status_code == 200:
                st.success("Updated!")
                st.experimental_rerun()
            else:
                st.error("Update failed.")
    with col2:
        if st.button("🗑️ Delete", key=f"delete_{index}"):
            res = requests.delete(f"{API_URL}/tasks/{task['id']}")
            if res.status_code == 200:
                st.success("Deleted!")
                st.experimental_rerun()
            else:
                st.error("Delete failed.")

    st.markdown("---")

# 🟡 Incomplete Tasks
if incomplete_tasks:
    st.subheader("📌 Incomplete Tasks")
    for i, task in enumerate(incomplete_tasks):
        with st.container():
            render_task(task, i)

# ✅ Completed Tasks
if complete_tasks:
    st.subheader("✅ Completed Tasks")
    for i, task in enumerate(complete_tasks):
        with st.container():
            render_task(task, i + len(incomplete_tasks))
