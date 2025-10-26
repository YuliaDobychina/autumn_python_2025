# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.


from autumn_python_2025.task37 import Product

class Order:
    def __init__(self):
        self.products = []

    @property
    def total_price(self):
        return sum(product.price for product in self.products)

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def info(self):
        return print({product.name:product.price for product in self.products})



# Пример использования
book = Product("Book", 20)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12

order.info()