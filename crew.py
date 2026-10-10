"""Simple multi-agent workflow. Each agent has one clearly defined responsibility."""

from datetime import datetime


def manager_agent(title, description, priority):
    """Break the request into manageable work steps."""
    return [
        f"Clarify the request: {title}",
        "Collect relevant context and identify likely causes or requirements",
        "Prepare a safe, actionable response",
        "Check the response and produce a report",
    ]


def research_agent(title, description):
    """Demo research agent: organizes the user's input into known facts and unknowns."""
    return (
        f"Request reviewed: {title}. "
        f"Available context: {description}. "
        "Information still to confirm: exact environment, recent changes, and any supporting evidence. "
        "No external systems or live logs were accessed by this demo."
    )


def execution_agent(title, description, priority):
    """Create a plan, rather than taking real-world actions."""
    actions = [
        "Confirm the issue and reproduce it if possible.",
        "Gather relevant evidence and record what changed recently.",
        "Try the lowest-risk troubleshooting step first.",
        "Record the outcome and escalate if the issue remains unresolved.",
    ]
    if priority in ("High", "Critical"):
        actions.insert(0, "Notify the responsible person and follow the organization's escalation procedure.")
    actions.append("Obtain human approval before making consequential changes.")
    return "Suggested action plan:\n" + "\n".join(f"{i}. {item}" for i, item in enumerate(actions, 1))


def quality_agent(research, plan):
    """Perform simple quality checks on generated outputs."""
    checks = []
    checks.append("Request context included" if research.strip() else "Missing research context")
    checks.append("Action plan contains steps" if plan.count("\n") >= 2 else "Action plan may need more detail")
    checks.append("Human approval reminder included" if "human approval" in plan.lower() else "Add human approval safeguard")
    return "Quality review:\n" + "\n".join(f"- {check}" for check in checks)


def monitoring_agent(title, priority, steps):
    """Summarize the workflow and status."""
    return (
        "MULTI-AGENT OPS CREW REPORT\n"
        f"Task: {title}\n"
        f"Priority: {priority}\n"
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        "Workflow status: Completed (demo workflow)\n"
        f"Agents used: {len(steps)}\n\n"
        "Important limitation: this project produces recommendations using rule-based demo logic. "
        "It does not inspect real infrastructure, send messages, or execute changes.\n\n"
        "Next step: a human operator should review the plan, validate facts, and approve any real action."
    )


def run_crew(title, description, priority):
    """Coordinate the agents in a fixed, understandable order."""
    tasks = manager_agent(title, description, priority)
    research = research_agent(title, description)
    plan = execution_agent(title, description, priority)
    quality = quality_agent(research, plan)

    steps = [
        {"agent": "1. Manager Agent", "output": "Task broken into steps:\n" + "\n".join(f"- {t}" for t in tasks)},
        {"agent": "2. Research Agent", "output": research},
        {"agent": "3. Execution Agent", "output": plan},
        {"agent": "4. Quality Agent", "output": quality},
    ]
    report = monitoring_agent(title, priority, steps)
    steps.append({"agent": "5. Monitoring Agent", "output": report})
    return {"steps": steps, "report": report}
