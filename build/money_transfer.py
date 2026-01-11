from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import requests
import subprocess
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\OneDrive\Desktop\tkinter\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def convert_currencies():
    from_currency = choose_current.get()
    to_currency = choose_current1.get()
    amount = float(entry1.get("1.0", "end-1c"))
    original_amount = amount / exchange_rates[from_currency]
    converted_amount = original_amount * exchange_rates[to_currency]
    entry2.delete("1.0", "end")
    entry2.insert("end", f"{converted_amount}")

def clear():
    entry1.delete(1.0, 'end')
    entry2.delete(1.0, 'end')

api_key = "fecec220f73b4d8ca9fc1079b503f100"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
response = requests.get(url)
data = response.json()
exchange_rates = data["rates"]

window = Tk()

window.geometry("380x667")
window.configure(bg = "#DD5E8E")


canvas = Canvas(
    window,
    bg = "#DD5E8E",
    height = 667,
    width = 380,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("mn1.png"))
image_1 = canvas.create_image(
    190.0,
    333.0,
    image=image_image_1
)

choose_current = ttk.Combobox(window,
                              width=10,
                              state='randomly',
                              font=('verdana', 15, 'bold'),
                              foreground='pink')
choose_current['values'] = ('USD', 'VND', 'ALL',
                            'AMD', 'ANG', 'AOA',
                            'ARS', 'AUD', 'AWG',
                            'AZN', 'BAM', 'BBD',
                            'BDT', 'BGN', 'BHD',
                            'BIF', 'BMD', 'BND',
                            'BOB', 'BRL', 'BSD',
                            'BTC', 'BTN', 'BWP',
                            'BYN', 'BZD', 'CAD',
                            'CDF', 'CHF', 'CLF',
                            'CLP', 'CNH', 'CNY',
                            'COP', 'CRC', 'CUC',
                            'CUP', 'CVE', 'CZK',
                            'DJF', 'DKK', 'DOP',
                            'DZD', 'EGP','THB',
                            'INR','EUR','TWD')
choose_current.place(x=120, y=190)
choose_current.current(0)

choose_current1 = ttk.Combobox(window,
                              width=10,
                              state='randomly',
                              font=('verdana', 15, 'bold'),
                              foreground='pink')
choose_current1['values'] = ('USD', 'VND', 'ALL',
                             'AMD', 'ANG', 'AOA',
                             'ARS', 'AUD', 'AWG',
                             'AZN', 'BAM', 'BBD', 'BDT',
                             'BGN', 'BHD', 'BIF', 'BMD',
                             'BND', 'BOB', 'BRL', 'BSD',
                             'BTC', 'BTN', 'BWP', 'BYN',
                             'BZD', 'CAD', 'CDF', 'CHF',
                             'CLF', 'CLP', 'CNH', 'CNY',
                             'COP', 'CRC', 'CUC', 'CUP',
                             'CVE', 'CZK', 'DJF', 'DKK',
                             'DOP', 'DZD', 'EGP','THB',
                             'INR','EUR','TWD')
choose_current1.place(x=120, y=440)
choose_current1.current(0)

entry1 = Text(window,
        width=20,
        height=3,
        borderwidth=0,
        highlightthickness=0,
        bg='#FFF4F4',
        font=('verdana',15))
entry1.place(x=67, y=230)

entry2 = Text(window,
        width=20,
        height=3,
        borderwidth=0,
        highlightthickness=0,
        bg='#FFF4F4',
        font=('verdana',15))
entry2.place(x=60, y=490)

image_image_2 = PhotoImage(
    file=relative_to_assets("mn2.png"))
image_2 = canvas.create_image(
    213.0,
    280.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("mn3.png"))
image_3 = canvas.create_image(
    202.0,
    531.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("mn4.png"))
image_4 = canvas.create_image(
    194.0,
    102.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("bn1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg='#FFFFFF',
    command=lambda: convert_currencies(),
    relief="flat"
)
button_1.place(
    x=170.0,
    y=380.0,
    width=50.0,
    height=44.0
)

bt2 = Button(window,
             command=lambda: run_menu(),
             text='   Back   ',
             borderwidth=2,
             font=('vardana', 10, 'bold'),
             bg='#248aa2',
             fg='white')
bt2.place(x=80, y=600)

bt3 = Button(window,
             command=lambda: clear(),
             text='   Clear   ',
             borderwidth=2,
             font=('vardana', 10, 'bold'),
             bg='#248aa2',
             fg='white')
bt3.place(x=240, y=600)

def run_menu():
    window.destroy() 
    window.after(1000,subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\gui_menu.py']))

window.resizable(False, False)
window.mainloop()
