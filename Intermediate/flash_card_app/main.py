# ---------------------------- IMPORTS ------------------------------------------ #
import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# ---------------------------- READING DATA ------------------------------------- #
try:
    my_data_frame = pandas.read_csv("data/words_to_learn.csv")
    list_of_words = my_data_frame.to_dict(orient='records')
except FileNotFoundError:
    my_data_frame = pandas.read_csv("data/german_words.csv")
    list_of_words = my_data_frame.to_dict(orient='records')
# ---------------------------- NEXT CARD ---------------------------------------- #
def get_next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_of_words)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text="German", fill="Black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="Black")
    flip_timer = window.after(3000, get_translation)

# ---------------------------- KNOWN CARD --------------------------------------- #
def known_card():
    list_of_words.remove(current_card)
    new_data_frame = pandas.DataFrame(list_of_words)
    new_data_frame.to_csv("data/words_to_learn.csv", index=False)
    get_next_card()
# ---------------------------- GET TRANSLATION ---------------------------------- #
def get_translation():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
# ---------------------------- UI SETUP ----------------------------------------- #
window = Tk()
window.title("MG Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), tags="word")
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=known_card)
check_button.grid(column=1, row=1)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=get_next_card)
unknown_button.grid(column=0, row=1)

flip_timer = window.after(3000, get_translation)

get_next_card()
# ---------------------------- MAIN LOOP ---------------------------------------- #
window.mainloop()
