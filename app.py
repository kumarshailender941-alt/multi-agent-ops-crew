import streamlit as st
import pandas as pd
from datetime import datetime
from crew import run_crew

st.set_page_config(page_title="Multi-Agent Ops Crew", page_icon="🤖", layout="wide")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🤖 Multi-Agent Ops Crew")
st.caption("A beginner-friendly multi-agent operations workflow demo")

with st.sidebar:
    st.header("About the project")
    st.write("Submit a task and let five specialized agents process it.")
    st.info("Demo mode: agents use transparent rule-based logic. No paid API key is required.")
    st.write("For real-world actions, require human approval before execution.")

col1, col2, col3 = st.columns(3)
col1.metric("Tasks submitted", len(st.session_state.tasks))
col2.metric("Completed", sum(1 for t in st.session_state.tasks if t["status"] == "Completed"))
col3.metric("Agents", 5)

st.subheader("Create an operational task")
with st.form("task_form"):
    title = st.text_input("Task title", placeholder="Example: Investigate slow lab computers")
    description = st.text_area("Task details", placeholder="Describe the issue or work that needs to be done.")
    priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"], index=1)
    submitted = st.form_submit_button("Run Ops Crew", type="primary")

if submitted:
    if not title.strip() or not description.strip():
        st.error("Please enter both a task title and task details.")
    else:
        result = run_crew(title.strip(), description.strip(), priority)
        task = {
            "id": len(st.session_state.tasks) + 1,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "status": "Completed",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "result": result,
        }
        st.session_state.tasks.insert(0, task)
        st.success("The agents have completed their demo workflow.")
        st.rerun()

st.divider()
st.subheader("Task history")
if not st.session_state.tasks:
    st.write("No tasks yet. Try: “Prepare a plan to fix a projector that is not working.”")
else:
    summary = pd.DataFrame([{
        "ID": t["id"],
        "Title": t["title"],
        "Priority": t["priority"],
        "Status": t["status"],
        "Created": t["created_at"]
    } for t in st.session_state.tasks])
    st.dataframe(summary, use_container_width=True, hide_index=True)

    for task in st.session_state.tasks:
        with st.expander(f'#{task["id"]} — {task["title"]} ({task["priority"]})'):
            st.write("**Request:**", task["description"])
            st.write("**Final status:**", task["status"])
            for step in task["result"]["steps"]:
                st.markdown(f'### {step["agent"]}')
                st.write(step["output"])
            st.markdown("### Final operations report")
            st.write(task["result"]["report"])
            st.download_button(
                "Download report",
                data=task["result"]["report"],
                file_name=f'ops_report_{task["id"]}.txt',
                mime="text/plain",
                key=f'download_{task["id"]}'
            )
