#
# Лабораторная работа №2
#
import scipy as sc
import numpy as np
import scipy as sc

#N = int (input('Введите количество элементов в исходном массиве: '))
N = 100
X = [N//4,N//2,N]

# Создание массивов с помощью numpy
A = np.random.randint(0,1000,N)
a1 = A [:(N//2)]
a2 = A [(N//2):(N//2 + N//4)]

B = np.sort(A)
b1 = B [:(N//2)]
b2 = B [(N//2):(N//2 + N//4)]

C = np.flip(B)
c1 = C [:(N//2)]
c2 = C [(N//2):(N//2 + N//4)]

# Сортировка методом слияния
def merge(left_list, right_list):  
	sorted_list = []
	left_list_index = right_list_index = 0

	left_list_length, right_list_length = len(left_list), len(right_list)

	for _ in range(left_list_length + right_list_length):
		if left_list_index < left_list_length and right_list_index < right_list_length:
			if left_list[left_list_index] <= right_list[right_list_index]:
				sorted_list.append(left_list[left_list_index])
				left_list_index += 1
			else:
				sorted_list.append(right_list[right_list_index])
				right_list_index += 1

		elif left_list_index == left_list_length:
			sorted_list.append(right_list[right_list_index])
			right_list_index += 1
		elif right_list_index == right_list_length:
			sorted_list.append(left_list[left_list_index])
			left_list_index += 1

	return sorted_list

def merge_sort(nums):

	if len(nums) <= 1:
		return nums

	mid = len(nums) // 2

	left_list = merge_sort(nums[:mid])
	right_list = merge_sort(nums[mid:])

	return merge(left_list, right_list)

# Сортировка из библиотеки numpy

def merge_sort_numpy(list):
	list.sort(axis=0,kind='mergesort')
	return list

# Замеряем время работы каждой функции
def time_counter(list,f):
	import timeit

	start_time = timeit.default_timer()
	f(list)
	k = timeit.default_timer() - start_time

	return k

# Сравнение через matlib
def graph_01(x,y1,y2,y3):

	import matplotlib.pyplot as plt

	plt.plot(x,y1,'r','-',linewidth=2,label='Случайный')
	plt.plot(x,y2,'y','-',linewidth=2,label='По возраст.')
	plt.plot(x,y3,'b','-',linewidth=2,label='По убыванию')

	y4 = y1 + y2 + y3
	y4.sort()

	plt.yticks(y4,y4)

	plt.show()


def print_title():

	print('Цвет графиков:\n\
		красный - случайный массив\n\
		желтынй - массив по возрастанию\n\
		синий - массив по убыванию\n')

print_title()

# Печать первой таблицы
def table_01():
	print('{:^50}'.format('Метод слияния'))
	print('┌','─'*4,'┬','─'*13,'┬','─'*12,'┬','─'*17,'┐',sep='')
	print('│{:^4}│{:^13}│{:^12}│{:^12}│'.format('№','Размерность','Вид','Затраченное время'))
	print('├','─'*4,'┼','─'*13,'┼','─'*12,'┼','─'*17,'┤',sep='')

	# Для больших массивов

	Y1 = [time_counter(a2,merge_sort),time_counter(a1,merge_sort),time_counter(A,merge_sort)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('1',len(A),'Случайный',Y1[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('2',len(a1),'Случайный',Y1[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('3',len(a2),'Случайный',Y1[0]))

	# Для средних массивов

	Y2 = [time_counter(b2,merge_sort),time_counter(b1,merge_sort),time_counter(B,merge_sort)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('4',len(B),'По возраст.',Y2[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('5',len(b1),'По возраст.',Y2[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('6',len(b2),'По возраст.',Y2[0]))

	# Для маленьких массивов

	Y3 = [time_counter(c2,merge_sort_numpy),time_counter(c1,merge_sort_numpy),time_counter(C,merge_sort_numpy)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('7',len(C),'По убыванию',Y3[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('8',len(c1),'По убыванию',Y3[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('9',len(c2),'По убыванию',Y3[0]))

	print('└','─'*4,'┴','─'*13,'┴','─'*12,'┴','─'*17,'┘',sep='')

	return Y1,Y2,Y3

y11,y22,y33=table_01()

graph_01(X,y11,y22,y33)
print()

# Печать второй таблицы
def table_02():

	print('{:^50}'.format('Метод mergesort numpy'))
	print('┌','─'*4,'┬','─'*13,'┬','─'*12,'┬','─'*17,'┐',sep='')
	print('│{:^4}│{:^13}│{:^12}│{:^12}│'.format('№','Размерность','Вид','Затраченное время'))
	print('├','─'*4,'┼','─'*13,'┼','─'*12,'┼','─'*17,'┤',sep='')

	# Для больших массивов

	Y1 = [time_counter(a2,merge_sort_numpy),time_counter(a1,merge_sort_numpy),time_counter(A,merge_sort_numpy)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('1',len(A),'Случайный',Y1[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('2',len(a1),'Случайный',Y1[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('3',len(a2),'Случайный',Y1[0]))

	# Для средних массивов

	Y2 = [time_counter(b2,merge_sort_numpy),time_counter(b1,merge_sort_numpy),time_counter(B,merge_sort_numpy)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('4',len(B),'По возраст.',Y2[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('5',len(b1),'По возраст.',Y2[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('6',len(b2),'По возраст.',Y2[0]))

	# Для маленьких массивов

	Y3 = [time_counter(c2,merge_sort_numpy),time_counter(c1,merge_sort_numpy),time_counter(C,merge_sort_numpy)]

	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('7',len(C),'По убыванию',Y3[2]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('8',len(c1),'По убыванию',Y3[1]))
	print('│{:^4}│{:^13d}│{:^12}│{:^17.1e}│'.format('9',len(c2),'По убыванию',Y3[0]))

	print('└','─'*4,'┴','─'*13,'┴','─'*12,'┴','─'*17,'┘',sep='')

	return Y1,Y2,Y3

y1,y2,y3 = table_02()

graph_01(X,y1,y2,y3)

# Сравнение двух методов

full_time_01 = y11 + y22 + y33
full_time_02 = y1 + y2 + y3

min_time1 = min(min(y1),min(y2),min(y3))
max_time1 = max(max(y1),max(y2),max(y3))

min_time = min(min(y11),min(y22),min(y33))
max_time = max(max(y11),max(y22),max(y33))

print()
print('{:^55}'.format('Сравнение двух методов'))

print('┌','─'*20,'┬','─'*15,'┬','─'*17,'┐',sep='')
print('│{:^20}│{:^15}│{:^17}│'.format('Тип сравнения','Метод слияния','mergesort numpy'))
print('├','─'*20,'┼','─'*15,'┼','─'*17,'┤',sep='')

print('│{:^20}│{:^15.1e}│{:^17.1e}│'.format('Ср. арифметическое',sum(full_time_01)/9,sum(full_time_02)/9))
print('│{:^20}│{:^15.1e}│{:^17.1e}│'.format('Минимальное знач.',min_time,min_time1))
print('│{:^20}│{:^15.1e}│{:^17.1e}│'.format('Максимальное знач.',max_time,max_time1))
print('└','─'*20,'┴','─'*15,'┴','─'*17,'┘',sep='')
