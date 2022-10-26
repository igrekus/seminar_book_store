from dataclasses import dataclass


@dataclass()
class Item:
    name: str = ''
    sell_in: int = 0
    quality: int = 0


class BookShop:

    def __init__(self, items: list):
        self.items: list = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Д. Кнут, Искусство программирования" and item.name != "Скидочный купон на курс":
                if item.quality > 0:
                    if item.name != "Марк Лутц, Изучаем Python, 3й том":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Скидочный купон на курс":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Марк Лутц, Изучаем Python, 3й том":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Д. Кнут, Искусство программирования":
                    if item.name != "Скидочный купон на курс":
                        if item.quality > 0:
                            if item.name != "Марк Лутц, Изучаем Python, 3й том":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
