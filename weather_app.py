import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    print(json.dumps(data, indent=4))  # Print the full response for debugging
    return data

def display_weather(data):
    if data.get("cod") == "404":
        print("City Not Found")
    elif "main" in data and "weather" in data:
        main = data["main"]
        weather = data["weather"][0]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}K")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print("Unexpected response format.")

if __name__ == "__main__":
    api_key = "8864756af48285707e6439d6d727687c"
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)
