import re

from models.incident_state import IncidentState


class SecurityAgent:

    def process(self, incident: IncidentState):

        notes = []

        report = incident.report

        # Detect phone numbers
        if re.search(r"\b\d{10}\b", report):
            notes.append("PHONE_NUMBER_DETECTED")

        # Detect emails
        if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", report):
            notes.append("EMAIL_DETECTED")

        # Prompt injection keywords

        suspicious_phrases = [
            "ignore previous instructions",
            "override system",
            "mark this critical",
            "system override"
        ]

        redacted_report = report

        redacted_report = re.sub(
            r"\b\d{10}\b",
            "[REDACTED_PHONE]",
            redacted_report
        )

        redacted_report = re.sub(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            "[REDACTED_EMAIL]",
            redacted_report
        )

        incident.redacted_report = redacted_report

        for phrase in suspicious_phrases:

            if phrase in report.lower():
                notes.append("PROMPT_INJECTION_DETECTED")
                break

        incident.security_notes = notes

        if notes:
            incident.security_status = "FLAGGED"
        else:
            incident.security_status = "PASSED"

        incident.security_notes = notes

        incident.redacted_report = redacted_report

        incident.status = "SECURITY_CHECKED"

        return incident
    
        redacted_report = report

        redacted_report = re.sub(
            r"\b\d{10}\b",
            "[REDACTED_PHONE]",
            redacted_report
        )

        redacted_report = re.sub(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            "[REDACTED_EMAIL]",
            redacted_report
        )

        incident.redacted_report = redacted_report

        #incident.redacted_report = report

        return incident