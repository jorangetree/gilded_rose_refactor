import sys

from degradation.degradation_rate import DegradationRate
from degradation.degradation_rule import DegradationRuleStandard, DegradationRuleDropsToZero

STANDARD_DEGRADATION_RATE = -1

ITEM_DEGRADATIONS = {
    "Aged Brie": DegradationRate(
        [
            DegradationRuleStandard(-sys.maxsize, sys.maxsize, -STANDARD_DEGRADATION_RATE, 50, 0)
        ],
        False
    ),
    "Sulfuras": DegradationRate(
        [
            DegradationRuleStandard(-sys.maxsize, sys.maxsize, 0, 50, 0)
        ],
        True
    ),
    "Backstage passes": DegradationRate(
        [
            DegradationRuleStandard(11, sys.maxsize, -STANDARD_DEGRADATION_RATE, 50, 0),
            DegradationRuleStandard(6, 10, -STANDARD_DEGRADATION_RATE*2, 50, 0),
            DegradationRuleStandard(0, 5, -STANDARD_DEGRADATION_RATE*3, 50, 0),
            DegradationRuleDropsToZero(-sys.maxsize, -1)
        ],
        False
    ),
    "Conjured": DegradationRate(
        [
            DegradationRuleStandard(-sys.maxsize, sys.maxsize, STANDARD_DEGRADATION_RATE*2, 50, 0)
        ],
        False
    ),
    "": DegradationRate(
        [
            DegradationRuleStandard(0, sys.maxsize, STANDARD_DEGRADATION_RATE, 50, 0),
            DegradationRuleStandard(-sys.maxsize, -1, STANDARD_DEGRADATION_RATE*2, 50, 0)
        ],
        False
    ),
}


class DegradationNotFoundException(Exception):
    pass


def get_degradation_rate(name: str) -> DegradationRate:
    for key, value in ITEM_DEGRADATIONS.items():
        if name.startswith(key):
            return value

    raise DegradationNotFoundException
