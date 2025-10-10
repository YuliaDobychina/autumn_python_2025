#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
#1) "C4.5"
#2) "k - means"
#.....

f = open("algoritm.csv","at+",encoding="utf-8")
for item in algoritm:
    f.write(f'{algoritm.index(item)+1}) "{item}"\n')

f.seek(0)
print(f.read())
f.close()