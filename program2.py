l=[1,2,3,2,0,65,21,4,2,10]
key=int(input("Element: "))
indices=[]

for i in range(0,len(l)):
	if l[i]==key:
		indices.append(i)
print(indices)