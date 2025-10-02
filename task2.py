# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

age = int(age)
print('age = ',age,' - type:',type(age))

#1 вариант
foo = int(foo[0:2])
print('foo = ',foo,' - type:',type(foo))

#2 вариант
def extract_numbers(s):
    result = ""
    for char in s:
        if char >= '0' and char <= '9':
           result += char
    return result

print(extract_numbers("23abc"))



#
# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print('age = ',age,' - type:',type(age))

#
# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print('flag = ', flag,' - type:',type(flag))

#
# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one = bool(str_one)
print('str_one = ', str_one,' - type:',type(str_one))

str_two = bool(str_two)
print('str_two = ', str_two,' - type:',type(str_two))

#
# Преобразуйте значение 0 и 1 в Boolean
one = bool(1)
print('one = ', one,' - type:',type(one))

zero = bool(0)
print('zero = ', zero,' - type:',type(zero))

# Преобразуйте False в строку
f = str(False)
print('f = ', f,' - type:',type(f))