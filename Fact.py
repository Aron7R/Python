import requests

#Define API URL
url = "https://uselessfacts.jsph.pl/random.json?laguage=en"

#Send the GET request
response = requests.get(url)

#Check if the request was successful (status ode 200)
if response.status_code == 200:
    #Parse the JSON respose
    fact_data = response.json()
    print(fact_data["text"]) #Print the fact
else:
    print("Failed to retrive fact")