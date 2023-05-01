from degradation.degradation_rule import DegradationRule
from models.item import Item


class DegradationRate:
    """
    Collection of degradation rates rules to be applied to an item.
    """
    def __init__(self, rules: [DegradationRule], legendary: bool):
        self.__degradation_rules = rules
        # When an item is legendary, sell_in won't be updated
        self.__legendary = legendary

    def apply_degradation(self, item: Item):
        for degradation_rule in self.__degradation_rules:
            degradation_rule.apply_degradation(item)
        if not self.__legendary:
            item.sell_in -= 1
