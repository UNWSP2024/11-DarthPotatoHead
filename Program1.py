#Program Written By: Ainsley Bellamy
#Date Written: 04/09/2025
#Program Title: Simple_GUI


import tkinter
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("StarWars_GUI")
        self.label = tkinter.Label(self.main_window, text='"No, I am your father."')
        self.label1 = tkinter.Label(self.main_window, text="--Darth Vader,")
        self.label2 = tkinter.Label(self.main_window, text="The Empire Strikes Back")

        self.label.pack(padx=50, pady=15)
        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = MyGUI()