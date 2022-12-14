# Идея: совместная разработка

# Система собирает информацию с датчиков, в ней есть
# модуль логирования, который заносит в журнал все обращения к датчикам.
# В системе есть модуль, выполняющий обращение для 
# получения данных с датчиков и модуля генерации
# html-представления.
# Запуск системы осуществляется из головного модуля.

# Выделяется 5 модулей

# Модуль 1: сбор информации с датчиков
# Модуль 2: логирование
# Модуль 3: UI
# Модуль 4: HTML-генератор
# Модуль 5: главный модуль

# Название файлов .py даём соответствующие

# Модуль 1: data_provider
# Модуль 2: logger
# Модуль 3: user_interface
# Модуль 4: html_creater
# Модуль 5: main


import html_creater as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))






