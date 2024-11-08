import tkinter as tk
import tkinter.font as tkFont
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
from gtts import gTTS
import os
import numpy as np



def on_submit():
    print(1)

def close_window():
    Top_screen.destroy()


Top_screen = tk.Tk()
Top_screen.configure(bg="#84869B")
Top_screen.attributes("-fullscreen", True)
Top_screen.resizable(False, False)

Top_font = tkFont.Font(family="Symbol", size=50, weight="bold")
Promt_font = tkFont.Font(family="Symbol", size=12, weight="bold")
Button_font = tkFont.Font(family="Symbol", size=14, weight="bold")

lable = tk.Label(Top_screen, text="Тут може бути ваша реклама", bg="#84869B", fg="#003856", font=Top_font)
lable.place(relx=0.5, rely=0.1, anchor="center")

start_tr_button = tk.Button(Top_screen, width=25, height=2, text="надіслати", bg="#D7CFA1", fg="#003856",
                             font=Button_font, padx=8, pady=4, borderwidth=10, relief="flat", command=on_submit)
start_tr_button.place(relx=0.5, rely=0.6, anchor="center")

Close_button = tk.Button(Top_screen, width=4, height=2, text="х", bg="#D7CFA1", fg="#003856",
                         font=Button_font, relief="flat", padx=2, pady=1, borderwidth=2, command=close_window)
Close_button.place(relx=0.98, rely=0.03, anchor="center")

Top_screen.mainloop()
