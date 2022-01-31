x1,y1=map(int,input('Введите координаты x1,y1 первой точки : ').split())
x2,y2=map(int,input('Введите координаты x2,y2 второй точки : ').split())
x3,y3=map(int,input('Введите координаты x3,y3 третьей точки : ').split())

mcos=1 # наименьший косинус угла
mediana=0 
mincos=1
storx=0
story=0
stor=''

def Sushestv(a,b,c): # проверка на существование треугольника
    if a+b>c:
        if a+c>b:
            if b+c>a:
                return(True)
            else:
                return(False)


from math import sqrt

abx=x3-x1 # координаты вектора АВ
aby=y3-y1

bcx=x2-x3 # координаты вектора ВС
bcy=y2-y3

cax=x1-x2 # координаты вектора СА
cay=y1-y2

AB=sqrt(abx**2 + aby**2) # длины сторон треугольника
BC=sqrt(bcx**2 + bcy**2)
CA=sqrt(cax**2 + cay**2)

Sush=Sushestv(AB,BC,CA)

if Sush == True:
    
    cosa= - (abx*bcx + aby*bcy)/(AB*BC) # косинусы углов треугольника 
    cosb= -(cax*abx + cay*aby)/(CA*AB)
    cosj= -(cax*bcx + cay*bcy)/(CA*BC)

   # нахождение наименьшего косинуса

    if cosa<cosb and cosa<cosj:
        mcos=cosa
        ugol='ABC'
    else:
        if cosb<cosa and cosb<cosj:
            mcos=cosb
            ugol='CAB'
        else:
            mcos=cosj
            ugol='ACB'
   # нахождение медианы по формуле

    if mcos==cosj:
        mediana=(1/2)*sqrt(2*((bcx**2+bcy**2)+(cax**2+cay**2))-(abx**2+aby**2))
    elif mcos==cosb:
        mediana=(1/2)*sqrt(2*((cax**2+cay**2)+(abx**2+aby**2))-(bcx**2+bcy**2))
    else:
        mediana=(1/2)*sqrt(2*((bcx**2+bcy**2)+(abx**2+aby**2))-(cax**2+cay**2))

    print('{}{}{:.4f}{}{:.4f}{}{:.4f}'.format('Длины сторон равны ',\
'AB=',AB,' BC=',BC,' CA=',CA))
    print('{}{:.4f}{}{}'.format('Медиана треугольника равна M=',mediana,\
' и проведена из наибольшего угла ',ugol))

    # проверка на прямоугольный треугольник
    
    if cosj==0 or cosa==0 or cosb==0:
        print('{}'.format('Прямоугольный треугольник'))
    else:
        print('{}'.format('Треугольник не является прямоугольным'))

    x0,y0=map(int,input('Введите координаты X,Y точки: ').split())

    apx=x0-x1  # координаты вектора АР
    apy=y0-y1

    bpx=x0-x3  # координаты вектора BP
    bpy=y0-y3

    cpx=x0-x2  # координаты вектора СР
    cpy=y0-y2
    
    AP=abx*apy-aby*apx  # векторное произведение АР и АВ
    BP=bcx*bpy-bcy*bpx  # векторное произведение ВР и ВС
    CP=cax*cpy-cay*cpx  # векторное произведение СР и СА

    if (AP>=0 and BP>=0 and CP>=0) or (AP<=0 and BP<=0 and CP<=0):
        print('{}'.format('Точка лежит внутри треугольника'))
        
        cosl=(apx*abx+apy*aby)/(AB*sqrt(apx**2+apy**2)) 
        cosm=(bpx*bcx+bpy*bcy)/(BC*sqrt(bpx**2+bpy**2))
        cosk=(cpx*cax+cpy*cay)/(CA*sqrt(cpx**2+cpy**2))

        # нахождение наименьшего косинуса 

        if cosl<cosm and cosl<cosk:
            mincos=cosl
            storx=apx
            story=apy
            stor='АВ'
        else:
            if cosm<cosl and cosm<cosk:
                mincos=cosm
                storx=bpx
                story=bpy
                stor='BC'
            else:
                mincos=cosk
                storx=cpx
                story=cpy
                stor='CA'

        H=sqrt((storx**2+story**2)*(1-mincos**2)) 
    
        print('{}{}{}{:.4f}'.format('Расстоние до наиболее удаленной стороны '\
,stor,' H=',H))
    else:
        print('{}'.format('Точка лежит вне треугольника'))

else:
    print('Треугольника не существует')
    
