from tkinter import ttk
import tkinter as tk
from input_module import InputModule
from drawing_module import DrawingModule

root = tk.Tk()
input_module = InputModule(root)
drawing_module = DrawingModule(input_module)

animate_button = ttk.Button(root, text="Запустить анимацию", command=drawing_module.show_animation)
animate_button.pack()

root.mainloop()
