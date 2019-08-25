#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:24:21 2019

@author: Soo Hyeon Kim
- Reads the requested location from the command line.
- Downloads JSON weather data from OpenWeatherMap.org
- Converts the string of JSON data to a Python data structure.
- Prints the weather for today and the next two days
"""

import json, requests, sys

# Compute location from command line arguments.
print(sys.argv)
if len(sys.argv) < 2:
    print('Usage quick_weather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
api_key = 'NO_PERMISSON_FOR_MY_MEMBERSHIP'

# TODO: Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&APPID={}'.format(location, api_key)
res = requests.get(url)
res.raise_for_status()

# TODO: Load JSON data into a Python variable. 
weather_data = json.loads(res.text)

# Print weather descriptions.
w = weather_data['list']
print('Current weather in {}'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
