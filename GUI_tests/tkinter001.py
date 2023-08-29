# Window opens fine
# Example button code didn't work, found nothing helpful on StackOverflow
# so I'll leave Tkinter alone for a now


import tkinter as tk

window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()

# Start the event loop.
window.mainloop()