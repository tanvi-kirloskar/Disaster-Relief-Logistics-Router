from agents.intake_agent import IntakeAgent
from agents.security_agent import SecurityAgent
from agents.severity_agent import SeverityAgent

class DisasterWorkflow:

    def __init__(self):
        self.severity_agent = SeverityAgent()
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
        incident = self.severity_agent.process(
            incident
        )
        return incident