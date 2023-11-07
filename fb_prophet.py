import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data=pd.read_csv("/content/drive/MyDrive/datasets/DailyDelhiClimateTrain.csv")
#printing data snapshot
print(data.head())
#Printing descriptve statistics
print(data.describe())
#printing data information
print(data.info())
#Temperature in Delhi over the years
figure= px.line(data, x="date", y="meantemp",
                 title='Mean Temperature in Delhi Over the Years')
figure.show()
#Humidity over the years
figure=px.line(data,x="date", y="humidity",
               title="Humidity in delhi over the years")
figure.show()
#Plotting Wind speed in delhi over the years
figure=px.line(data,x="date", y="wind_speed",
               title="Wind speed in delhi over the years")
figure.show()
#Exploring relationship by using a scatter plot
figure = px.scatter(data_frame = data, x="humidity",
                    y="meantemp", size="meantemp",
                    trendline="ols",
                    title = "Relationship Between Temperature and Humidity")
figure.show()
#analyzing temperature over months & years by converting date to months and year
#converting date data to months & time
data["date"] = pd.to_datetime(data["date"],format = '%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
print(data.head())
#temperature change segmented over months
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.title("Temperature Change in Delhi Over the Years")
sns.lineplot(data = data, x='month', y='meantemp', hue='year')
plt.show()
#installing prophet package
pip install prophet
#renaming columns according to Prophet packages nomenclature of date as 'ds' and mean temp as 'y'
forecast_data = data.rename(columns = {"date": "ds",
                                       "meantemp": "y"})
print(forecast_data)
#forecastimg using prophet
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
plot_plotly(model, predictions)