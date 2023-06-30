from tkinter import BOTTOM, END, Frame, Tk, Label, Button, Text, Scrollbar, RIGHT, Y

from fileManage import chooseFolder, createFile


class mainGUI:
    def __init__(self, master):
        padding = 3

        frame = Frame(root)
        footer_frame = Frame(root)
        frame.pack()
        footer_frame.pack(side=BOTTOM)

        width = 400  # Width
        height = 300  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.master = master
        master.title("CV Automation")
        master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # master.eval('tk::PlaceWindow . center')

        l = Label(frame, text="Enter Name:")
        l.config(font=("Courier", 10))

        T = Text(frame, height=1, width=25)
        T.insert(END, "First Name")
        # T.bind('<KeyRelease>',self.my_upd)
        self.fname = T

        l2 = Label(frame, text="Last Name")
        l2.config(font=("Courier", 10))

        T2 = Text(frame, height=1, width=25)
        T2.insert(END, "Last Name")
        # T.bind('<KeyRelease>',self.my_upd)
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

        self.close_button = Button(footer_frame, text="Close", command=master.quit)

        # for child in master.winfo_children():
        #     child.config(padx=10, pady=10)
        # child.place(relx = .5, rely = 0, anchor="center")

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

    def my_upd(self, value):
        my_str = self.fname.get(
            "1.0", "end-1c"
        )  # The input string except the last line break
        breaks = my_str.count("\n")  # Number of line breaks ( except the last one )
        char_numbers = len(my_str) - breaks  # Number of chars user has entered
        # l2.config(text=str(char_numbers)) # display number of chars
        if char_numbers > 7:
            self.fname.delete(
                "end-{}c".format(char_numbers - 7)
            )  # remove last char of text widget


root = Tk()
my_gui = mainGUI(root)
root.mainloop()
