from workflow.orchestrator import DisasterWorkflow

workflow = DisasterWorkflow()

incident = workflow.run(
    report="""
    My phone number is 9876543210.
    Family trapped by flood.
    """
)

print(incident.model_dump())