#Задача 1

def fibonacci(n, m):
	zn1 = 1
	zn2 = 1
	res = []
	if (n == 1) or (m == 1) :
		res.append(1)
	if (n == 2) or ((n==1) and (m >= 2)) :
		res.append(1)
	i = 3
	while i <= m :
		znach = zn1 + zn2
		zn1 = zn2
		zn2 = znach
		if i >= n :
			res.append(znach)
		i += 1
	
	return(res)
			

#Задача 2
# сортируем методом пузырька

def sort_cycle(lst) :
	res = True
	totalElems = len(lst)
	if totalElems < 2 :
		return res
	currNum = totalElems - 1
	while currNum > 0 :
		if lst[currNum - 1] > lst[currNum] :
			tmp = lst[currNum]
			lst[currNum] = lst[currNum - 1]
			lst[currNum - 1] = tmp
			res = False
		currNum -= 1

	return res

def sorting(lst) :
	job_done = False
	while not job_done :
		job_done = sort_cycle(lst)
	return(lst)
	

print(sorting([5,2,8,4,5,3,-5,7,56,24]))