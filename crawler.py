import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.theweathernetwork.com/ca/weather/british-columbia/richmond')
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-days-only")
forecast_items = seven_day.find_all(class_="day_name")
forecast_items_deg = seven_day.find_all(class_="chart-daily-temp seven_days_metric seven_days_metric_c")
forecast_items_weather = seven_day.find_all(class_="day_outlook")
today = forecast_items[0]
todayTemp = forecast_items_deg[0]
todayWeather = forecast_items_weather[0]

print(today.prettify())
print(todayTemp.prettify())


print("here's Richmond's weather forecast ")
for i in range (0,len(forecast_items)):
    weather = forecast_items_weather[i].get_text()
    temp = forecast_items_deg[i].get_text()
    date = forecast_items[i].get_text()
    print("date:",date," weather:",weather," temperature:",temp)
