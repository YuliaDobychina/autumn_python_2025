#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


text = 'grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy euaxk jazin.'

def new_text(lag):
    text_new = ''
    index_chr_ = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for chr in text:
        if chr in alphabet:
            index_chr = alphabet.index(chr)
            index_chr_new = lag + index_chr if index_chr + lag >= 0 else -lag - 25 + index_chr
            index_chr_.append(index_chr_new)
            text_new += alphabet[index_chr_new]
        else: text_new += chr
    print(f'Лаг = {lag} - ', text_new)


for lag in range(-24,1):
    new_text(lag)

# В результате получается сдвиг был на 6 вперёд
# Исходный текст: "althohgh that jal mal not be obiiohs at first hnless lohre dhtch."
