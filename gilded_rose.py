# -*- coding: utf-8 -*-
from degradation import get_degradation_rate
from models.item import Item


class GildedRose(object):

    def __init__(self, items: [Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            degradation_rate = get_degradation_rate(item.name)
            degradation_rate.apply_degradation(item)
