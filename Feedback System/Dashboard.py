from tkinter import *
from PIL import Image,ImageTk
import time
from tkinter import ttk,messagebox
import sqlite3
import os
from faculty import facultyClass
from feedback_report import FeedbackReport


class FS:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback  Management  System !!")
        self.root.geometry("1900x1080+0+0")
        

        # ====Title of the Project======

        title=Label(self.root,text="Feedback Management System",font=("times new roman",40,"bold"),bg="#c7f1f4",fg="#fc2a99",anchor='w',padx=450).place(x=0,y=0,relwidth=1,height=70)
        # ==============Buttton Logout=============
        
        btn_logout=Button(self.root, command=self.logout,text="Logout", font=("times new roman",15,"bold"),bg="#f8dcfb",cursor="hand2").place(x=1350,y=10,height=50,width=100)
        
#         # ================Time==========================
        self.lbl_clock=Label(self.root,text="  You are Heartly Welcomed in Feedback Management System!!\t\t  Date: DD-MM-YYYY\t\t Time: HH-MM-SS\t\t",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
#         # ================LeftMenu=================
        
        self.MenuLogo=Image.open("D://VS Studio Code//Feedback System//image//feedback.png")
        self.MenuLogo=self.MenuLogo.resize((350,350))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#ffffff")
        LeftMenu.place(x=0,y=102,width=250,height=522 )
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        lbl_menu=Label(LeftMenu, text="Menu", font=("times new roman",25,),bg="#f8dcfb").pack(side=TOP,fill=X)
        
        
        btn_faculty=Button(LeftMenu, text="Faculty",command=self.faculty, font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_feedback_report=Button(LeftMenu, text="Feedback Report" ,command=self.feedback_report,font=("times new roman",20,"bold"),bg="skyblue",bd=5,cursor="hand2").pack(side=TOP,fill=X)
        
#         
        
        
    
#         #===============Content==============
        
        self.lbl_faculty=Label(self.root,text="Total Faculties\n[ 0 ]",bd=5,relief=RIDGE,bg="#f1dcfd",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_faculty.place(x=400,y=120,height=150,width=300)
        
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",bd=5,relief=RIDGE,bg="#c8f889",fg="#ef0289",font=("goudy old style",22,"bold"))
        self.lbl_student.place(x=950,y=120,height=150,width=300)
        
        self.lbl_rljit=Label(self.root,text="RLJIT",bd=5,relief=RIDGE,bg="#faf0e6",fg="#ef0289",font=("goudy old style",250,"bold"))
        self.lbl_rljit.place(x=400,y=320,height=400,width=1000)
        

        
        # Footer
        lbl_footer=Label(self.root,text="FMS: Feedback Management System  | Developed by PRASHANT KUMAR & SHOAIB REHMAN ",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        self.update_content()
        
# # ===================================================================
    def faculty(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=facultyClass(self.new_win)
        
    def feedback_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=FeedbackReport(self.new_win)
        


    def update_content(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            cur.execute('select * from faculty')
            faculty=cur.fetchall()
            self.lbl_faculty.config(text=f"Total Faculty\n[ {str(len(faculty))} ]")
            
            cur.execute('select * from student')
            student=cur.fetchall()
            self.lbl_student.config(text=f'Total Students\n[ {str(len(student))} ]')
            
    
            
            time_=time.strftime('%I:%M:%S')    
            date_=time.strftime('%d:%m:%Y')
            self.lbl_clock.config(text=f"  You are Heartly Welcomed by PRASHANT KUMAR & SHOAIB REHMAN !!\t\t  Date: {str(date_)}\t\t Time:{str(time_)}")   
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
        
    def logout(self):
        self.root.destroy()
        os.chdir(r"Feedback System")
        os.system("python login.py")
    
    
if  __name__=="__main__":
    root=Tk()
    obj=FS(root)
    root.resizable(True,False)
    root.mainloop()