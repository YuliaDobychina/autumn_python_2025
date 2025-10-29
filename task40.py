# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)


class NotificationSender:
    def send(self, message, user):
        print( f'Отправляем "{message}" пользователю {user}')

# Дочерние классы:
# EmailSender: отправляет email с темой "Образовательная платформа"
# SMSSender: отправляет SMS (первые 50 символов сообщения)
# PushSender: отправляет push-уведомление с иконкой "🎓"

class EmailSender(NotificationSender):
    def send(self, message, user):
        self.message = '"Образовательная платформа" ' + message
        super().send(self.message, user)

class SMSSender(NotificationSender):
    def send(self, message, user):
        print(f'Отправляем SMS "{message[:50]}" пользователю {user}')

class PushSender(NotificationSender):
    def send(self, message, user):
        print( f'Отправляем push-уведомление 🎓"{message[:50]}" пользователю {user}')


# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)

class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications or []

    def notify(self, user,  message):
        for sender in self.preferred_notifications:
            sender.send(message, user.name)




# Этот код должен работать после реализации:
user = User("Мария", [EmailSender(), PushSender()])

#notify_user(user, "Блок аналитики начинается с 27 октября!")

user.notify(user, "Блок аналитики начинается с 27 октября!")
