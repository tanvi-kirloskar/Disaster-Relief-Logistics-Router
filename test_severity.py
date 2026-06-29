from agents.intake_agent import IntakeAgent
from agents.severity_agent import SeverityAgent

intake = IntakeAgent()
severity_agent = SeverityAgent()

incident = intake.process(
    report="School building collapsed with multiple injuries reported."
)

incident = severity_agent.process(
    incident
)

print(incident.model_dump())