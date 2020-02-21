import csv
while True:
	print("1.Add participant")
	print("2.See participant")
	n=int(input("Enter your choice: "))
	if(n==1):
		def add():
			var1=input("Enter the name: ")
			var2=input("Enter the usn: ")
			var3=input("enter the event:\n1)Cs\n2)GoogleIt\n3)Treasure Hunt\n")
			with open('prgrm.csv','a',newline="") as file:
 				writer=csv.writer(file,dialect='excel')
 				writer.writerow([var1,var2,var3])
	elif n==2:
		def see():
			with open('prgrm.csv','r') as file:
				reader=csv.reader(file)

				for row in reader:
					print(row[0],row[1],row[2])
	else:
		break
	add()
	see()



