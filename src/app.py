import json

# Load tasks from file
with open("data/tasks.json", "r") as file:
    tasks = json.load(file)

print("📋 Project Tasks:\n")

for task in tasks:
    print(f"Task: {task['task']}")
    print(f"Status: {task['status']}")
    print(f"Priority: {task['priority']}")
    print(f"Deadline: {task['deadline']}")
    print("-" * 30)
