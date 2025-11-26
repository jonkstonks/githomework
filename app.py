import random
import tkinter as tk
from tkinter import ttk

# create root widget, which is the app's main window
root = tk.Tk()
root.geometry('300x200')
root.title('Widget Test')

testLabel = tk.Label(
    text="it is wednesday ,",
    fg="navy"
)

testButton = tk.Button(
    text="mm yes give me the moeny"
)

password = ttk.Entry(root, show='*')

testLabel.pack()
password.pack()
testButton.pack()
root.mainloop()
