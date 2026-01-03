def generate_ai_response(intent, tasks):
    if not tasks:
        return "No project data available. Please add tasks."

    delayed = [t["name"] for t in tasks if t["status"] == "Delayed"]
    low_progress = [t["name"] for t in tasks if t["progress"] < 50]

    if intent == "CHECK_DELAY":
        return (
            f"Delayed tasks: {', '.join(delayed)}\n"
            "Would you like to reassign resources?"
            if delayed else "No delayed tasks detected."
        )

    if intent == "CHECK_PROGRESS":
        response = "Project Progress Summary:\n"
        for t in tasks:
            response += f"- {t['name']}: {t['progress']}%\n"
        return response

    if intent == "CHECK_RISK":
        return (
            f"Potential risks found in tasks: {', '.join(low_progress)}\n"
            "Are there any blockers?"
            if low_progress else "No major risks identified."
        )

    if intent == "RECOMMEND":
        return (
            "AI Recommendations:\n"
            "- Prioritize delayed tasks\n"
            "- Allocate additional resources\n"
            "- Review deadlines\n"
            "Is the deadline flexible?"
        )

    return "I can help with progress, risks, delays, or recommendations."
