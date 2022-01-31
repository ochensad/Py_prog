# Задача: написать программу, вычисляющую интеграл на промежутке
#
# ФУНКЦИИ:
#         F (Функция, которая содержит интегрируемую функцию)   
#         
#         Method1_trapezoid (Функция,вычисляющая интеграл методом трапеции)
#         ПЕРЕМЕННЫЕ:
#              sum0 - Сумма оснований трапеций
#              step - шаг между аргументами
#              result - вычисленный интеграл
#       
#         Method2_3_8 (Функция, вычисляющая интеграл методом 3/8)
#         ПЕРЕМЕННЫЕ:
#              step - шаг между аргументами
#              sum1 - сумма значений функции f при номере аргум кратном 3
#              sum2 - сумма значений функции f при номере аргум не кратном 3
#              (в sum1 и sum2 не входят значения функции при номере аргум=0 
#              и аргум=n)
#              result - вычисленный интеграл 
#
#         Answer (Функция для вычисления интеграла по заданному методу с 
#                 точностью eps)
#         ПЕРЕМЕННЫЕ:
#              func - заданный метод
#              n - количество разбиений
#              a1 - первый интеграл от n
#              a2 - второй интеграл от  2n

# Интегрируемая финкция
def f(x):
    return x*x*x

# Метод трапеций
def Method1_trapezoid(f, a, b, n):
    sum0=0
    step = (b-a)/float(n)
    for k in range(1,n):
        sum0+=(f(a+k*step-step)+f(a+k*step))
    result = step * sum0/2
    return result

# Метод 3/8
def Method2_3_8(f,a,b,n):
    step=(b-a)/float(n)
    sum1=0
    sum2=0
    for k in range(1,n):
        if k%3==0:
            sum1+=f(a+k*step)
        else:
            sum2+=f(a+k*step)
    result=(3/8)*step*(3*sum2+2*sum1+f(a)+f(b))
    return result

# Вычисление с точнотью eps
def Answer(func,a,b,eps,n=1):
    a1=func(f,a,b,n)
    a2=func(f,a,b,(n*2))
    while abs(a1-a2)>eps:
        n*=2
        a1=func(f,a,b,n)
        a2=func(f,a,b,n*2)
    return a2,n*2

a,b = map(float,input('Введите промежуток: ').split())
n1 =  int(input('Введите целое количество разбиений n1: '))
n2=int(input('Введите целое количество разбиений n2: '))

n11=Method1_trapezoid(f,a,b,n1)
n21=Method2_3_8(f,a,b,n1)
n12=Method1_trapezoid(f,a,b,n2)
n22=Method2_3_8(f,a,b,n2)


print('{:^55}'.format('\nТаблица вычисления интегралов разными методами'))
print('┌'+'─'*14+'┬'+'─'*14+'┬'+'─'*14+'┐')
print('│{:^14}│ n1={:<9} │ n2={:<9} │'.format('Метод',n1,n2))
print('├'+'─'*14+'┼'+'─'*14+'┼'+'─'*14+'┤')
print('│{:^14}│{:>13.7f} │{:>13.7f} │'.format('трапеций',n11,n12))
print('│{:^14}│{:>13.7f} │{:>13.7f} │'.format('3/8',n21,n22))
print('└'+'─'*14+'┴'+'─'*14+'┴'+'─'*14+'┘\n')


eps=float(input('Введите точность: '))
iAnswer2,nAnswer2=Answer(Method2_3_8,a,b,eps)
print('Вычисленный с точностью интеграл: {:<8.7f}'.format(iAnswer2))
print('Количество разбиений на промежутке: {:<8.0f}\n'.format(nAnswer2))


tochnoe=iAnswer2
pribl=n22

print('При n =',n2)
print('Абсолютная погрешность: {:<8.7f}'.format(abs(tochnoe-pribl)))
print('Относительная погрешность: {:<8.7f}'.format(abs((tochnoe - pribl)/tochnoe)))


