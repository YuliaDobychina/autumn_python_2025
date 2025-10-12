#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

f = open("inverted_sort.txt","a+",encoding="utf-8")

f.write('''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
)

f.seek(0)
set = f.readlines()

while len(set)>0:
    f.write(set.pop())

f.seek(0)
print(f.read())

f.close()

#Содержимое файла inverted_sort.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

# Результат
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.
