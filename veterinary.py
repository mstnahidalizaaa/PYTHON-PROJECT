from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox





class Veterinary:
    def __init__(self,root):
        self.root=root
        self.root.title("Veterinary Appionment Appication")
        self.root.geometry("800x600+0+0")
        labeltitle=Label(self.root,bd=20,relief=RIDGE,text="+ Pet Care Bd",fg="red",bg="white",font=("Times New Roman",30,"bold"))    
        labeltitle.pack(side=TOP,fill=X)
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=800,height=400)  

        #=====================buttonframe======================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=515,width=800,height=70)


        #=================DataFrame=============

        label_Pet_Name=Label(Dataframe,text="Pet Name:",font=("Calibri (Body)",12,"bold"),padx=2,pady=6)
        label_Pet_Name.grid(row=0,column=0,sticky=W)
        text_Pet_Name=Entry(Dataframe,font=("arial",13,"bold"),width=20)
        text_Pet_Name.grid(row=0,column=1)

        label_Sex=Label(Dataframe,text="Sex:",font=("Calibri (Body)",12,"bold"),padx=2,pady=6)
        label_Sex.grid(row=2,column=0,sticky=W)
        sex_var = StringVar()
        male_radio = Radiobutton(Dataframe, text="Male", variable=sex_var, value="Male")
        male_radio.grid(row=2, column=1, sticky=W)
        female_radio = Radiobutton(Dataframe, text="Female", variable=sex_var, value="Female")
        female_radio.grid(row=2, column=2, sticky=W)




root=Tk() 
ob=Veterinary(root)
root.mainloop()
