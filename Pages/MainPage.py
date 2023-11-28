from tkinter import Button, Frame, Text, END, Label
import tkinter as tk
from Modules.fileManage import chooseFolder, createFile


class MainPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        padding = 3
        frame = Frame(self)

        mainText = Label(frame, text="Generate an empty .docx file With your\n first and last Name as the file name.")
        mainText.config(font=("Arial", 12))

        l = Label(frame, text="Enter Name:")
        l.config(font=("Courier", 10))

        T = Text(frame, height=1, width=25)
        T.insert(END, "First Name")
        self.fname = T

        l2 = Label(frame, text="Last Name")
        l2.config(font=("Courier", 10))

        T2 = Text(frame, height=1, width=25)
        T2.insert(END, "Last Name")
        self.lname = T2

        self.gen_file_button = Button(
            frame, text="Generate File", command=self.gen_file
        )

        self.label = Label(frame, text="Directory path for resumes:")

        self.path = Label(frame, text="No path selected", bg="white")

        self.choose_path_button = Button(
            frame, text="Choose Path", command=self.choose_path
        )

        frame.pack(padx=padding, pady=padding)
        mainText.pack(padx=padding, pady=padding)
        l.pack(padx=padding, pady=padding)
        self.fname.pack(padx=padding, pady=padding)
        self.lname.pack(padx=padding, pady=padding)

        self.label.pack(padx=padding, pady=padding)
        self.path.pack(padx=padding, pady=padding)
        self.choose_path_button.pack(padx=padding, pady=padding)
        self.gen_file_button.pack(padx=padding, pady=padding)

    def choose_path(self):
        print("choose folder")
        self.path.config(text=chooseFolder())

    def gen_file(self):
        fname = self.fname.get("1.0", "end-1c")
        lname = self.lname.get("1.0", "end-1c")
        createFile(fname, lname)
