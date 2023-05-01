from models.item import Item


class DegradationRule:
    """
    A degradation rule will apply a degradation if the item sell_in is in the range predefined by the rule
    """
    def __init__(self, sell_in_init: int, sell_int_end: int):
        self.__sell_in_init = sell_in_init
        self.__sell_in_end = sell_int_end

    def apply_degradation(self, item: Item):
        if self.__sell_in_init <= item.sell_in <= self.__sell_in_end:
            self._apply_degradation(item)

    def _apply_degradation(self, item: Item):
        raise NotImplementedError


class DegradationRuleStandard(DegradationRule):
    def __init__(self, sell_in_init: int, sell_int_end: int, degradation: int, max_quality: int, min_quality: int):
        super().__init__(sell_in_init, sell_int_end)
        self.__degradation = degradation
        self.__max_quality = max_quality
        self.__min_quality = min_quality

    def _apply_degradation(self, item: Item):
        item.quality += self.__degradation
        if self.__degradation > 0 and item.quality > self.__max_quality:
            item.quality = self.__max_quality
        elif self.__degradation < 0 and item.quality < self.__min_quality:
            item.quality = self.__min_quality


class DegradationRuleDropsToZero(DegradationRule):
    def __init__(self, sell_in_init: int, sell_int_end: int):
        super().__init__(sell_in_init, sell_int_end)

    def _apply_degradation(self, item: Item):
        item.quality = 0
