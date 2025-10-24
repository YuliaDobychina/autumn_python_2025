# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

currency = {'USD':80.98 ,'$':80.98,'€':94.58, '¥':0.5396,'₽':1}

# Исходный набор данных
prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "₽18.99", "N/A", "¥5000"]

# Преобразование данных
prices = [price.replace('USD','$') for price in prices]

prices_ruble = {price : float(price.replace(item,'')) * currency[item] for price in prices for item in price if item in currency.keys()}

print(prices_ruble)