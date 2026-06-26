from workflow.orchestrator import DisasterWorkflow
from pprint import pprint


workflow = DisasterWorkflow()

incident = workflow.run(
    report="""
    School building collapsed.
    Multiple injuries reported.
    """
)

pprint(incident.model_dump())