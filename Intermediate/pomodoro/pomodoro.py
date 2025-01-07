# ---------------------------- IMPORTS --------------------------------------- #
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_MIN = 5
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_MIN = 20
LONG_BREAK_SEC = LONG_BREAK_MIN * 60
check_mark = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ----------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)  # Cancel the after job
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    mark_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_SEC)
    elif reps % 2 == 1:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_SEC)
    elif reps % 2 == 0 and reps < 8:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_SEC)
# ---------------------------- COUNTDOWN MECHANISM --------------------------- #
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    time_formatted = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_formatted)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark_label.config(text=(reps // 2) * check_mark)
# ---------------------------- UI SETUP -------------------------------------- #
window = Tk()
window.title("Pomodoro 🍅")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)
mark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
mark_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_bt = Button(text="Start", highlightthickness=0, command=start_timer)
start_bt.grid(column=0, row=2)
reset_bt = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2, row=2)


# ---------------------------- MAIN LOOP ------------------------------------- #
window.mainloop()
