import cgi
import html

form = cgi.FieldStorage()

fio = form.getfirst("fio", "Не задано")
name_university = form.getfirst("name_university", "Не задано")
tel_number = form.getfirst("tel_number", "Не задано")

fio = html.escape(fio)
name_university = html.escape(name_university)
tel_number = html.escape(tel_number)

print("Content-type text/html")
print()
print("""<!DOCTYPE HTML>
        <html>
            <head>
                <title>Каторгин М.К. ИВТ-М-1-Д-2021-1</title>
            </head>
    <body>""")
print("<h1>Обработка</h1>")

print("<p>Фамилия, Инициалы: {}</p>".format(fio))
print("<p>Наименование университета: {}</p>".format(name_university))
print("<p>Мобильный телефон: {}</p>".format(tel_number))
print("</html>")

#Запись имен и значений в "names.txt" с помощью writelines()

file = open('names.txt', 'w')
file.writelines("ФИО: fio\n" + "Наименование университета: name_university\n" + "Мобильный телефон: tel_number")
file.close()

#Запись имен и значений в "values.txt" с помощью writelines()

file = open('values.txt', 'w')
file.writelines("ФИО: " + fio + "\n" + "Наименование университета:" + name_university +"\n"
                + "Мобильный телефон:" + tel_number)
file.close()

#Определение длины файла "names.txt"

file = open('names.txt', 'r')
fileReader = file.read()
print("<p> Длина файла names.txt: ", len(fileReader), "</p>")
file.close()

#Определение длины файла "values.txt"

file = open('values.txt', 'r')
fileReader = file.read()
print("<p> Длина файла values.txt: ", len(fileReader), "</p>")
file.close()

