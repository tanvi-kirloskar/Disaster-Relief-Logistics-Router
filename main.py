from workflow.orchestrator import DisasterWorkflow
from pprint import pprint


workflow = DisasterWorkflow()

incident = workflow.run(
    report="""
    School building collapsed.
    Multiple injuries reported.
    """
)

print("\n===== FINAL INCIDENT STATE =====\n")

pprint(
    incident.model_dump()
)