# main.py

from gui import CampusGuideGUI
import tkinter as tk


def start_application():

    window = tk.Tk()

    app = CampusGuideGUI(window)

    window.mainloop()



if __name__ == "__main__":

    start_application()