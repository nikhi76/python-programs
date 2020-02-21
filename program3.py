lst=[1,1,2,3,4,64,35,93,35,87,4,3]
unique=[]
for i in lst:
	if i not in unique:
		unique.append(i)
print(unique)