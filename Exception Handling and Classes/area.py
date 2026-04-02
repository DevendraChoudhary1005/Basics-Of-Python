def calculate_area(base,height):
    print("__name__: ", __name__)
    return base * height / 2

if __name__ == "__main__":
    print("I am in area.py")
    area = calculate_area(10,20)
    print("Area:", area)