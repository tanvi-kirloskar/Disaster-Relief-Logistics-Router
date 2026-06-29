from agents.notification_agent import NotificationAgent
from agents.intake_agent import IntakeAgent

intake = IntakeAgent()

incident = intake.process(
    report="School collapsed."
)

incident.severity = "CRITICAL"

incident.review_status = "APPROVED"

notification_agent = NotificationAgent()

incident = notification_agent.process(
    incident
)

print(
    incident.model_dump()
)