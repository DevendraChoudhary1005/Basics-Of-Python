"""class Father():
    def gardening(self):
        print("I enjoy Gardening")

class Mother():
    def cooking(self):
        print("I enjoy Cooking")

class child(Mother, Father):
    def sports(self):
        print("I enjoy Sports")

c = child()
c.gardening()
c.cooking()
c.sports()"""

class Father():
    def skills(self):
        print("Programming and Gardening")

class Mother():
    def skills(self):
        print("Art and Cooking")

class child(Mother, Father):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c = child()
c.skills()
