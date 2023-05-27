import requests
from tkinter import *

# This program uses the advice split api to generate a piece of advice.
window = Tk()
window.title("Advice Bot")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="#C8C8C8")
x_padding = 20
y_padding = 20

# The end functions simply closes the tkinter window and ends the program.
def end():
    exit()


# The get_advice function performs the api request and then changes the tkinter label to the new piece of advice.
def get_advice():
    response = requests.get(url="https://api.adviceslip.com/advice")
    advice = response.json()["slip"]["advice"]
    # advice = "TESTING TEXT SO I DONT SPAM THE ADVICE API"
    advice_label.config(text=advice)
    title_label.config(text="Here's your advice")


# Title label
title_label = Label(text="", padx=x_padding, pady=y_padding, justify=CENTER, bg="#C8C8C8")
title_label.grid(row=2, column=1, columnspan=3)

# Button for getting advice
button = Button(text="Get advice", padx=5, pady=5, command=get_advice)
button.grid(row=5, column=1)

# Button for stopping the program and closing the tkinter window.
close_button = Button(text="Close", padx=5, pady=5, command=end)
close_button.grid(row=5, column=3)

# spacer label
spacer = Label(text="", bg="#C8C8C8")
spacer.grid(row=4, column=1, columnspan=3)

# Label section for the advice
advice_label = Label(text="Click the Get advice button!", padx=5, pady=5, justify=CENTER, wraplength=200)
advice_label.grid(row=3, column=1, columnspan=3)

# Canvas section for the free robot image. See the code below for the image attribution.
canvas = Canvas(width=100, height=100, bg="#C8C8C8", highlightthickness=0)
robot_image = PhotoImage(file="robot.png")  # Robot image source:"https://www.flaticon.com/free-icons/bot" title="bot icons">Bot icons created by Freepik
canvas.create_image(50, 50, image=robot_image)
canvas.grid(row=1, column=1, columnspan=3)

# main window loop to keep the tkinter window active.
window.mainloop()
