#!/usr/bin/env python3

import cgi, cgitb
import re
print("Content-Type: text/html\n")

# Принимаем данные из формы
form = cgi.FieldStorage()
data1 = form.getvalue("data1", "None")
data2 = form.getvalue("data2", "None")
data3 = form.getvalue("data3", "None")
lit = form.getvalue("lit", "None")

# Фамилия и имя студента должны начинаться с заглавной буквы
data1_reg = re.compile(r"Группа ([a-zA-Za-яА-Я0-9]*\s?) ст. ([a-zA-Za-яА-Я0-9]*\s?)")#Группа {} ст. {}
data2_reg = re.compile(r"И.О. Фамилия ([А-Я][а-я]*\s?)")#И.О. Фамилия {}
data3_reg = re.compile(r"Номер тел. [0-9]{6}")
lit_reg = re.compile(r"[\"[\s0-9],*")

print("<h3>Получение данных</h3>")
print("data1: ", data1)
print("<br>data2: ", data2)
print("<br>data3: ", data3)
print("<br>Литерал: ", lit, "<hr>")


if re.search(data1_reg, data1):
	print("<br>Данные 1 введены верно")
else:
	print("<br>Данные 1 введены неверно")

if data2_reg.match(data2):
	print("<br>Данные 2 введены верно")
else:
	print("<br>Данные 2 введены неверно")

if data3_reg.search(data3):
	print("<br>Данные 3 введены верно")
else:
	print("<br>Данные 3 введены неверно")

if re.match(lit_reg, lit):
	print("<br>Литерал введен верно")
else:
	print("<br>Литерал введен неверно")
