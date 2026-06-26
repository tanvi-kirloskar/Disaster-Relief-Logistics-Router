from models.incident_state import IncidentState
from uuid import uuid4

class IntakeAgent:

    def process(self, report: str, location: str = "Unknown"):

        incident = IncidentState(
            incident_id=f"INC-{str(uuid4())[:8]}",
            report=report.strip(),
            location=location
        )

        return incident