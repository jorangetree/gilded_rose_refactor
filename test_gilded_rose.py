# -*- coding: utf-8 -*-
import unittest

import pytest

from gilded_rose import Item, GildedRose


testdata_update_quality = [
    # DAYS | ITEM | EXPECTED_SELL_IN | EXPECTED_QUALITY
    (1, Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 9, 19),
    (1, Item(name="Aged Brie", sell_in=2, quality=0), 1, 1),
    (1, Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 4, 6),
    (1, Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 0, 80),
    (1, Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), -1, 80),
    (1, Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 14, 21),
    (1, Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 9, 50),
    (1, Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 4, 50),
    (1, Item(name="Conjured Mana Cake", sell_in=3, quality=6), 2, 4),
]


@pytest.mark.parametrize("days, item, expected_sell_in, expected_quality", testdata_update_quality)
def test_foo(days: int, item: Item, expected_sell_in: int, expected_quality: int):
    gilded_rose = GildedRose([item])
    for _ in range(days):
        gilded_rose.update_quality()
    assert item.quality == expected_quality
    assert item.sell_in == expected_sell_in
