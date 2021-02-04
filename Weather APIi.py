import requests
import json

city_name = input('Enter your city: ')

url = 'https://www.metaweather.com/api/location/search/?query=' + city_name
response = requests.get(url)

city_info = json.loads(response.content)
city_info_dict = city_info[0]

weather_info_url = 'https://www.metaweather.com/api/location/' + str(city_info_dict['woeid']) + '/'
response = requests.get(weather_info_url)

city_weather = json.loads(response.content)

tomorrow_weather = city_weather['consolidated_weather'][1]
print(tomorrow_weather['the_temp'] '\n', tomorrow_weather['humidity'] '\n', city_weather['title'])

if tomorrow_weather['the_temp'] > 30:
    print("go out have fun!")
elif tomorrow_weather['the_temp'] > 40:
    print("its too hot today!")
else:
    print("Don't go out anyway, CORONA is their")