exp = [1234, 2345,3456,4567,5678,6789,7890,8901]

#total = exp[0]+exp[2]+exp[3]+exp[4]+exp[5]+exp[6]+exp[7]
#print(total)

#instead of writing above code we use loops

total=0

for i in range(len(exp)):
    print("Month:", (i+1), "Expense:" , exp[i])
    total=total+exp[i]

for item in exp:
    total=item+total
print("Total Expense:", total)
