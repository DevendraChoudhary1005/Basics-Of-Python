def sum(a,b=0):  #if we assign a value to the variable here then if we don't assign a value it is assigned as default value like here it is 0
    """""This Functions takes two arguments
    which are integers and it will return
    sum as the output"""
    print("a:", a)
    print("b:", b)

    total=a+b  #here total is  a local variable
    print("Total Inside Function:", total)
    return total

n=sum(5)
o=sum(b=1, a=7)

print("Total Outside Function:", o)
print("Total Outside Function:", n)

#variable inside a function is known as local variable and function outside any function is known as Global variable