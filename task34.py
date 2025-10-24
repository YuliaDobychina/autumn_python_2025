# todo: Перепишите игру "Поле чудес" на классах.
import datetime
import random
import uuid
from db import DICT_DEFENITION_WORD

class Yakubovich:
    def __init__(self):
        self.name = input("Введите имя:")
        self.session_uuid = uuid.uuid4()
        self.print_menu()

    def _generate_key(self) -> str:
        keys = list(DICT_DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()

    def print_menu(self):
        print("""   
            1. Начать игру
            2. Загрузить игру
            3. Выход из игры 
            """)
        num = int(input("Пункт меню:"))

        match num:
            case 1:
                self.key = self._generate_key()
                self.list_word = list(self.key)
                self.mask = ['#'] * len(self.key)
                self.definition = DICT_DEFENITION_WORD[self.key]
                self.start_game()
                # print('The UUID is: ' + str(session_uuid))
            case 2:
                self.load_game()
            case 3:
                print(f"Спасибо {self.name} за игру! Заходи еще! ")
                pass

    def start_game(self):
        print('Игра началась :) ')
        print('Как называется '+self.definition )
        print(self.mask)
        while '#' in self.mask:
            alfa = input("Введите букву:")
            if alfa == "2":
                print("Сохранение игры!")
                self.save_game()
            elif alfa == "0":
                print("Возвращаемся в главное меню")
                self.print_menu()
            cnt = 0
            for i in self.list_word:
                if alfa == i:
                    print(f'Вы угадали букву "{alfa}"' )
                    self.mask[cnt] = alfa
                    cnt += 1
                    continue
                cnt += 1
            else:
                print(self.mask)
                print('Для сохранения игры нажми "2", а для выхода в главное меню - "0"')

    def save_game(self):
        f = open("save_game.csv", "a+",encoding="utf-8")
        dt = datetime.datetime.now()
        mask = "".join(self.mask)
        str = f"{dt}|{self.session_uuid}|{self.name}|{self.definition}|{mask}| {self.list_word}\n"
        print(str)
        f.write(str)
        f.close()
        print("Сохранил игру!")

    def load_game(self):
        f = open("save_game.csv", "tr",encoding="utf-8")
        indx = 0
        list_str = f.readlines()
        for csv_str in list_str:
            if self.name in csv_str:
                print(indx, ") ", csv_str)
            indx += 1
        indx_load = int(input("Введите номер:"))
        sg = list_str[indx_load].split("|")
        self.definition = sg[3].strip()
        self.mask = list(sg[4])
        self.list_word = sg[5]
        self.dt = sg[0]
        self.session_uuid = sg[1]
        print('Загружена игра: ',self.dt, self.definition, list(self.mask))
        self.start_game()

    def end_game(self):
        print('До скорых встреч!')




game = Yakubovich()
game.print_menu()