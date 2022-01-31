#
# ЛАБАРАТОРНАЯ №1
# Уточнение корней уравнения

mash=float(input('Введите шаг: '))
left=float(input('Задайте левую границу интервала: '))
right=float(input('Задайте правую границу интервала: '))
exp=float(input('Задайте точность: '))
max_iter=int(input('Максимальное количество итераций: '))


left1=left
right1=right

Errors=['Ошибка деления на 0','Превыш. кол-во итерац','Ошибки нет']
j=0
for x in Errors:
	print(j,' - ',x)
	j+=1
from math import cos,sin
from scipy import optimize

def F(x):
	return sin(x)
def F1(x):
	return cos(x)

def method(y,y1,a,b,iter_m,delta):
	count=0
	if y(a)*y(b)>0:
		return None,count,0

	if abs(y((a+b)/2)) < abs (y(a)) and abs(y((a+b)/2)) < abs (y(b)):
		x0=(a+b)/2
	elif abs(y(a))>abs(y(b)):
		x0=b
	elif abs(y(b))>abs(y(a)):
		x0=a
	xn=x0
	xn=xn-(y(xn)/y1(xn))
	while abs(y(xn))>delta:
		if count>=iter_m:
			return xn,count,1
		count+=1
		xn=xn-y(xn)/y1(xn)
	return xn,count,2
print('{:^50}'.format('\nТаблица уточнения корней функции y=sin(x) \
методом касательных'))
print('┌','─'*4,'┬','─'*13,'┬','─'*12,'┬','─'*12,'┬','─'*12,'┬','─'*12,'┐',
      sep='')
print('│{:^4}│{:^13}│{:^12}│{:^12}│{:^12}│{:^12}│'.format(\
	'№','Отрезок','х','f(x)','Итерации','Код ошибки'))
print('├','─'*4,'┼','─'*13,'┼','─'*12,'┼','─'*12,'┼','─'*12,'┼','─'*12,'┤',
      sep='')

c=int((right-left)/mash)

for i in range(c):
	x_ret,count_ret,error_code=method(F,F1,left,left+mash,max_iter,exp)
	if x_ret!=None:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+2,left,left+mash,x_ret,F(x_ret),count_ret,error_code))
	left+=mash
if left < right:
	x_ret,count_ret,error_code=method(F,F1,left,right,max_iter,exp)
	if x_ret!=None:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+2,left,right,x_ret,F(x_ret),count_ret,error_code))

print('└','─'*4,'┴','─'*13,'┴','─'*12,'┴','─'*12,'┴','─'*12,'┴','─'*12,'┘',sep='')


print('{:^50}'.format('\nТаблица уточнения корней функции y=sin(x)\
 с помощью ф-ции newton'))
print('┌','─'*4,'┬','─'*13,'┬','─'*12,'┬','─'*12,'┬','─'*12,'┬','─'*12,'┐',sep='')
print('│{:^4}│{:^13}│{:^12}│{:^12}│{:^12}│{:^12}│'.format(\
	'№','Отрезок','х','f(x)','Итерации','Код ошибки'))
print('├','─'*4,'┼','─'*13,'┼','─'*12,'┼','─'*12,'┼','─'*12,'┼','─'*12,'┤',sep='')

c=int((right1-left1)/mash)
for i in range(c):

	if abs(F((2*left1+mash)/2)) < abs (F(left1)) and\
	abs(F((2*left1+mash)/2)) < abs (F(left1+mash)):
		x0=(2*left1+mash)/2
	elif abs(F(left1))>abs(F(left1+mash)):
		x0=left1+mash
	elif abs(F(left1+mash))>abs(F(left1)):
		x0=left1

	x_ret,count_ret=optimize.newton(F,x0, fprime=F1, tol=exp,maxiter=max_iter,
		full_output=True,disp=False)
	if count_ret.iterations>=max_iter:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+1,left1,left1+mash,x_ret,F(x_ret),count_ret.iterations,1))
	else:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+1,left1,left1+mash,x_ret,F(x_ret),count_ret.iterations,2))
	left1+=mash
if left1 < right1:
	x_ret,count_ret=optimize.newton(F,((left1+right1)/2), fprime=F1, tol=exp,
                                        maxiter=max_iter,full_output=True,disp=False)
	if count_ret.iterations>=max_iter:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+2,left1,right1,x_ret,F(x_ret),count_ret.iterations,1))
	else:
		print('│{:^4}│[{:<5.2f},{:>5.2f}]│{:>11.7f} │{:>11.0e} │{:^12}│{:^12}│'\
			.format(i+2,left1,right1,x_ret,F(x_ret),count_ret.iterations,2))

print('└','─'*4,'┴','─'*13,'┴','─'*12,'┴','─'*12,'┴','─'*12,'┴','─'*12,'┘',sep='')






