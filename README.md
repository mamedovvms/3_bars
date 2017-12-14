# Ближайшие бары

Пользователь вводит путь к файлу с данными по барам в формате json, и gps-координаты.
Программа выводит:
    самый большой бар;
    самый маленький бар;
    самый близкий бар


# Функции

def load_data(filepath) - функция загрузки json данных из файла переданного в качестве параметра

def get_biggest_bar(data) - функция возвращает данные по самому большому бару

def get_smallest_bar(data) - функция возвращает данные по самому маленькому бару

def get_closest_bar(data, longitude, latitude) - функция возвращает самый блазкий бар

data - параметр. Данные в формате json

longitude, latitude - параметры gps - координат


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python

Программа предложит ввести путь к файлу и координаты

Пример:

Path to file: g:\json_bars.txt
Longitude: 37.464747
Latitude: 55.78499

Biggest bar:  {'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Smallest bar:  {'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Closest bar:  {'geometry': {'coordinates': [37.464747458690354, 55.784996653238544], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'dd1d7beb-1b51-4776-b7f9-7095098b0178', 'Attributes': {'global_id': 20660639, 'Name': 'Грэйс Бар', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Хорошёво-Мнёвники', 'Address': 'улица Маршала Тухачевского, дом 49', 'PublicPhone': [{'PublicPhone': '(499) 940-34-49'}], 'SeatsCount': 68, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
