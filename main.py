import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Python Development')
root.geometry('800x450+300+100')

imagem = Image.open('./images/mario.webp').resize((600, 450))
photo = ImageTk.PhotoImage(imagem)

label = ttk.Label(root, image=photo).pack()

# Start minloop
root.mainloop()
