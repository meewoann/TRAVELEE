from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator #pip install googletrans==3.1.0a0
from tkinter import messagebox
import speech_recognition as sr
import subprocess
import sys
from tkinter import Text, RIDGE
import pyttsx3
import os 
from gtts import gTTS  
import pygame
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\OneDrive\Desktop\tkinter\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = tk.Tk()
root.title('Language Translation')
root.geometry('375x667')

root.attributes('-topmost', True)
canvas = Canvas(
    root,
    bg = "#F1BACF",
    height = 667,
    width = 380,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("tr1.png"))
image_1 = canvas.create_image(
    190.0,
    333.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("tr2.png"))
image_2 = canvas.create_image(
    190.0,
    80.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("tr3.png"))
image_3 = canvas.create_image(
    190.0,
    306.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("tr3.png"))
image_4 = canvas.create_image(
    190.0,
    530.0,
    image=image_image_4
)

trans_image_1 = PhotoImage(
    file=relative_to_assets("bn1.png"))
trans_1 = Button(
    image=trans_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg='#F3DDE7',
    command=lambda: translate(),
    relief="flat"
)
trans_1.place(
    x=160.0,
    y=387.0,
    width=50.0,
    height=44.0
)

def translate():
    lang_1 = entry1.get('1.0', 'end-1c')
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        entry2.insert('end', output.text)


def clear():
    delete_audio_files()
    entry1.delete(1.0, 'end')
    entry2.delete(1.0, 'end')

c = tk.StringVar()




auto_select = ttk.Combobox(canvas, width=10, textvariable= c, state='radomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto Select',
                        )

auto_select.place(x=130, y=210)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(canvas, width=10, textvariable=l, state='randomly', font=('verdana', 10, 'bold'))

choose_language['values'] = (
                        'Afrikaans', 
                        'Albanian', 
                        'Amharic',
                        'Arabic',
                        'Armenian',
                        'Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                        'Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese (simplified)',
                        'Chinese (traditional)',
                        'Corsican',
                        'Croatian',
                        'Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi', 
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'korean',
                        'Kurdish (kurmanji)',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Mltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Myanmar (burmese)',
                        'Nepali',
                        'Norwegian',
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa',
                        'Yiddish',
                        'Yoruba',
                        'Zulu'
                           )

choose_language.place(x=130, y=435)
choose_language.current(0)

entry1 = Text(canvas,
         width=20,
         height=4,
         relief=RIDGE,
         font=('verdana',15),
         borderwidth=0,
         highlightthickness=0,
         bg = '#F7EAF8')
entry1.place(x=60, y=250)

entry2 = Text(canvas,
         width=20,
         height=4,
         borderwidth=0,
         highlightthickness=0,
         relief=RIDGE,
         bg='#F7EAF8',
         font=('verdana',15))
entry2.place(x=60, y=480)


bt2 = Button(canvas,
             command=clear,
             text='   Clear   ',
             relief=RAISED,
             borderwidth=2,
             font=('vardana', 10, 'bold'),
             bg='#248aa2',
             fg='white')
bt2.place(x=70, y=610)

bt3 = Button(canvas,
             command=lambda: run_menu(),
             text='   Back   ',
             relief=RAISED,
             borderwidth=2,
             font=('vardana', 10, 'bold'),
             bg='#248aa2',
             fg='white')
bt3.place(x=220, y=610)

def record_and_translate1():
    # Khởi tạo recognizer
    recognizer = sr.Recognizer()

    # Khởi tạo translator
    translator = Translator()

    # Ghi âm từ microphone
    with sr.Microphone() as source:

        audio = recognizer.listen(source)

    try:
        # Nhận dạng giọng nói thành văn bản
        text = recognizer.recognize_google(audio, language='auto')

        # Hiển thị văn bản dịch trong entry1
        entry1.delete('1.0', tk.END)
        entry1.insert(tk.END,text)

    except sr.UnknownValueError:
        print("Không nhận diện được giọng nói")
    except sr.RequestError as e:
        print("Lỗi trong quá trình kết nối với API: {0}".format(e))

def convert_to_speech1():
    text = entry1.get("1.0",'end-1c')  # Lấy văn bản từ entry1
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def convert_to_speech2():
    text = entry2.get("1.0",'end-1c')  # Lấy văn bản từ entry1
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def convert_to_speech3():
    text = entry2.get("1.0", 'end-1c')  # Lấy văn bản từ entry1
    language = "vi"  # Ngôn ngữ của văn bản (ví dụ: tiếng Việt)
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

def delete_audio_files():
    # Xóa các file âm thanh nếu tồn tại
    for filename in ["output.mp3"]:
        if os.path.exists(filename):
            os.remove(filename)
            os.remove('output.mp3')

button_image_2 = PhotoImage(
    file=relative_to_assets("bn3.png"))

bt4 = Button(canvas,
            command=lambda:record_and_translate1(),
            text=' Voice ',
            borderwidth=0,
            highlightthickness=0,
            bg='#F7EAF8',
            image=button_image_2)
bt4.place(x=70, y=330)

button_image_3 = PhotoImage(
    file=relative_to_assets("bn2.png"))
bt5 = Button(canvas,
             command=lambda: convert_to_speech1(),
             bg='#F7EAF8',
            borderwidth=0,
            highlightthickness=0,
            image= button_image_3,)
bt5.place(x=280, y=340)

bt6 = Button(canvas,
             command=lambda: convert_to_speech3(),
             bg='#F7EAF8',
            borderwidth=0,
            highlightthickness=0,
            image=button_image_3,
            relief="flat")
bt6.place(x=280, y=570)

def run_menu():
    root.destroy() 
    root.after(1000,subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\gui_menu.py']))

# def update_choose_language(*args):
#     chosen_language = l.get()
#     print("Selected Language:", chosen_language)  
#     if chosen_language == 'Vietnamese':
#         c = 'vi'
#         return c


# updated_language = l.trace('w', update_choose_language)
# print(update_choose_language)

root.resizable(False, False)
root.mainloop()