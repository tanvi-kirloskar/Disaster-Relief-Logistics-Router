import json


class InventoryTool:

    def get_inventory(self):

        with open(
            "data/inventory.json",
            "r"
        ) as file:

            inventory = json.load(file)

        return inventory