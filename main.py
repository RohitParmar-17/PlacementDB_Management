from tkinter import *
from Student import *
from College import *
from Company import *
from Job import *
from Interviewer import *

class main:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('300x300')
        self.root.title("Admin")
        

        self.l1=Label(self.root,text='Select ')
        self.l1.grid(row=0,column=0)
        self.clicked=StringVar()
        self.options=["Company","College","Job","Interviewer","Student"]
        self.drop=OptionMenu(self.root,self.clicked,*self.options)
        self.drop.grid(row=0,column=1)
        self.clicked.set('Choose')
        self.b1=Button(self.root,text="Submit",width=20,command=self.next)
        self.b1.grid(row=1,column=0,columnspan=2)
        self.b2=Button(self.root,text="Exit",width=20,command=self.exit)
        self.b2.grid(row=2,column=0,columnspan=2)
        
        self.root.mainloop()
    def exit(self):
        self.root.destroy()
    def next(self):
        if self.clicked.get()=="Company":
            self.root.destroy()
            Company()
            
        elif self.clicked.get()=="Student":
            self.root.destroy()
            Student()

        elif self.clicked.get()=="Job":
            self.root.destroy()
            Job()
          
        elif self.clicked.get()=="Interviewer":
            self.root.destroy()
            Interviewer()
            
        elif self.clicked.get()=="College":
            self.root.destroy()
            College()
            
if __name__=="__main__":
    main()



