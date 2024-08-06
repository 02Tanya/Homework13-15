from src.products import Product


class Category:
    name: str
    description: str
    goods: list

    quantity_category = 0
    quantity_sku = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.quantity_category += 1

        goods_set = []
        for good in self.__goods:
            if good not in goods_set:
                goods_set.append(good)
            continue
        Category.quantity_sku += len(goods_set)

    def add_goods(self, value):

        if not isinstance(value, Product):  # проверка соответствия классу
            raise TypeError('Продукт не соответствует классу')
        elif value.quantity == 0:   # проверка наличия у товара остатков
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.__goods.append(value)

    @property
    def goods(self):
        return self.__goods

    @property
    def print_good(self):
        """Декоратор для вывода информации о товаре в формате цена/ остаток"""
        output = ''
        for good in self.__goods:
            output += f'{good.name}, {good.price} руб. Остаток: {good.quantity}\n'
        return output

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        """Для вывода количества товаров на складе"""
        quantity = 0
        for good in self.__goods:
            quantity += good.quantity
        return quantity
