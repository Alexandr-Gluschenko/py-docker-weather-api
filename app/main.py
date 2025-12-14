import os
import requests

def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")

    if not API_KEY:
        raise ValueError("API_KEY is not provided")
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print("Error:", data["error"]["message"])
        return
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Paris/France {data} Weather: {temp} {condition}")

if __name__ == "__main__":
    get_weather()
