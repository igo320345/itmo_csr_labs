import tkinter as tk
import random
import string
from PIL import Image, ImageTk

def generate():
    key = []
    for _ in range(4):
        block = ''
        block += str(random.randint(0, 9))
        block += random.choice(string.ascii_uppercase)
        block += random.choice(string.ascii_uppercase)
        block += random.choice(string.ascii_uppercase)
        key.append(block)
    output.insert(tk.END, '-'.join([i for i in key]))

window = tk.Tk()
window.title('Civilization V keygen')
window.geometry('500x300')
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack(fill='both', expand=True)
image = ImageTk.PhotoImage(Image.open('civ5.jpg'))
canvas.create_image(0, 0, image=image, anchor='nw')
input = tk.Text(canvas, height=1, width=25).place(x = 170, y = 100)
output = tk.Text(canvas, height=1, width=25)
output.place(x = 170, y= 125)
button = tk.Button(canvas, text='Generate', command=lambda:generate()).place(x = 220, y = 150)
window.mainloop()