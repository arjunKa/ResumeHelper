from tkinter import LEFT, Button, Frame, Text, END, Label, filedialog
import tkinter as tk
from Modules.readJobPosting import preprocess_text
from Modules.pdfReader import readPdf

import json
import sys
import os


class ResumePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        padding = 3
        self.frame = Frame(self)
        self.frame.pack(padx=padding, pady=padding)
        self.file_path = ""
        
        self.frame_upper = Frame(self.frame)
        self.frame_upper.pack(padx=padding, pady=padding)
        
        self.frame_pdf = Frame(self.frame_upper)
        self.frame_pdf.pack(padx=padding, pady=padding, side=LEFT)
        self.label = Label(self.frame_pdf, text="Resume file (PDF):")
        self.label.pack(padx=padding, pady=padding)
        self.path = Label(self.frame_pdf, text="No file selected", bg="white")
        self.path.pack(padx=padding, pady=padding)
        
        self.frame_buttons = Frame(self.frame_pdf)
        self.choose_path_button = Button(
            self.frame_buttons, text="Choose Path", command=self.choose_path
        )
        self.read_pdf_button = Button(
            self.frame_buttons, text="Read PDF", command=self.read_file
        )
        self.read_pdf_button.pack(padx=padding, pady=padding, side=LEFT)
        self.choose_path_button.pack(padx=padding, pady=padding, side=LEFT)
        self.frame_buttons.pack(padx=padding, pady=padding)
        

        self.job_input = Frame(self.frame_upper)
        self.job_input.pack(padx=padding, pady=padding, side=LEFT)
        self.main_label = Label(self.job_input, text="Enter job posting text here:")
        self.text_input = Text(self.job_input, height=7, width=30, undo=True, wrap="word")
        self.text_input.insert(END, "Enter job posting text")
        self.text_input.config(font=("arial", 10), undo=True, wrap="word")
        self.main_label.pack(padx=padding, pady=padding)
        self.text_input.pack(padx=padding, pady=padding)
        


        

        self.frame_output = Frame(self.frame)
        self.frame_output.pack(padx=padding, pady=padding)
        
        self.output_label = Label(self.frame, text="Skills/Topics:")
        self.output_label.pack(padx=padding, pady=padding)

        self.text_output = Text(self.frame, height=7, width=30)
        self.text_output.pack(padx=padding, pady=padding)
        self.text_output.config(font=("arial", 10), undo=True, wrap="word")

    

        

    def choose_path(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            print("Selected PDF file path:", file_path)
        else:
            print("No PDF file selected.")
            self.file_path == ""
            self.path.config(text="No file selected")
            return
        self.path.config(text=file_path)
        self.file_path = file_path
        return file_path

    def get_packaged_files_path(self):
        """Location of relative paths """
        if getattr(sys, 'frozen', False):
            path = sys._MEIPASS  # pylint: disable=no-member
        else:
            path = '.'

        return path

    def get_posting_skills(self):
        out = []

        filepath = self.get_packaged_files_path()
        filename = os.path.join(filepath, 'languages.json')
        with open(filename, "r") as file:
            data = json.load(file)
        posting_words = preprocess_text(self.text_input.get("1.0", "end-1c")).split()
        data = [word.lower() for word in data]
        for word in data:
            if word in posting_words and word not in out:
                out.append(word)
        return out

    def read_file(self):
        if self.file_path == "":
            return
        self.text_output.delete("1.0", "end")
        print(self.path.cget("text"))
        text = preprocess_text(readPdf(self.path.cget("text")))
        text2 = self.check_skills(text)
        for t in text2:
            self.text_output.insert(END, t + "\n")

    def check_skills(self, text):
        out = []
        data = self.get_posting_skills()
        words = text.split()
        for word in data:
            if word in words:
                out.append(word)
            else:
                out.append(word + " X")

        return out
