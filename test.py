class Character:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability

    def introduce(self):
        print("I'm " + self.name)
        print("I can " + self.ability)


class HeroFly(Character):
    def __init__(self,name,ability,weak):
        super().__init__(name,ability)
        self.weak = weak

    def introduce(self):
        super().introduce()
        print("Weakness " + self.weak)

