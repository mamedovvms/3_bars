# Разбор файла с информацией о барах

Скрипту разбирает файл, в котором в формате
json находятся данные о барах. Его можно скачать в формате JSON. Для этого нужно:
зарегистрироваться на сайте  [data.mos.ru](https://data.mos.ru/) и получить ключ API;
скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.
Скрипт после разбора выводит:
- самый большой бар
- самый маленький бар
- самый близкий баро

# Функции

```python def load_data(filepath)``` - функция получения списка с данными баров

```python def get_biggest_bar(json_data)``` - функция возвращает данные по самому большому бару

```python def get_smallest_bar(json_data)``` - функция возвращает данные по самому маленькому бару

```python def get_closest_bar(json_data, longitude, latitude)``` - функция возвращает самый блазкий бар к пользователю,
по долготе и широте нахождения пользователя.


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
$ python bars.py g:\json_bars.txt 37.464747 55.78499# possibly requires call of python3 executive instead of just python
```
В качестве параметров передается файл в формате json с данными баров, долгота и широта пользователя

#Пример:
```bash
$python bars.py g:\json_bars.txt 37.464747 55.78499

Biggest bar:  Спорт бар «Красная машина» по адресу Автозаводская улица, дом 23, строение 1
Smallest bar: БАР. СОКИ по адресу Дубравная улица, дом 34/29
Closest bar:  Таверна по адресу проспект Защитников Москвы, дом 8
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
