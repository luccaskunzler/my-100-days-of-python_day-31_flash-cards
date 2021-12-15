from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
NORMAL_FONT = ("Arial", 36, "normal")
SMALL_FONT = ("Arial", 10, "normal")
BIG_FONT = ("Arial", 48, "bold")


def italian(word):
    canvas.delete(ALL)
    canvas.create_image(400, 263, image=front_card)
    canvas.create_image(500, 100, image=italian_flag)
    canvas.configure(bg=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=2)
    language = canvas.create_text(350,100,fill="darkblue",font=NORMAL_FONT,
                            text="Italiano")
    word = canvas.create_text(400,260,fill="darkblue",font=BIG_FONT,
                            text=f"{word}")


def english(word):
    canvas.delete(ALL)
    canvas.create_image(400, 263, image=back_card)
    canvas.create_image(500, 100, image=english_flag)
    canvas.configure(bg=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=2)
    language = canvas.create_text(350, 100, fill="darkblue", font=NORMAL_FONT,
                                  text="English")
    word = canvas.create_text(400, 260, fill="darkblue", font=BIG_FONT,
                              text=f"{word}")

def got_wrong():
    global wrong
    wrong += 1
    give_random()

def give_random():
    global random_line
    random_line = random.randint(0, len(data))
    global i
    i = 0
    flip()

def got_right():
    global random_line, right
    right += 1
    data.drop([random_line], axis=0, inplace=True)
    give_random()


def flip(event=None):
    global i
    if i % 2 == 0:
        italian(data["Italian"].values[random_line])
        i += 1
    else:
        english(data["English"].values[random_line])
        i += 1

# screen setup
window = Tk()
window.title("Italian Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
italian_flag = PhotoImage(file="./images/italy.png")
english_flag = PhotoImage(file="./images/english.png")

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=got_wrong, borderwidth=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=got_right, borderwidth=0)
right_button.grid(row=1, column=1)

# import csv of word to data
data = pandas.read_csv("./data/italian-english.csv")

right = 0
wrong = 0
print(f"You have {len(data)} words yet to go")

# starts with a random number
give_random()
# executes the italian function with the value from line random_line and column Italian
italian(data["Italian"].values[random_line])

# sets initial counter to 1, so flip always (when pressed) to the English card
i = 1
window.bind("<space>", flip)



window.mainloop()

data.to_csv("./data/italian-english.csv", index=False)
print(f"You have {len(data)} words yet to go")
print(f"In this session, you got {right} words right!")
print(f"In this session, you got {wrong} words wrong!")
