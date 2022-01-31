#      Практика 1 семестр
#  Ляпина Наталья Викторовна ИУ7-12Б


# ПЕРЕМЕННЫЕ

# массивы
dictionary_Array=[]
phrases_Array=[]

# строки
dictionary_Word=''
phrase_Word=''

# Определение количества различных букв в слове или фразе
def letters_Counter(word):
	word_length=len(word)
	letters={}
	word=''.join(sorted(word))

	for i in range(word_length):

		if word[i]!=' ':

			if letters.get(word[i])==None:
				letters[word[i]]=1

			else:
				letters[word[i]]+=1

	return letters

# создание словаря с анаграммами для фразы
def anagrams_Dict(phrase,dict_Array):

	anagrams=[]
	k=0
	phrase_letters=letters_Counter(phrase)

	for word in dict_Array:
		new_word=letters_Counter(word)
		for i in (new_word.keys()):
			if phrase_letters.get(i)!=None and phrase_letters[i]-new_word[i]>=0:
				k+=1

		if k==(len(new_word.keys())):
			anagrams.append(word)

		k=0
	if len(anagrams)!=0:
		return anagrams


# удаление пробела во фразе
def delite_space(phrase):
	K=''
	for letter in range(len(phrase)):
		if phrase[letter]!=' ':
			K+=phrase[letter]
	return K

# проверка двух словарей на идентичность
def dict_compare(dict1,dict2):
	comp=0

	if dict1.keys()!= dict2.keys():
		return False

	else:

		for i in dict1:
			if dict1[i]==dict2[i]:
				comp+=1

		if comp==len(dict1.keys()):
			return True

		else:
			return False

# перевод в двоичную систему счисления
def Binary(k):
	b=''
	while k>0:
		b=str(k%2)+b
		k=k//2
	return b

# перебор всех возможных комбинаций для словаря с анаграммами
def combinated_Anagrams(phrase,dict):
	combinatinons=[]
	n=Binary(pow(2,len(dict))-1)

	for i in range(1,pow(2,len(dict))):

		b=Binary(i)
		b='0'*(len(n)-len(b))+b

		combinated_phrase_str=''
		combinated_phrase_array=[]
		len_Combination=0

		for j in range(len(b)):

			if b[j]=='1':
				combinated_phrase_str+=dict[j]
				combinated_phrase_array.append(dict[j])
				len_Combination+=len(dict[j])

		if len_Combination==len(phrase):

			if dict_compare(letters_Counter(phrase),letters_Counter(combinated_phrase_str)
				)==True:
				combinatinons.append(combinated_phrase_array)

	return combinatinons
    	

# проверка фразы на полную анаграмму
def full_Anagrams(main_Phrase,dictionary):
	word=''
	flag=0
	main_Phrase+=' '

	for i in range(len(main_Phrase)):
		flag=0

		if main_Phrase[i]!=' ':
			word+=main_Phrase[i]

		else:

			for j in range(len(dictionary)):

				if word==dictionary[j]:
					flag=1

			if flag==0:
				break

			word=''
	return(flag>0)


# Ввод словаря
while dictionary_Word!='#':
	dictionary_Word=input()

	if dictionary_Word!='#':
		dictionary_Array.append(dictionary_Word)


# Ввод фраз
while phrase_Word!='#':
	phrase_Word=input()

	if phrase_Word!='#':
		phrases_Array.append(phrase_Word)

# перебор всех анаграмм для фразы
for i in range(len(phrases_Array)):
	Answer=[]
	if full_Anagrams(phrases_Array[i],dictionary_Array)==False:

		Answer=combinated_Anagrams(delite_space(phrases_Array[i]),anagrams_Dict(
			phrases_Array[i],dictionary_Array))

		# вывод 
		Answer.reverse()
		for j in range(len(Answer)):
			print(phrases_Array[i],end =' = ')
			for k in Answer[j]:
				print(k,end=' ')
			print()




