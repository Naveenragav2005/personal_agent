Personal Life Orchestrator

A prototype multi-agent system that automates a human’s day-to-day tasks by using a calendar (simulated via JSON) as the central orchestrator.
Each task is assigned to a specialized agent (IoT, Finance, Health, etc.) which decides how to execute it.

The system supports automation for low-sensitivity tasks and requests human approval for high-sensitivity tasks (e.g., financial transactions).

🎯 Purpose

Build an AI-driven daily life assistant that can orchestrate multiple tasks from a planner/calendar.

Explore multi-agent systems for real-world personal automation.

Ensure privacy & security by requiring human intervention for sensitive actions.

Lay the groundwork for a research prototype that can later connect to IoT devices, APIs, or cloud services.

⚙️ Features

✅ Calendar as Orchestrator → Reads tasks and their scheduled times.

✅ Agents → Specialized agents for different domains:

IoT Agent → Simulates smart devices (heater, coffee machine).

Finance Agent → Handles sensitive tasks like bill payments (requires approval).

Health Agent → Reminders for exercise, medicine, hydration.

✅ Human-in-the-loop → Sensitive tasks are flagged and require confirmation.

✅ Extensible Design → Easy to add more agents (shopping, travel, communication).

🛠️ Tech Stack

Language → Python 3.9+

Data Source → Local tasks.json (later can connect to Google Calendar API)

Agents → Implemented as Python functions (can be expanded into services)

Version Control → Git + GitHub

(Future Work) IoT (MQTT, Raspberry Pi), APIs (Uber, Gmail, Payment Gateways), Multi-Agent Frameworks (LangChain, AutoGen)

📂 Project Structure
personal-life-orchestrator/
│
├── orchestrator.py     # Main orchestrator script
├── tasks.json          # Example daily tasks (simulated calendar)
└── README.md           # Documentation

▶️ Usage
1. Clone Repo
git clone https://github.com/<your-username>/personal-life-orchestrator.git
cd personal-life-orchestrator

2. Run Orchestrator
python orchestrator.py

3. Example Run
🔔 Task: Wake up and turn on heater | Agent: iot | Time: 2025-09-08 06:00:00
[IoT Agent] Executing: Wake up and turn on heater

🔔 Task: Pay electricity bill | Agent: finance | Time: 2025-09-08 10:00:00
[Finance Agent] Preparing to execute: Pay electricity bill
⚠️ Approve this sensitive task? (y/n): y
[Finance Agent] ✅ Approved and executed: Pay electricity bill

📌 Roadmap

 Stage 1: JSON-based planner + basic agents

 Stage 2: Connect to Google Calendar API

 Stage 3: Replace dummy IoT with MQTT / smart plug simulation

 Stage 4: Add more agents (shopping, travel, communication)

 Stage 5: Build a web/mobile interface for confirmations

 Stage 6: Integrate privacy-aware security (encryption, authentication)

 Stage 7: Deploy as a full multi-agent orchestrator

📖 Research Context

This project is designed as part of a research exploration into multi-agent systems for daily life orchestration.
It touches on:

Multi-Agent Systems (MAS)

Human-AI Interaction (HAI)

IoT & Ubiquitous Computing

Privacy-Preserving AI Assistants

Potential applications:

Smart homes

Personal productivity assistants

Elderly care support systems