fruits = ("Apple", "Mango", "Blueberry", "Banana")
car = ("BMW", "Lambo", "Maruti")
numbers = (1, 2, 3, 4.5, 6, 7)

print(car)
print(fruits[1])
print(car[1])




Aron = {
    "Grade":6,
    "Country":"Uganda",
    "Phone":893701308
}

Phonebook = {
    "Aron":824572057,
    "Safayan":5942752,
    "Rahul":592597,
}

print(Phonebook.get("Aron"))
print(Aron.get("Country"))
print(Phonebook["Safayan"])

Phonebook["Rahul"]=69
print(Phonebook)
del Phonebook ["Rahul"]
print(Phonebook)
