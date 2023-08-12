from tkinter import LEFT, Button, Frame, Scrollbar, Text, END
import tkinter as tk
from Modules.readJobPosting import preprocess_text
from Modules.topicModelling import return_topics

class JobPosting(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        padding = 3
        self.frame2 = Frame(self)
        

        T3 = Text(self.frame2, height=13, width=60, undo=True, wrap='word')
        T3.insert(END, "Enter job posting text")
        self.text_input = T3

        self.frame_buttons = Frame(self.frame2)

        self.display_topics_button = Button(
            self.frame_buttons, text="Generate Topics", command=self.process_posting
        )
        self.process_text_button = Button(
            self.frame_buttons, text="Preprocess Text", command=self.process_text
        )
        
        # self.choose_pdf_button = Button(
        #     self.frame_buttons, text="Choose PDF", command=self.pdf_action
        # )

        self.frame_output = Frame(self.frame2)
        self.text_output = Text(
            self.frame_output, height=12, width=60
        )
        self.text_output.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scroll_bar = Scrollbar(self.frame_output, command=self.text_output.yview)
        self.text_output['yscrollcommand'] = scroll_bar.set
        self.text_output.config(font=("consolas", 12), undo=True, wrap='word')
        scroll_bar.grid(row=0, column=1, sticky='nsew')

        self.frame2.pack(padx=padding, pady=padding)
        self.text_input.pack(padx=padding, pady=padding)
        self.frame_buttons.pack(padx=padding, pady=padding)
        self.display_topics_button.pack(padx=padding, pady=padding, side=LEFT)
        self.process_text_button.pack(padx=padding, pady=padding, side=LEFT)
        # self.text_output.pack(side=LEFT)
        # scroll_bar.pack(side=LEFT)
        
        self.frame_output.pack(padx=padding, pady=padding)
        
 
    def process_posting(self):
        self.text_output.delete("1.0","end")
        self.text_output.insert(
            END, return_topics(self.text_input.get("1.0", "end-1c"))
        )

    def process_text(self):
        self.text_output.delete("1.0","end")
        self.text_output.insert(
            END, preprocess_text(self.text_input.get("1.0", "end-1c"))
        )