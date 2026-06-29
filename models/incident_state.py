from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class IncidentState(BaseModel):
    incident_id: str
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

    report: str
    location: str = "Unknown"

    redacted_report: str = ""

    security_status: str = "PENDING"
    security_notes: List[str] = []

    severity: str | None = None

    recommended_resources: List[str] = []

    human_review_required: bool = False
    review_status: str = "NOT_REQUIRED"

    notifications: List[str] = []

    status: str = "RECEIVED"