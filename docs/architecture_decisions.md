# Architecture Decisions

## Why Multi-Agent Architecture?

The Google AI Agents Intensive emphasized decomposing complex workflows into specialized agents.

Instead of one large agent, this project uses multiple focused agents that are easier to evaluate, debug, and extend.

---

## Why MCP?

MCP provides a standardized mechanism for agents to access external tools and data.

The Resource Planner Agent uses MCP to retrieve inventory information and make allocation decisions.

This demonstrates tool usage and context retrieval concepts taught during the course.

---

## Why Security Agent?

Security was a major theme of the course.

The Security Agent performs:

* PII detection
* PII redaction
* Prompt injection detection

before any downstream reasoning occurs.

This ensures safer agent behavior.

---

## Why Human-in-the-Loop?

High-risk decisions should not be fully automated.

Critical incidents require human approval before notifications are generated.

This demonstrates Human-in-the-Loop (HITL) workflows.

---

## Why Evaluation?

Agent systems should be measurable.

The project includes:

* Severity Classification Accuracy
* Routing Accuracy
* Security Detection Rate
* LLM-as-a-Judge Evaluation

This follows evaluation practices recommended during the Google AI Agents Intensive.

---

## Why No RAG?

RAG was intentionally excluded from the MVP.

The project already demonstrates:

* Multi-Agent Systems
* MCP
* Security
* HITL
* Evaluation

Adding RAG would increase complexity without significantly improving learning outcomes or demo quality.

RAG remains future work.

---

## Why No Real Emergency Integrations?

This project is an educational demonstration.

No real hospitals, NGOs, dispatch systems, or government services are contacted.

All notifications are simulated.

