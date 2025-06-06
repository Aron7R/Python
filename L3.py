
class Human:
    Legs = 2
    Eyes = 2
    Hands = 2
    Nose = 1
    Brain = 1

    def __init__(self, Name, Height, Weight, Language, Color):
        self.Name = Name
        self.Height = Height
        self.Weight = Weight
        self.Language = Language
        self.Color = Color

Aron = Human("Aron", 4.9, 65, "Bengali", "Brown")
Pariza = Human("Pariza", 4.8, 55, "Bengali", "Brown")

print(Aron.Height)
print(Pariza.Height)

print(Pariza.Hands)
print(Aron.Hands)
