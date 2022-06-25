import pandas as pd
import numpy as np



# Функция очистки содержимого тегов от переносов строк внутри таблицы
def clear_(tr):
    '''
    Данная функиця удаляет табуляцию в строках таблицы (внутри тегов tr).
    '''
    for i in range(tr.count('\n')):
        tr.remove('\n')
    for i in range(tr.count(' ')):
        tr.remove(' ')
    for i in range(tr.count('')):
        tr.remove('')


# Функция извлечения содержимого внутри тегов
def inside_text(tr):
    '''
    Данная функция получает текстовое содержимое внутри строки таблицы (тега tr)
    '''
    if len(tr) != 1:
        return list(map(lambda teg: teg.text, tr))
    else:
        return [tr.text]


# Функция обработки тела таблицы
def table_row(tab):
    '''
    Данная функция создаёт двумерный список с содержимым таблицы.
    Каждый подсписок - это строка таблицы. Элементы подсписка содержимое тегов td
    '''
    l = len(tab)
    res = [[] for i in range(l)]
    for row in range(l):
        
        clear_(tab[row].contents)
        for col in tab[row].contents:
            res[row].append(col.text)
    return res


# Создание DataFrame таблицы:
def create_table(tab_name, tab_body):
    '''
    Эта функция создаёт DataFrame объект спарсенной таблицы.
    '''
    tab_body = np.transpose(tab_body)
    data = {
        key:None for key in tab_name
        }
    keys = list(data.keys())
    for i in range(len(data)):
        data[keys[i]] = tab_body[i]
    return pd.DataFrame(
        data = data
        )



def parsing_more_tables(soup, n):
    '''
    Эта функция, которая парсит сразу несколько таблиц, которые имеют атрибут
    class со значением napde. Возвращает список DataFrame объектов.
    '''
    lst_table = []
    for i in range(0,n,1):
        table = soup.find_all('table', class_ = 'napde')[i].contents
        clear_(table) # Таблица

        # Парсинг имени таблицы
        table_name = inside_text(list(table[0]))
        clear_(table_name)


        # Парсинг тела таблицы
        clear_(table)
        table.pop(0)
        table_body = table_row(table)
        lst_table.append(create_table(table_name, table_body))
    return lst_table





def create_part_of_table(soup, id_):
    
    '''
    Данная функция разбивает одну таблицу на две подтаблицы в том случае,
    когда в какой-то строке таблицы написан критерий наименование.
    Функция находит такие строки названия и их содержимое берёт за одну таблицу.
    То есть если таких строк названий в таблице n, то функция создаст n таблиц
    '''
    
    table_name = soup.find('table', id = id_).thead.tr.contents
    clear_(table_name)
    table_name = inside_text(table_name) # Готовое имя таблицы
    
    table_body = soup.find('table', id = id_).contents
    clear_(table_body)
    table_body.pop(0) # Удаление названий полей таблицы
    table_body = table_row(table_body) # Основное тело таблицы в формате списка

    
    # Позиции строк
    pos_str = []
    for i in range(len(table_body)):
        if len(table_body[i]) == 1:
            pos_str.append(i)
            

    pos_str.append(len(table_body))
    #print('Строки', pos_str)
    
    # Готовые списки тел частей таблиц
    lst_part_of_table = []
    for i in range(len(pos_str)-1):
        tp = table_body[pos_str[i]+1:pos_str[i+1]]
        for i in range(len(tp)): # Добавление значений в подстроках строки
            if len(tp[i])==3:
                tp[i].insert(0, f'1.{i}')
        tp = create_table(table_name, tp)
        lst_part_of_table.append(tp)

    return lst_part_of_table





def create_part_of_table_2(soup, id_):
    
    '''
    Данная функция работает аналогично функции create_part_of_table,
    но она разбивает обобщающий столбец, на подстолбцы
    '''
    
    str11 = 'Число вузов, частично реализующих образовательные программы данной УГН(С), в регионе'
    str12 = 'Число вузов, плохо реализующих образовательные программы данной УГН(С), в регионе2'
    str21 = 'Число филиалов, частично реализующих образовательные программы данной УГН(С), в регионе'
    str22 = 'Число филиалов, плохо реализующих образовательные программы данной УГН(С), в регионе'
    table_name = soup.find('table', id = id_).thead.tr.contents
    clear_(table_name)
    table_name = inside_text(table_name) # Готовое имя таблицы
    table_name.insert(-1, str11)
    table_name.insert(-1, str12)
    table_name.append(str21)
    table_name.append(str22)
    clear_(table_name)
    
    table_body = soup.find('table', id = id_).contents
    clear_(table_body)
    table_body.pop(0) # Удаление названий полей таблицы
    table_body = table_row(table_body) # Основное тело таблицы в формате списка

    
    # Позиции строк
    pos_str = []
    for i in range(len(table_body)):
        if len(table_body[i]) == 1:
            pos_str.append(i)
            

    pos_str.append(len(table_body))

    
    # Готовые списки тел частей таблиц
    lst_part_of_table = []
    for i in range(len(pos_str)-1):
        tp = table_body[pos_str[i]+1:pos_str[i+1]]
        for i in range(len(tp)):
            tp[i].remove('')
        tp = create_table(table_name, tp)
        lst_part_of_table.append(tp)
        
    return lst_part_of_table




def create_part_of_table_3(soup, id_):
    
    '''
    Крч, эта функция для таблицы которая не соответсвует ниодному шаблону
    '''
    
   
    str1 = 'Число вузов, плохо реализующих образовательные программы данной УГН(С), в регионе2'
    str2 = 'Число филиалов, плохо реализующих образовательные программы данной УГН(С), в регионе'
    table_name = soup.find('table', id = id_).thead.tr.contents
    clear_(table_name)
    table_name = inside_text(table_name) # Готовое имя таблицы
    table_name.insert(-1, str1)

    table_name.append(str2)
    clear_(table_name)
    
    table_body = soup.find('table', id = id_).contents
    clear_(table_body)
    table_body.pop(0) # Удаление названий полей таблицы
    table_body = table_row(table_body) # Основное тело таблицы в формате списка

    
    # Позиции строк
    pos_str = []
    for i in range(len(table_body)):
        if len(table_body[i]) == 1:
            pos_str.append(i)
            

    pos_str.append(len(table_body))

    
    # Готовые списки тел частей таблиц
    lst_part_of_table = []
    for i in range(len(pos_str)-1):
        tp = table_body[pos_str[i]+1:pos_str[i+1]]
        for i in range(len(tp)):
            tp[i].remove('')
        tp = create_table(table_name, tp)
        lst_part_of_table.append(tp)
        
    return lst_part_of_table