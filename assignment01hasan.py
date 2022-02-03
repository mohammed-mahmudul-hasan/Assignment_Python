print("How much Oreo Cookies you ate(only number input please) ?")
amount_cookies=input()
amount_cookies=int(amount_cookies)

calories=amount_cookies*160
fat=amount_cookies*7
sodium=amount_cookies*190
carbo=amount_cookies*25
protein=amount_cookies*2

print("You've consumed "+str(calories)+" calories")
print("Total Fat: "+str(fat)+ "g")
print("Sodium: "+str(sodium)+ "mg")
print("total Carbohydrate: "+str(carbo)+ "g")
print("Protein: "+str(protein)+"g")
if (amount_cookies*160) > 2000 :
    print("Alert! Stop eating")



