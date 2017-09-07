
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import *
import random
import time




global message
message = "Objasni baki šta je: "                                                                          

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("Objasni Baki")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
                
        frame1 = Frame(self)
        frame1.pack(fill=X)
           
        
        label = Label(frame1, text=message, font=(None, 18)).grid(row=0, column=0, pady=20, padx=5)
        
        

        frame2 = Frame(self)
        frame2.pack(fill=X)
        start = Button(frame2, text = "START", command = start_click)
        start.pack(pady = 30)
        start.config(height=15, width = 30)

        
def start_click():
        i = 0
        while(i < 5):
                message += str(i)
                i += 1
                time.sleep(1)
        """
        f = open("pojmovi.txt", "r")
        List = f.readlines()
        f.close()
        randomTema = random.choice(List)
        print(randomTema)

        f = open("pojmovi.txt", "w")
        for line in List:
                if line != randomTema:
                        f.write(line) 
        """  
        
        


def main():
  
    root = Tk()
    root.geometry("500x200+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
