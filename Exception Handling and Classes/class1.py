class Human:
    def __init__(self, n, o, a):
        self.name = n
        self.occupation = o
        self.age = a

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name, "Plays Tennis")
        elif self.occupation == "Actor":
            print(self.name, "Shoots a film")

    def speaks(self):
        print(self.name, "Says how are you?")

tom = Human("Tom Cruise", "Actor", "55")
tom.do_work()
tom.speaks()

maria = Human("Maria Sharapova", "Tennis Player", "25")
maria.do_work()
maria.speaks()