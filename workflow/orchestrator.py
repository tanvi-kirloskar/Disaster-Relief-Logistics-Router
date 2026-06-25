from agents.intake_agent import IntakeAgent
from agents.security_agent import SecurityAgent


class DisasterWorkflow:

    def __init__(self):

        self.intake_agent = IntakeAgent()
        self.security_agent = SecurityAgent()

    def run(self, report, location="Unknown"):

        incident = self.intake_agent.process(
            report,
            location
        )

        incident = self.security_agent.process(
            incident
        )

        return incident