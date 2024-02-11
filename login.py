from tkinter import *
from main import *
from tkinter import messagebox

root=Tk()
root.title("Login Page")
root.geometry('250x130')
class login:
    def __init__(self,root):
        self.root=root

        self.l1=Label(self.root,text="Username ")
        self.l1.grid(row=0,column=0)
        self.e1=Entry(self.root,borderwidth=5)
        self.e1.grid(row=0,column=1)
        self.l2=Label(self.root,text="Password ")
        self.l2.grid(row=1,column=0)
        self.e2=Entry(self.root,show='*',borderwidth=5)
        self.e2.grid(row=1,column=1)
        self.b1=Button(self.root,text="Proceed",width=30,command=self.proc)
        self.b1.grid(row=2,column=0,columnspan=2)
        self.b2=Button(self.root,text="Exit",width=30,command=self.exit)
        self.b2.grid(row=3,column=0,columnspan=2)
        self.root.mainloop()
    def exit(self):
        self.root.destroy()
    def proc(self):
        if self.e1.get()=="Rohit" and self.e2.get()=="Rohit@17":
            self.root.destroy()
            main()
        else:
            messagebox.showerror("Error","Authentication failed")


if __name__=="__main__":
     login(root)
     

