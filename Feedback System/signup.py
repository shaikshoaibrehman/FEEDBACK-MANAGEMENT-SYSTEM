from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import smtplib
import time
# from login import Login_System


class Signup_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback Management System!!")
        self.root.geometry("1900x1080+0+0")
        self.root.config(bg="#f4bbff")
        
        
    
        #====== Images==============
        self.phone_image=ImageTk.PhotoImage(file="D:\VS Studio Code\Feedback System\image/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=300,y=50)
        
        # =======  Login Frame ============
        
        self.usn=StringVar()
        self.password=StringVar()
        self.name=StringVar()
        self.sem=StringVar()
        self.email=StringVar()
        self.otp=StringVar()
        
        signup_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#fafafa")
        signup_frame.place(x=750,y=90,width=500,height=550)
        
        title=Label(signup_frame,text="Sign Up System",font=("Elephant",30,"bold"),bg="#fafafa",fg="#9400d3").place(x=0,y=30,relwidth=1)
        
        lbl_usn=Label(signup_frame,text="Student USN :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=100)
        
        txt_usn=Entry(signup_frame,textvariable=self.usn,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=190,y=100,width=280,height=35)

        lbl_name=Label(signup_frame,text="Student Name :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=170)
        
        txt_name=Entry(signup_frame,textvariable=self.name,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=200,y=170,width=270,height=35)


        lbl_sem=Label(signup_frame,text="Semester:",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=240)
        
        txt_sem=Entry(signup_frame,textvariable=self.sem,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=190,y=240,width=280,height=35)

        lbl_pass=Label(signup_frame,text="Password :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=310)
        
        txt_pass=Entry(signup_frame,textvariable=self.password,font=("goudy old style",18),show="*",bg="#ECECEC",fg="#00008b").place(x=190,y=310,width=280,height=35)
        
        
        lbl_email=Label(signup_frame,text="Email ID :",font=("Times New Roman",18,"bold"),bg="#fafafa").place(x=30,y=380)
        
        txt_email=Entry(signup_frame,textvariable=self.email,font=("goudy old style",18),bg="#ECECEC",fg="#00008b").place(x=190,y=380,width=280,height=35)
        
        btn_signup=Button(signup_frame, text="Sign Up",command=self.add, font=("times new roman",18,"bold"),bg="#29ab87",cursor="hand2",activebackground="#29ab87").place(x=180,y=450,height=40,width=150)
        

        
        
        # Footer
        lbl_footer=Label(self.root,text="FMS: Feedback Management System !!  | Developed by PRASHANT KUMAR & SHOAIB REHMAN ",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        
        
        
        # ======Animation Images =================
        
        self.loginim1=ImageTk.PhotoImage(file="D:\VS Studio Code\Feedback System\image/logim1.png")
        self.loginim2=ImageTk.PhotoImage(file="D:\VS Studio Code\Feedback System\image/logim2.png")
        self.loginim3=ImageTk.PhotoImage(file="D:\VS Studio Code\Feedback System\image/logim3.png")
        
        
        
        self.lbl_change_image=Label(self.root,bg="#fafafa")
        self.lbl_change_image.place(x=467,y=153,width=240,height=428)
        
        self.animate()
        

        #======================functions=================================
        
    
        
    def animate(self):
        self.im=self.loginim1
        self.loginim1=self.loginim2    
        self.loginim2=self.loginim3    
        self.loginim3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def signup(self):
        self.root.destroy()
        os.chdir(r"Feedback System")
        os.system("python login.py")
    
    
    def add(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.usn.get()=="":
                messagebox.showerror("Error","USN Must be Required",parent=self.root)
            elif self.name.get()=="":
                messagebox.showerror("Error","Name Must be Required",parent=self.root)
            elif self.sem.get()=="":
                messagebox.showerror("Error","Semester Must be Required",parent=self.root)
            elif self.email.get()=="":
                messagebox.showerror("Error","Email Must be Required",parent=self.root)
            elif self.password.get()=="":
                messagebox.showerror("Error","Password Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from student where usn=?",(self.usn.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Student already registred")
                else:
                    cur.execute("Insert into student(usn , name , sem , password  ,email ) values(?,?,?,?,?)",(
                                                    self.usn.get(),
                                                    self.name.get(),
                                                    self.sem.get(),
                                                    self.password.get(),
                                                    self.email.get(),
                                                    # self.password.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added SUCCESSFULLY !!",parent=self.root)
                    # self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

    

    

    
    
                        
    
    
if  __name__=="__main__":
    root=Tk()
    obj=Signup_System(root)
    root.mainloop()