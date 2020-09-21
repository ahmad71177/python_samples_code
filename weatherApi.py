# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:46:12 2019

@author: Ahmad
"""


import requests, json 
  
 
complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=449f2b285581edf545efa60d4ffb64a9&q=Montreal" 
response = requests.get(complete_url)  
x = response.json()  
if x["cod"] != "404":  
    y = x["main"] 
    current_temperature = y["temp"] 
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"]  
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 
