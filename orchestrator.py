import json
from datetime import datetime

# --- Agents ---
def iot_agent(task):
    print(f"[IoT Agent] Executing: {task}")

def finance_agent(task):
    print(f"[Finance Agent] Preparing to execute: {task}")
    approval = input("⚠️ Approve this sensitive task? (y/n): ")
    if approval.lower() == "y":
        print(f"[Finance Agent] ✅ Approved and executed: {task}")
    else:
        print(f"[Finance Agent] ❌ Rejected by user")

def health_agent(task):
    print(f"[Health Agent] Reminder: {task}")

# --- Orchestrator ---
def orchestrator():
    with open("tasks.json") as f:
        tasks = json.load(f)

    for t in tasks:
        task_time = datetime.fromisoformat(t["time"])
        task = t["task"]
        agent = t["agent"]

        print(f"\n🔔 Task: {task} | Agent: {agent} | Time: {task_time}")

        if agent == "iot":
            iot_agent(task)
        elif agent == "finance":
            finance_agent(task)
        elif agent == "health":
            health_agent(task)
        else:
            print(f"[Orchestrator] Unknown agent for task: {task}")

if __name__ == "__main__":
    orchestrator()
