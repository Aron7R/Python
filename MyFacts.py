import requests

url = "https://uselessfacts.jsph.pl/random.json?laguage=en"

while True:
    input("Press Enter to get a random fact or type 'q' to quit")
    if input().lower() == 'q':
       
        break

    
    response = requests.get(url)
    fact_data = response.json()
    print(f"Fact: {fact_data['text']}")