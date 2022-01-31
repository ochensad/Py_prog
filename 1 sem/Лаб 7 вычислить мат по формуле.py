#     Задача: написать программу, которая вычисляет матрицу по формуле
#             y(ij)=e^X(i) + cos(b(j))
# ПЕРЕМЕННЫЕ:
#            stroka - переменная, содержащая кол-во строк в матрице
#            stolbec - переменная, содержащая кол-во столбцов в матрице
#            X - массив, вводимый с клавиатуры
#            b - переменная изменяющаяся от 0 с шагом pi/12
#            Y - полученная матрица
#            maxY - содержит максимальный элемент матрицы Y
#            minY - содержит минимальный элемент матрицы Y
#            maxZ - содержит номер строки, в которой находится максимальный
#                   элемент матрицы Y
#            minZ - содержит номер строки, в которой находится минимальный
#                   элемент матрицы Y
#            Z - сформированный вектор

from math import*

print('Матрица вычисляется по формуле y(ij)=e^X(i) + cos(b(j))')
print()

stroka=int(input('Введите кол-во строк в матрице: '))
stolbec=int(input('Введите кол-во столбцов в матрице: '))
X=list(map(float,input('Введите значения Х для массива: ').split()))

b=0
Y=[0]*stroka
minZ=0
maxZ=0
Z=[]

if len(X)==stroka and stroka < 11 and stolbec < 16:

    # Вычасление матрицы Y
    for i in range(stroka):
        Y[i]=[]
        for j in range(stolbec):
            y=exp(X[i])+cos(b)
            (Y[i]).append(y)
            b+=(pi/12)
        b=0

    # Вывод полученной матрицы
    print()
    print('Полученная матрица: ')
    print()
    for i in range(stroka):
        print('│',end=' ')
        for j in range(stolbec):
            print('{:>8.4f}'.format(Y[i][j]),end=' ')
        print('  │',end=' ')
        print()

    # Поиск минимального и максимального элемента матрицы Y
    minY=maxY=Y[0][0]
    for i in range(stroka):
        for j in range(stolbec):
            if Y[i][j]>maxY:
                maxY=Y[i][j]
                maxZ=i
            if Y[i][j]<minY:
                minY=Y[i][j]
                minZ=i
                
    # Заполнение начала вектора Z
    for j in range(stolbec):
        Z.append(Y[maxZ][j])
                
    # Заполнение конца вектора Z
    for j in range (stolbec):
        Z.append(Y[minZ][j])
        
    print()
    
    # Вывод вектора Z
    print('Вектор Z = ',end='')
    for x in Z:
        print('{:8.4f}'.format(x),end=' ')

    
else:
    if len(X)>stroka:
        print('В массиве X больше элементов, чем нужно')
    if len(X)<stroka:
        print('В массиве Х меньше элементов, чем нужно')
    if stroka >= 11 or stolbec >=16:
        print('Вы ввели недопустимые размеры матрицы')


