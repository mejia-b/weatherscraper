'''
Description: This program scrapes weather forecast for the week and converts it to a csv file using pandas library
Author: Brenda Mejia
Date: 10/24/2020
'''
import pandas as pd
import requests
import bs4

# Weather website for West Palm Beach, Fl zipcode(33411) edit link for any other city
url = requests.get('https://forecast.weather.gov/MapClick.php?lat=26.720290000000034&lon=-80.05684999999994#.X5TEN4hKiUk')
soup = bs4.BeautifulSoup(url.text,'lxml')

# Selects class container with week forecast information
week = soup.select('.tombstone-container')

# Using list comprehensions lists are created to grab the names, descriptions, and temperatures of each day
period_names = [day.find(class_='period-name').get_text() for day in week[1:]]
short_descriptions = [day.find(class_='short-desc').get_text() for day in week[1:]]
temperatures = [day.find(True,{'class':['temp temp-low','temp temp-high']}).get_text() for day in week[1:]]

# Create the table using Pandas with the above lists, arrays have to be of same length
weatherData = pd.DataFrame(
    {
        'Period': period_names,
        'Short-Descriptions': short_descriptions,
        'Temperatures': temperatures,
    })

#UNCOMMENT BELOW LINES TO DISPLAY THE DATA AND SAVE TO A FILE
#print(weatherData)
#weatherData.to_csv('weatherdata.csv')