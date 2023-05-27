import requests
from tkinter import *

# This program uses the advice split api to generate a piece of advice.
window = Tk()
window.title("Advice Bot")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="#C8C8C8")
x_padding = 20
y_padding = 20


def end():
    exit()


def get_advice():
    response = requests.get(url="https://api.adviceslip.com/advice")
    advice = response.json()["slip"]["advice"]
    # advice = "TESTING TEXT SO I DONT SPAM THE ADVICE API"
    advice_label.config(text=advice)


# Title label
title_label = Label(text="Here's your advice", padx=x_padding, pady=y_padding, justify=CENTER, bg="#C8C8C8")
title_label.grid(row=1, column=1, columnspan=3)

# Button for getting advice
button = Button(text="Get advice", padx=5, pady=5, command=get_advice)
button.grid(row=4, column=1)

# Button for stopping the program and closing the tkinter window.
close_button = Button(text="Close", padx=5, pady=5, command=end)
close_button.grid(row=4, column=3)

# spacer label
spacer = Label(text="", bg="#C8C8C8")
spacer.grid(row=3, column=1, columnspan=3)

# Label section for the advice
advice_label = Label(text="Click the Get advice button!", padx=5, pady=5, justify=CENTER, wraplength=200)
advice_label.grid(row=2, column=1, columnspan=3)

window.mainloop()
