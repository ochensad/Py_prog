# Лабараторная №9
#


def get_index(word):
	result=[]

	for i in range(len(word)):

		if word[i]!=' ':
			result.append(ord(word[i])-ord('a'))

	return result

def encode(word,key):
	encodedPhrase=[]

	for i in range(len(word)):

		encodedPhrase.append(((word[i]+key[i%len(key)])%26)+ord('a'))

	return encodedPhrase

def decoder(word,key):
	decode_word=[]
	
	for i in range(len(word)):
                
		decode_word.append((abs(word[i]-key[i%len(key)]+26)%26)+ord('a'))
		
	return decode_word


def printResults(resultArray):
	S=''
	for x in resultArray:
		S+=chr(x)
	return S

print('{:^40}'.format('Меню программы\n'))

choice =None
main_srting=''
while choice!='0':
	print('\
		1 - Ввод строки.\n\
		2 - Настройка шифрующего алгоритма.\n\
		3 - Шифрование строки, используя шифр Виженера.\n\
		4 - Расшифровывание строки.\n\
		0 - Выход из программы\n')


	choice=input('Выбор: ')


	if choice=='0':
		print('Выход')
		break

	elif choice=='1':
		main_srting=input('Введите строку для шифрования: ')

	elif choice=='2':
		cipher_key=input('Введите ключ: ')

	elif choice=='3':

		if cipher_key=='':
			print('Вы не ввели ключ для шифрования')

		elif main_srting=='':
			print('Вы не ввели фразу для шифрования')

		else:
			print('\nЗашифрованная фраза')
			print(printResults(encode(get_index(main_srting),get_index(cipher_key))))

	elif choice=='4':

		if cipher_key=='':
			print('Вы не ввели ключа для дешифрования')

		elif main_srting=='':
			print('Вы не ввели фразу для дешифрования')
			
		else:
			print('\nРасшифрованная фраза')
			print(printResults(decoder(get_index(main_srting),get_index(cipher_key))))
	else:
		print('Введеного номера нет в списке')


