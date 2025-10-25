# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.

class Product:
    # Инициализация новой БД
    def __init__(self,name,price):
        self.__name = name

        if price > 0:
            self.__price = price
        else:
            self.__price = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value > 0:
            self.__price = value
        else:
            self.__price = 0
            #print(f'Указана отрицательная цена {value}, поэтому она заменена на 0')


# Пример использования
product = Product("Book", 10)


print(product.price)  # 10
product.price = -5
print(product.price)  # 0



