"""
FastAPI integration layer for the existing DisasterWorkflow.

IMPORTANT: This file does NOT modify any agent logic. It only:
  1. Wraps the existing DisasterWorkflow.run() call in an HTTP endpoint.
  2. Maps IncidentState fields onto the shape the React frontend expects.

Run with:
    uvicorn app:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from workflow.orchestrator import DisasterWorkflow

app = FastAPI(title="Disaster Relief Logistics Router API")

# Allow the Vite dev server to call this API. Adjust origins for production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Reuse a single workflow instance (agents are stateless per .process() call,
# matching how main.py already uses it).
workflow = DisasterWorkflow()


class AnalyzeRequest(BaseModel):
    report: str
    location: str = "Unknown"


def _map_security_status(status: str) -> str:
    """Map free-form backend security_status onto the frontend's closed enum."""
    s = (status or "").upper()
    if s in ("PASSED", "PASS", "OK", "CLEAR", "CLEARED"):
        return "PASSED"
    if s in ("FAILED", "FAIL", "BLOCKED", "FLAGGED", "REJECTED"):
        return "FAILED"
    return "REVIEWING"


def _map_review_status(status: str) -> str:
    """Map free-form backend review_status onto the frontend's closed enum."""
    s = (status or "").upper()
    if "APPROVE" in s:
        return "APPROVED"
    if "REJECT" in s:
        return "REJECTED"
    return "PENDING"


def _build_reasoning(incident) -> str:
    """
    Build a short factual summary from real IncidentState fields.
    No agent currently produces free-text reasoning, so this is composed
    from data that actually exists rather than fabricated.
    """
    parts = [f"Severity classified as {incident.severity or 'UNKNOWN'} based on the submitted report."]
    if incident.recommended_resources:
        parts.append(
            f"{len(incident.recommended_resources)} resource type(s) recommended for response."
        )
    return " ".join(parts)


def _build_security_note(incident) -> str:
    if incident.security_notes:
        return " ".join(incident.security_notes)
    return f"Security screening status: {incident.security_status}."


def _build_approval_note(incident) -> str:
    if incident.review_status and incident.review_status != "NOT_REQUIRED":
        return f"Human review status: {incident.review_status}."
    return "No human review was required for this incident."


@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    if not req.report or not req.report.strip():
        raise HTTPException(status_code=400, detail="report must not be empty")

    try:
        incident = workflow.run(req.report, location=req.location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow failed: {e}")

    return {
        "incidentId": incident.incident_id,
        "status": incident.status,
        "severity": incident.severity or "LOW",
        "securityStatus": _map_security_status(incident.security_status),
        "humanReview": _map_review_status(incident.review_status),
        "reasoning": _build_reasoning(incident),
        "securityNote": _build_security_note(incident),
        "approvalNote": _build_approval_note(incident),
        "resources": incident.recommended_resources,
        "notifications": incident.notifications,
        # aiConfidence intentionally omitted: no agent computes this.
        # The frontend treats it as optional and hides the UI block when absent.
    }


@app.get("/health")
def health():
    return {"status": "ok"}
