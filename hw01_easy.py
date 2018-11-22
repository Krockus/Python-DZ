#Задача 1


def GetRoundNum(dec, symb_num) :

	strok = str(dec)
	lastNum = int(str(dec)[-1])
	NeedRounding = False
	mnojitel = 1

	print(strok)
	GotPoint = False
	strRes = ''
	for x in strok :
		if x == '.' :
			GotPoint = True
		elif GotPoint :
			symb_num -= 1
			mnojitel /= 10
		strRes += x
		if symb_num == -1 :
			lastNum = int(x)
			NeedRounding = True
			#отсекаем последнюю цифру
			strRes = strRes[:-1]
			mnojitel *= 10
			break

	res = float(strRes)
	if NeedRounding and lastNum >= 5 :
		res = res + mnojitel
	

	return res

print(GetRoundNum(123.456, 4))
	
			
#Задача 2   +
	
def NumberIsLucky(strok) :
	strok = str(strok)
	length = len(strok) 
	subLeng = length // 2
	substr1 = strok[:subLeng]
	if length % 2 > 0:    # число символов нечётно
		subLeng += 1
	substr2 = strok[subLeng:]

	sum1 = sum(map(lambda x: int(x),substr1))
	sum2 = sum(map(lambda x: int(x),substr2))		

	res = False
	if sum1 == sum2 :
		res = True
	return res