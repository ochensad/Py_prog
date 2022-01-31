#
#      Практика 1 семестр
#


# ПЕРЕМЕННЫЕ

# массивы
dictionaryArray=[]
phrasesArray=[]

# строки
dictionaryWord=''
phraseWord=''

# Определение количества различных букв в слове или фразе
def lettersCounter(word):
	wordlength=len(word)
	letters={}
	word=''.join(sorted(word))
	print(type(word))

	for i in range(wordlength):

		if word[i]!=' ':

			if letters.get(word[i])==None:
				letters[word[i]]=1

			else:
				letters[word[i]]+=1

	return letters
lettersCounter('jdkeysbskfielsof fjsj hsfr g')
# создание словаря с анаграммами для фразы
def AnagramsDict(phrase,dictArray):

	anagrams=[]
	k=0
	phrase_letters=lettersCounter(phrase)

	for word in dictArray:
		new_word=lettersCounter(word)
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
def Combinated_Anagrams(phrase,dict):
	combinatinons=[]
	n=Binary(pow(2,len(dict))-1)

	for i in range(1,pow(2,len(dict))):

		combinated_phrase_str=''
		combinated_phrase_array=[]
		lenCombination=0

		b=Binary(i)
		b='0'*(len(n)-len(b))+b

		for j in range(len(b)):

			if b[j]=='1':
				combinated_phrase_str+=dict[j]
				combinated_phrase_array.append(dict[j])
				lenCombination+=len(dict[j])

		if lenCombination==len(phrase):

			if dict_compare(lettersCounter(phrase),lettersCounter(combinated_phrase_str))==True:
				combinatinons.append(combinated_phrase_array)

	return combinatinons
    	

# проверка фразы на полную анаграмму
def fullAnagrams(mainPhrase,dictionary):
	wordInPhrase=''
	counter=0
	mainPhrase+=' '

	for i in range(len(mainPhrase)):
		counter=0

		if mainPhrase[i]!=' ':
			wordInPhrase+=mainPhrase[i]

		else:

			for j in range(len(dictionary)):

				if wordInPhrase==dictionary[j]:
					counter=1

			if counter==0:
				break

			wordInPhrase=''
	return(counter>0)


# Ввод словаря
while dictionaryWord!='#':
	dictionaryWord=input()

	if dictionaryWord!='#':
		dictionaryArray.append(dictionaryWord)


# Ввод фраз
while phraseWord!='#':
	phraseWord=input()

	if phraseWord!='#':
		phrasesArray.append(phraseWord)

# перебор всех анаграмм для фразы
for i in range(len(phrasesArray)):
	Answer=[]
	if fullAnagrams(phrasesArray[i],dictionaryArray)==False:

		Answer=Combinated_Anagrams(delite_space(phrasesArray[i]),AnagramsDict(phrasesArray[i],dictionaryArray))

		# вывод 
		Answer.reverse()
		for j in range(len(Answer)):
			print(phrasesArray[i],end =' = ')
			for k in Answer[j]:
				print(k,end=' ')
			print()




