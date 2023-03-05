from transfer.client import main_client

import customtkinter as ctk
import sys

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class GUI(ctk.CTkFrame):
    def __init__(self, master):
        self.root = super().__init__(master)
        sys.stdout.write = self.redirector
        self.client_frame = self.create_client_frame()
        self.client_label = self.create_client_label()
        self.upload_button = self.create_start_upload_button()
        self.stop_button = self.create_stop_button()
        self.textbox = self.create_textbox()

    def create_client_frame(self):
        frame = ctk.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both")
        return frame

    def create_client_label(self):
        label = ctk.CTkLabel(
            master=self.client_frame, text="Client", font=("Roboto", 24)
        )
        label.pack(pady=20, padx=60)
        return label

    def create_textbox(self):
        textbox = ctk.CTkTextbox(
            master=self.root,
            font=("Roboto", 20),
        )
        textbox.pack(pady=20, padx=60, fill="both")
        return textbox

    def create_stop_button(self):
        button = ctk.CTkButton(
            master=self.root,
            text="Close program",
            command=quit,
            font=("Roboto", 20),
        )
        button.pack(pady=12, padx=10)
        return button

    def create_start_upload_button(self):
        button = ctk.CTkButton(
            master=self.client_frame,
            text="Start upload",
            command=lambda: main_client(choose_file()),
            font=("Roboto", 20),
        )
        button.pack(pady=12, padx=10)
        return button

    def redirector(self, input_string):
        self.textbox.insert(ctk.INSERT, text=input_string)
        self.textbox.update_idletasks()


def initialize_root():
    root = ctk.CTk()
    root.title("Digital Library")
    root.geometry("1024x720")
    return root


def choose_file():
    filename = ctk.filedialog.askopenfilename(
        initialdir="~",
        filetypes=(("all files", "*.*"),),
    )
    return filename


if __name__ == "__main__":
    app = GUI(initialize_root())
    app.mainloop()
