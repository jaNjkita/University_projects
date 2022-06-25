import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

import visual as vl

years = ['2021', '2020', '2019', '2018', '2017', '2016', '2015']
years.reverse()

publications = [vl.publications[year].iloc[1] for year in  years]
quantity_asp = [vl.quantity_asp[year].iloc[1] for year in  years]
income_of_NIOKR = [vl.income_of_NIOKR[year].iloc[1] for year in  years]
income_of_inostr_to_NIOKR = [vl.income_of_inostr_to_NIOKR[year].iloc[1] for year in  years]
income_of_inostr = [vl.income_of_inostr[year].iloc[1] for year in  years]
quantity_of_pps = [vl.quantity_of_pps[year].iloc[1] for year in  years]
quantity_of_sience_workers = [vl.quantity_of_sience_workers[year].iloc[1] for year in  years]
salary_of_pps = [vl.salary_of_pps[year].iloc[1] for year in  years]
salary_of_sience_workers  = [vl.salary_of_sience_workers[year].iloc[1] for year in  years]
revenue = [vl.revenue[year].iloc[1] for year in  years]
revenue_off_budget = [vl.revenue_off_budget[year].iloc[1] for year in  years]




# Количество студентов
quontity_full_time_students = [vl.quontity_full_time_students[year].iloc[1] for year in  years]
quontity_full_part_time_students = [vl.quontity_full_part_time_students[year].iloc[1] for year in  years]
quontity_part_time_students = [vl.quontity_part_time_students[year].iloc[1] for year in  years]
from_SNG = [vl.from_SNG[year].iloc[1] for year in  years]
not_from_SNG = [vl.not_from_SNG[year].iloc[1] for year in  years]

# Объединим данные для корреляции
data_1 = pd.DataFrame(
    data = {
        'Количество публикаций' : vl.to_float(publications),
        'Количество аспирантов' : vl.to_float(quantity_asp),
        'Общий объем научно-исследовательских и опытно-конструкторских работ' : vl.to_float(income_of_NIOKR),
        'Количество ППС' : vl.to_float(quantity_of_pps),
        'Количество научных работников' : vl.to_float(quantity_of_sience_workers),
        'Зарплаты ППС' : vl.to_float(salary_of_pps),
        'Зарплаты научных работников' : vl.to_float(salary_of_sience_workers),
        'Объем средств, полученный от иностранных граждан и юр. лиц на НИОКР' : vl.to_float(income_of_inostr_to_NIOKR)
        },
    index = years
    )



data_2 = pd.DataFrame(
    data = {
        'Количество студентов обучающихся на очном обучении' : vl.to_float(quontity_full_time_students),
        'Количество студентов обучающихся на очно-заочном обучении' : vl.to_float(quontity_full_part_time_students),
        'Количество студентов обучающихся на заочном обучении' : vl.to_float(quontity_part_time_students),
        'Количество аспирантов' : vl.to_float(quantity_asp),
        'Количество ППС' : vl.to_float(quantity_of_pps),
        'Количество научных работников' : vl.to_float(quantity_of_sience_workers),
        'Зарплаты ППС' : vl.to_float(salary_of_pps),
        'Зарплаты научных работников' : vl.to_float(salary_of_sience_workers),
        'Доходы вуза из всех источников' : vl.to_float(revenue),
        },
    index = years
    )




data_3 = pd.DataFrame(
    data = {
        'Зарплаты ППС' : vl.to_float(salary_of_pps),
        'Зарплаты научных работников' : vl.to_float(salary_of_sience_workers),
        'Количество ППС' : vl.to_float(quantity_of_pps),
        'Количество научных работников' : vl.to_float(quantity_of_sience_workers),
        'Доходы вуза  из всех источников' : vl.to_float(revenue),
        'Общий объем научно-исследовательских и опытно-конструкторских работ' : vl.to_float(income_of_NIOKR),
        'Объем средств, полученный от иностранных граждан и юр. лиц' : vl.to_float(income_of_inostr),
        'Объем средств, полученный от иностранных граждан и юр. лиц на НИОКР' : vl.to_float(income_of_inostr_to_NIOKR),
        },
    index = years
    )


data_4 = pd.DataFrame(
    data = {
        'Процент иностранных студентов из СНГ' : vl.to_float(from_SNG),
        'Процент иностранных студентов не из СНГ' : vl.to_float(not_from_SNG),
        'Количество студентов обучающихся на очном обучении' : vl.to_float(quontity_full_time_students),
        'Количество студентов обучающихся на очно-заочном обучении' : vl.to_float(quontity_full_part_time_students),
        'Количество студентов обучающихся на заочном обучении' : vl.to_float(quontity_part_time_students),
        'Количество ППС' : vl.to_float(quantity_of_pps),
        'Количество научных работников' : vl.to_float(quantity_of_sience_workers),
        
        },
    index = years
    )




corrmat_data_1 = data_1.corr()
sn.heatmap(corrmat_data_1, annot = True, linewidths = 0.1)
plt.show()


corrmat_data_2 = data_2.corr(method='spearman')
sn.heatmap(corrmat_data_2, annot = True, linewidths = 0.1)
plt.show()


corrmat_data_3 = data_3.corr(method='spearman')
sn.heatmap(corrmat_data_3, annot = True, linewidths = 0.1)
plt.show()


corrmat_data_4 = data_4.corr()
sn.heatmap(corrmat_data_4, annot = True, linewidths = 0.1)
plt.show()