
from tkinter import *

def calculate_Km():
   value_km =  float(input_miles.get()) * 1.609
   label_3.config(text = float(value_km))


window = Tk()
window.minsize(width= 200, height= 100)
window.title(" Mile to Km Converter ")
window.config(padx=20,pady = 20)
# Entry
input_miles = Entry(width = 10)
input_miles.grid(column = 1, row = 0)

#labels
label_1 = Label(text="Miles")

label_1.grid(column = 2, row = 0)

label_2 = Label(text=" is equal to")
label_2.grid(column = 0, row = 1)

label_3 = Label(text= 0)
label_3.grid(column = 1 , row = 1)

label_4 = Label(text="Km")
label_4.grid(column = 2, row = 1)

# Button
button_1 = Button(text="Calculate", command=calculate_Km)
button_1.grid(column = 1, row = 2)

window.mainloop()
