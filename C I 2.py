Indian = ["samosa","daal","naam"]
Chinese = ["egg role", "pot sticker", "fried rice"]
Italian = ["pizza", "pasta", "risotto"]

dish=input("Enter a Dish:")

if dish in Indian:
    print("Indian")
elif dish in Chinese:
    print("Chinese")
elif dish in Italian:
    print("Italian")
else:
    print("Based on little knowledge I have I don't know which cuisine is", dish)