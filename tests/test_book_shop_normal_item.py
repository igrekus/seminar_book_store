from src.book_shop import BookShop, Item


def test_normal_item_before_sell_data():
    shop = BookShop([Item('normal item', sell_in=50, quality=50)])

    shop.update_quality()

    assert shop.items == [Item('normal item', sell_in=49, quality=49)]


def test_normal_on_sell_date():
    shop = BookShop([Item('normal item', sell_in=0, quality=10)])

    shop.update_quality()

    assert shop.items == [Item('normal item', sell_in=-1, quality=8)]


def test_normal_item_after_sell_date():
    shop = BookShop([Item('normal item', sell_in=-1, quality=10)])

    shop.update_quality()

    assert shop.items == [Item('normal item', sell_in=-2, quality=8)]


def test_normal_item_of_zero_quality():
    shop = BookShop([
        Item('normal item', sell_in=10, quality=0),
        Item('normal item', sell_in=0, quality=0),
        Item('normal item', sell_in=-1, quality=0),
    ])

    shop.update_quality()

    assert shop.items == [
        Item('normal item', sell_in=9, quality=0),
        Item('normal item', sell_in=-1, quality=0),
        Item('normal item', sell_in=-2, quality=0),
    ]
