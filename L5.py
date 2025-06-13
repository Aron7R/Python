class Alien:
    Legs = 8
    Eyes = 4
    Hands = 3
    Nose = 0
    Brain = 900

    def __init__(self, Name, Height, Weight, Language, Color):
        self.Name = Name
        self.Height = Height
        self.Weight = Weight
        self.Language = Language
        self.Color = Color

Jackeo = Alien("Ankara", 20.9, 2000, "Unknown", "Green")
Poleo = Alien("Siuuu", 10.9, 200, "Unknown", "White")

print(Jackeo.Height)
print(Poleo.Height)

print(Jackeo.Hands)
print(Poleo.Hands)