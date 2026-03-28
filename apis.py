import requests
from requests import RequestException
import datetime

def get_public_ip():
    try:
        response = requests.get("https://httpbin.org/ip").json()
        return response["origin"]
    except RequestException as e:
        print(f"Error fetching IP: {e}")
        return

def get_weather(city):
    conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Icy fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight showers",
        81: "Moderate showers",
        82: "Violent showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    try: 
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        data = requests.get(url).json()
        lat = data["results"][0]["latitude"]
        long = data["results"][0]["longitude"]
    except RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return

    try: 
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
        weather_data = requests.get(weather_url).json()
        temp = weather_data["current_weather"]["temperature"]
        wind = weather_data["current_weather"]["windspeed"]
        code = weather_data["current_weather"]["weathercode"]
        condition = conditions.get(code, "Unknown")
    except RequestException as e:
        print(f"Error fetching weather: {e}")
        return
    
    print(f"Weather in {city}:")
    print(f"    Temperature: {temp}°C")
    print(f"    Wind speed: {wind}")
    print(f"    Condition: {condition}")

def check_site(site_URL):
    if not site_URL.startswith(("http://", "https://")):
        site_URL = "https://" + site_URL
    try:
        response = requests.head(site_URL)
        response.raise_for_status()
        print(f"{site_URL} - UP ({response.status_code})")
        return True
    except RequestException as e:
        print(f"{site_URL} - DOWN (Error: {e})")
        return False

def get_fact():
    try: 
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        data = requests.get(url).json()
        fact = data["text"]
        print(f"Random fact: {fact}")
    except RequestException as e:
        print(f"Error fetching fact: {e}")
        return

def homelab_status():
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    public_IP = get_public_ip()
    
    pihole_up = check_site("http://192.168.8.110/admin")
    homelab_up = check_site("http://192.168.8.110")
    
    print("=== Homelab Status ===")
    print(f"Public IP:  {public_IP}")
    print(f"Pi-hole:    {'UP' if pihole_up else 'DOWN'}")
    print(f"Homelab:    {'UP' if homelab_up else 'DOWN'}")
    print(f"Checked:    {date_time}")
    print("=======================")


print(get_public_ip())

get_weather("Houston")

check_site("https://google.com")
check_site("https://notarealsite12345.com")
check_site("https://192.168.8.110")

get_fact()

homelab_status()