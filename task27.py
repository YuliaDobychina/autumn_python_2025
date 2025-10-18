#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

text  = input('Введите зашифрованный текст:')

alf = 'abcdefghijklmnopqrstuvwxyz'
text= list(text.split(' '))
final = ''

for i in range(0,len(text)):
    chr = text[i]
    final +=  alf[int(chr)-1]  if chr.isnumeric() else chr

print(final)