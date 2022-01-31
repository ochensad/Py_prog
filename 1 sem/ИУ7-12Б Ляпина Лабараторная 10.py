

Text=[
'В город ворвалась зима. Еще вчера ветер гонял по улицам опавшие листья,',
'моросил холодный дождь. Сегодня же с утра все белым-бело 5*(-(-3)) . За ночь снежная',
'туча щедро поделилась снегом, который теперь искрился и переливался в лучах',
'яркого утреннего солнца. Лицо прохожих, 4/(-1+1) одетых в теплые шубы и пуховики, были',
'по-детски радостными. Ребятишки же не скрывали свой восторг и громко','',
'кот',
'радовались долгожданному снегу. Возле 1//2//3+2 школ развернулись настоящие снежные',
'баталии. Многие школьники, да и некоторые учителя оказались обстреляны',
'снежками. У всех в этот день было радостное, приподнятое настроение. Зима',
'вступила в свои владения, 12-(5^(2//(2*4%3))+10*(3+1)) подарив людям ощущение',
'сказки, волшебства.']

# Выравнивание по левому краю
def left_alignment(text):

	for x in text:
		print(x)

# Поиск самой длинной строки
def MaxStr(text):

	Maxlen=0

	for i in text:
		if len(i)>Maxlen:
			Maxlen=len(i)
	return Maxlen

# Выравнивание по правому краю
def right_alignment(text):

	M=MaxStr(text)

	for x in text:
		print((' '*(M-len(x)))+x)

# Счетчик пробелов в строке
def space_counter(str):

	count=0

	for i in range(len(str)):
		if str[i]==' ':
			count+=1
	return count

# Выравнивание по ширине
def width_alignment(text):

	M=MaxStr(text)

	for i in text:

		if len(i)<M:

			space=space_counter(i)
			space_numbers=[0]*space
			delta=M-len(i)
			if space>0:
				while delta>0:

					for j in range(space):

						space_numbers[j]+=1
						delta-=1

						if delta==0:
							break

					if delta==0:
						break
				k=0
				for x in i:

					if x==' ':

						print(x+' '*space_numbers[k],end='')
						k+=1

					else:
						print(x,end='')
				print()
			else:
				print(i,' '*(M-len(i)-1))

		else:
			print(i)

# Удаление введеного слова
def delite_word(text,del_word):
	AnswerStr=''
	word=''
	find=0

	for i in range(len(text)):
		k=0

		for j in range(len(text[i])):

			if text[i][j]!=' ' and j!=len(text[i])-1:
				word+=text[i][j]

			else:
				k+=1

				if j==len(text[i])-1:
					word+=text[i][j]

				if word!=del_word and word!=del_word+',':

					if k==1:
						AnswerStr+=word

					else:
						AnswerStr+=(' '+word)

				elif word==(del_word +'.'):
					find+=1
					AnswerStr+='.'

				elif word==del_word or word==del_word+',':
					find+=1

				word=''

		text[i]=AnswerStr
		AnswerStr=''

	return find

# Замена слова во всем тексте
def change_word(text,ch_word,change):

	find=0
	
	for i in range(len(text)):
		AnswerStr=''
		word=''
		k=0

		for j in range(len(text[i])):

			if text[i][j]!=' ' and j!=len(text[i])-1:
				word+=text[i][j]

			else:
				k+=1

				if j==len(text[i])-1:
					word+=text[i][j]

				if word!=ch_word and word!=ch_word+',' and word!=ch_word+'.':

					if k==1:
						AnswerStr+=word

					else:
						AnswerStr+=(' '+word)

				else:

					if word==ch_word:
						find+=1

						if k==1:
							AnswerStr+=change

						else:
							AnswerStr+=' '+change

					elif word==ch_word+',':

						find+=1

						if k==1:
							AnswerStr+=change+','

						else:
							AnswerStr+=(' '+change+',')

					elif word==ch_word+'.':

						find+=1
						AnswerStr+=change+'.'

				word=''
		text[i]=AnswerStr
		AnswerStr=''

	return find

# Получение массива из операций и чисел
def get_Array(str):

	u=[]
	word=''
	str+=' '
	operations=['^','*','/','+','%']

	for i in range(len(str)):

		if str[i]!=' ':

			if '0'<=str[i]<='9':
				word+=str[i]

			else:
				if word!='':
					u.append(word)
				word=''
				if i==0 and str[i]=='-':
					word+=str[i]
				else:
					if str[i]=='-' and str[i-1] in operations:
						word+=str[i]
					else:
						u.append(str[i])
		else:
			u.append(word)
	return u

# Вычисление выражения без скобок 
def clear_arifm(expression):
	expr=get_Array(expression)

	operations=[]

	for i in range(len(expr)):
		if expr[i]=='^':
			operations.append(expr[i])

	for i in range(len(expr)):
		if expr[i]=='*' or expr[i]=='/' or expr[i]=='%':
			operations.append(expr[i])

	for i in range(len(expr)):
		if expr[i]=='+' or expr[i]=='-':
			if expr[i-1]!='-' and expr[i]=='-':
				operations.append(expr[i])
			elif expr[i]!='-':
				operations.append(expr[i])

	for i in range(len(operations)):

		if operations[i] in expr:

			k=expr.index(operations[i])


			if expr[k]=='^':
				number=int(expr[k-1])**int(expr[k+1])
				expr[k]=number
				expr.pop(k-1)
				expr.pop(k)

			elif expr[k]=='*':
				number=int(expr[k-1])*int(expr[k+1])
				expr[k]=number
				expr.pop(k-1)
				expr.pop(k)

			elif expr[k]=='/' and expr[k+1]!='/':
				if int(expr[k+1])!=0:
					number=int(expr[k-1])/int(expr[k+1])
					expr[k]=number
					expr.pop(k-1)
					expr.pop(k)
				else:
					return 'Деление на ноль'
					break

			elif expr[k]=='/' and expr[k+1]=='/':
				if int(expr[k+2])!=0:
					number=int(expr[k-1])//int(expr[k+2])
					expr[k]=number
					expr.pop(k-1)
					expr.pop(k+1)
					expr.pop(k)
				else:
					return 'Деление на ноль'
					break

			elif expr[k]=='%':
				if int(expr[k+1])!=0:
					number=int(expr[k-1])%int(expr[k+1])
					expr[k]=number
					expr.pop(k-1)
					expr.pop(k)
				else:
					return 'Деление на ноль'
					break

			elif expr[k]=='+':
				number=int(expr[k-1])+int(expr[k+1])
				expr[k]=number
				expr.pop(k-1)
				expr.pop(k)

			elif expr[k]=='-':
				if expr[k+1]!='-':
					number=int(expr[k-1])-int(expr[k+1])
					expr[k]=number
					expr.pop(k-1)
					expr.pop(k)
				elif i==0 and expr[k+1]=='-':
					number=expr[k+2]
					expr[k]=number
					expr.pop(k+1)
					expr.pop(k+1)

				else:
					number=int(expr[k-1])+int(expr[k+2])
					expr[k]=number
					expr.pop(k-1)
					expr.pop(k+1)
					expr.pop(k)

	if len(expr)==1:
		return str(expr[0])
	else:
		return ''

# Раскрытие скобок и разбиение на отдельные выражения
def full_arifm(expression):

	if expression.rfind('(')!=-1 and expression.rfind(')')!=-1 and expression.count('(')==expression.count(')'):

			for i in range(expression.count('(')):
				left=expression.rfind('(')
				right=expression.index(')',left)
				number=clear_arifm(expression[left+1:right])
				expression=expression[:left]+number+expression[right+1:]
			return clear_arifm(expression)

	elif expression.find('(')==-1 and expression.find(')')==-1:
		return clear_arifm(expression)


# Поиск арифметического выражения в тексте
def find_arifm(text):
	number=''
	string=''

	for i in range(len(text)):

		for j in range(len(text[i])):

			k=text[i][j]
			arifm_string=''

			if '0'<=k<='9' or k=='+' or k=='-' or k=='*' or k=='/' or k=='^' or k=='%' or k=='(' or k==')':
				number+=k

			else:
				arifm_string=full_arifm(number)
				string+=arifm_string
				string+=k
				number=''

		text[i]=string
		string=''

# Поиск слова с максимальным количеством согласных букв
def vowels(text):
	vowelsArray=['Б','В','Г','Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ',
	'б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
	k=1
	count=0
	maximum=0
	maximumSentence=0

	for i in range(len(text)):
		for j in range(len(text[i])):

			if text[i][j]=='.':
				k+=1

			if text[i][j]!=' ':
				if text[i][j] in vowelsArray:
					count+=1
			else:
				if count>=maximum:
					maximum=count
					maximumSentence=k
				count=0

		if count>=maximum:
			maximum=count
			maximumSentence=k
		count=0

	return maximumSentence

print('\nИсходный текст\n')
for x in Text:
	print(x)

choice=-1
while choice!=0:
	print('{:^40}'.format('\nВыберите действие'))
	print('\
            ...\n\
            1. Выравнивание текста по левому краю.\n\
            2. Выравнивание текста по правому краю.\n\
            3. Выравнивание текста по ширине.\n\
            4. Удаление заданного слова.\n\
            5. Замена одного слова другим во всем тексте.\n\
            6. Вычисление арифметического выражения.\n\
            7. Найти предложение, в котором слово с максимальным количеством\
 согласных букв.\n\
                 \n\
            0. Выход\n\
            ...'
              )
	choice=int(input('Выбор:'))

	if choice==1:
		left_alignment(Text)

	elif choice==2:
		right_alignment(Text)

	elif choice==3:
		width_alignment(Text)

	elif choice==4:

		delited=input('Введите слово, которое нужно удалить: ')
		found1=delite_word(Text,delited)
		if found1>0:
			for x in Text:
				print(x)
		else:
			print('Слово не найдено')

	elif choice==5:

		firstword=input('Ввидете слово, которое нужно заменить: ')
		secondword=input('Введите слово-замену: ')
		found2=change_word(Text,firstword,secondword)
		
		if found2>0:
			for y in Text:
				print(y)
		else:
			print('Слово не найдено')

	elif choice==6:

		find_arifm(Text)
		for z in Text:
			print(z)

	elif choice==7:

		answer=vowels(Text)
		print('Слово с максимальным количеством согласных находится в\
предложении номер ',answer)

	elif choice==0:
		break

	else:
		print('Введенного вами числа нет в списке')


























