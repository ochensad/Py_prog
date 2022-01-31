a=input('Введите длину ребра (действительное число): ')

def Proverka(x):
    if a.isdigit()==False:
        if a.isalpha()==False:
            if a.find('.')==a.rfind('.') and a.find('.')!=-1 and a.find('-')==-1:
                return(float(a))
            else:
                print('Неправильный формат ввода. Введите снова')
                return(-1)
                
        else:
            print('Неправильный формат ввода. Введите снова')
            return(-1)
    else:
        return(int(a))

from math import sqrt,pow

b=Proverka(a)

if b!=-1:
    H=b*sqrt(2/3)
    S=b*b*sqrt(3)
    V=pow(b,3)*sqrt(2)/12
    R=b*sqrt(6)/4
    r=R/3

    print('{}{:.3f}'.format('Высота H=',H))
    print('{}{:.3f}'.format('Площадь поверхности S=',S))
    print('{}{:.3f}'.format('Объём V=',V))
    print('{}{:.3f}'.format('Радиус описанной окружности R=',R))
    print('{}{:.3f}'.format('Радиус вписанной окружности r=',r))
