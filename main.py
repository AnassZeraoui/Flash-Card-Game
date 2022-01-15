"""
* we will create a flashcard project from scratch to help us study a new language which is English

"""
from tkinter import *
import pandas
import random
dict_data = {}
random_data = {}

# reading the csv file using Pandas and convert it to a Dictionary
"""
 here we try to catch an Error which is FileNotFoundError which it may occurs due to a problem which is the data_to_learn is delete it.
 using try ,except , else . we manage to find a solution for that which is when the problem occurs , we run the code using the original data 
 'french_words.csv'
"""
try:
    french_data = pandas.read_csv('data/data_to_learn.csv')  # we load data from the data_to_learn to not begin from 100 words again
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_data = original_data.to_dict(orient="records", index=False)  # this orient options records will display a list containing a key and value of each column ,
    # [{'French': 'partie', 'English': 'part'}] , this index option won't include any index
    french_data.to_dict(orient="records")
def card():
    # we will pick some data randomly
    # we know that we access a Dictionary using the key and value , so we will catch those keys which they are "French" and "English"
    global random_data, timer
    window.after_cancel(timer)
    random_data = random.choice(dict_data)
    # to configure the canvas text , we must use the item config option
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(card_word, text=random_data["French"], fill="black")
    canvas.itemconfig(background_image, image=card_front)
    timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_data["English"], fill="white")
    canvas.itemconfig(background_image, image=card_back)


def is_known_card():
    # when we press the check button , we will remove that word from the 100 words and store them in a csv file "data_to_lear"
    dict_data.remove(random_data)
    data_to_learn = pandas.DataFrame(dict_data)
    data_to_learn.to_csv("data/data_to_learn.csv")
    card()  # calling the card function when we press the check button


# window configuration :
window = Tk()
window.title("Flash Card Game created by Ziraoui Anas")
window.config(bg="#B1DDC6")
window.minsize(915, 710)
window.maxsize(915, 710)
# we can control the time in our GUI using the After method , this method requires the time in Miliseconds and a function to call after
timer = window.after(3000, func=flip)

# configuring the canvas  :
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(window, width=800, height=526)
background_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.place(x=50, y=50)

# configuring the buttons :
cross_image = PhotoImage(file="images/wrong.png")
no_button = Button(window, image=cross_image, highlightthickness=0, command=card)
no_button.place(x=200, y=590)

mark_image = PhotoImage(file="images/right.png")
yes_button = Button(window, image=mark_image, highlightthickness=0, command=is_known_card)
yes_button.place(x=600, y=590)

# we will call the function next_card in order to not see the title and word when we run the program
card()

window.mainloop()
