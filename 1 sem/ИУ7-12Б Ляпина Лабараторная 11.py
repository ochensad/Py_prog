#
# Лабараторна №11
#
#
import pickle as p

def writing_to_file(books_counter,name):

	main_file=open(name,'ab')

	for i in range(books_counter):

		print('\nВведите данные')
		auther=input('Введите автора: ')
		book_name=input('Введите название: ')
		year=input('Введите год издания: ')

		note={'Автор':auther,'Название':book_name,'Год':year}

		p.dump(note,main_file)

	main_file.close()

def print_all_file(name):

	try:
		main_file=open(name,'rb')
	except FileNotFoundError:
		print('В файле ничего нет')
	else:

		i=-1

		while True:
			try:
				i+=1
				note=p.load(main_file)
				print('Книга номер ',i+1)
				print('Автор: ',note['Автор'])
				print('Название: ', note['Название'])
				print('Год издания: ',note['Год'],'\n')

			except EOFError:
				break
			except p.PickleError:
				print('Целостность файла нарушена')
				break

		main_file.close()

def find_by_one_string(name,key,value):

	try:
		main_file=open(name,'rb')
	except FileNotFoundError:
		print('В файле ничего нет')
		Answer=[0]
	else:

		A=[]
		i=-1

		while True:
			try:
				i+=1
				note=p.load(main_file)

				if note[key]==value:
					note['Номер']=i+1
					A.append(note)
			except EOFError:
				break
			except p.PickleError:
				print('Целостность файла нарушена')
				break

		main_file.close()
		return A

def find_by_two_strings(name,key1,value1,key2,value2):

	try:
		main_file=open(name,'rb')
	except FileNotFoundError:
		print('В файле ничего нет')

	else:

		A=[]
		i=-1

		while True:
			try:

				i+=1
				note=p.load(main_file)

				if note[key1]==value1 and note[key2]==value2:
					note['Номер']=i+1
					A.append(note)

			except EOFError:
				break
			except p.PickleError:
				print('Целостность файла нарушена')
				break

		main_file.close()
		return A

choice=-1
keys=['Автор','Название','Год']
name=''
while choice!=0:
	print('{:^40}'.format('\nВыберите действие'))
	print('\
            ...\n\
            1. Создание Базы данных.\n\
            2. Запись в Базу данных.\n\
            3. Вывод базы данных.\n\
            4. Поиск записи по одному полю.\n\
            5. Поиск записи по двум полям.\n\
                 \n\
            0. Выход\n\
            ...'
              )
	try:
		choice=int(input('Выбор: '))
	except ValueError:
		print('Недопустимое значение выбора')
		continue

	if choice==1:

		name=input('Введите название Базы данных: ')

		if name[len(name)-5:]!='.bin':
			name+='.bin'
		try:
			main_file=open(name,'rb')
		except FileNotFoundError:
			continue
		else:
			print('База данных уже существует. Хотите ее перезаписать? (нет- 0, да - 1) ')
			c=int(input())
			if c==1:
				main_file=open(name,'wb')
				main_file.close()

	elif choice==2:

		if name!='':
			n=int(input('Введите количество книг: '))

			if n>0:
				writing_to_file(n,name)
			else:
				print('Недопустимое значение')
		else:
			print('Вы не создали файл')

	elif choice==3:

		if name!='':
			print_all_file(name)
		else:
			print('Вы не создали файл')

	elif choice==4:

		if name!='':
			skey=input('Введие поле: ')
			svalue=input('Введите значение поля: ')
			print()

			if skey in keys:
				Answer=find_by_one_string(name,skey,svalue)
				if Answer==None:
					print('Ничего не найдено')
				elif Answer[0]==0:
					print()
				else:
					for i in Answer:
						print('Книга номер ',i['Номер'])
						print('Автор: ',i['Автор'])
						print('Название: ', i['Название'])
						print('Год издания: ',i['Год'],'\n')

			else:
				print('Такого поля нет')
		else:
			print('Вы не создали файл')

	elif choice==5:

		if name!='':
			skey1=input('Введите первое поле: ')
			svalue1=input('Введите значение: ')
			skey2=input('Введите второе поле: ')
			svalue2=input('Введите значение: ')
			print()

			if skey1 in keys and skey2 in keys:
				Answer=find_by_two_strings(name,skey1,svalue1,skey2,svalue2)
				if Answer==[]:
					print('Ничего не найдено')
				else:
					for i in Answer:
						print('Книга номер ',i['Номер'])
						print('Автор: ',i['Автор'])
						print('Название: ', i['Название'])
						print('Год издания: ',i['Год'],'\n')
			else:
				print('Такого поля нет')
		else:
			print('Вы не создали файл')

	elif choice==0:
		break
	else:
		print('Такого выбора нет')
