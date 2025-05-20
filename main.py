from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root = Tk()
root.title("Vremenska prognoza")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="cordadanilo@gmail.com")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    tamezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&appid=213efbe74ec334eb48298f3b96d69c28"
    json_data = requests.get(api).json()
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    print(json_data)
    
    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=(description))
    
    #cells
    #1
    firstdayImage = json_data['daily'][0]['weather'][0]['icon']
    
    photo1 = ImageTk.PhotoImage(file=f"imgs/{firstdayImage}@2x.png")
    firstImage.config(image=photo1)
    firstImage.image = photo1
    
    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")
    
    #ostale
    #2
    seconddayImage = json_data['daily'][1]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{seconddayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondImage.config(image=photo2)
    secondImage.image = photo2
    
    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")
    
    #3
    thirddayImage = json_data['daily'][2]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{thirddayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdImage.config(image=photo3)
    thirdImage.image = photo3
    
    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")
    
    #4
    fourthdayImage = json_data['daily'][3]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{fourthdayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthImage.config(image=photo4)
    fourthImage.image = photo4
    
    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")
    
    #5
    fifthdayImage = json_data['daily'][4]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{fifthdayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthImage.config(image=photo5)
    fifthImage.image = photo5
    
    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")
    
    #6
    sixthdayImage = json_data['daily'][5]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{sixthdayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthImage.config(image=photo6)
    sixthImage.image = photo6
    
    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")
    
    #7
    seventhdayImage = json_data['daily'][6]['weather'][0]['icon']
    
    img = (Image.open(f"imgs/{seventhdayImage}@2x.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhImage.config(image=photo7)
    seventhImage.image = photo7
    
    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")
    
    #days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    


image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)

round_box = PhotoImage(file="images/Rounded Rectangle 1.png")
Label(root, image=round_box, bg="#57adff").place(x=30, y=110)

label1 = Label(root, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind", font=("Helvetica", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

search_image = PhotoImage(file="images/Rounded Rectangle 3.png")
myimage = Label(image=search_image, bg="#203243")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify="center", width=15, font=("popins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="images/Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)


frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=40, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=20)

clock = Label(root, font=("Helvectica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

tamezone = Label(root, font=("Helvectica", 20), fg="white", bg="#57adff")
tamezone.place(x=650, y=20)

long_lat = Label(root, font=("Helvectica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=60)



t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=148, y=160)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)
        

#Prva kocka
firstFrame = Frame(root, width=250, height=132, bg="#282829")
firstFrame.place(x=35, y=315)

day1 = Label(firstFrame, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

firstImage = Label(firstFrame, bg="#282829")
firstImage.place(x=1, y=15)

day1temp = Label(firstFrame, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

#Ostale
#2
secondFrame = Frame(root, width=70, height=115, bg="#282829")
secondFrame.place(x=305, y=315)

day2 = Label(secondFrame, bg="#282829", fg="#fff")
day2.place(x=10, y=5)

secondImage = Label(secondFrame, bg="#282829")
secondImage.place(x=7,y=20)

day2temp = Label(secondFrame, bg="#282829", fg="#fff")
day2temp.place(x=2, y=70)
#3
thirdFrame = Frame(root, width=70, height=115, bg="#282829")
thirdFrame.place(x=405, y=315)

day3 = Label(thirdFrame, bg="#282829", fg="#fff")
day3.place(x=10, y=5)

thirdImage = Label(thirdFrame, bg="#282829")
thirdImage.place(x=7,y=20)

day3temp = Label(thirdFrame, bg="#282829", fg="#fff")
day3temp.place(x=2, y=70)
#4
fourthFrame = Frame(root, width=70, height=115, bg="#282829")
fourthFrame.place(x=505, y=315)

day4 = Label(fourthFrame, bg="#282829", fg="#fff")
day4.place(x=10, y=5)

fourthImage = Label(fourthFrame, bg="#282829")
fourthImage.place(x=7,y=20)

day4temp = Label(fourthFrame, bg="#282829", fg="#fff")
day4temp.place(x=2, y=70)
#5
fifthFrame = Frame(root, width=70, height=115, bg="#282829")
fifthFrame.place(x=605, y=315)

day5 = Label(fifthFrame, bg="#282829", fg="#fff")
day5.place(x=10, y=5)

fifthImage = Label(fifthFrame, bg="#282829")
fifthImage.place(x=7,y=20)

day5temp = Label(fifthFrame, bg="#282829", fg="#fff")
day5temp.place(x=2, y=70)
#6
sixthFrame = Frame(root, width=70, height=115, bg="#282829")
sixthFrame.place(x=705, y=315)

day6 = Label(sixthFrame, bg="#282829", fg="#fff")
day6.place(x=10, y=5)

sixthImage = Label(sixthFrame, bg="#282829")
sixthImage.place(x=7,y=20)

day6temp = Label(sixthFrame, bg="#282829", fg="#fff")
day6temp.place(x=2, y=70)
#7
seventhFrame = Frame(root, width=70, height=115, bg="#282829")
seventhFrame.place(x=805, y=315)

day7 = Label(seventhFrame, bg="#282829", fg="#fff")
day7.place(x=10, y=5)

seventhImage = Label(seventhFrame, bg="#282829")
seventhImage.place(x=7,y=20)

day7temp = Label(seventhFrame, bg="#282829", fg="#fff")
day7temp.place(x=2, y=70)







root.mainloop()