#!/usr/bin/env python
 
# Yahoo Weather API
# https://developer.yahoo.com/weather/
 
import urllib2, urllib, json
 
city = "Zele"
country = "Belgium"
 
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where u='c' and woeid in (select woeid from geo.places(1) where text='" + city + "," + country + "')"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
 
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
 
current_weather = data['query']['results']['channel']['item']['condition']['text']
current_temperature = data['query']['results']['channel']['item']['condition']['temp']
 
forecast_weather = data['query']['results']['channel']['item']['forecast'][0]['text']
forecast_temperature_high = data['query']['results']['channel']['item']['forecast'][0]['high']
forecast_temperature_low = data['query']['results']['channel']['item']['forecast'][0]['low']
 
response = "Today's weather forecast is " + forecast_weather + " with a high of " + forecast_temperature_high + " and low of " + forecast_temperature_low + " degrees. The current weather is: " + current_weather + " with a temperature of " + current_temperature + " degrees."
 
print response
