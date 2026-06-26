from utils.gemini_client import client


class SeverityAgent:

    def process(self, incident):

        incident_text = (
            incident.redacted_report
            if incident.redacted_report
            else incident.report
        )

        prompt = f"""
You are a disaster response severity classifier.

Classify the incident into ONE category:

LOW
MEDIUM
HIGH
CRITICAL

Definitions:

LOW:
Minor supply requests.

MEDIUM:
Shelter issues, infrastructure disruptions.

HIGH:
People trapped, evacuation required, rescue needed.

CRITICAL:
Building collapse, severe injuries, deaths,
hospital evacuation, mass casualty events.

Return ONLY one word.

Incident Report:

{incident_text}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        severity = response.text.strip().upper()

        valid_levels = [
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        ]

        if severity not in valid_levels:
            severity = "MEDIUM"

        incident.severity = severity

        if severity == "CRITICAL":
            incident.human_review_required = True

        incident.status = "SEVERITY_CLASSIFIED"

        return incident