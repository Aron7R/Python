class Computer:

    Keyboard = 2
    Mouse = 1
    Monitor = 2
    Price = 10000

    def _init_(self, Monitor, Keyboard, Mouse, Price):
        self.Monitor = Monitor
        self.Keyboard = Keyboard
        self.Mouse = Mouse
        self.Price = Price

Apple = Computer("A4tTech","Asus","Wish",9000)
Windows = Computer("VOGUE","Instict","Vpro",1000)

print(Apple.Monitor)
print(Windows.Monitor)

print(Apple.Price)
print(Windows.Price)
