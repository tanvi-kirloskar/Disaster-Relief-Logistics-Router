from agents.intake_agent import IntakeAgent
from agents.resource_planner_agent import (
    ResourcePlannerAgent
)

intake = IntakeAgent()

planner = ResourcePlannerAgent()

incident = intake.process(
    report="Flood rescue required."
)

incident.severity = "HIGH"

incident = planner.process(
    incident
)

print(
    incident.model_dump()
)