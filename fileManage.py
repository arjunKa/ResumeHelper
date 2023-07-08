from tkinter.filedialog import askdirectory
from datetime import datetime
import os

x = datetime.now()


class FileManage:
    def __init__(self):
        self.path = ""


fm = FileManage()


def chooseFolder():
    path = askdirectory(title="Select Folder")  # shows dialog box and return the path
    fm.path = path
    return path


def createFile(fname, lname):
    x = datetime.now()
    file_path = os.path.join(
        fm.path,
        "Resume_"
        + fname.strip().replace(" ", "")
        + lname.strip().replace(" ", "")
        + "_"
        + x.strftime("%d-%m-%Y.docx"),
    )
    print(fm.path)
    f = open(file_path, "a")
