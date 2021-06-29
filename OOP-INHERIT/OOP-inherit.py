class Species:
    def __init__(self,called,name,gender):
        self.called = called
        self.name = name
        self.gender = gender
        print("Those are " + self.called)

    def introduce(self):
        if self.called == "Human" or self.called == "human":
            if self.gender == "Male" or self.gender == "male":
                print("Him name is " + self.name)
            else:
                print("Her name is " + self.name)
        else:
            print("It is a " + self.name)

class Human(Species):
    def __init__(self,called,name,gender):
        super().__init__(called,name,gender)
    def fullProfile(self):
        super().introduce()
        print(True)

hOne = Human("Human","Yujin","Female")
hOne.fullProfile()

class Animals(Species):
    def __init__(self,called,name,gender):
        super().__init__(called,name,gender)

aOne = Animals("Animals","Dog","Male")
aOne.introduce()



