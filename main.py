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


class mainGUI:
    def __init__(self, master):
        padding = 3

        tabmanager = Notebook(root)
        frame = Frame(tabmanager)
        tabmanager.pack(expand=1, fill="both")
        tabmanager.add(frame, text="Main")
        job_tab = Frame(tabmanager)
        tabmanager.add(job_tab, text="Job Posting Analysis")

        footer_frame = Frame(root)

        footer_frame.pack(side=BOTTOM)

        width = 650  # Width
        height = 500  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.master = master
        master.title("CV Automation")
        master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # master.eval('tk::PlaceWindow . center')

        # frame.pack()

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

        self.label = Label(frame, text="This is our first GUI!")

        l3 = Label(frame, text="No path selected", bg="white")
        # T3.insert(END, "File Path")
        self.path = l3

        self.choose_path_button = Button(
            frame, text="Choose Path", command=self.choose_path
        )

        T3 = Text(job_tab, height=13, width=60)
        T3.insert(END, "Enter job posting text")
        self.job_text = T3

        self.job_posting_button = Button(
            job_tab, text="Enter", command=self.process_posting
        )

        job_frame = Frame(job_tab)

        scroll_bar = Scrollbar(job_frame)
        scroll_bar.pack(side=RIGHT)

        self.text_widget = Text(
            job_frame, height=20, width=70, yscrollcommand=scroll_bar.set
        )
        self.text_widget.pack(side=LEFT)
        scroll_bar.config(command=self.text_widget.yview)

        self.label_job_analysis = Label(
            job_frame,
            text="",
            bg="white",
            width=100,
            height=200,
            wraplength=600,
            justify="left",
        )
        self.label_job_analysis.config(font=("Courier", 10))
        # self.label_job_analysis.pack(side=LEFT)

        self.job_text.pack(padx=padding, pady=padding)
        self.job_posting_button.pack(padx=padding, pady=padding)
        job_frame.pack(padx=padding, pady=padding)

        self.close_button = Button(footer_frame, text="Close", command=master.quit)

        l.pack(padx=padding, pady=padding)
        self.fname.pack(padx=padding, pady=padding)
        self.lname.pack(padx=padding, pady=padding)

        self.label.pack(padx=padding, pady=padding)
        self.path.pack(padx=padding, pady=padding)
        self.choose_path_button.pack(padx=padding, pady=padding)
        self.gen_file_button.pack(padx=padding, pady=padding)

        self.close_button.pack(padx=padding, pady=padding + 10, side=BOTTOM)

    def choose_path(self):
        print("choose folder")
        self.path.config(text=chooseFolder())

    def gen_file(self):
        fname = self.fname.get("1.0", "end-1c")
        lname = self.lname.get("1.0", "end-1c")
        createFile(fname, lname)

    def process_posting(self):
        # self.label_job_analysis.config(text=preprocess_text(self.job_text.get("1.0", "end-1c")))
        self.text_widget.insert(
            END, preprocess_text(self.job_text.get("1.0", "end-1c"))
        )


root = Tk()
my_gui = mainGUI(root)
root.mainloop()
