from par2021 import all_tables_2021
from par2020 import all_tables_2020
from par2019 import all_tables_2019
from par2018 import all_tables_2018
from par2017 import all_tables_2017
from par2016 import all_tables_2016
from par2015 import all_tables_2015


all_years = [
    all_tables_2021, all_tables_2020, all_tables_2019,
    all_tables_2018, all_tables_2017,all_tables_2016, all_tables_2015
    ]

def flattenlist(_2dlist):
    '''Функция сглаживает 2D массивы'''
    flatlist = [] 
    for item in _2dlist: 
        if type(item) is list:
            for element in item: 
                flatlist.append(element) 
        else: 
            flatlist.append(item) 
    return flatlist 

def data_of_years(all_data):
    '''Функция создаёт список с таблицами DataFrame за каждый год'''
    for i in range(len(all_data)):
        all_data[i] = flattenlist(all_data[i])
        # Пока в разработке, если не хвати времени просто удали участок кода ниже
    keys = []
    for i in range(2021, 2014, -1):
        keys.append(f'{i}')
    d = {i: 1 for i in keys}
    for i in range(len(keys)):
        d[keys[i]] = all_data[i]
    return d

all_years = data_of_years(all_years)