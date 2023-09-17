# Window appears fine
# Example button code didn't work, found nothing helpful on StackOverflow
# so I'll leave Tkinter alone for a now


import tkinter as tk

window = tk.Tk()
window.title("This is the NEWS")
window.geometry("500x200")

l1 = tk.Label(window, text = "ah it's yourself", font=("Arial Bold", 50))
l1.grid(column=0,row=0)

def clicky():
    l1.configure(text=txt.get())


button = tk.Button(window, text = "Clicky", command=clicky)
button.grid(column=0,row=1)

txt = tk.Entry(window, width=11)
txt.grid(column=0,row=2)

window.mainloop()