import json
import os
from inspect import getsourcefile

class FICalculator:
    def get_personal_details(self):
        with open("fi_calculator/personal_details.json") as f:
            personal_details = json.load(f)

        return personal_details

    def set_personal_details(self, current_age, fi_age, lifespan):
        with open("fi_calculator/personal_details.json", "w+") as f:
            json.dump({"current_age": current_age, "fi_age": fi_age, "lifespan": lifespan}, f)

        return 0

    def get_market_expectations(self):
        with open("fi_calculator/market_expectations.json") as f:
            market_expectations = json.load(f)

        return market_expectations

    def set_market_expectations(self, inflation, asset_classes):
        with open("fi_calculator/market_expectations.json", "w+") as f:
            json.dump({"inflation": inflation, "asset_classes": asset_classes}, f)

        return 0