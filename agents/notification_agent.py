class NotificationAgent:

    def process(self, incident):

        notifications = []

        if incident.review_status != "APPROVED":

            incident.notifications = notifications
            return incident

        if incident.severity == "LOW":

            notifications.append(
                "SUPPLY ALERT: Deliver water and basic supplies."
            )

        elif incident.severity == "MEDIUM":

            notifications.append(
                "SHELTER ALERT: Prepare temporary shelter support."
            )

        elif incident.severity == "HIGH":

            notifications.append(
                "RESCUE ALERT: Deploy rescue team immediately."
            )

            notifications.append(
                "MEDICAL ALERT: Prepare emergency medical assistance."
            )

        elif incident.severity == "CRITICAL":

            notifications.append(
                "RESCUE ALERT: Deploy rescue team immediately."
            )

            notifications.append(
                "HOSPITAL ALERT: Prepare emergency beds and trauma support."
            )

            notifications.append(
                "NGO ALERT: Prepare food, water and relief supplies."
            )

        incident.notifications = notifications

        incident.status = "NOTIFICATIONS_GENERATED"

        return incident