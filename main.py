import requests
from tkinter import *

# This program uses the advice split api to generate a piece of advice.
window = Tk()
window.title("Advice Generator")
response = requests.get(url="https://api.adviceslip.com/advice")
advice = response.json()["slip"]["advice"]


print(advice)