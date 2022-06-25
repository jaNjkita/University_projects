import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import parsing_module as pm


# Общая часть парсинга за 2018 год
url = 'https://monitoring.miccedu.ru/iam/2018/_vpo/inst.php?id=100256'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'lxml')




# Парсинг названия таблицы
table_name = soup.find('table', id = 'result').thead.contents # Заголовок таблицы
pm.clear_(table_name)
table_name = pm.inside_text(table_name)



# Парсинг тела таблицы
body_table =  list(soup.find('table', id = 'result'))
pm.clear_(body_table)
body_table.pop(0)

body_table = pm.table_row(body_table)

# Первая таблица: Сведения по показателям мониторинга эффективности деятельности
table1_2018 = pm.create_table(table_name, body_table)



# Парсинг остальных таблиц:
lst_tables_2018 = pm.parsing_more_tables(soup, 7)







# Парсинг таблиц Роль организации в системе подготовки кадров для региона
lst_tables_region_2018 = pm.create_part_of_table(soup, 'analis_reg')



# Парсинг дополнительной таблицы
lst_tables_dop_2018 = pm.create_part_of_table(soup, 'analis_dop')



all_tables_2018 = [table1_2018, lst_tables_2018, lst_tables_region_2018, lst_tables_dop_2018]