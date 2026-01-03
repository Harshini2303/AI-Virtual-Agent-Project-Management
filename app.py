from flask import Flask, render_template, request
import json
from nlp_processor import extract_intent
from ai_engine import generate_ai_response

app = Flask(__name__)

def load_data():
    with open("project_data.json") as f:
        return json.load(f)

def save_data(data):
    with open("project_data.json", "w") as f:
        json.dump(data, f, indent=2)

project_data = load_data()

def calculate_metrics(tasks):
    if not tasks:
        return {"progress": 0, "risks": 0, "team_load": 0, "deadline": "N/A"}

    avg_progress = sum(t["progress"] for t in tasks) // len(tasks)
    risks = len([t for t in tasks if t["status"] == "Delayed"])
    team_load = min(100, avg_progress + 20)

    return {
        "progress": avg_progress,
        "risks": risks,
        "team_load": team_load,
        "deadline": "2025-01-20"
    }

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    edit_task = None
    edit_index = None

    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "project_input":
            project_data["project_name"] = request.form["project_name"]
            project_data["tasks"].append({
                "name": request.form["task_name"],
                "status": request.form["task_status"],
                "progress": int(request.form["task_progress"])
            })
            save_data(project_data)

        elif form_type == "delete_task":
            idx = int(request.form["task_index"])
            project_data["tasks"].pop(idx)
            save_data(project_data)

        elif form_type == "edit_task":
            edit_index = int(request.form["task_index"])
            edit_task = project_data["tasks"][edit_index]

        elif form_type == "update_task":
            idx = int(request.form["task_index"])
            project_data["tasks"][idx] = {
                "name": request.form["task_name"],
                "status": request.form["task_status"],
                "progress": int(request.form["task_progress"])
            }
            save_data(project_data)

        elif form_type == "agent_query":
            intent = extract_intent(request.form["query"])
            response = generate_ai_response(intent, project_data["tasks"])

    metrics = calculate_metrics(project_data["tasks"])

    return render_template(
        "index.html",
        project=project_data,
        metrics=metrics,
        response=response,
        edit_task=edit_task,
        edit_index=edit_index
    )

if __name__ == "__main__":
    app.run(debug=True)
