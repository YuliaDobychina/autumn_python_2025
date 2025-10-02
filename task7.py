#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a = int(input("Введите число A:"))
b = int(input("Введите число B:"))
c = int(input("Введите число C:"))

ac = c-a if a<c else a-c
bc = c-b if b<c else b-c

print ('ac = ', ac)
print ('bc = ', bc)
print ('ac + bc = ', ac+bc)