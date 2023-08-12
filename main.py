from tkinter import (
    BOTTOM,
    Frame,
    Button
)
from tkinter.ttk import Notebook
import tkinter as tk

from Pages.JobPosting import JobPosting
from Pages.MainPage import MainPage
from Pages.ResumePage import ResumePage

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        padding = 3
        self.title("CV Helper")

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight()  # Height of the screen
        width = 700  # Width
        height = 600  # Height
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.geometry("%dx%d+%d+%d" % (width, height, x, y-40))

        self.tabmanager = Notebook(self)
        self.tabmanager.pack(expand=1, fill="both")
        self.tabmanager.grid_propagate(False)
        self.tabmanager.grid_rowconfigure(0, weight=1)
        self.tabmanager.grid_columnconfigure(0, weight=1)
        
        frame = MainPage(self.tabmanager, self)
        frame2 = JobPosting(self.tabmanager, self)
        frame3 = ResumePage(self.tabmanager, self)
        
        self.tabmanager.add(frame, text="Main")
        self.tabmanager.add(frame2, text="Job Posting Analysis")
        self.tabmanager.add(frame3, text="Resume-Job Posting")

        footer_frame = Frame(self.tabmanager)
        footer_frame.pack(side=BOTTOM)
        self.close_button = Button(footer_frame, text="Close", command=self.quit)
        self.close_button.pack(padx=padding, pady=padding + 10, side=BOTTOM)

    

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()