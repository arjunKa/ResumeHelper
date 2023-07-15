from tkinter import (
    BOTTOM,
    END,
    LEFT,
    Frame,
    Tk,
    Label,
    Button,
    Text,
    Scrollbar,
    RIGHT,
)
from tkinter.ttk import Notebook

from fileManage import chooseFolder, createFile
from readJobPosting import preprocess_text
from topicModelling import return_topics


class mainGUI:
    def __init__(self, master):
        padding = 3
        self.master = master
        self.master.title("CV Automation")

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen
        width = 650  # Width
        height = 500  # Height
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.tabmanager = Notebook(root)
        self.MainPage()
        self.Page2()

        footer_frame = Frame(self.tabmanager)
        footer_frame.pack(side=BOTTOM)
        self.close_button = Button(footer_frame, text="Close", command=self.master.quit)
        self.close_button.pack(padx=padding, pady=padding + 10, side=BOTTOM)

    def MainPage(self):
        padding = 3
        frame = Frame(self.tabmanager)
        self.tabmanager.pack(expand=1, fill="both")
        self.tabmanager.add(frame, text="Main")

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

        l3 = Label(frame, text="No path selected", bg="white")
        self.path = l3

        self.choose_path_button = Button(
            frame, text="Choose Path", command=self.choose_path
        )

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

    def Page2(self):
        padding = 3
        self.frame2 = Frame(self.master)
        self.tabmanager.add(self.frame2, text="Job Posting Analysis")

        T3 = Text(self.frame2, height=13, width=60)
        T3.insert(END, "Enter job posting text")
        self.text_input = T3

        self.frame_buttons = Frame(self.frame2)

        self.display_topics_button = Button(
            self.frame_buttons, text="Generate Topics", command=self.process_posting
        )
        self.process_text_button = Button(
            self.frame_buttons, text="Preprocess Text", command=self.process_text
        )

        self.frame_output = Frame(self.frame2)

        scroll_bar = Scrollbar(self.frame_output)

        self.text_output = Text(
            self.frame_output, height=20, width=70, yscrollcommand=scroll_bar.set
        )

        self.text_input.pack(padx=padding, pady=padding)
        self.frame_buttons.pack(padx=padding, pady=padding)
        self.display_topics_button.pack(padx=padding, pady=padding, side=LEFT)
        self.process_text_button.pack(padx=padding, pady=padding, side=LEFT)
        self.text_output.pack(side=LEFT)
        scroll_bar.pack(side=RIGHT)
        scroll_bar.config(command=self.text_output.yview)
        self.frame_output.pack(padx=padding, pady=padding)


root = Tk()
my_gui = mainGUI(root)
root.mainloop()
