
import requests

def get_weather_forcast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Cincinnati,oh&units=imperial&appid=9e06e94d0bfc31229deea8a15eca8ae0'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_min'] 

    print(description)
    print(temp_min)
    print(temp_max)

get_weather():
