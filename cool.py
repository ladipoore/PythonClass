word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]

for i in range(len(word)):
	print(word[i:len(word)])
	if i ==len(word)-1:
		j = i-1
		while j < len(word):
			print(word[j:len(word)])
			j-=1
			if j ==0:
				break
		break