#!/Users/mayanksingh/Desktop/PycharmProjects/pythonProject/weather_checking_cmd/venv/bin/python

import sys
import requests
import time
import json

# Global list to store favorite cities
favorite_cities = []

# WeatherAPI.com API key (replace with your own)
api_key = "82178c3ef4c24e64db77b5fa3c5e6b99"

# Function to check weather by city name
def check_weather(city):
    try:
        url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response_req = requests.get(url)
        response_req.raise_for_status()  # Raise an exception for HTTP errors

        weather_data = json.loads(response_req.text)
        # print(weather_data)

        # Check for errors in the API response
        if 'error' in weather_data:
            print(f"API Error: {weather_data['error']['message']}")
        else:
            tem_data = weather_data['main']
            # print(tem_data)
            print(f"Weather in {city}:")
            print(f"{tem_data['temp']-273}°C")
            print(f"Maximum-temperature: {tem_data['temp_max']-273}°C")
            print(f"Minimum-temperature: {tem_data['temp_min'] - 273}°C")
            print(f"Feels Like: {tem_data['feels_like']-273}°C")

            climate_condition = weather_data['weather']
            # print(climate_condition)

            print(f"clouds in {city} is: {climate_condition[0]['description']}")





    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")

# Function to add a city to the favorite list
def add_favorite(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in favorites.")

# Function to list favorite cities
def list_favorites():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

# Function to remove a city from the favorite list
def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in favorites.")

# Main loop with auto-refresh every 15-30 seconds
while True:
    print("\nOptions:")
    print("1. Check Weather by City")
    print("2. Add to Favorites")
    print("3. List Favorites")
    print("4. Remove from Favorites")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        city_name = input("Enter city name: ")
        check_weather(city_name)
    elif choice == '2':
        city_name = input("Enter city name to add to favorites: ")
        add_favorite(city_name)
    elif choice == '3':
        list_favorites()
    elif choice == '4':
        city_name = input("Enter city name to remove from favorites: ")
        remove_favorite(city_name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    # Auto-refresh every 15-30 seconds
    refresh_time = 15 + (15 * (0.5 - (time.time() % 1)))
    time.sleep(refresh_time)
