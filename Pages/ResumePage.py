from tkinter import LEFT, Button, Frame, Text, END, Label, filedialog
import tkinter as tk
from Modules.readJobPosting import preprocess_posting_text
from Modules.pdfReader import readPdf
from Modules.data import getData
import sys
from os.path import abspath as abspath


class ResumePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        padding = 3
        self.frame = Frame(self)
        # self['bg'] = "white"
        self.frame.pack(padx=padding, pady=padding)
        self.file_path = ""

        self.frame_upper = Frame(self.frame)
        self.frame_upper.pack(padx=padding, pady=padding)

        self.frame_pdf = Frame(self.frame_upper)
        # self.frame_pdf['bg'] = "white"
        self.frame_pdf.pack(padx=padding, pady=padding)
        self.label = Label(self.frame_pdf, text="Choose Resume file (PDF):")
        self.label.config(font=("Arial", 11))

        self.label.pack(padx=padding, pady=padding)
        self.path = Label(self.frame_pdf, text="No file selected", bg="white")
        self.path.pack(padx=padding, pady=padding)

        self.frame_buttons = Frame(self.frame_pdf)
        # self.frame_buttons['bg'] = "white"
        self.choose_path_button = Button(
            self.frame_buttons, text="Choose File", command=self.choose_path
        )
        self.read_pdf_button = Button(
            self.frame_buttons, text="Read File", command=self.ATS_Check
        )

        self.choose_path_button.pack(padx=padding, pady=padding, side=LEFT)
        self.read_pdf_button.pack(padx=padding, pady=padding, side=LEFT)
        self.frame_buttons.pack(padx=padding, pady=padding)

        self.job_input = Frame(self.frame_upper)
        self.job_input.pack(padx=padding, pady=padding)
        self.main_label = Label(self.job_input, text="Enter job posting text here:")
        self.main_label.config(font=("Arial", 11))

        self.text_input = Text(
            self.job_input, height=8, width=30, undo=True, wrap="word"
        )
        self.text_input.insert(END, "Enter job posting text")
        self.text_input.config(font=("arial", 10), undo=True, wrap="word")
        self.main_label.pack(padx=padding, pady=padding)
        self.text_input.pack(padx=padding, pady=padding)

        self.frame_output = Frame(self.frame)
        self.frame_output.pack(padx=padding, pady=padding)

        self.output_label = Label(
            self.frame, text="Skills identified\n(Missing skills marked with 'X'):"
        )
        self.output_label.config(font=("Arial", 11))
        self.output_label.pack(padx=padding, pady=padding)

        self.text_output = Text(self.frame, height=9, width=30)
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
        """Location of relative paths"""
        if getattr(sys, "frozen", False):
            path = sys._MEIPASS  # pylint: disable=no-member
        else:
            path = "."

        return path

    def ATS_Check(self):
        if self.file_path == "":
            return
        self.text_output.delete("1.0", "end")

        pdf_text = readPdf(self.path.cget("text"))
        # print(pdf_text)

        skills_in_pdf = self.check_skills(pdf_text)
        skills_in_posting = self.check_skills(
            preprocess_posting_text(self.text_input.get("1.0", "end-1c"))
        )
        for t in skills_in_posting:
            if t in skills_in_pdf:
                self.text_output.insert(END, t + "\n")
            else:
                self.text_output.insert(END, t + " (X)" + "\n")

    def check_skills(self, text):
        data = getData()
        word_data = [word.lower() for word in data]
        listOfSkills = []
        n = len(word_data)

        for i in range(n):
            if word_data[i] in text:
                listOfSkills.append(data[i])

        return listOfSkills
