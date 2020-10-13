# Capstone: Retrieving, Processing, and Visualizing Data with Python

## "Global Landslide Data" project:

This project is the final assignment of Capstone: Retrieving, Processing, and Visualizing Data with Python which is the last course of 5 from the Python for Everybody Specialization offered by University of Michigan and taught by Dr. Charles Severance on Coursera.
In this Capstone project you are required  to select, process, and visualize the data of your choice.
The data choosen was the "Global Landslide Data" by NASA's Open Data Portal.

>The Global Landslide Catalog (GLC) was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources.
https://data.nasa.gov/Earth-Science/Global-Landslide-Data-Export-Visual-Explorer/angv-aquq

From this data set  various informations about lnadslide events occurred in the period of time from 2006 to 2016 could be retrieved.Informations such as event's date,trigger, location, number of injuries and fatalities,size and ect.
With this data,the countries most affected by landslide accidents will be compared and the results will be visualised in chart graphs.
### Scripts and Process
#### landslide_loads.py
* get data of landslide events in JSON format via Socrata Open Data API
* parse the data and store it in "landslide-data" database
#### basic_output_data.py
* retrieve data from "landslide-data"
* output the list of countries sorted by the number of landslide events
* output the list of countries sorted by the number of fatalities caused by landslide events
#### deaths_word_cloud.py
* retrieve data from "landslide-data"
* write a JavaScript file with countries fatalities count releated text size, this file is to be used to visualize the number of deaths per countriy in a word cloud graph
* after running deaths_word_cloud.py, a "deaths_word_cloud.js" file will be created and would be used to visualize data with the help of D3.js library 
* run the "deaths_word_cloud.htm" to visualize data
#### events_line_chart.py
* retrieve data from "landslide-data"
* write in a JavaScript file the events count in each country per year , this file is to be used to visualize the number of deaths per countriy in a line chart graph.
* after running events_line_chart.py, a "events_line_chart.js" file will be created and would be used to visualize data with the help of D3.js library.
* run the "events_line_chart.htm" to visualize data
### Sources
[Global Landslide Data ][PlDa]

[NASA's Open Data Portal][PlDb]

[Coursera][PlDc]

[Python for Everybody specialization][PlDd]

[PlDa]: <https://data.nasa.gov/Earth-Science/Global-Landslide-Data-Export-Visual-Explorer/angv-aquq>
[PlDb]: <https://nasa.github.io/data-nasa-gov-frontpage/>
[PlDc]: <https://https://www.coursera.org/>
[PlDd]: <https://www.coursera.org/programs/e3f17f0d-dfae-4b16-8880-584e171069bc?collectionId=&productId=F-h1g0w7EeWeOApO_l5R1w&productType=s12n&showMiniModal=true>
