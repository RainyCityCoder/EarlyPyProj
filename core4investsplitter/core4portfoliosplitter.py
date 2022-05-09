print("Use at your own risk. Creator not responsible for anything. Please see README.md")

number = input("Amount here (dollars only): ")
amount = float(number.replace(",",""))

bond = str(amount*0.4)
reit = str(amount*0.06)
stocks = str(amount*0.54)
intl = str(amount*0.18)
totstock = str(amount*0.36)

print("For Bond fund (40% of total): $" + bond)
print("For REIT fund (6% of total): $" + reit)
print("For International fund: (18% of total): $" + intl)
print("For Total Stock fund (36% of total): $" + totstock)
print("(All stock funds are 54% of total and sums to $" + stocks + ")")
print("More info at: https://www.bogleheads.org/forum/viewtopic.php?t=10413")
