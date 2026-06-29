class HumanReviewAgent:

    def process(
        self,
        incident,
        decision="PENDING"
    ):

        if not incident.human_review_required:

            incident.review_status = "NOT_REQUIRED"
            incident.status = "REVIEW_NOT_REQUIRED"

        else:

            if decision == "APPROVE":

                incident.review_status = "APPROVED"
                incident.status = "REVIEW_APPROVED"

            elif decision == "REJECT":

                incident.review_status = "REJECTED"
                incident.status = "REVIEW_REJECTED"

            else:

                incident.review_status = "PENDING_APPROVAL"
                incident.status = "AWAITING_HUMAN_REVIEW"

        return incident