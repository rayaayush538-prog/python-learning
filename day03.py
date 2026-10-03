
#cupon card
shoping= int(input("pay amount : "))
cupon = input("cupon :  ")
if cupon == "save50":
	print(shoping - 50)
elif shoping > 2000 :
	print(shoping - shoping * 20/100) 
    #print(" 20% discount ")
elif shoping < 2000 and shoping >= 1000 :
	print(shoping - shoping * 10/100)
		#print(" 10% discount ")
else:
	print("no discount")
