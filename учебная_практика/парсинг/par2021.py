import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import parsing_module as pm


# Общая часть парсинга за 2021 год
url = 'https://monitoring.miccedu.ru/iam/2021/_vpo/inst.php?id=100256'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'lxml')




# Парсинг верхней части названия таблицы
t_name_up = soup.find('table', id = 'result').thead.tr # Заголовок таблицы
t_name_up = t_name_up.contents
pm.clear_(t_name_up)
t_name_up = pm.inside_text(t_name_up)




# Парсинг нижней части названия таблицы и обработка
t_name_down = list(soup.find('table', id = 'result').thead.tr.next_siblings)
pm.clear_(t_name_down) # Очистка
t_name_down = t_name_down[0].contents
pm.clear_(t_name_down) # Очистка
t_name_down = pm.inside_text(t_name_down)


# Объединение Наименования таблицы
t_name_up.append(t_name_up[-1])
t_name_up.append(t_name_up[-1])
for i in range(1,4,1):
    t_name_up[-i] = t_name_up[-i] +' ' + t_name_down[-i]

table_name = t_name_up.copy()


# Парсинг тела таблицы
body_table =  list(soup.find('table', id = 'result').thead.next_siblings)
pm.clear_(body_table)


body_table = pm.table_row(body_table) # СОСТАВИЛИ ТЕЛО ФУНКЦИИ


# Первая таблица: Сведения по показателям мониторинга эффективности деятельности
table1_2021 = pm.create_table(table_name, body_table)



# Парсинг остальных таблиц:
lst_tables_2021 = pm.parsing_more_tables(soup, 6)


# Парсинг таблиц Роль организации в системе подготовки кадров для региона
lst_tables_region_2021 = pm.create_part_of_table(soup, 'analis_reg')



# Парсинг дополнительной таблицы
lst_tables_dop_2021 = pm.create_part_of_table(soup, 'analis_dop')

all_tables_2021 = [table1_2021, lst_tables_2021, lst_tables_region_2021, lst_tables_dop_2021]