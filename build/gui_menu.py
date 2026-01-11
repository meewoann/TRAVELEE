
from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\OneDrive\Desktop\tkinter\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('menu')
window.geometry("375x667")
window.configure(bg = "#9C677B")

HEIGHT = 667
WIDTH = 375


canvas = Canvas(
    window,
    bg = "#9C677B",
    height = HEIGHT,
    width = WIDTH,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("menu1.png"))
image_1 = canvas.create_image(
    190.0,
    308.0,
    image=image_image_1
)


image_image_0 = PhotoImage(
    file=relative_to_assets("m1.png"))
image_0 = canvas.create_image(
    190.0,
    350.0,
    image=image_image_0
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scale_img3(5.0,reg),
    bg='#F3DDE7',
    relief="flat"
)
button_1.place(
    x=198.0,
    y=263.0,
    width=100.0,
    height=95.34883880615234
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scale_img1(5.0,reg) ,
    bg='#F3DDE7',
    relief="flat"
)
button_2.place(
    x=70.0,
    y=261.0,
    width=100.0,
    height=96.70329284667969
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg='#F3DDE7',
    relief="flat",
    command=lambda: scale_img4(5.0,reg)
)
button_3.place(
    x=198.0,
    y=370.0,
    width=100.0,
    height=97.61902618408203
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scale_img(5.0,reg),
    bg='#F3DDE7',
    relief="flat"
)
button_4.place(
    x=70.0,
    y=372.0,
    width=100.0,
    height=93.54838562011719
)

button_image_5 = PhotoImage(
    file=relative_to_assets("icon.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=140.0,
    y=50.0,
    width=100.0,
    height=93.54838562011719
)
#
m_image_2 = PhotoImage(
    file=relative_to_assets("m2.png"))
m2 = canvas.create_image(
    190.0,
    1090.0,
    image=m_image_2
)

b_image_1 = PhotoImage(
    file=relative_to_assets("b.png"))
b_1 = Button(
    image=b_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: move_canvas_up(700, m2),
    bg='#FFFFFF',
    relief="flat"
)
b_1.place(
    x=139.0,
    y=595.0,
    width=102.0,
    height=57.0
)
#
image_image_4 = PhotoImage(
    file=relative_to_assets("menu3.png"))
image_4 = canvas.create_image(
    187.0,
    94.0,
    image=image_image_4
)

def delete_button():
    button_1.pack()
    button_2.pack()
    button_3.pack()
    button_4.pack()
    button_5.pack()
    b_1.pack()
    button_1.pack_forget()
    button_2.pack_forget()
    button_3.pack_forget()
    button_4.pack_forget()
    button_5.pack_forget()
    b_1.pack_forget()


scale_factor = 1
scale_counter = 1.0
def scale_img(scale_rate, item):
    delete_button()
    global scale_counter
    if scale_counter < scale_rate:  
        coords = canvas.coords(item)
        x0, y0, x1, y1 = coords
        center_x = (x0 + x1) / 2
        center_y = (y0 + y1) / 2
        canvas.scale(item, center_x, center_y, scale_rate, scale_rate)
        scale_counter += 0.5
        window.after(100, scale_img, scale_rate, item)
        window.after(2000, lambda: run_menu_client())

def scale_img1(scale_rate, item):
    delete_button()
    global scale_counter
    if scale_counter < scale_rate:  
        coords = canvas.coords(item)
        x0, y0, x1, y1 = coords
        center_x = (x0 + x1) / 2
        center_y = (y0 + y1) / 2
        canvas.scale(item, center_x, center_y, scale_rate, scale_rate)
        scale_counter += 0.5
        window.after(100, scale_img1, scale_rate, item)
        window.after(2000, lambda: run_menu_translate())

def scale_img3(scale_rate, item):
    delete_button()
    global scale_counter
    if scale_counter < scale_rate:  
        coords = canvas.coords(item)
        x0, y0, x1, y1 = coords
        center_x = (x0 + x1) / 2
        center_y = (y0 + y1) / 2
        canvas.scale(item, center_x, center_y, scale_rate, scale_rate)
        scale_counter += 0.5
        window.after(100, scale_img1, scale_rate, item)
        window.after(1000, lambda: run_menu_money_transfer())

def scale_img4(scale_rate, item):
    delete_button()
    global scale_counter
    if scale_counter < scale_rate:  
        coords = canvas.coords(item)
        x0, y0, x1, y1 = coords
        center_x = (x0 + x1) / 2
        center_y = (y0 + y1) / 2
        canvas.scale(item, center_x, center_y, scale_rate, scale_rate)
        scale_counter += 0.5
        window.after(100, scale_img1, scale_rate, item)
        window.after(1000, lambda: run_menu_GPS())

move_counter = 0
def move_canvas_up(high, object):
    delete_button()
    global move_counter
    if move_counter < high:  
        canvas.move(object, 0, -10)  
        move_counter += 10
        window.after(10, move_canvas_up, high, object)
        window.after(1000, lambda: run_menu_cam())

reg = canvas.create_rectangle(WIDTH//2, HEIGHT//2, WIDTH//2+1, HEIGHT//2+1, fill='pink', outline='pink')

def run_menu_client():
    window.destroy() # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\client1.py']) 

def run_menu_translate():
    window.destroy() # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\app_translate.py']) 

def run_menu_money_transfer():
    window.destroy() # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\money_transfer.py']) 

def run_menu_GPS():
    window.destroy() # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\GPS.py']) 

def run_menu_cam():
    window.destroy() # Tắt cửa sổ intro
    subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\camera_gui.py']) 

window.resizable(False, False)
window.mainloop()
