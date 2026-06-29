from tools.inventory_tool import InventoryTool


class ResourcePlannerAgent:

    def __init__(self):

        self.inventory_tool = InventoryTool()

    def process(self, incident):

        inventory = self.inventory_tool.get_inventory()

        resources = []

        severity = incident.severity

        if severity == "LOW":

            resources.append("Water Pack")

        elif severity == "MEDIUM":

            resources.append(
                "Temporary Shelter Kit"
            )

        elif severity == "HIGH":

            resources.extend([
                "Boat Team",
                "Medical Kit"
            ])

        elif severity == "CRITICAL":

            resources.extend([
                "Rescue Team",
                "Ambulance",
                "Medical Kit"
            ])

        available_resources = []

        for resource in resources:

            if (
                resource in inventory
                and inventory[resource] > 0
            ):

                available_resources.append(
                    resource
                )

        incident.recommended_resources = (
            available_resources
        )

        incident.status = (
            "RESOURCES_ALLOCATED"
        )

        return incident