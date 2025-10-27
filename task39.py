# Модель учебных материалов
# todo: Создайте иерархию классов для представления различных типов учебных материалов.
#
# Требования: Базовый класс LearningMaterial:
# Свойства: title, author, duration_minutes
# Методы:
# display_info() - выводит основную информацию
# get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)

class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        print( f'Основная информация: {self.title} - {self.author} - {self.duration_minutes}')

    def get_difficulty(self):
        return 'Средняя (по умолчанию)'


# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"

class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        LearningMaterial.__init__(self, title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def display_info(self):
        LearningMaterial.display_info(self)
        print( f'Характеристики VideoLesson: {self.video_quality}, {self.subtitles_available} ')

    def get_difficulty(self):
        return 'Средняя'

#v = VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True)
#v.display_info()


# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)

class Article:
    def __init__(self, title, author, duration_minutes,word_count, reading_level):
        LearningMaterial.__init__(self, title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def display_info(self):
        LearningMaterial.display_info(self)
        print(f'Характеристики Article: {self.word_count}, {self.reading_level} ')

    def get_difficulty(self):
        int_word_count = int(self.word_count)
        if int_word_count / 1000 <1:
            difficulty = 'Лёгкая'
        elif int_word_count / 1000 <3:
            difficulty = 'Средняя'
        else:
            difficulty = 'Сложная'

        return difficulty


#a = Article("Глубокое обучение", "Анна Петрова", 10, 1200, "advanced")
#a.display_info()
#a.get_difficulty()

# Quiz:
# Дополнительные свойства: questions_count, passing_score
# Сложность: "Высокая" если passing_score > 80, иначе "Средняя"

class Quiz:
    def __init__(self, title, author, duration_minutes,questions_count, passing_score):
        LearningMaterial.__init__(self, title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def display_info(self):
        LearningMaterial.display_info(self)
        print(f'Характеристики Quiz: {self.questions_count}, {self.passing_score} ')

    def get_difficulty(self):
        return 'Высокая' if self.passing_score / self.questions_count > 80 else 'Средняя'

#q = Quiz("Проверка знаний", "Платформа", 20, 75, 10)
#q.get_difficulty()
#q.display_info()


# Этот код должен работать после реализации:
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 10, 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")