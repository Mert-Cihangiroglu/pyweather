import requests
import pytemperature
api_address = "https://api.openweathermap.org/data/2.5/weather?appid=7bde04f0c2735bbd4770b0861f21e98f&q="
city = input("city Name : ")
url = api_address + city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
celciusdata=formatted_data2 =json_data['main']['temp']
newcelcius=pytemperature.k2c(celciusdata)
print(formatted_data)
print(newcelcius)