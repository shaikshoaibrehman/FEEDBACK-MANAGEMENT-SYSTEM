from tkinter import *
from PIL import Image,ImageTk
import time
from tkinter import ttk,messagebox
import sqlite3
import os

class FeedbackReport:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback  Management  System !!")
        self.root.geometry("1900x1080+0+0")
        
        
        
        
    # ====Title of the Project======

        title=Label(self.root,text="Feedback Management System",font=("times new roman",40,"bold"),bg="#c7f1f4",fg="#fc2a99",anchor='w',padx=450).place(x=0,y=0,relwidth=1,height=70)
        # ==============Buttton Logout=============
        
        # btn_logout=Button(self.root, command=self.logout,text="Logout", font=("times new roman",15,"bold"),bg="#f8dcfb",cursor="hand2").place(x=1350,y=10,height=50,width=100)
        
#         # ================Time==========================
        self.lbl_clock=Label(self.root,text=" You are Heartly Welcomed in Feedback Management System !!\t\t  Date: DD-MM-YYYY\t\t Time: HH-MM-SS\t\t",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)    
        
        
        
        # ======================================================
    
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_fac_id=StringVar()
        self.var_fac_name=StringVar()
        self.var_sem=StringVar()
        self.var_q1=StringVar()
        self.var_q2=StringVar()
        self.var_q3=StringVar()
        self.var_q4=StringVar()
        self.var_q5=StringVar()
        
        
        
        
        
        searchFrame=LabelFrame(self.root,text="Search Faculty",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#ecf8f9",fg="#f30f0f")
        searchFrame.place(x=500,y=120,width=600,height=70)
        
        # ==========Option================
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","FAC_NAME","FAC_ID"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=10)
        
        btn_search=Button(searchFrame,text="Search",cursor="hand2",command=self.search,font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=420,y=8,width=150,height=30)
            

        #======= Faculty Details  Frame ========================
        
        FacultyFrame=Frame(self.root,bd=4,relief=RIDGE)
        FacultyFrame.place(x=50,y=250,width=1400,height=500)
        
        scrollx=Scrollbar(FacultyFrame,orient=HORIZONTAL)
        scrolly=Scrollbar(FacultyFrame,orient=VERTICAL)
        
        self.facultyTable=ttk.Treeview(FacultyFrame,columns=("fac_id","fac_name","sem","q1","q2","q3","q4","q5"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.facultyTable.xview)
        scrolly.config(command=self.facultyTable.yview)
        
        self.facultyTable.heading("fac_id",text="FACULTY ID")
        self.facultyTable.heading("fac_name",text="FACULTY NAME")
        self.facultyTable.heading("sem",text="SEM")
        self.facultyTable.heading("q1",text="Presentation of Subject matter")
        self.facultyTable.heading("q2",text='''       Communication Skills &
    Interaction with the students''')
        self.facultyTable.heading("q3",text="Punctuality & Regularity")
        self.facultyTable.heading("q4",text='''Ability to motivate the students &
        Clarification of doubts''')
        self.facultyTable.heading("q5",text='''        Teacher’s approach
        towards students''')

        self.show()
        
        self.facultyTable["show"]="headings"
        
        self.facultyTable.column("fac_id",width=100)
        self.facultyTable.column("sem",width=100)
    
        
        self.facultyTable.pack(fill=BOTH,expand=1)
        self.facultyTable.bind("<ButtonRelease-1>")
        self.show()

        
        btn_print=Button(self.root,text="Print",cursor="hand2",font=("goudy old style",20,"bold"),bg="#ff4500",fg="#ffffff").place(x=1200,y=770,width=150,height=40)
        
        btn_clear=Button(self.root,text="Clear",cursor="hand2",command=self.clear,font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=1150,y=145,width=100,height=40)
        
        # Footer
        lbl_footer=Label(self.root,text="FMS: Feedback Management System  | Developed by PRASHANT KUMAR & SHOAIB REHMAN ",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        self.update_content()
        #==============================functions=====================
    def update_content(self):
        time_=time.strftime('%I:%M:%S')    
        date_=time.strftime('%d:%m:%Y')
        self.lbl_clock.config(text=f" You are Heartly Welcomed by PRASHANT KUMAR & SHOAIB REHMAN!!\t\t  Date: {str(date_)}\t\t Time:{str(time_)}")   
        self.lbl_clock.after(200,self.update_content)
        
        
        
    
    def search(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select a valid Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Give  Search Area Input",parent=self.root)
            else:
                cur.execute("select * from feedback where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.facultyTable.delete(*self.facultyTable.get_children())
                    for row in rows:
                        self.facultyTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.facultyTable.focus()
        content=(self.facultyTable.item(f))
        row=content['values']
        self.var_fac_id.set(row[0])
        self.var_fac_name.set(row[1])
        self.var_sem.set(row[2])
        self.var_q1.set(row[3])
        self.var_q2.set(row[4])
        self.var_q3.set(row[5])
        self.var_q4.set(row[6])
        self.var_q5.set(row[7])
        
    def show(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from feedback")
            rows=cur.fetchall()
            self.facultyTable.delete(*self.facultyTable.get_children())
            for row in rows:
                self.facultyTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
    def clear(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()



    # def logout(self):
    #     self.root.destroy()
    #     os.chdir(r"Feedback System")
    #     os.system("python login.py")
    


if  __name__=="__main__":
    root=Tk()
    obj=FeedbackReport(root)
    root.resizable(True,False)
    root.mainloop()
        