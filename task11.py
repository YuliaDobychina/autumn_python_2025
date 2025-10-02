#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

num_month = 12

match num_month:
    case 12 | 1 | 2 :
        print('Месяц №',num_month, ' - это зима')
    case num if 3 <= num <= 5:
        print('Месяц №',num_month, ' - это весна')
    case num if 6 <= num <= 8:
        print('Месяц №',num_month, ' - это лето')
    case num if 9 <= num <= 11:
        print('Месяц №',num_month, ' - это осень')
    case _:
        print('Номер месяца должен быть от 1 до 12')
