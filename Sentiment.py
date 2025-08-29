from textblob import TextBlob
print("Welcome to Sentiment Analysis Ai")


text = input("Say something: ")
blob = TextBlob(text)

if blob.polarity >0.25:
    print("Great")
elif blob.polarity < -0.25:
    print("Sorry to hear that")
else:
    print("It happens sometine")
