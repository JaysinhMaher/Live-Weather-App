# Imports
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image


"""Creates the tkinter window and places various elements"""
def create_app():
    root = tk.Tk()
    root.title('Weather app')
    root.config(bg='white')
    root.resizable(False, False)
    location_label = tk.Label(root, font=('Calibri', 25), bg="white")
    location_label.grid(row=0, column=0, columnspan=2, padx=50)
    temp_label = tk.Label(root, font=('Calibri', 75), bg="white")
    temp_label.grid(row=1, column=0)
    forecast_label = tk.Label(root, font=('Calibri', 20), bg="white")
    forecast_label.grid(row=2, column=0)
    img = Image.open("weather icon.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(root, image=img, bg="white")
    image_label.grid(row=1, column=1, rowspan=2)

    return root, temp_label, location_label, forecast_label, img


"""Gets the webpage data"""
def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


"""Gets the specific data we need from the filtered data"""
def get_data(soup):
    temp = soup.find("span", class_="CurrentConditions--tempValue--3a50n").text
    location = soup.find("h1", class_="CurrentConditions--location--kyTeL").text
    forecast = soup.find("div", class_="CurrentConditions--phraseValue--2Z18W").text
    return temp, location, forecast


"""Updates the weather data shown on the app"""
def update_app(temp_label, location_label, forecast_label):
    soup = get_soup("https://weather.com/weather/today/")   # Change this link with the weather.com link that relates to your location
    temp, location, forecast = get_data(soup)
    temp_label.config(text=temp)
    location_label.config(text=location)
    forecast_label.config(text=forecast)
    temp_label.after(300000, lambda: update_app(temp_label, location_label, forecast_label))
    root.update()


# Main
root, temp_label, location_label, forecast_label, img = create_app()
update_app(temp_label, location_label, forecast_label)
root.mainloop()
