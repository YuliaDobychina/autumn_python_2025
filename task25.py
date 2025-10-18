# todo: Шифр Цезаря
#Описание шифра.
#В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
#является одним из самых простых и широко известных методов шифрования.
#Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
#фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
#E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

#Задача.
#Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
#циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

with open("message.txt","r",encoding="utf-8") as f:
    text = f.readlines()

alphabet = [chr(i) for i in range(ord('а'), ord('я'))]

text_new = ''
index_chr_ = []

for line in text:
    lag = text.index(line) + 1
    for chr in line:
        chr_lower, flag_lower = (chr,1) if chr.islower() else (chr.lower(),0)
        if chr_lower in alphabet:
            index_chr = alphabet.index(chr_lower)
            index_chr_new = lag - 31 + index_chr if index_chr + lag >=31 else lag + index_chr
            index_chr_.append(index_chr_new)
            #print(index_chr, index_chr_new)
            text_new += alphabet[index_chr_new].upper() if flag_lower == 0 else alphabet[index_chr_new]
            #print(chr, ' - ', alphabet[index_chr_new], ' - ', flag_lower)
            #print(alphabet[index_chr_new].upper())
        else: text_new += chr

print(text_new)
