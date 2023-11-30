import os
import sys
from tkinter import BOTTOM, Frame, Button
from tkinter.ttk import Notebook
import tkinter as tk

import base64
from io import BytesIO
from PIL import Image, ImageTk

#from Pages.JobPosting import JobPosting
#from Pages.MainPage import MainPage
from Pages.ResumePage import ResumePage

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        padding = 3
        self.title("Resume Helper")
        
        icon_path = resource_path(".\RH.ico")  # Change this to the actual path of your icon file 
        self.iconbitmap(icon_path)
  
        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight()  # Height of the screen
        width = 400  # Width
        height = 600  # Height
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.geometry("%dx%d+%d+%d" % (width, height, x, y - 40))
        self.minsize(width, height)
        
        self.tabmanager = Notebook(self)
        self.tabmanager.pack(expand=1, fill="both")
        self.tabmanager.grid_propagate(False)
        self.tabmanager.grid_rowconfigure(0, weight=1)
        self.tabmanager.grid_columnconfigure(0, weight=1)

        #frame = MainPage(self.tabmanager, self)
        #frame2 = JobPosting(self.tabmanager, self)
        frame3 = ResumePage(self.tabmanager, self)

        #self.tabmanager.add(frame, text="Main")
        self.tabmanager.add(frame3, text="Analyze Resume")
        #self.tabmanager.add(frame2, text="Analyze Job Posting")

        footer_frame = Frame(self.tabmanager)
        footer_frame.pack(side=BOTTOM)
        self.close_button = Button(footer_frame, text="Close", command=self.quit)
        self.close_button.pack(padx=padding, pady=padding + 10, side=BOTTOM)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
