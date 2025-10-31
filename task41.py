# # todo: Создайте иерархию классов для экспорта данных в разные форматы.

# Для класса JSONExporter
import json, datetime
#Для класса CSVExporter
import csv, io
#Для класса XMLExporter
import xml.etree.ElementTree as ET

# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)

class DataExporter:
    def export(self,data):
        return 'Переопределяемый метод'

    def get_format_name(self):
        pass

    def validate_data(self, data):
        flag_none = 0
        for dict_ in data:
            if None in dict_.values():
                flag_none += 1
            else:
                flag_none += 0
        print(
            'Нет пустых значений' if flag_none == 0 else f'В данных {flag_none} строки, в которых есть хотя бы 1 пустое значение')


# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем

ct = datetime.datetime.now()
timestamp = ct.timestamp()

class JSONExporter(DataExporter):
    def export(self, data):
        for dict_ in data:
            dict_['export_timestamp'] = timestamp
        json_formatted_string = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        print(json_formatted_string)

    def get_format_name(self):
        return 'json'


# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента

class CSVExporter(DataExporter):
    def export(self, data):
        output = io.StringIO()
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()  # записать заголовки
        writer.writerows(data)  # записать строки из словарей

        csv_string = output.getvalue()  # получить CSV-строку
        output.close()

        print(csv_string)

    def get_format_name(self):
        return 'csv'

# XMLExporter:
# Создает XML структуру с корневым элементом <report>
class XMLExporter(DataExporter):
    def export(self, data):
        root = ET.Element("report")
        headers = sales_data[0].keys()
        for row in sales_data:
            for header in headers:
                child = ET.SubElement(root, header)
                child.text = str(row[header])

        xml_string = ET.tostring(root, encoding='unicode')
        print(xml_string)

    def get_format_name(self):
        return 'xml'



# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями


# Этот код должен работать после реализации:
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")