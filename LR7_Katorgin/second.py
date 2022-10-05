from multiprocessing.connection import wait
import struct
#Создание последовательности
a = bytes(range(0,10))
print("Сгенерированная последовательность: ", a)

#Запись в двоичный файл
file = open('binary_data.dat', 'wb')
file.write(a)
file.close()

#Чтение значения байта файла "binary_data.dat", перемещение с условием 4
#Смещение = 6, Откуда = 0
file = open('binary_data.dat', 'rb')
file.seek(4,0)#Перемещение указателя
b = file.read(4)
print('Значение байта №4: ', b)
file.close()
file = open('binary_data.dat', 'rb')
file.seek(6,0)

b = file.read(4)#Чтение 4 байтов
file.close()
print('Значение четырех байтов:', b)
file = open('binary_data.dat', 'rb')
#Перемещение указателя в конец
file.seek(4,0)
b = file.read(1)#Чтение последнего байта
file.close()
try :
   inputvalue = int(input('Введите цифру: '))
   assert(struct.pack('B', inputvalue) == b)
except AssertionError:
   print('Числа не совпадают')