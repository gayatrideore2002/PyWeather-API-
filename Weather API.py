import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"

# Function to get weather data for a specific date
def get_weather(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json() 
        for forecast in data['list']:
            if str(forecast['dt']).startswith(date):
                temperature = forecast['main']['temp']
                print(f"Temperature on {forecast['dt']}: {temperature}°C")
                return
        print("No weather data found for the given date.")
    else:
        print("Error fetching weather data.")

# Function to get wind speed data for a specific date
def get_wind_speed(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            if str(forecast['dt']).startswith(date):
                wind_speed = forecast['wind']['speed']
                print(f"Wind Speed on {forecast['dt']}: {wind_speed} km/h")
                return
        print("No wind speed data found for the given date.")
    else:
        print("Error fetching wind speed data.")

# Function to get pressure data for a specific date
def get_pressure(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            if str(forecast['dt']).startswith(date):
                pressure = forecast['main']['pressure']
                print(f"Pressure on {forecast['dt']}: {pressure} hPa")
                return
        print("No pressure data found for the given date.")
    else:
        print("Error fetching pressure data.")

# Main program
while True:
    print("\nOptions:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit") 

    option = int(input("Enter your choice: "))

    if option == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        get_weather(date)
    elif option == 2:
        date = input("Enter the date (YYYY-MM-DD): ")
        get_wind_speed(date)
    elif option == 3:
        date = input("Enter the date (YYYY-MM-DD): ")
        get_pressure(date)
    elif option == 0:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")