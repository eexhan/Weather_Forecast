import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "x-rapidapi-key": "2e026bbb73msh7b17507736ab174p165f9bjsn2295190a6bc1",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring) 

    
    if response.status_code == 200:
        data = response.json()
        try:
            city_name = data['location']['city']
            temperature = data['current_observation']['condition']['temperature']
            condition = data['current_observation']['condition']['text']
            weather_info = f"City: {city_name}\nTemperature: {temperature}°F\nCondition: {condition}"
        except KeyError:
            weather_info = "Error fetching weather data."
    else:
        weather_info = "Failed to get response from the weather service."

    result_label.config(text=weather_info)


window=tk.Tk()
window.title()
window.geometry('900x600')
window.config(bg='#677D6A')

heading=tk.Label(text="Today's weather",font=('Berlin Sans FB Demi',40),bg='#677D6A',fg='white')
heading.pack()

sub_heading=tk.Label(text='Enter Your City',font=('Brush Script MT',30),fg='white',bg='#677D6A')
sub_heading.pack(pady=10)

city_entry=tk.Entry(font=('Franklin Gothic Medium Cond',30),width=40)
city_entry.pack(pady=20)

button=tk.Button(text='GET WEATHER',font=('Franklin Gothic Medium Cond',30),fg='#677D6A',bg='white',command=get_weather)
button.pack()

result_label = tk.Label( text="",font=('Berlin Sans FB',30),fg='white',bg='#677D6A')
result_label.pack(padx=10, pady=10)


window.mainloop()