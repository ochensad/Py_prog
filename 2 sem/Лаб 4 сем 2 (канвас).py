
from tkinter import *
root = Tk()
 
c = Canvas(root, width=600, height=600, bg='white')
c.pack()

# Прическа
c.create_polygon(150, 300,80, 160, 150, 120,160,50,230,90,300,30,350,90,420,70
                 ,420,120,500,150,450,300,fill='#c46ccc',outline='black',width=3)
# Тело
# Кривые Безье
def F(t,coef):
	A=coef[0]
	B=coef[1]
	C=coef[2]
	D=coef[3]
	E=coef[4]
	G=coef[5]
	f = pow(1-t,5)*A+5*(pow(1-t,4))*t*B + 10*pow(1-t,3)*t*t*C + 10*(1-t)*(1-t)*pow(t,3)*D+5*(1-t)*pow(t,4)*E+pow(t,5)*G
	return f

Cxa=[155,70,120,190,125,170]
Cya=[300,430,480,480,330,290]
Cxb=[430,475,410,480,530,445]
Cyb=[290,330,480,480,430,300]
Cxc=[310,300,330,470,300,340]
Cyc=[450,520,520,520,500,410]
Cxd=[260,300,130,270,300,290]
Cyd=[410,500,520,520,530,435]
Cxe=[285,290,305,315,308,320]
Cye=[330,360,370,380,335,330]
Xa=[]
Xb=[]
Xc=[]
Xd=[]
Xe=[]
t = 0
while t < 1:
	Xa.append(int(F(t,Cxa)))
	Xa.append(int(F(t,Cya)))
	Xb.append(int(F(t,Cxb)))
	Xb.append(int(F(t,Cyb)))
	Xc.append(int(F(t,Cxc)))
	Xc.append(int(F(t,Cyc)))
	Xd.append(int(F(t,Cxd)))
	Xd.append(int(F(t,Cyd)))
	Xe.append(int(F(t,Cxe)))
	Xe.append(int(F(t,Cye)))
	t+=0.05
#Руки
c.create_polygon(Xa,width=3,fill='#fa55ad',outline='black')
c.create_polygon(Xb,width=3,fill='#fa55ad',outline='black')
#Ноги
c.create_polygon(Xc,width=3,fill='#fa55ad',outline='black')
c.create_polygon(Xd,width=3,fill='#fa55ad',outline='black')
#Тело
c.create_oval(150, 150, 450, 450, width=3,fill='#fa55ad',outline='black')
c.create_polygon(Xe,width=2,fill='#b00b55',outline='#ba145f')
# Уши
c.create_oval(160,190,185,215,fill='#fa55ad',outline='black',width=3)
c.create_oval(415,190,440,215,fill='#fa55ad',outline='black',width=3)
# Глаза и очки
c.create_oval(220,230,300,310,fill='#fcfafc',outline = '#8e468f', width = 10)
c.create_oval(380,230,300,310,fill='#fcfafc',outline = '#8e468f', width = 10)
c.create_oval(270,260,290,280,fill='black')
c.create_oval(310,260,330,280,fill='black')
c.create_line(188,195, 230, 239,fill='#8e468f',width=10)
c.create_line(410,195,370,240,fill='#8e468f',width=10)
# Нос
c.create_polygon(293,304,293,300,310,300,310,304,301,320,fill='#cc1869')
c.create_line(301,313,301,330,width=3,fill='#cc1869')
# Брови
c.create_line(235,200,270,180,width=10,fill='#cc1869')
c.create_line(365,200,330,180,width=10,fill='#cc1869')

root.mainloop()
