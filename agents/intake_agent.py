from models.incident_state import IncidentState


class IntakeAgent:

    def process(self, report: str, location: str = "Unknown"):

        incident = IncidentState(
            incident_id="INC001",
            report=report,
            location=location
        )

        return incident