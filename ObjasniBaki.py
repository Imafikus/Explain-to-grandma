
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import *
import random
import time
import pygame


                                                                 

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
    
        
    def initUI(self):
        self.message = StringVar()
        self.master.title("Objasni Baki")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
        
        frame1 = Frame(self)
        frame1.pack(fill=X)
        #message = StringVar()
        self.message.set("Objasni baki šta je: ")
        
               
        
        label = Label(frame1, textvariable=self.message, font=(None, 18)).grid(row=0, column=0, pady=20, padx=5)
        
        

        frame2 = Frame(self)
        frame2.pack(fill=X)
        start = Button(frame2, text = "START", command = self.start_click)
        start.pack(pady = 30)
        start.config(height=15, width = 30)

    def start_click(self):
       
        f = open("pojmovi.txt", "r")
        List = f.readlines()
        f.close()
        randomTema = random.choice(List)
        #print(randomTema)

        f = open("pojmovi.txt", "w")
        for line in List:
                if line != randomTema:
                        f.write(line)
        
       
        randomTema = "Objasni baki šta je: " + randomTema
        self.message.set(randomTema)
        file = 'suspense.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
        
        
        


def main():
  
    root = Tk()
    root.geometry("500x200+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
