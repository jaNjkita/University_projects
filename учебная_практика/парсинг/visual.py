import matplotlib.pyplot as plt

from union_of_data import all_years # Данные за все года


def to_float(lst):
    '''Данные парсятся в виде строк, но для корректной работы числовые значения
    должны быть в float. Данная функция принимает lst и конвертирует числа в строках
    во float'''
    lst = list(map(lambda x: float(x.replace(',', '.').replace(' ', '')), lst))
    return lst


years = ['2021', '2020', '2019', '2018', '2017', '2016', '2015'] # Список годом для извлечения данных таблиц словаря
years.reverse()


# Создаём словарь очищенных таблиц с баллами ЕГЭ
ekzam_balls = {year: 1 for year in years}
for year in years:
    ekzam_balls[year] = all_years[year][1].iloc[0:3:1] # Извлекаем баллы ЕГЭ
    ekzam_balls[year] = ekzam_balls[year].drop(columns = ['№ п/п', 'Единица измерения']) # Удаляем ненужные столбцы


# Словарь с призёрами олимпиад школьных или ВСЕРОСА
winners = {year: 1 for year in years}
for year in years:
    winners[year] = all_years[year][1].iloc[4:6:1]
    winners[year] = winners[year].drop(columns = ['№ п/п', 'Единица измерения'])

# Словарь с целевиками
targets = {year: 1 for year in years}
for year in years:
    targets[year] = all_years[year][1].iloc[6]
    targets[year] = targets[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь c магистрами имеющих дипломы из других вузов
mgs_from_out = {year: 1 for year in years}
for year in years:
    mgs_from_out[year] = all_years[year][1].iloc[10]
    mgs_from_out[year] = mgs_from_out[year].drop(index = ['№ п/п', 'Единица измерения'])


# Словарь c магистрами и аспирантами имеющих дипломы из других вузов
mgs_asp_from_out = {year: 1 for year in years}
for year in years:
    mgs_asp_from_out[year] = all_years[year][1].iloc[11]
    mgs_asp_from_out[year] = mgs_asp_from_out[year].drop(index = ['№ п/п', 'Единица измерения'])




# Словарь c долей магистров от общего числа студентов
procent_of_mgs = {year: 1 for year in years}
for year in years:
    procent_of_mgs[year] = all_years[year][1].iloc[8]
    procent_of_mgs[year] = procent_of_mgs[year].drop(index = ['№ п/п', 'Единица измерения'])


# Словарь c долей магистров и аспирантов от общего числа студентов
procent_of_mgs_asp = {year: 1 for year in years}
for year in years:
    procent_of_mgs_asp[year] = all_years[year][1].iloc[9]
    procent_of_mgs_asp[year] = procent_of_mgs_asp[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с доходами от НИОКР
income_of_NIOKR = {year: 1 for year in years}
for year in years:
    income_of_NIOKR[year] = all_years[year][2].iloc[6]
    income_of_NIOKR[year] = income_of_NIOKR[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с долей иностранных студентов из СНГ от общего числа
not_from_SNG = {year: 1 for year in years}
for year in years:
    not_from_SNG[year] = all_years[year][3].iloc[0]
    not_from_SNG[year] = not_from_SNG[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с долей иностранных студентов не из СНГ от общего числа
from_SNG = {year: 1 for year in years}
for year in years:
    from_SNG[year] = all_years[year][3].iloc[1]
    from_SNG[year] = from_SNG[year].drop(index = ['№ п/п', 'Единица измерения'])




# Словарь с выделенными средствами на НИОКР от иностранных граждан и юридических лиц
income_of_inostr_to_NIOKR = {year: 1 for year in years}
for year in years:
    income_of_inostr_to_NIOKR[year] = all_years[year][3].iloc[11]
    income_of_inostr_to_NIOKR[year] = income_of_inostr_to_NIOKR[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с выделенными средствами от иностранных граждан и юридических лиц
income_of_inostr = {year: 1 for year in years}
for year in years:
    income_of_inostr[year] = all_years[year][3].iloc[12]
    income_of_inostr[year] = income_of_inostr[year].drop(index = ['№ п/п', 'Единица измерения'])





# Общая численность иностранных студентов
quantity_of_inostr = {year: 1 for year in years}
for year in years:
    quantity_of_inostr[year] = all_years[year][-1].iloc[0]
    quantity_of_inostr[year] = quantity_of_inostr[year].drop(index = ['№ п/п', 'Единица измерения'])




# Доля иностранных студентов
proportion_of_inostr = {year: 1 for year in years}
for year in years:
    proportion_of_inostr[year] = all_years[year][-1].iloc[1]
    proportion_of_inostr[year] = proportion_of_inostr[year].drop(index = ['№ п/п', 'Единица измерения'])





# Доходы вуза из всех источников
revenue = {year: 1 for year in years}
for year in years:
    revenue[year] = all_years[year][-1].iloc[0]
    revenue[year] = revenue[year].drop(index = ['№ п/п', 'Единица измерения'])




# Доходы вуза из внебюджетных источников
revenue_off_budget = {year: 1 for year in years}
for year in years:
    revenue_off_budget[year] = all_years[year][-1].iloc[1]
    revenue_off_budget[year] = revenue_off_budget[year].drop(index = ['№ п/п', 'Единица измерения'])




# Количество студентов ежегодно на очном обучении
quontity_full_time_students = {year: 1 for year in years}
for year in years:
    quontity_full_time_students[year] = all_years[year][-6].iloc[1]
    quontity_full_time_students[year] = quontity_full_time_students[year].drop(index = ['№ п/п', 'Единица измерения'])




# Количество студентов ежегодно на очно-заочном обучении
quontity_full_part_time_students = {year: 1 for year in years}
for year in years:
    quontity_full_part_time_students[year] = all_years[year][-6].iloc[2]
    quontity_full_part_time_students[year] = quontity_full_part_time_students[year].drop(index = ['№ п/п', 'Единица измерения'])



# Количество студентов ежегодно на заочном обучении
quontity_part_time_students = {year: 1 for year in years}
for year in years:
    quontity_part_time_students[year] = all_years[year][-6].iloc[3]
    quontity_part_time_students[year] = quontity_part_time_students[year].drop(index = ['№ п/п', 'Единица измерения'])





# Средний балл ЕГЭ по всем формам обучения
average_ball = {year: 1 for year in years}
for year in years:
    average_ball[year] = all_years[year][-6].iloc[4]
    average_ball[year] = average_ball[year].drop(index = ['№ п/п', 'Единица измерения'])





# Словарь с публикациями за год научных работников
publications = {year: 1 for year in years}
for year in years:
    publications[year] = all_years[year][-5].iloc[2]
    publications[year] = publications[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с общей численностью професоро-преподавательского состава образовательной организации
quantity_of_pps = {year: 1 for year in years}
for year in years:
    quantity_of_pps[year] = all_years[year][-4].iloc[1]
    quantity_of_pps[year] = quantity_of_pps[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с общей численностью научных работников образовательной организации
quantity_of_sience_workers = {year: 1 for year in years}
for year in years:
    quantity_of_sience_workers[year] = all_years[year][-4].iloc[2]
    quantity_of_sience_workers[year] = quantity_of_sience_workers[year].drop(index = ['№ п/п', 'Единица измерения'])


# Словарь с зарплатой ППС
salary_of_pps = {year: 1 for year in years}
for year in years:
    salary_of_pps[year] = all_years[year][-4].iloc[-2]
    salary_of_pps[year] = salary_of_pps[year].drop(index = ['№ п/п', 'Единица измерения'])



# Словарь с зарплатой научных работников образовательной организации
salary_of_sience_workers = {year: 1 for year in years}
for year in years:
    salary_of_sience_workers[year] = all_years[year][-4].iloc[-1]
    salary_of_sience_workers[year] = salary_of_sience_workers[year].drop(index = ['№ п/п', 'Единица измерения'])





# Словарь с количество аспирантов
quantity_asp = {year: 1 for year in years}
for year in years:
    quantity_asp[year] = all_years[year][-5].iloc[7]
    quantity_asp[year] = quantity_asp[year].drop(index = ['№ п/п', 'Единица измерения'])




# Кандидаты наук
doctors = {year: 1 for year in years}
for year in years:
    if int(year) <= 2018:
        doctors[year] = all_years[year][7].iloc[0]
        doctors[year] = doctors[year].drop(index = ['№ п/п', 'Единица измерения'])
    else:
        doctors[year] = all_years[year][6].iloc[0]
        doctors[year] = doctors[year].drop(index = ['№ п/п', 'Единица измерения'])




# Кандидаты наук
candidates = {year: 1 for year in years}
for year in years:
    if int(year) <= 2018:
        candidates[year] = all_years[year][7].iloc[1]
        candidates[year] = candidates[year].drop(index = ['№ п/п', 'Единица измерения'])
    else:
        candidates[year] = all_years[year][6].iloc[1]
        candidates[year] = candidates[year].drop(index = ['№ п/п', 'Единица измерения'])











# ВИЗУАЛИЗАЦИЯ
###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in ekzam_balls:
    values.append(ekzam_balls[year].iloc[0,1])

# Строим гистограмму для 1 группы лиц
values = to_float(values)
title = ekzam_balls['2021'].iloc[0,0].replace('мам ', 'мам\n', 1)
plt.title(title) # Название для графика
plt.bar(years, values)
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in ekzam_balls:
    values.append(ekzam_balls[year].iloc[1,1])

values = to_float(values)
title = ekzam_balls['2021'].iloc[1,0].replace('средств ', 'средств\n', 1)
plt.title(title) # Название для графика
plt.bar(years, values, color = 'orange')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in ekzam_balls:
    values.append(ekzam_balls[year].iloc[2,1])

values = to_float(values)
title = ekzam_balls['2021'].iloc[2,0].replace('с ', 'с\n', 1)
plt.title(title) # Название для графика
plt.bar(years, values, color = 'red')
plt.grid(which = 'both')
plt.show()
###############################################################################




# Призёры ВСЕРОСА
###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in winners:
    values.append(winners[year].iloc[0,1])

values = to_float(values)
title = 'Численность студентов обедители ВсеРоса, принятых на очную форму обучения на первый курс по программам бакалавриата и специалитета без вступительных испытаний'
plt.title(title) # Название для графика
plt.bar(years, values, color = 'red')
plt.grid(which = 'both')
plt.show()
###############################################################################




# Призёры
###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in winners:
    values.append(winners[year].iloc[1,1])

values = to_float(values)
title = 'Численность студентов, победителей и призеров олимпиад школьников,\nпринятых на очную форму обучения на первый курс\n по программам бакалавриата и специалитета по специальностям и (или) направлениям подготовки,\n соответствующим профилю олимпиады школьников, без вступительных испытаний'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#CD5C5C')
plt.grid(which = 'both')
plt.show()
###############################################################################





###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in targets:
    values.append(targets[year].iloc[1])

values = to_float(values)
title = 'Численность студентов, принятых по результатам целевого приема\nна первый курс на очную форму обучения по программам бакалавриата и специалитета'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FF00FF')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in mgs_from_out:
    values.append(mgs_from_out[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности студентов, имеющих диплом бакалавра, специалиста или магистра других организаций,\nпринятых на первый курс на обучение по программам магистратуры\n образовательной организации, в общей численности студентов, принятых на первый курс по программам магистратуры на очную форму обучения\n(в %)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#CDAD00')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in mgs_asp_from_out:
    values.append(mgs_asp_from_out[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности обучающихся по программам магистратуры и подготовки научно-педагогических кадров\n в аспирантуре, имеющих диплом бакалавра, диплом специалиста или\n диплом магистра других организаций в общей численности обучающихся по программам магистратуры\n и подготовки научно-педагогических кадров в аспирантуре (в %)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FFF68F')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in procent_of_mgs:
    values.append(procent_of_mgs[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности студентов (приведенного контингента), обучающихся по программам магистратуры,\n в общей численности приведенного контингента обучающихся\n по образовательным программам бакалавриата, специалитета и магистратуры (в %)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#8B658B')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in procent_of_mgs_asp:
    values.append(procent_of_mgs_asp[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности обучающихся (приведенного контингента), по программам магистратуры\n и подготовки научно-педагогических кадров в аспирантуре в общей численности приведенного контингента обучающихся\n по основным образовательным программам высшего образования (в %)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#00FFFF')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in income_of_NIOKR:
    values.append(income_of_NIOKR[year].iloc[1])

values = to_float(values)
title = 'Общий объем научно-исследовательских и опытно-конструкторских работ (далее – НИОКР) (в тысячах рублях)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#008B8B')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in not_from_SNG:
    values.append(not_from_SNG[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности иностранных студентов не из СНГ, обучающихся программам бакалавриата,\nспециалитета, магистратуры, в общей численности студентов (приведенный контингент) (в %)'
plt.title(title) # Название для графика
plt.bar(years, values, color = 'blue')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in from_SNG:
    values.append(from_SNG[year].iloc[1])

values = to_float(values)
title = 'Удельный вес численности иностранных студентов из СНГ, обучающихся по программам бакалавриата,\nспециалитета, магистратуры, в общей численности студентов (приведенный контингент)'
plt.title(title) # Название для графика
plt.bar(years, values, color = 'red')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in income_of_inostr_to_NIOKR:
    values.append(income_of_inostr_to_NIOKR[year].iloc[1])

values = to_float(values)
title = 'Объем средств, полученных образовательной организацией на выполнение НИОКР\nот иностранных граждан и иностранных юридических лиц (в тыс. рублях)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FF7256')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in income_of_inostr:
    values.append(income_of_inostr[year].iloc[1])

values = to_float(values)
title = 'Объем средств от образовательной деятельности, полученных образовательной организацией\n от иностранных граждан и иностранных юридических лиц (в тыс. рублях)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#F4A460')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quantity_of_inostr:
    values.append(quantity_of_inostr[year].iloc[1])

values = to_float(values)
title = 'Общая численность иностранных студентов, обучающихся по программам бакалавриата, специалитета, магистратуры'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FF69B4')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in proportion_of_inostr:
    values.append(proportion_of_inostr[year].iloc[1])

values = to_float(values)
title = 'Доля иностранных студентов в общей численности студентов, обучающихся по программам бакалавриата, специалитета, магистратуры'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#98F5FF')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in revenue:
    values.append(revenue[year].iloc[1])

values = to_float(values)
title = 'Доходы вуза  из всех источников (в тыс. рублях)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#98F5FF')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in revenue_off_budget:
    values.append(revenue_off_budget[year].iloc[1])

values = to_float(values)
title = 'Доходы вуза  из внебюджетных источников (в тыс. рублях)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#9370DB')
plt.grid(which = 'both')
plt.show()
###############################################################################












# Число студентов
###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quontity_full_time_students:
    values.append(quontity_full_time_students[year].iloc[1])

values = to_float(values)
title = 'Число студентов обучающихся на очной форме обучения'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FF7256')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quontity_full_part_time_students:
    values.append(quontity_full_part_time_students[year].iloc[1])

values = to_float(values)
title = 'Число студентов обучающихся на очно-заочной форме обучения'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#9370DB')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quontity_part_time_students:
    values.append(quontity_part_time_students[year].iloc[1])

values = to_float(values)
title = 'Число студентов обучающихся на заочной форме обучения'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#3CB371')
plt.grid(which = 'both')
plt.show()
###############################################################################




###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in average_ball:
    values.append(average_ball[year].iloc[1])

values = to_float(values)
title = 'Средний балл ЕГЭ студентов, принятых на обучение по программам бакалавриата и специалитета, по всем формам обучения'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#3CB371')
plt.grid(which = 'both')
plt.show()
###############################################################################














# НАУЧНАЯ РАБОТА
###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in publications:
    values.append(publications[year].iloc[1])

values = to_float(values)
title = 'Общее количество публикаций организации в расчете на 100 НПР'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#1E90FF')
plt.grid(which = 'both')
plt.show()
###############################################################################


###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quantity_asp:
    values.append(quantity_asp[year].iloc[1])

values = to_float(values)
title = 'Общая численность аспирантов (адъюнктов), интернов, ординаторов, ассистентов-стажеров'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#3CB371')
plt.grid(which = 'both')
plt.show()
###############################################################################





###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in candidates:
    values.append(candidates[year].iloc[1])

values = to_float(values)
title = 'Удельный вес НПР, имеющих ученую степень кандидата наук, в общей численности НПР'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#6A5ACD')
plt.grid(which = 'both')
plt.show()
###############################################################################


###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in doctors:
    values.append(doctors[year].iloc[1])

values = to_float(values)
title = 'Удельный вес НПР имеющих ученую степень доктора наук, в общей численности НПР'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#778899')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quantity_of_pps:
    values.append(quantity_of_pps[year].iloc[1])

values = to_float(values)
title = 'Общая численность ППС (без внешних совместителей и работающих по договорам ГПХ)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#125341')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in quantity_of_sience_workers:
    values.append(quantity_of_sience_workers[year].iloc[1])

values = to_float(values)
title = 'Общая численность научных работников (без внешних совместителей и работающих по договорам ГПХ)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#772399')
plt.grid(which = 'both')
plt.show()
###############################################################################


###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in salary_of_pps:
    values.append(salary_of_pps[year].iloc[1])

values = to_float(values)
title = 'Средняя заработная плата ППС (без внешних совместителей и работающих по договорам ГПХ)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#7788FF')
plt.grid(which = 'both')
plt.show()
###############################################################################



###############################################################################
values = [] # Данная переменная будет хранить значения по оси Y у гистограммы
for year in salary_of_sience_workers:
    values.append(salary_of_sience_workers[year].iloc[1])

values = to_float(values)
title = 'Средняя заработная плата научных работников (без внешних совместителей и работающих по договорам ГПХ)'
plt.title(title) # Название для графика
plt.bar(years, values, color = '#FF8899')
plt.grid(which = 'both')
plt.show()
###############################################################################