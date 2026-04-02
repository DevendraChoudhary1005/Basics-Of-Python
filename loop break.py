key_location="Chair"
location=["Garage", "Living Room", "Chair", "Closet"]
for i in location:
    if i==key_location:
        print("Key is Found in ", i)
        break
    else:
        print("Key is not Found in ", i)