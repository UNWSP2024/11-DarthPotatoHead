#Program Written By: Ainsley Bellamy
#Date Written: 04/09/2025
#Program Title: Simple_GUI

#Import proper modules.
import tkinter
class MyGUI:
#Initialize main window.
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("StarWars_GUI")
#Set labels.
        self.label = tkinter.Label(self.main_window, text='"No, I am your father."', borderwidth=6, relief="solid")
        self.label1 = tkinter.Label(self.main_window, text="--Darth Vader,")
        self.label2 = tkinter.Label(self.main_window, text="The Empire Strikes Back")
#Pack and format.
        self.label.pack(padx=50, pady=15, ipadx=3, ipady=2)
        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()
#Create main window object.
if __name__ == "__main__":
    my_gui = MyGUI()