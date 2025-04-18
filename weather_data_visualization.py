
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API details
API_KEY = "a482f980da9e92e4fe3aaa9298e52732"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Define the city and parameters
CITY = "Mumbai"
PARAMS = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

# Fetch data from the API
response = requests.get(BASE_URL, params=PARAMS)
data = response.json()

if response.status_code == 200:
    # Parse the forecast data
    timestamps = []
    temperatures = []
    humidity = []
    
    for entry in data['list']:
        timestamps.append(datetime.datetime.fromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

    # Create visualizations
    sns.set(style="darkgrid")

    # Plot temperature and humidity on the same plot with scatter plot for better comparison
    plt.figure(figsize=(10, 6))
    plt.scatter(timestamps, temperatures, label='Temperature (°C)', color='orange', marker='o')
    plt.scatter(timestamps, humidity, label='Humidity (%)', color='blue', marker='x')
    
    plt.title(f"Temperature & Humidity Trends for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot a separate temperature trend with line plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label='Temperature (°C)', color='orange', marker='o')
    plt.title(f"Temperature Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot a separate humidity trend with line plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, humidity, label='Humidity (%)', color='blue', marker='o')
    plt.title(f"Humidity Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to fetch data: {data.get('message', 'Unknown error')}")
