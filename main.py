import tkinter as tk
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
French_Words = data.French
English_Words = data.English
current_card = 0



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.randint(0, 101)
    canvas.itemconfig(Word, text=French_Words[current_card], fill="black")
    canvas.itemconfig(Title, text="French", fill="black")
    canvas.itemconfig(cards, image=card_front_img)

    with open("learn.csv", "a") as f:
        f.write(f"{French_Words[current_card]},{English_Words[current_card]}\n")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(Word, text=English_Words[current_card], fill="white")
    canvas.itemconfig(cards, image=card_back_img)


# UI
window = tk.Tk()
window.title("flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
right_button = tk.PhotoImage(file="images/right.png")
wrong_button = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=800, height=526, highlightthickness=0)

cards = canvas.create_image(400, 263, image=card_front_img)
Title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
Word = canvas.create_text(400, 264, text="", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR)

canvas.grid(column=1, row=0, columnspan=2)

Button_Right = tk.Button(image=right_button, highlightthickness=0, command=next_card)
Button_Right.grid(column=1, row=1)
Button_Wrong = tk.Button(image=wrong_button, highlightthickness=0, command=next_card)
Button_Wrong.grid(column=2, row=1)
next_card()

window.mainloop()
