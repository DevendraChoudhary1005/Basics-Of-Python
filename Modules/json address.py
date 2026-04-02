book={}
book['tom']={
    'name': 'tom',
    'Address': '1 Red Street, NY',
    'Phone': 2947384723874
}
book['Bob']={
    'name': 'Bob',
    'Address': '1 Green Street, NY',
    'Phone': 5273598982589
}

import json
s=json.dumps(book)
with open('book.json','w') as f:
    f.write(s)

#You can now read this JSON data using any language that supports JSON such as JavaScript, C++, etc.
#Hence this is called data exchange format (i.e exchanging data from python program to javascript program)