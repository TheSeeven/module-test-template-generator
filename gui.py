from tkinter import *
from globals import *
import os, sys


def generate_result(functionName, username, numberOfTests):
    Header = generateHeader(functionName, username)
    NameHeader = generateHeaderName(functionName)
    TestGroup = generateTestGroup(functionName, numberOfTests)
    TestCases = generateTestCases(functionName)
    return fileTemplate.replace("$$$HEADER$$$", Header).replace(
        "$$$INCLUDES$$$",
        Includes).replace("$$$NAME_HEADER$$$", NameHeader).replace(
            "$$$TEST_GROUP$$$", TestGroup).replace("$$$TEST_CASES$$$",
                                                   TestCases)


class Interface:
    backgroundColor = '#1b1b1b'
    functionName = ""
    username = ""
    numberOfTests = -1

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def copyToClipboard(self):
        global TEST_NAMES, CURRENT_TEST_CASE_NAME, TEST_COUNTER
        Interface.functionName = str(self.functionName_Input.get())
        Interface.username = str(self.username_Input.get())

        try:
            Interface.numberOfTests = int(self.numberOfTests_Input.get())
        except:
            Interface.numberOfTests = -1
        if Interface.username != "" and Interface.functionName != "" and Interface.numberOfTests > 0:

            self.interface.clipboard_clear()
            self.interface.clipboard_append(
                generate_result(Interface.functionName, Interface.username,
                                Interface.numberOfTests))
            self.interface.update()
            self.status_Label.config(background="green",
                                     text="Copied to clipboard!",
                                     font=("San Francisco", 27))
        else:
            self.status_Label.config(
                background="red",
                text=
                "Fields can't be empty or \nNumber of tests must be a positive number",
                font=("San Francisco", 13))
        cleanValues()

    def __init__(self):

        #BASE
        #background an other customizations
        self.interface = Tk(className="module test template generator")
        self.interface.iconbitmap(
            default=Interface.resource_path('blender.ico'))
        self.interface.resizable(False, False)
        self.interface['background'] = Interface.backgroundColor
        self.buttonFrame = Frame(self.interface)
        self.statusFrame = Frame(self.interface)
        #BASE

        self.username_Label = Label(self.interface,
                                    text="Username:",
                                    fg="#dddddd",
                                    bg=Interface.backgroundColor,
                                    font=("San Francisco", 21),
                                    padx=20,
                                    pady=10)

        self.filename_Label = Label(self.interface,
                                    text="Function name:",
                                    fg="#dddddd",
                                    bg=Interface.backgroundColor,
                                    font=("San Francisco", 21),
                                    padx=20,
                                    pady=10)
        self.numberOfTests_Label = Label(self.interface,
                                         text="Number of tests:",
                                         fg="#dddddd",
                                         bg=Interface.backgroundColor,
                                         font=("San Francisco", 21),
                                         padx=20,
                                         pady=10)
        self.status_Label = Label(self.statusFrame,
                                  text="Ready to generate!",
                                  fg="#dddddd",
                                  bg="green",
                                  font=("San Francisco", 28),
                                  padx=20,
                                  pady=10)

        self.numberOfTests_Input = Entry(
            self.interface,
            font=("San Francisco", 13),
            highlightthickness=10,
            highlightbackground=Interface.backgroundColor,
            highlightcolor=Interface.backgroundColor)
        self.username_Input = Entry(
            self.interface,
            font=("San Francisco", 13),
            highlightthickness=10,
            highlightbackground=Interface.backgroundColor,
            highlightcolor=Interface.backgroundColor)
        self.functionName_Input = Entry(
            self.interface,
            font=("San Francisco", 13),
            highlightthickness=10,
            highlightbackground=Interface.backgroundColor,
            highlightcolor=Interface.backgroundColor)
        self.clipboardButton = Button(
            self.buttonFrame,
            text="Copy to clipboard",
            font=("San Francisco", 13),
            highlightthickness=5,
            highlightbackground=Interface.backgroundColor,
            highlightcolor=Interface.backgroundColor,
            command=self.copyToClipboard)

        self.buttonFrame.grid(row=3, column=0, pady=15, padx=10)
        self.statusFrame.grid(row=3, column=1, pady=15, padx=10)

        self.clipboardButton.grid(row=0, column=0)

        self.username_Label.grid(row=0, column=0)
        self.filename_Label.grid(row=1, column=0)
        self.numberOfTests_Label.grid(row=2, column=0)
        self.status_Label.grid(row=0, column=0)

        self.username_Input.grid(row=0, column=1)
        self.functionName_Input.grid(row=1, column=1)
        self.numberOfTests_Input.grid(row=2, column=1)


GUI = Interface()