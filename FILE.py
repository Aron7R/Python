MyFile = open("Friends.txt","w")
MyFile.write(" Ronald\n. ")
MyFile.write(" Mendes\n. ")
MyFile.close()

MyFile = open("Friends.txt","a")
MyFile.write(" Leao\n. ")
MyFile.write(" Cruyff\n. ")

MyFile = open("Friends.txt","r")
content = MyFile.read()
print(content)

MyFile = open("Friends.txt","r")
# content = MyFile.read()
#print(MyFile.readline())
#print(MyFile.readline())
#print(MyFile.readline())
#print(MyFile.readline())