from  tkinter import *
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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer",fg=GREEN)
    global reps
    reps=0
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_secs=WORK_MIN*60
    sbreak_secs=SHORT_BREAK_MIN*60
    lbreak_secs=LONG_BREAK_MIN*60
    if reps%2!=0:
        countdown(work_secs)
        title_label.config(text="Work",fg=GREEN)

    if reps%2==0 and reps!=8:
        countdown(sbreak_secs)
        title_label.config(text="Break",fg=PINK)
    if reps%8==0:
        countdown(lbreak_secs)
        title_label.config(text="Break",fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    mins=math.floor(count/60)
    secs=count%60
    if len(str(secs))==1:
        secs=f"0{secs}"

    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        for each in range(math.floor(reps/2)):
            mark+="✔"
        check_marks.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


title_label=Label(text="Timer",font=(FONT_NAME,50),bg=YELLOW,fg=GREEN)
title_label.grid(column=1,row=0)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(bg=YELLOW,fg=GREEN)
check_marks.grid(column=1,row=3)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


window.mainloop()


