from tkinter import *
import pandas
import random

def click_action_check():
    click_action()
    [(data_dict.remove(x)) for x in data_dict if (x['French'] ==  random_list[0]['French'])]
    # print (type(data_dict))
    # for x in data_dict:
    #     if x['French'] == random_list[0]['French']:
    #         data_dict.remove(x)
    # data_dict.remove(random_list)
    # print(len(data_dict))
    new_df = pandas.DataFrame.from_dict( data_dict)
    new_df.to_csv("data/words_to_learn.csv", index = False)


def click_action():
    global random_list, flip_timer
    window.after_cancel(flip_timer)
    random_list = random.choices(data_dict)
    # print(random_list)
    canvas_card.itemconfig(image_update,image = front_image)
    canvas_card.itemconfig(title_update,text = "French", fill ="black",)
    canvas_card.itemconfig(text_update,text =random_list[0]['French'], fill = "black")
    flip_timer=window.after(3000,call_english)
def call_english():
    canvas_card.itemconfig(title_update, text="English", fill = "white")
    canvas_card.itemconfig(text_update,text =random_list[0]['English'], fill="white")
    canvas_card.itemconfig(image_update, image = back_image)

BACKGROUND_COLOR = "#B1DDC6"


window =Tk()
window.title("Flashy")
window.config(padx = 100, pady=100, bg=BACKGROUND_COLOR)
try:
    with open ("data/words_to_learn.csv", 'r') as myfile:
        data_csv = pandas.read_csv(myfile)
except FileNotFoundError:
    data_csv = pandas.read_csv("data/french_words.csv")

data_dict = data_csv.to_dict(orient="records")
random_list = {}

flip_timer = window.after(3000,func = call_english )
canvas_card = Canvas(height= 526, width= 800)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image_update = canvas_card.create_image(400, 263,image = front_image)
title_update = canvas_card.create_text(400,150 ,text = "", fill = "black",font=("Ariel",40,"italic"))
text_update = canvas_card.create_text(400, 263 ,text = "", fill = "black",font=("Ariel",60,"bold"))
canvas_card.config( highlightthickness=0, background=BACKGROUND_COLOR)
canvas_card.grid(column =0,row = 0, columnspan = 2)

wrong_image = PhotoImage(file = "images/wrong.png")
button_wrong = Button(image=wrong_image,command= click_action)
button_wrong.config(highlightthickness=0)
button_wrong.grid(column = 0, row = 1)


right_image = PhotoImage(file = "images/right.png")
button_right = Button(image=right_image,command=click_action_check)
button_right.config(highlightthickness=0)
button_right.grid(column = 1, row = 1)

click_action()
window.mainloop()
