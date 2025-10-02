# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах

units_mass = 3
mass = 12

def conversion_to_kilograms(units_mass_):
    match units_mass_:
        case 1: units = 1
        case 2: units = 0.000001
        case 3: units = 0.001
        case 4: units = 1000
        case 5: units = 100
    return units

print('Масса данного тела в килограммах = ', mass*conversion_to_kilograms(units_mass))
