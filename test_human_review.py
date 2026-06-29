from agents.intake_agent import IntakeAgent
from agents.human_review_agent import HumanReviewAgent

intake = IntakeAgent()
review_agent = HumanReviewAgent()

incident = intake.process(
    report="School collapsed."
)

incident.human_review_required = True

incident = review_agent.process(
    incident
)

print(
    incident.model_dump()
)