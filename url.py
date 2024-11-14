import tkinter as tk
import requests as r
from tkinter import messagebox

window=tk.Tk()
tk.Label(text="Dame una ciudad : ").grid(column=0, row=0)
ciudad=tk.Entry()
ciudad.grid(column=1, row=0)
def respo(event):
     ciudad2=ciudad.get()
     URL = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad2}&appid=fb6b0285c5cee9586077d091d865f155"
     response = r.get(URL)
     if response.status_code == 200:
          data = response.json()
          temperaturaacutal=int(data["main"]["temp"])-273.15
          clima=data["weather"][0]["description"]
          temperaturamax=int(data["main"]["temp_max"])-273.15
          temperaturamin=int(data["main"]["temp_min"])-273.15
          viento=data["wind"]["speed"]
          tk.Label(text=f"Temp Actual: {temperaturaacutal:.2f}°C \n Clima: {clima} \n Temp Max: {temperaturamax:.2f}°C \n Temp Min: {temperaturamin:.2f}°C \n Viento: {viento} km/h").grid(column=0, row=1, columnspan=2)
     else:
          messagebox.showinfo("NO","No ciudad, no hay")
ciudad.bind("<Return>", respo)
window.mainloop()