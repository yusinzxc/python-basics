print("(C/c) Charmander | (B/b) Bulbasaur | (D/d) Dratini")
user = input("Pick a pokemon: ")

class Pokemon:
    def __init__(self,name,hp,mana,lvl):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.lvl = lvl
        print("\n",name,"Created\n")
    def intro(self):
        print("Name:",self.name)
        print("HP:",self.hp)
        print("Mana:",self.mana)
        print("Lvl:",self.lvl)
#Charmander
if user == "C" or user == "c":
    mainChar = Pokemon("Charmander",100,90,5)
    mainChar.intro()
#Bulbasaur
elif user == "B" or user == "b":
    mainChar = Pokemon("Bulbasaur",150,50,4)
    mainChar.intro()
#Dratini
elif user == "D" or user == "d":
    mainChar = Pokemon("Dratini",90,100,6)
    mainChar.intro()
else:
    print("Wrong: ")

