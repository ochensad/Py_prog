from math import *
import tkinter.messagebox as box
from tkinter import *
from tkinter import ttk

def sum_n1_n2(n1,n2):

	result_array=[]

	for i in range(len(n1)-1,-1,-1):
		if n1[i] != '.':
			if n1[i]+n2[i] < 4:
				result_array.append(n1[i]+n2[i])
			else:
				if n1[i-1]!='.':
					n1[i-1] +=1
				else:
					n1[i-2]+=1
				result_array.append(abs(4-(n1[i]+n2[i])))
		else:
			result_array.append('.')
		if i== 0:
			if n1[i] == 4:
				result_array.append(1)
			elif n2[i] == 4:
				result_array.append(1)
			elif n1[i]+n2[i]>=4:
				result_array.append(1)
	result_array.reverse()
	return (result_array)

def sub_n1_n2(n1,n2):

	result_array=[]

	for i in range(len(n1)-1,-1,-1):
		if n1[i]!='.':
			if n1[i] >= n2[i]:
				result_array.append(n1[i]-n2[i])
			else:
				if n1[i-1]!=0:
					if n1[i-1]!='.':
						n1[i-1]-=1
						result_array.append((4+n1[i])-n2[i])
					else:
						n1[i-2]-=1
						result_array.append((4+n1[i])-n2[i])
				else:
					k = 1
					while n1[i-k] == 0 or n1[i-k]=='.':
						if n1[i-k]!='.':
							n1[i-k] = 3
						k+=1
					n1[i-k]-=1
					result_array.append((4+n1[i])-n2[i])
		else:
			result_array.append('.')
	result_array.reverse()
	j=0
	while result_array[j]==0:
		j+=1
	if j!=0:
		return result_array[j-1:]
	else:
		return result_array

def compare_n1_n2(A,B):

	for i in range(min(len(A),len(B))):
		if A[i]<B[i] and A[i]!='.' and B[i]!='.':
			return B, A
		if B[i]<A[i] and A[i]!='.' and B[i]!='.':
			return A,B

def make_arrays(A,B,f):

	flag1=A.index('.')
	flag2=B.index('.')

	if flag1 > flag2:

		if len(A)-(flag1+1)>len(B)-(flag2+1):
			n1 = A
			n2 = [0]*(flag1-flag2) + B + [0]*(len(A)-(flag1+1)-len(B)+(flag2+1))

		elif len(A)-(flag1+1)<len(B)-(flag2+1):
			n1 = A + [0]*(len(B)-(flag2+1)-len(A)+(flag1+1))
			n2 = [0]*(flag1-flag2) + B

		else:
			n1 = A
			n2 = [0]*(flag1-flag2) + B

	elif flag2 > flag1:

		if len(B)-(flag2+1)>len(A)-(flag1+1):
			n1 = B
			n2 = [0]*(flag2-flag1) + A + [0]*(len(B)-(flag2+1)-len(A)+(flag1+1))

		elif len(B)-(flag2+1)<len(A)-(flag1+1):
			n1 = B + [0]*(len(A)-(flag1+1)-len(B)+(flag2+1))
			n2 = [0]*(flag2-flag1) + A

		else:
			n1 = B
			n2 = [0]*(flag2-flag1) + A
	else:

		if len(B)-(flag2+1)>len(A)-(flag1+1):
			n1 = B
			n2 = A + [0]*(len(B)-(flag2+1)-len(A)+(flag1+1))

		elif len(B)-(flag2+1)<len(A)-(flag1+1):
			n2 = B + [0]*(len(A)-(flag1+1)-len(B)+(flag2+1))
			n1 = A
		else:
			n1 = A
			n2 = B
		n1,n2=f(n1,n2)

	return (n1,n2)

def choice_of_operation(A,B,sum_op,sub_op,make_op,comp_op):
	# sign = 0 (+); sing = 1 (-)
	signa = 0
	signb = 0
	signexp = 0

	new_a=[]
	new_b=[]

	expression=[]

	if A[0]!='-':
		singa=0
	else:
		singa=1

	if B[0]!='-':
		singb=0
	else:
		singb=1

	if singa==1 and singb==1:
		signexp=1
		new_a,new_b=make_op(A[1:],B[1:],comp_op)
		expression=[signexp]*1 +sum_op(new_a,new_b)

	elif singa==1 and singb==0:

		if A.index('.') > B.index('.'):
			signexp = 1

		elif A.index('.')==B.index('.'):
			if comp_op(A[1:],B[1:])==(A[1:],B[1:]):
				signexp=1

		new_a,new_b=make_op(A[1:],B[1:],comp_op)
		expression=[signexp]*1 +sub_op(new_a,new_b)

	elif singb == 1 and singa == 0:

		if B.index('.') > A.index('.'):
			signexp = 1

		elif A.index('.')==B.index('.'):
			if comp_op(A[1:],B[1:])==(B[1:],A[1:]):
				signexp=1

		new_a,new_b=make_op(A[1:],B[1:],comp_op)
		expression=[signexp]*1+sub_op(new_a,new_b)

	elif singa==0 and singb==0:
		new_a,new_b=make_op(A[1:],B[1:],comp_op)
		expression=[signexp]*1+sum_op(new_a,new_b)

	return expression

def make_str(A):
	S='+'
	if A[0]==1:
		S='-'
	for i in range(1,len(A)):
		S+=str(A[i])
	return S

def make_arr(S):
	A=[]
	for i in range(len(S)):
		if S[i]!='.' and S[i]!='-' and S[i]!='+':
			if i==0:
				A.append('+')
			A.append(int(S[i]))
		else:
			A.append(S[i])
	return(A)

def main(expr,sum_ab,sub_ab,make_ab,compare_ab,choice_ab,do_str,do_array):

	operations=[]
	numbers=[]
	num=''
	for k in expr:
		if k!='-' and k!='+':
			num+=k
		else:
			if num!='':
				if num.find('.')==-1:
					num+='.0'
				numbers.append(num)
			num=''
			operations.append(k)
	if num.find('.')==-1:
		num+='.0'
	numbers.append(num)

	while len(numbers)!=1:
		if len(operations)==len(numbers):
			n1=operations[0]+numbers[0]
			n2=operations[1]+numbers[1]
			operations.pop(0)
		else:
			n1=numbers[0]
			n2=operations[0]+numbers[1]
		numbers.pop(0)
		operations.pop(0)
		numbers[0]=do_str(choice_of_operation(do_array(n1),do_array(n2),sum_n1_n2,sub_n1_n2,make_arrays,compare_n1_n2))

	if numbers[0][0]=='+':
		entry.insert(END, "=" + numbers[0][1:])
	else:
		entry.insert(END, "=" + numbers[0])

def start():
    expression1 =(entry.get())

    if ('*' or '/' or ')' or '(' or '=') in entry.get():
        F = box.showwarning(title="Ошибка", message = 'Неверное выражение')
        entry.insert(END,' ERROR ')
    elif ('4' or '5' or '6' or '7' or '8' or '9') in entry.get():
    	F = box.showwarning(title='Ошибка', message= 'В 4-ой системе такие цифры не поддерживаются')
    	entry.insert(END,' ERROR ')
    else:
    	main(expression1,sum_n1_n2,sub_n1_n2,make_arrays,compare_n1_n2,choice_of_operation,make_str,make_arr)

def clean():
    entry.delete(0, END)

def info():
    F = box.showinfo(title='Справка', message =
    '''
    Калькулятор для 4-ой системы

    Ляпина Наталья ИУ7-22Б
    ''')

def BACK():
    s = entry.get()
    k = 0
    snew=''
    for b in s:
        k += 1

    for i in range(k-1):
        snew += s[i]
    clean()
    entry.insert(END, snew)
        
def Zero():
    entry.insert(END, '0')

def One():
    entry.insert(END, '1')

def Two():
    entry.insert(END, '2')

def Three():
    entry.insert(END, '3')

def Dot():
    entry.insert(END, ".")

def Minus():
    entry.insert(END, "-")

def Plus():
    entry.insert(END, "+")

window=Tk()
window.title('Калькулятор')
window.geometry('300x300')
self = Frame(window)

mainmenu = Menu(window)
window.config(menu=mainmenu)
mainmenu.add_command(label='Справка',command = info)
mainmenu.add_command(label='Очистка',command = clean)


self.columnconfigure(0, pad=5)
self.columnconfigure(1, pad=5)
self.columnconfigure(2, pad=5)
self.columnconfigure(3, pad=5)

self.rowconfigure(0, pad=20)
self.rowconfigure(1, pad=20)
self.rowconfigure(2, pad=20)
self.rowconfigure(3, pad=20)
self.rowconfigure(4, pad=20)


#Поле ввода
entry = Entry(self)
entry.grid(row=1, columnspan=4, ipady=8, sticky=W+E)

cls = Button(self, text="AC", command = clean)
cls.grid(row=2, column=3, ipadx = 8,ipady = 6)

back = Button(self,text="Back", command = BACK)
back.grid(row=2, column=2, ipadx = 8,ipady = 6)

empty = Button(self,text="")
empty.grid(row=2,column=0,ipadx=10,ipady=6)

empty = Button(self,text="")
empty.grid(row=2,column=1,ipadx=10,ipady=6)

#Кнопки      
one = Button(self, text="1",command = One)
one.grid(row=4, column=1, ipadx = 8,ipady = 6)        
two = Button(self, text="2",command = Two)
two.grid(row=3, column=1, ipadx = 8,ipady = 6)         
thr = Button(self, text="3",command = Three)
thr.grid(row=3, column=0, ipadx = 8,ipady = 6) 
mns = Button(self, text="-",command = Minus)
mns.grid(row=4, column=3, ipadx = 8,ipady = 6)         
        
zer = Button(self, text="0",command=Zero)
zer.grid(row=4, column=0, ipadx = 8,ipady = 6)        
dot = Button(self, text=".",command = Dot)
dot.grid(row=4, column=2, ipadx = 8,ipady = 6)         
equ = Button(self, text="=",command = start)
equ.grid(row=3, column=2, ipadx = 8,ipady = 6) 
pls = Button(self, text="+",command = Plus)
pls.grid(row=3, column=3, ipadx = 8,ipady = 6)
        
self.pack()
window.mainloop()