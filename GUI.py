from transfer.server import main

import customtkinter
import sys

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('1024x720')


def test():
    print(f'Hosting at test')


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both')
termf = customtkinter.CTkFrame(master=root)
termf.pack(pady=20,padx=60, fill='both')
textbot = customtkinter.CTkTextbox(master=root)
textbot.pack(pady=20, padx=60, fill='both')


def redirector(input_string):
    textbot.insert(customtkinter.INSERT, text=input_string)
    textbot.update_idletasks()


label = customtkinter.CTkLabel(
    master=frame,
    text='Test',
)
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(
    master=frame,
    text='Testilovo',
    command=main,
)
button.pack(pady=12, padx=10)
button = customtkinter.CTkButton(
    master=frame,
    text='print',
    command=test,
)
button.pack(pady=12, padx=10)

sys.stdout.write = redirector

root.mainloop()
