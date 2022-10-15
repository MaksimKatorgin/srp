#!/usr/bin/env python3
import cgi, random
print("Content-Type: text/html\n")
#Создание экземпляра FieldStorage
form = cgi.FieldStorage()
#Среднего арифметическое чисел (Примечание: среднее значение = (сумма) / (количество))
def func1(list):
	arithmetic_mean = sum(list)/len(list)
	return arithmetic_mean
#Минимальное среди положительных чисел
def func2(list):
	return min([x for x in list if x > 0])
#Сортировка чисел, взятых по модудю 3
def func3(list):
	list.sort(key = lambda x: x % 3)
	return list
#Принимаем анализ данных, полученных из формы с целью определения:
#Группа 1: г) Среднего арифметического чисел
#Группа 2: а) Минимального числа среди положительных чисел
#Группа 3: б) Отсортированного по модулю 3 результата
print("<h1>Получение данных</h1>")
name = form.getvalue("name")
print("Имя пользователя: ", name, "<br><br>")

result_list = form.getlist("func")

number_list = []
for i in range(22): #Количество 22
	number_list.append(random.randrange(-25, 40)) #Диапазон (-25, 40)
print("Сгенерированный список: ", number_list, "<br>")

for i in result_list:
	if i == "func1":
		print("<br>Среднее арифметическое чисел: ", func1(number_list))
	if i == "func2":
		print("<br>Минимальное число среди положительных чисел:", func2(number_list))
	if i == "func3":
		print("<br>Отсортированный по модулю 3 результат:  ", func3(number_list))




