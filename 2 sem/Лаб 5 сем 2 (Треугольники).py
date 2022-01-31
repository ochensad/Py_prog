from tkinter import *
import tkinter.messagebox as box
import numpy as np
from math import *
X_p=[]
Y_p=[]
NP=0
def find_min(x_1,y_1,x_2,y_2,x_3,y_3):
	a = sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
	b = sqrt((x_2 - x_3)**2 + (y_2 - y_3)**2)
	c = sqrt((x_3 - x_1)**2 + (y_3 - y_1)**2)
	p = (a + b + c) / 2
	try:
		S_tr = sqrt(p*(p-a)*(p-b)*(p-c))
		global R
		R = (a*b*c)/(4*S_tr)
		S = pi*((a*a*b*b*c*c)/(16*S_tr*S_tr)) - S_tr
		return S
	except ZeroDivisionError:
		return 1000000


D = [0,0,0,0,0,0]
def combinations():
	min_s=100000
	for i in range(0,len(X_p) - 1):
		for j in range(i+1,len(X_p)-1):
			for k in range(j+1,len(X_p)):
				c = find_min(X_p[i],Y_p[i],X_p[j],Y_p[j],X_p[k],Y_p[k])
				if c < min_s:
					min_s = c
					global r_min
					r_min = R
					D[0] = X_p[i]
					D[1] = Y_p[i]
					D[2] = X_p[j]
					D[3] = Y_p[j]
					D[4] = X_p[k]
					D[5] = Y_p[k]

def points():
    x = ''
    y = ''
    flag = 0
    for sym in en1.get():
        if sym == ' ':
            flag = 1
        if flag == 0:
            x += sym
        else:
            y += sym
    if (x == '' or y == ''):
    	F = box.showerror("Ошибка","Недостаточно данных")
    	return 0
    x = int(x)
    y = int(y)
    X_p.append(x)
    Y_p.append(y)
    en1.delete(0, END)

def k_paint():
	if len(X_p) < 3:
		F = box.showerror("Ошибка","Недостаточно данных")
		return 0
	window2 = Tk()
	window2.title("Решение")
	cvs = Canvas(window2, width = 1500, height = 900, bg = "lightblue")
	combinations()
	for i in range(len(X_p)):
		cvs.create_oval(X_p[i]-5,Y_p[i]-5,X_p[i]+5,Y_p[i]+5,fill = "green")
	d = 2*(D[0]*(D[3]-D[5])+D[2]*(D[5]-D[1])+D[4]*(D[1]-D[3]))
	ux = ((D[0]*D[0]+D[1]*D[1])*(D[3]-D[5])+(D[2]*D[2]+D[3]*D[3])*(D[5]-D[1])+(D[4]*D[4]+D[5]*D[5])*(D[1]-D[3]))/d
	uy = ((D[0]*D[0]+D[1]*D[1])*(D[4]-D[2])+(D[2]*D[2]+D[3]*D[3])*(D[0]-D[4])+(D[4]*D[4]+D[5]*D[5])*(D[2]-D[0]))/d
	cvs.create_oval(ux-r_min,uy-r_min,ux+r_min,uy+r_min)
	cvs.create_line(D[0],D[1],D[2],D[3])
	cvs.create_line(D[2],D[3],D[4],D[5])
	cvs.create_line(D[4],D[5],D[0],D[1])
	cvs.pack()

def m_paint(event):
	if len(X_p) < 3:
		F = box.showerror("Ошибка","Недостаточно данных")
		return 0
	combinations()
	for i in range(len(X_p)):
		cvs.create_oval(X_p[i]-5,Y_p[i]-5,X_p[i]+5,Y_p[i]+5,fill = "green")
	d = 2*(D[0]*(D[3]-D[5])+D[2]*(D[5]-D[1])+D[4]*(D[1]-D[3]))
	if d == 0:
		F = box.showerror("Ошибка","Нет треугольника")
		return 0
	ux = ((D[0]*D[0]+D[1]*D[1])*(D[3]-D[5])+(D[2]*D[2]+D[3]*D[3])*(D[5]-D[1])+(D[4]*D[4]+D[5]*D[5])*(D[1]-D[3]))/d
	uy = ((D[0]*D[0]+D[1]*D[1])*(D[4]-D[2])+(D[2]*D[2]+D[3]*D[3])*(D[0]-D[4])+(D[4]*D[4]+D[5]*D[5])*(D[2]-D[0]))/d
	cvs.create_oval(ux-r_min,uy-r_min,ux+r_min,uy+r_min)
	cvs.create_line(D[0],D[1],D[2],D[3])
	cvs.create_line(D[2],D[3],D[4],D[5])
	cvs.create_line(D[4],D[5],D[0],D[1])

def com_point(event):
    global figure
    figure = 0

def paint(event):
    x1 = event.x
    y1 = event.y
    if ((x1 - 5 >= 0) and (x1 + 5 <= 1500) and (y1 - 5 >= 0) and (y1 + 5 <= 900)):
        cvs.create_oval(x1-5,y1-5,x1+5,y1+5,fill = "green")
        X_p.append(x1)
        Y_p.append(y1)
def Keyboard():
    but2.config(state = DISABLED)
    but3.config(state = NORMAL)
    but5.config(state = NORMAL)

def Mouse():
    global figure
    figure = 0

    but1.config(state = DISABLED)
    but3.config(state = DISABLED)
    window2 = Tk()
    window2.title("Решение")
    global cvs
    cvs = Canvas (window2, width = 1500, height = 900, bg = "lightblue")
    cvs.pack()
    point = cvs.create_oval(60,30,70,40,fill="green")
    cvs.tag_bind(point, '<Button-2>', com_point)
    cvs.bind('<Button-1>', paint)
    cvs.bind('<Button-3>', m_paint)

window = Tk()
window.geometry('450x200')
window.resizable(width=False, height=False)
window.title("Параметры")
Choice = Frame(window)
Choice.grid()

name1 = Label(Choice, text = "Выберете способ ввода:", relief = "solid")
name1.grid(row = 1, columnspan = 2)
but1 = Button(Choice, text = "Клавиатура",command = Keyboard)
but1.grid(row = 1, column = 2)

but2 = Button(Choice, text = "Мышь", command = Mouse)
but2.grid(row = 1,column = 3)

name3 = Label(Choice, text = "Введите координаты точки:")
name3.grid(row = 6, column = 1)
en1 = Entry(Choice)
en1.grid(row = 6, column = 2)
but3 = Button(Choice, state = DISABLED, text = "ОК", command = points)
but3.grid(row = 6, column  = 3)

name5 = Label(Choice, text = "Нажать по окончанию: ")
name5.grid(row = 8, column = 1)
but5 = Button(Choice, state = DISABLED, text = " Окончить ввод ", command = k_paint)
but5.grid(row = 8,column = 2)

Choice.pack(padx=1,pady=50)
window.mainloop()	
