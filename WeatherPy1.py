#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
from api_keys import api_key

# OpenWeatherMap API Key
api_key = "7f7ae4ea9f686de9a99d7a6a08fbe977"

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[3]:


#info to hold
newcity = []
cloudiness = []
country = []
date = []
humidity = []
lat = []
lng = []
Maxtemp = []
WindSpeed = []

print ("Beginning Data Retrieval")
print ("------------")

for city in cities:
 query_url = url + "&q=" + city
    response = requests.get(query_url).json()
    
if record < 50:
   record += 1
else:
    sets += 1
    record = 0

newcity.append(response["name"])
cloudiness.append(response["clouds"]["all"])
country.append(response["sys"]["country"])
date.append(responde["dt"])
humidity.append(response["main"]["humidity"])
lat.append(response["coord"]["lat"])
lng.append(response["coord"]["lon"])
maxtemp.append(response["main"]["maxtemp"])
windspeed.append(response["wind"]["speed"])

except KeyError:
    print("City not found. Skipping...")
    pass

print("Processing record {} of set {},{}".format(record,sets,city))

print("-------")
print("Data Retrieval Complete")
print("-------")


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[4]:


weatherdata = pd.DataFrame({
"City": newcities,
"Cloudiness": cloudiness,
"Country":country,
"date":date,
"humidity":humidity,
"Lat":lat,
"Lng":lng,
"MaxTemp": maxtemp,
"WindSpeed": windspeed,
})

weather_data.head()
weather_df.count()


# In[5]:


output_file = weather_df.to_csv ('output_file.csv', index = None, header=True)
weather_df.head()


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[6]:


currentdate=datetoday()

#scatter details
plt.scatter(weather_df["Lat"],
weather_df["Max Temp"],
marker = "8", color = "#8f9805",
edgecolors="black")

plt.xlim(-70,90)
plt.ylim(-50,120)
plt.xlabel("Latitude")
plt.ylabel("Max Temperature(F)")
plt.grid()
plt.title("City Latitude vs. Max Temperature (%s/%s/%s" %
(Current_date.month,current_date.day, current_date.year) + ")")

plt.savefig("Lat_vs_MaxTemp.png)


# #### Latitude vs. Humidity Plot

# In[7]:


plt.scatter(weather_df["Lat"],
weather_df["Humidity"], marker="8", color = "#8f9805", edgecolor = "black"
plt.xlim(-70,90)
plt.ylim(0,105)
plt.xlabel("Latitude")
plt.ylabel("Humidity(%)")
plt.grid()
plt.title("City Latitude vs. Humidity (%s/%s/%s" % (current_date.month,current_date.day,current_date.year) + ")")

plt.savefig("Lat_vs_Humidity.png")


# #### Latitude vs. Cloudiness Plot

# In[8]:


plt.scatter(weather_df["Lat"], weather_df["Cloudiness"], marker ="8", color = "#8f9805", edgecolor = "black")
plt.xlim(-70, 90)
plt.ylim(-10, 105)
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)"")
plt.grid()
plt.title("City Latitude vs. Cloudiness (%s/%s/%s" % (current_date.month, current_date.day, current_date.year) + "))

plt.savefig("Lat_vs_Cloudiness.png")


# #### Latitude vs. Wind Speed Plot

# In[2]:


plt.scatter(weather_df["Lat"], weather_df["Wind Speed"], marker ="8", color = "#8f9805", edgecolor = "black")
plt.xlim(-70, 90)
plt.ylim(-1, 45)
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.grid()
plt.title("City Latitude vs. Wind Speed (%s/%s/%s' % (current_date.month, current_date.day, current_date.year) + ")")

plt.savefig("Lat_vs_Wind_Speed.png")


# In[ ]:




