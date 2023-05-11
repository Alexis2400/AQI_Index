#examples of numpy and panda
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#Dataset from 2022 going to 2023
# Displays the First Five countries from the dataset assigned with their columns.
df = pd.read_csv('aqi.csv')
print(df.head())


#Setting variable air
#Function that allows to ouput in the terminal the "Top 10 countries with the highest AQI value"
highest = df.iloc[-141: ,:].sort_values(ascending = False ,by = "AQI Value")[:10]
print(highest)

#Display of date wise AQI status of the "Top 10 countries with the highest AQI value" in a bar graph.
#Uses library plotly.express to showcase the graph.
fig =px.bar(highest , x = "AQI Value", y = "Country" , color = "Status" , title = "Top 10 countries with highest AQI value.")
print(fig.show())

#Setting variable air
#Function that allows to ouput in the terminal the "Top 10 countries with the lowest AQI value"
lowest = df.iloc[-141: ,:].sort_values(ascending = True ,by = "AQI Value")[:10]
print(lowest)

#Display of date wise AQI status of the "Top 10 countries with the highest AQI value" in a bar graph.
#Uses library plotly.express to showcase the graph.
fig =px.bar(lowest , x = "AQI Value", y = "Country" , color = "Status" , title = "Top 10 countries with the lowest AQI value.")
print(fig.show())


#Display of date wise AQI status of countries on world map with different colors matching the aqi status.
#Uses library plotly.express to showcase the graph.
fig = px.choropleth(df,locations = "Country", locationmode='country names', color="Status", animation_frame="Date",range_color= [25,450])
print(fig.show())

