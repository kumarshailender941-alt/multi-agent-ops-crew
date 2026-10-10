# Multi-Agent Ops Crew

A beginner-friendly college project demonstrating how specialized agents can collaborate to process an operations request.

## Features
- Streamlit web dashboard
- Five agents: Manager, Research, Execution, Quality, Monitoring
- Task history during the current session
- Downloadable report
- Priority-aware recommendations
- Human approval reminder for consequential actions

## Requirements
- Python 3.10 or newer
- Internet connection for installing Python packages (the app itself does not need an AI API)

## Windows setup (VS Code / PowerShell)

1. Extract the ZIP file.
2. Open the extracted `multi_agent_ops_crew` folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

5. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run this command for the current terminal only, then activate again:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

6. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the app:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Demo input
Title: Investigate slow lab computers

Details: Several computers in the lab are slow after startup. Prepare a safe troubleshooting plan and list information that should be collected.

Priority: High

## Architecture

User -> Streamlit Dashboard -> Manager Agent -> Research Agent -> Execution Agent -> Quality Agent -> Monitoring Agent -> Report

The demo uses transparent rule-based logic and does not call an LLM or perform live system operations. This keeps it easy to run and explain. An optional future enhancement is connecting an LLM to selected agents.

## Limitations
- Task history is stored in Streamlit session state and may reset when the session restarts.
- Research is based on the user-provided description; no external sources or real logs are inspected.
- Execution Agent proposes steps only; it does not perform real-world actions.
- Quality checks are simple rule-based checks, not a guarantee of correctness.

## Future enhancements
- SQLite database for persistent task history
- LLM integration for richer agent reasoning
- Login and roles
- Human approval queue
- Audit logs and real integrations with ticketing tools
