from agents.intake_agent import IntakeAgent
from agents.security_agent import SecurityAgent
from agents.severity_agent import SeverityAgent
from agents.resource_planner_agent import ResourcePlannerAgent
from agents.human_review_agent import (
    HumanReviewAgent
)


class DisasterWorkflow:

    def __init__(self):

        self.intake_agent = IntakeAgent()

        self.security_agent = SecurityAgent()

        self.severity_agent = SeverityAgent()

        self.resource_planner_agent = ResourcePlannerAgent()

        self.human_review_agent = (
            HumanReviewAgent()
        )

    def run(self, report, location="Unknown"):

        # Step 1: Intake
        incident = self.intake_agent.process(
            report,
            location
        )

        # Step 2: Security Check
        incident = self.security_agent.process(
            incident
        )

        # Step 3: Severity Classification
        incident = self.severity_agent.process(
            incident
        )

        # Step 4: Resource Planning
        incident = self.resource_planner_agent.process(
            incident
        )

        incident = self.human_review_agent.process(
            incident
        )

        incident = self.human_review_agent.process(
            incident,
            decision="APPROVE"
        )
        return incident
    

