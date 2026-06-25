# Workflow State Schema

## Purpose

The Disaster Relief Logistics Router uses a shared workflow state object that is passed between agents.

Each agent reads the current state, performs its task, and updates the state before passing it to the next agent.

This architecture provides:

* Traceability
* Agent interoperability
* Incident lifecycle tracking
* Easier debugging and evaluation

---

## State Object

```json
{
  "incident_id": "INC001",
  "timestamp": "2026-06-25T14:30:00Z",
  "location": "Mumbai",
  "report": "12 people trapped on school roof. Water level rising rapidly.",
  "redacted_report": "12 people trapped on school roof. Water level rising rapidly.",
  "security_status": "PASSED",
  "security_notes": [],
  "severity": "HIGH",
  "recommended_resources": [
    "1 rescue boat",
    "10 food kits"
  ],
  "human_review_required": false,
  "review_status": "NOT_REQUIRED",
  "notifications": [
    "Rescue Team Alert",
    "NGO Alert"
  ],
  "status": "COMPLETED"
}
```

---

## Field Definitions

| Field                 | Description                                   |
| --------------------- | --------------------------------------------- |
| incident_id           | Unique identifier for each incident           |
| timestamp             | Incident submission timestamp                 |
| location              | Reported disaster location                    |
| report                | Original incident report                      |
| redacted_report       | Security-filtered version of report           |
| security_status       | PASSED or FLAGGED                             |
| security_notes        | Security findings                             |
| severity              | LOW, MEDIUM, HIGH, CRITICAL                   |
| recommended_resources | Resources suggested by Resource Planner Agent |
| human_review_required | Whether approval is required                  |
| review_status         | APPROVED, REJECTED, MODIFIED, NOT_REQUIRED    |
| notifications         | Generated notification drafts                 |
| status                | Current workflow status                       |

---

## Incident Lifecycle

RECEIVED

↓

SECURITY_CHECKED

↓

SEVERITY_CLASSIFIED

↓

RESOURCES_ALLOCATED

↓

HUMAN_REVIEW (if required)

↓

NOTIFICATIONS_GENERATED

↓

COMPLETED

The state object acts as the single source of truth throughout the workflow.

```
```
