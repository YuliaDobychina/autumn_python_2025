# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius + 32

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self.celsius = fahrenheit - 32

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @kelvin.setter
    def kelvin(self, kelvin):
        self.celsius = kelvin - 273.15





# Пример использования
t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")