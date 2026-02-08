import requests

API_KEY = "97ad78eb20dd1b289d0d4b9e30b43c2f"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values:]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days="3"))

