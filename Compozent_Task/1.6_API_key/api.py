import requests 

def weather(city,api):
    #base url of openweather
    url =  f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    try:
        #Get request to the url
        response = requests.get(url)

        #raise http error 
        response.raise_for_status()

        #parsing response into json
        data =response.json()

        #filtering usefull objects from the response data
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_cond = data['weather'][0]['description']

        #printing the useful data such as temp,weather condition
        print(f"The weather in {city_name},{country}:")
        print(f"Temperture is {temperature}°C")
        print(f"The weather condition is :{weather_cond}")
    #making sure that it does'nt raise an error even if input is invailed
    except requests.exceptions.RequestException:
        print("Error ocured while fetching data")
            
#taking user input for the city
op = input("Enter the name of the city for which you want to check the weather of :")
weather(city=op, api="e7b60f5833602e4505a5891074b408c1")
    