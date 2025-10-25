# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

class User:
    def __init__(self, email,password):
        self.__password = hash(password)
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if '@' in email:
            self.__email = email

    def check_password(self, password):
        if self.__password == hash(password):
            return True
        else:
            return False


# Пример использования
user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False