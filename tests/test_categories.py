import pytest

from src.categories import Category

@pytest.fixture()
def category_beverages():
    return Category('beverages', 'the most popular and highly in-demand FMCG', ('bear', 'wine', 'juice', 'water'))


def test_init(category_beverages):
    assert category_beverages.name == 'beverages'
    assert category_beverages.description == 'the most popular and highly in-demand FMCG'
    assert category_beverages.goods == ('bear', 'wine', 'juice', 'water')
    assert Category.quantity_category == 1
    assert Category.quantity_sku == 4