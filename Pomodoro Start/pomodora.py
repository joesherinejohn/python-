from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_count():
    global  reps
    reps +=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 ==0 :
        count_down(short_break_sec)
        label_timer.config(text = "Break", fg = PINK)
    elif reps % 8== 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
def count_down(count):
    # print(count)
    count_min = math.floor(count/60)
    count_sec = count%60
    if len(str(count_sec)) < 2 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_count()
        text_out = ""
        for i in range (math.floor(reps/2)):
            text_out += CHECKMARK
        label_checkmark.config(text = f"{text_out}")
def reset_timer():
        global reps
        reps = 0
        window.after_cancel(timer)
        label_timer.config(text="Timer", fg = GREEN)
        canvas.itemconfig(timer_text, text = "00:00")
        label_checkmark.config(text= "")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
# window.minsize(width = 600, height = 600)
window.config(padx= 100,pady= 100, bg = YELLOW)
# text timer
label_timer = Label(text = "Timer", fg = GREEN, bg = YELLOW,font=(FONT_NAME, 35,'bold'))
label_timer.grid(column = 1, row = 0)
# tomato
canvas = Canvas(width= 200, height=224,bg = YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100, 135, text ="00.00",fill = "white",font=(FONT_NAME,35,'bold'))
canvas.grid(column = 1, row = 1)

# count_down(5)
# start
start_button = Button(text="Start", bd =0, highlightthickness= 0, command=start_count)
start_button.grid(column = 0 , row  = 2)
# check mark

label_checkmark = Label( fg = GREEN, bg = YELLOW, font=(FONT_NAME,35,'normal'))
label_checkmark.grid(column = 1 , row = 3)

# reset
start_reset = Button(text="Reset",  bd = 0 , highlightthickness= 0, command=reset_timer )
start_reset.grid(column = 2 , row  = 2)


window.mainloop()
