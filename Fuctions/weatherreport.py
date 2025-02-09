import requests

def get_weather_zip(local_zip, country = "US"):
    url = f"https://nominatim.openstreetmap.org/search?postalcode={local_zip}&country={country}&format=json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data:
            return f"We couldn't find data for the zip code {local_zip}."
        
        lat = float(data[0]["lat"])
        lat = float(data[0]["lon"])

        weather = data.get("current_weather, {}")
        if not weather:
            return "Weather data not availible."
        
        temp = weather.get("temperature")
        wind = weather.get("windspeed")
        weather_code = weather.get("weathercode")
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    
zipcode = input("What is your zip code?")

print(get_weather_zip(zipcode))