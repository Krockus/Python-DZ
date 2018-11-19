
__author__ = 'Ïàâëîâ Àëåêñàíäğ Îëåãîâè÷'

#çàäà÷à1

def is_eng_letter(symb) :
	res = False
	num = ord(symb)
	if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
		res = True
	return res

#ïîëó÷àåì ñòàòèñòèêó
def get_list_wordstat(str) :
	punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

	totalWords = 0
	totalEngLetters = 0

	wordList = str.split()
	for i in range(len(wordList)) :

		if wordList[i][-1] in punctuation :  
			wordList[i] = wordList[i][:-1]

		if wordList[i][0] in punctuation :
			wordList[i] = wordList[i][1:]
		
		
		addingToWords = False
		for x in wordList[i] :
			if is_eng_letter(x) == True :
				totalEngLetters += 1
			if not addingToWords :
				if not(x in punctuation) :
					addingToWords = True
		if addingToWords :
			totalWords += 1				
	
	print('Ñëîâ â òåêñòå - ', totalWords, ', àãëèéñêèõ áóêâ â òåêñòå - ', totalEngLetters)

get_list_wordstat('bla bla áëà bla,bla ')

#çàäà÷à2

#ïîëó÷àåì ñïèñîê ñëîâ â íèæíåì ğåãèñòğå èç òåêñòà
def get_lower_list(str) :
	punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

	wordList = str.split()
	for i in range(len(wordList)) :

		if wordList[i][-1] in punctuation :  
			wordList[i] = wordList[i][:-1]

		if wordList[i][0] in punctuation :
			wordList[i] = wordList[i][1:]

		wordList[i] = wordList[i].lower()
	return  wordList
	


def get_common_words(list1,list2) :
	words1 = get_lower_list(list1)
	words2 = get_lower_list(list2)

	res = []
	for el in words1 :
		if el in words2 :
			if not (el in res) :
				res.append(el)
	return res

text1 = 'ßãîÄà ÌàëÈÍÀ, â ËÅÑ ê ñåáå Ìàíèëà! ßãîäà Ìàëèíà ÑëàÄêîş Áûëà!'
text2 = ' Â ëåñó ğîäèëàñü ÿãîäà! Ñëàäêàÿ â ñåáå?'
print(get_common_words(text1,text2))