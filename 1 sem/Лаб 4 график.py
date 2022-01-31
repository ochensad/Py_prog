from math import log,sqrt

print('Внимание! Аргумент должен быть строго ПОЛОЖИТЕЛЬНЫМ,\
т.к функция не определена для неположительных аргументов')
mT = float(input('Введите нижнюю границу аргумента: ')) # нижняя граница аргумента
nT = float(input('Введите верхнююграницу аргумента: '))# верхняя граница аргумента
Sh = float(input('Введите шаг: ')) # шаг аргумента
l = int(input('Количество засечек: '))
zas = round((66-l)/(l-1)) # интервал между засечками
b = mT # текущее значение аргумента


# ТАБЛИЦА ЗНАЧЕНИЙ ФУНКЦИЙ
if mT>0 and nT>0 and Sh>0 and mT<nT:
    step=Sh # шаг аргумента
    bMin=mT # нижняя граница аргумента для таблицы
    bMax=nT # верхняя граница аргумента для таблицы
    b1=bMin # текущее значение аргумента
    SMin=pow(bMin,3)+9.57*bMin*bMin-243.7*bMin+773.6 
    k=0 # номер в таблице
    bs=bMin 

    print()
    print('{:^50}'.format('Таблица значений функций'))
    print('┌','─'*4,'┬','─'*10,'┬','─'*13,'┬','─'*11,'┬','─'*12,'┐',sep='')
    print('│{:^4}│{:^10}│{:^13}│{:^11}│{:^12}│'.format('№','b','S1','S2','S3'))
    print('├','─'*4,'┼','─'*10,'┼','─'*13,'┼','─'*11,'┼','─'*12,'┤',sep='')

    while b1<=bMax:
        S1=b1*b1*b1+9.57*b1*b1-243.7*b1+773.6
        if S1<SMin:
            SMin = S1
            bs=b1
        S2=b1*log(b1,)-18
        S3=sqrt(abs(S1-S2))
        k+=1
        if b1>44:
            print('│{:^4}│{:>9.4f} │{:>12.5e} │ {:>9.4f} │{:>11.4f} │'.format(k,\
b1,S1,S2,S3))
        else:
            print('│{:^4}│{:>9.4f} │{:>12.5f} │ {:>9.4f} │{:>11.4f} │'.format(k,\
b1,S1,S2,S3))
        
        b1+=step

    print('└','─'*4,'┴','─'*10,'┴','─'*13,'┴','─'*11,'┴','─'*12,'┘',sep='')
    print('{}{:.4f}{}{:.2f}'.format('Минимальное значение функции S1=',SMin,\
' достигается при b1=',bs))
    print()
    
# ГРАФИК ФУНКЦИИ S2

    print('{:^90}'.format('График функции S2=b*ln(b)-18'))
    print()


    Smin=Smax=b*b # функция

    for i in range(int((nT-mT)/Sh)+1):
        S=b*log(b,)-18
        if S > Smax:
            Smax = S
        if S < Smin:
            Smin = S
        b += Sh
    c = (Smax-Smin)/(l-1) # период для значений на Oy


    # Значения на Оy
    print(' '*3, '{:>8.1f}'.format(Smin), sep='' ,end='')
    for i in range(1, l-1):
        print(' '*(zas-7), '{:>8.1f}'.format(Smin+i*c), sep='', end='')
    print(' '*(zas-7), '{:>8.1f}'.format(Smax), sep='', end='')
    print('\t')

    # Засечки на Oy
    print(' '*7,chr(0x2500),chr(9524), end='', sep='')
    for i in range(l-2):
        print(chr(0x2500)*zas, chr(9524),sep='', end='')
    print(chr(0x2500)*zas, chr(9524), sep='', end='',)
    print('─>S2',sep='')


    p = (zas+1)*(l-1) # длина оси Oy
    b = mT # значение аргумента начальное
    M = 0 
    j = 0 
    if Smin<=0 and Smax>=0:
        M=round((0-Smin)/(Smax-Smin)*p) # расстояние до оси Ох
        j=1
    for i in range(int((nT-mT)/Sh)+1):
            print('{:>7.1f}'.format(b), end='')
            S=b*log(b,)-18
            g = round((S-Smin)/(Smax-Smin)*p) 
            if g > M:
                print(' '*(M+1), chr(9474)*j, ' '*(g-M-1), '*', sep='')
            elif g == M:
                print(' '*(g+1), '*', sep='')
            else:
                print(' '*(g+1), '*', ' '*(M-g-1), chr(9474)*j, sep='')
            b += Sh
    print('     ', 'b')
else:
    print()
    if mT<=0 or nT<=0:
        print('Функция не определена для такого b')
    if Sh<=0:
        print('Невозможное значение шага')
    if nT==mT:
        print('Вы ввели одинаковые значения аргумента!')
