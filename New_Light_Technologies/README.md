
# Extracting Building Values from Zillow
This project represents a collaboration between General Assembly and New Light Technologies.

This objective of this application is to allow users to search for the information about property values within areas projected to experience natural disasters.

## Problem Statement:

- During a disaster, it is important to model and estimate the potential or forecasted effect of the event, including the projected/forecasted damage.
- Existing indicators of forecasted damage include: number of structures within the affected area, number of people in the area, number of households, demographics of the impacted population, etc.
- This project adds an additional indicator: the value of the properties in the affected area. Property values are estimated according to the market price of houses published on real estate websites.
 
## Objective:
- Utilizing real-time data on property market prices published on  Zillow.com and Trulia.com, as well as downloaded csv files that include recent data from Realtor.com, we estimate the potential damage from natural disasters based on property values.  When available, data for the same properties listed on multiple websites are also averaged. Then data from all properties are aggregated within zip codes. 
- The tool allows an area's residents, planners, and /or policymakers to automatically search for the mean, median, minimum, and maximum estimated values of properties in areas affected by natural disasters using zip codes as inputs.
- The tool then retrieves and maps the current property values in the selected zip code, and graphs the historical values of properties.

## Installing / Getting started

To complete the analysis, the following libraries were utilized:

```shell
import bokeh
from bokeh.io import output_file, show, output_notebook, push_notebook, show
from bokeh.models import (ColumnDataSource, GMapOptions, HoverTool, 							   WheelZoomTool,PanTool, BoxSelectTool, Circle, 							   Patches,GMapPlot, Circle,
                          LogColorMapper, BasicTicker, ColorBar,Range1d,
                          DataRange1d, PanTool, WheelZoomTool, 								BoxSelectTool, ResetTool)
                          
from bokeh.embed import components
from bokeh.plotting import gmap
from bokeh.models.mappers import ColorMapper, LinearColorMapper
from bokeh.palettes import Viridis5
from bokeh.plotting import figure
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from historical_scraper import historical_data
from media_maker import plot_map, plot_historical, create_table
import numpy as np 
import os
import pandas as pd
import quandl from selenium import webdriver
from realtor_scraper import realtor_data
import sys
import time
from trulia_scraper import trulia_data
from uszipcode import SearchEngine
import zillow
from zillow_scraper import zillow_data 
```

## Data

| Column | Description |
| --- | --- |
| **Address** | The address for specific property listing. |
| **City** | The city in which specific property is located. |
| **Latitude** | The latitude at which specific property is located. |
| **Longitude** | The longitude at which specific property is located. |
| **Maximum** | The maximum price for properties in a particular zipcode.|
| **Mean** | The average price for properties in a particular zipcode. |
| **Median** | The median price for properties in a particular zipcode.|
| **Minimum** | The minimum price for properties in a particular zipcode.|
| **Area** | The total floor area of the property in square footage. |
| **Bedrooms** | The number of bedrooms that the property has. |
| **Bathrooms** | The number of bathrooms that the property has. |
| **Price** | The selling price for a specific property listed on Trulia and the ["Zestimate"](https://www.zillow.com/zestimate/) valuation for one listed on Zillow.|
| **State** | The state in which a specific property is listed. |
| **Zip** | The zipcode selected.|
 

### Initial Configuration

In order to use GMaps, you must obtain an API key from google's website. [Click here](https://developers.google.com/maps/documentation/javascript/tutorial) to go to their website.

## Project Development

To view this project follow the steps below:

```shell
git clone https://git.generalassemb.ly/hixjasmi/Project-4-Zillow.git
packagemanager install
```
 

## Features
 
* The app allows you to map out an area based on zipcode<br>
* Based on the zipcode, you can then click on individual properties for properties within the selected area and view the prices. <br> 
* A table is also generated describing the zipcode's average property value based on each source.<br>
* Additional value metrics for the table can be selected via a drop down menu. However, this can affect which sources can be compared.<br>

Following, a screenshot of the web app is illustrated,

![](./Screenshot.png)
 

## Links

API Links: 

- Project homepage: [https://github.com/hixjas/Project-4-Zillow]('https://github.com/hixjas/Project-4-Zillow') 
 

- Subdirectories:

Code for obtaining data from Zillow.com

[https://github.com/hixjas/Project-4-Zillow/blob/master/zillow_scraper.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/zillow_scraper.py')

Code for obtaining historical data
[https://github.com/hixjas/Project-4-Zillow/blob/master/historical_scraper.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/historical_scraper.py')

Code for obtaining data from Trulia.com

[https://github.com/hixjas/Project-4-Zillow/blob/master/trulia_scraper.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/trulia_scraper.py')

Code for obtaining data from Realtor.com
[https://github.com/hixjas/Project-4-Zillow/blob/master/realtor_scraper.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/realtor_scraper.py')

Code for making the map
[https://github.com/hixjas/Project-4-Zillow/blob/master/media_maker.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/media_maker.py')

Code for running the tool
[https://github.com/hixjas/Project-4-Zillow/blob/master/app.py]('https://github.com/hixjas/Project-4-Zillow/blob/master/app.py')

Presentation slides
[https://github.com/hixjas/Project-4-Zillow/blob/master/Client%20Project.pdf]('https://github.com/hixjas/Project-4-Zillow/blob/master/Client%20Project.pdf')

## Contact Info

Jasmine Hix - email: hixjas@gmail.com <br>
Alireza Karimi - email: a.karimi@neu.edu <br>
Amy DeSantis - email: desantis.amy@gmail.com <br>
Sam Michaelis - email: sam.michaelis@uconn.edu <br>
