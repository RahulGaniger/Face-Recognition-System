from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x790+0+0")  #heightxwidth+x-axis+y=axis
        self.root.title("Face Recognition System")


if __name__ == "__main__":
    # Create the main Tkinter window
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
        
        