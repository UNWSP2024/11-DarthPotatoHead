#Program Written By: Ainsley Bellamy
#Date Written: 04/09/2025
#Program Title: Simple_GUI


#Import proper modules.
import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
#Iinitialize main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("TopSecretInfo")
#Create both a showinfo button and a quit button.
        self.button = tkinter.Button(self.main_window, text="[TOP_SECRET_INFORMATION]", command=self.display, borderwidth=8, relief="sunken")
        self.terminate = tkinter.Button(self.main_window, text="-ESCAPE-", command=self.main_window.destroy)
#Pack into main window.
        self.button.pack(padx=10, pady=15)
        self.terminate.pack(side="right")

        tkinter.mainloop()
#Write display function for button.
    def display(self):
        tkinter.messagebox.showinfo('psst . . .', 'NAME: Ainsley Bellamy\nADDRESS: 16375 200th '
                                                      'St East Hastings, MN 55033')
#Create window object.
if __name__ == "__main__":
    my_gui = MyGUI()