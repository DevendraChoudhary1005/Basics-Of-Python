tom_exp_list=[2100, 1000, 4500]
joe_exp_list=[200, 230, 402]

def claculate_total(exp):
    total=0
    for item in exp:
        total+=item
    return total

toms_total=claculate_total(tom_exp_list)
joes_total=claculate_total(joe_exp_list)

print("Tom's Total Expenses: ", toms_total)
print("Joe's Total Expenses: ", joes_total)

#we will avoid writing this below code if we use functions
#total=0
#for item in tom_exp_list:
#    total=total+item
#print("Tom's Total Expenses: ",total)

#total=0
#for item in joe_exp_list:
#    total=total+item
#print("Joe's Total Expenses: ",total)
