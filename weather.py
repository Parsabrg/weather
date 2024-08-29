import requests

API_KEY = "9853ba24752e946408e749af2e447d8c"
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        print(f"Current Weather in {city.capitalize()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f"City '{city}' not found.")

def get_weather_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n5-Day Weather Forecast for {city.capitalize()}:\n")

        for entry in data['list']:
            timestamp = entry['dt_txt']
            temp = entry['main']['temp']
            weather_desc = entry['weather'][0]['description'].capitalize()

            print(f"{timestamp} | Temp: {temp}°C | {weather_desc}")
    else:
        print(f"City '{city}' not found.")

def main():
    print("Welcome to the Weather App!")
    
    while True:
        city = input("\nEnter the city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break

        get_current_weather(city)
        get_weather_forecast(city)

if __name__ == "__main__":
    main()
