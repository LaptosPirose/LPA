import tkinter as tk
from tkinter import ttk


class MainScreen(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Simple tkinter Screen _ OO')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 800
        window_height = 450

        window_pos_x = str(int((screen_width/2) - (window_width/2)))
        window_pos_y = str(int((screen_height/2) - (window_height/2)))

        self.geometry(str(window_width)+'x'+str(window_height) +
                      '+'+window_pos_x+'+'+window_pos_y)

        self.frame = Frame(self)
        self.frame.pack()

        for self.child in self.frame.winfo_children():
            self.child.grid_configure(padx=20, pady=20)

        self.bind('<Return>', self.frame.convert)


class Frame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container)
        self.container = container
        self.meter_value = tk.StringVar()
        self.feet_value = tk.StringVar()
        self.feet_value.set('Will appear here!')

        self.label_meter = ttk.Label(
            self,
            text="Meter here:",
            relief='flat'
        )
        self.label_meter.grid(row=0, column=0, sticky='EW')

        self.entry = ttk.Entry(
            self,
            textvariable=self.meter_value
        )
        self.entry.focus()
        self.entry.grid(row=0, column=1, sticky='EW')

        self.label_feet = ttk.Label(
            self,
            text='Feet here:',
        )
        self.label_feet.grid(row=1, column=0, sticky='EW')

        self.button = ttk.Button(
            self,
            text='Convert',
            command=self.convert
        )
        self.button.grid(row=2, column=1, sticky='EW')

        self.label_feet_display = ttk.Label(
            self,
            textvariable=self.feet_value
        )
        self.label_feet_display.grid(row=1, column=1, sticky='EW')

    def convert(self, *args):
        try:
            meters = float(self.meter_value.get())
            feet = meters * 3.28084
            self.feet_value.set(round(feet, 2))
        except ValueError:
            self.feet_value.set('Invalid Value')


root = MainScreen()
root.columnconfigure(0, weight=1)
root.mainloop()
