#We will just import the area code to this code
#we can import area file as these both files are in same directory

import sys
sys.path.append("jetbrains://pycharm/navigate/reference?project=Bascis Of Python&path=")
import Area as A

Area= A.calculate_square_area(5)
print("Area Of Square:", Area)