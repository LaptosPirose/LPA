import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Simple tkinter Screen')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 800
window_height = 450

window_pos_x = str(int((screen_width/2) - (window_width/2)))
window_pos_y = str(int((screen_height/2) - (window_height/2)))

print(f'A largura da tela do notebook é: {screen_width}')
print(f'A altura da tela do notebook é: {screen_height}')

root.geometry(str(window_width)+'x'+str(window_height)+'+'+window_pos_x+'+'+window_pos_y)      



root.mainloop()
