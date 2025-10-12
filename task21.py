#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.
# Содержимое файла config_default.txt

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
#app_name    =  "NextGen"
#version     =  '1.0.0'
#debug       =  True

# Настройки базы данных
#db_host     =  5432
#.....


#Открытие файла для записи стартовых данных
f = open("config_default.txt","w+",encoding="utf-8")
f.write('''
app_name    = ?
version     = ?
debug       = ?
db_host     = ?
db_port     = ?
db_name     = ?
db_user     = ?
db_password = ?
api_key     = ?
api_secret  = ?
base_url    = ?
log_file    = ?
data_dir    = ?
temp_dir    = ?
''')

#Перенос курсора в начало
f.seek(0)

#Построчное чтение файла и запись строк в массив
set = f.readlines()
f.close()

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

temp = []
for key in  config_values.keys():
    for conf in set:
        if conf.find(key) == 0:
            temp += [conf.replace('?',str(config_values[key]))]



#Перезапись файла
f = open("config_default.txt","w",encoding="utf-8")
for  line in temp: f.write(line)
f.close()

#Открытие файла для чтения
f = open("config_default.txt","r+",encoding="utf-8")
f.seek(0)
print(f.read())
f.close()
exit()






