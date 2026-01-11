
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import subprocess
import sys


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\OneDrive\Desktop\tkinter\build\assets\frame0")

WIDTH = 375
HEIGHT = 667

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("375x667")
window.configure(bg = "#DD49F6")
window.title('intro')

canvas = Canvas(
    window,
    bg = "#DD49F6",
    height = HEIGHT,
    width = WIDTH,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    185.0,
    900.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    185.0,
    379.0+550,
    image=image_image_2
)


icon1 = PhotoImage(
    file=relative_to_assets("icon.png"))
icon = canvas.create_image(
    WIDTH//2,
    HEIGHT//2 -300 ,
    image=icon1
)
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    185.0,
    408.0+600,
    image=image_image_3
)
image_image_4 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_4 = canvas.create_image(
    185.0,
    408.0+600,
    image=image_image_4
)
move_counter = 0
scale_counter = 0
def move_canvas_up(high, object):
    global move_counter
    if move_counter < high:  
        canvas.move(object, 0, -10)  
        move_counter += 10
        window.after(10, move_canvas_up, high, object)


def move_canvas_down(high,object):
    global move_counter
    if move_counter < high:  
        canvas.move(object, 0, +10)  
        move_counter += 10
        window.after(50, move_canvas_down, high,object)

def scale_canvas(high, object):
    global scale_counter
    if scale_counter < high:  
        canvas.scale(object, WIDTH//2, HEIGHT//2,WIDTH//2+100 , HEIGHT//2+100)  
        scale_counter += 1
        window.after(10, scale_canvas, high, object)

def cd():
    move_canvas_up(2500, image_4)
    window.after(2000, run_menu)

def run_menu():
    window.destroy()  # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\gui_menu.py']) 




move_canvas_up(1550, image_1)
move_canvas_up(1500, image_2)
move_canvas_up(1500, image_3)
move_canvas_down(1400, icon)

window.bind("<Button-1>", lambda event: cd())


window.resizable(False, False)
window.mainloop()

    