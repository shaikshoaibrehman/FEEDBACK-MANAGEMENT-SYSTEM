from tkinter import *
from PIL import Image,ImageTk
import time
from tkinter import ttk,messagebox
import sqlite3
import os

class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback  Management  System !!")
        self.root.geometry("1900x1080+0+0")
        
        
        
        
        # ====Title of the Project======

        title=Label(self.root,text="Feedback Management System",font=("times new roman",40,"bold"),bg="#c7f1f4",fg="#fc2a99",anchor='w',padx=450).place(x=0,y=0,relwidth=1,height=70)
        # ==============Buttton Logout=============
        
        btn_logout=Button(self.root, command=self.logout_feed,text="Logout", font=("times new roman",15,"bold"),bg="#f8dcfb",cursor="hand2").place(x=1350,y=10,height=50,width=100)
        
#         # ================Time==========================
        self.lbl_clock=Label(self.root,text="  You are Heartly Welcomed in Feedback Management System !!\t\t  Date: DD-MM-YYYY\t\t Time: HH-MM-SS\t\t",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)    
        
        
        
        # ======================================================
    
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.fac_id=StringVar()
        self.fac_name=StringVar()
        self.var_sem=StringVar()
        self.var_q1=StringVar()
        self.var_q2=StringVar()
        self.var_q3=StringVar()
        self.var_q4=StringVar()
        self.var_q5=StringVar()
        self.var_btn=StringVar()
        
        
        
        
        searchFrame=LabelFrame(self.root,text="Search Faculty",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#ecf8f9",fg="#f30f0f")
        searchFrame.place(x=500,y=120,width=600,height=70)
        
        # ==========Option================
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","FAC_ID","FAC_NAME"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=10)
        
        btn_search=Button(searchFrame,text="Search",cursor="hand2",command=self.search,font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=420,y=8,width=150,height=30)
        
        btn_clear=Button(self.root,text="Clear",cursor="hand2",command=self.clear,font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=1150,y=150,width=100,height=35)

        #============ Row 1 ==============================
        lbl_facid=Label(self.root,text="Faculty ID",font=("times new roman" ,18,"bold")).place(x=50,y=225)
        
        lbl_name=Label(self.root,text="Faculty Name",font=("times new roman" ,18,"bold")).place(x=450,y=225)

        lbl_sem=Label(self.root,text="Student Sem",font=("times new roman" ,18,"bold")).place(x=900,y=225)
        
        txt_facid=Entry(self.root,textvariable=self.fac_id,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=225)
        
    
        txt_facname=Entry(self.root,textvariable=self.fac_name,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=630,y=225)
        


        cmb_sem=ttk.Combobox(self.root,textvariable=self.var_sem,values=("Select","1st SEM","2nd SEM","3rd SEM","4th SEM","5th SEM","6th SEM","7th SEM","8th SEM"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        
        cmb_sem.place(x=1080,y=225,width=180)
        cmb_sem.current(0)
        
        
        #============ feedback ques ==============================
        
        
        lbl_q1=Label(self.root,text="1. Presentation of Subject matter",font=("times new roman" ,18,"bold")).place(x=250,y=300)

        cmb_q1=ttk.Combobox(self.root,textvariable=self.var_q1,values=("Select","Excellent","Very Good","Good","Satisfactory","Poor"),state='readonly',justify=CENTER,font=("goudy old style", 18,"bold"))
        
        cmb_q1.place(x=800,y=295,width=180)
        cmb_q1.current(0)
        
        lbl_q2=Label(self.root,text='''2. Communication Skills &
            Interaction with the students''',font=("times new roman" ,18,"bold")).place(x=203,y=350)

        cmb_q2=ttk.Combobox(self.root,textvariable=self.var_q2,values=("Select","Excellent","Very Good","Good","Satisfactory","Poor"),state='readonly',justify=CENTER,font=("goudy old style", 18,"bold"))
        
        cmb_q2.place(x=800,y=355,width=180)
        cmb_q2.current(0)

        lbl_q3=Label(self.root,text="3. Punctuality & Regularity",font=("times new roman" ,18,"bold")).place(x=250,y=430)

        cmb_q3=ttk.Combobox(self.root,textvariable=self.var_q3,values=("Select","Excellent","Very Good","Good","Satisfactory","Poor"),state='readonly',justify=CENTER,font=("goudy old style", 18,"bold"))
        
        cmb_q3.place(x=800,y=420,width=180)
        cmb_q3.current(0)
        
        lbl_q4=Label(self.root,text='''4. Ability to motivate the students &
    Clarification of doubts''',font=("times new roman" ,18,"bold")).place(x=250,y=480)

        cmb_q4=ttk.Combobox(self.root,textvariable=self.var_q4,values=("Select","Excellent","Very Good","Good","Satisfactory","Poor"),state='readonly',justify=CENTER,font=("goudy old style", 18,"bold"))

        cmb_q4.place(x=800,y=485,width=180)
        cmb_q4.current(0)
        
        lbl_q5=Label(self.root,text="5. Teacher’s approach towards students",font=("times new roman" ,18,"bold")).place(x=250,y=550)

        cmb_q5=ttk.Combobox(self.root,textvariable=self.var_q5,values=("Select","Excellent","Very Good","Good","Satisfactory","Poor"),state='readonly',justify=CENTER,font=("goudy old style", 18,"bold"))
        
        cmb_q5.place(x=800,y=550,width=180)
        cmb_q5.current(0)
        
        
        #======= Faculty Details  Frame ========================
        
        FacultyFrame=Frame(self.root,bd=4,relief=RIDGE)
        FacultyFrame.place(x=1050,y=300,width=398,height=300)
        
        scrollx=Scrollbar(FacultyFrame,orient=HORIZONTAL)
        scrolly=Scrollbar(FacultyFrame,orient=VERTICAL)
        
        self.facultyTable=ttk.Treeview(FacultyFrame,columns=("fac_id","fac_name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.facultyTable.xview)
        scrolly.config(command=self.facultyTable.yview)
        
        self.facultyTable.heading("fac_id",text="FACULTY ID")
        self.facultyTable.heading("fac_name",text="FACULTY NAME")

        self.show()
        
        self.facultyTable["show"]="headings"
        
        self.facultyTable.column("fac_id",width=50)
        self.facultyTable.column("fac_name",width=100)
        self.facultyTable.pack(fill=BOTH,expand=1)
        self.facultyTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        
        btn_submit=Button(self.root,text="Submit",cursor="hand2",command=self.feedback,font=("goudy old style",20,"bold"),bg="#ff4500",fg="#ffffff").place(x=810,y=650,width=150,height=40)

        # Footer
        lbl_footer=Label(self.root,text="FMS: Feedback Management System  | Developed by PRASHANT KUMAR & SHOAIB REHMAN ",font=("times new roman",18),bg="#008b8b",fg="#ffffff").pack(side=BOTTOM,fill=X)
        
        self.update_content()
#====================functions============================



            
            
    def feedback(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.fac_id.get()=="":
                messagebox.showerror("Error","Faculty ID Must be Required",parent=self.root)
            elif self.fac_name.get()=="":
                messagebox.showerror("Error","Faculty Name Must be Required",parent=self.root)
            elif self.var_sem.get()=="Select":
                messagebox.showerror("Error","Semester column Must Be Filled",parent=self.root)
            elif self.var_q1.get()=="Select":
                messagebox.showerror("Error","Question 1 Must be Filled",parent=self.root)
            elif self.var_q2.get()=="Select":
                messagebox.showerror("Error","Question 2 Must be Filled",parent=self.root)
            elif self.var_q3.get()=="Select":
                messagebox.showerror("Error","Question 3 Must be Filled",parent=self.root)
            elif self.var_q4.get()=="Select":
                messagebox.showerror("Error","Question 4 Must be Filled",parent=self.root)
            elif self.var_q5.get()=="Select":
                messagebox.showerror("Error","Question 5 Must be Filled",parent=self.root)
                
            else:
                
                cur.execute("Insert into feedback( fac_id , fac_name ,  sem , q1,q2,q3,q4,q5  ) values(?,?,?,?,?,?,?,?)",(
                                                        self.fac_id.get(),
                                                        self.fac_name.get(),
                                                        self.var_sem.get(),
                                                        self.var_q1.get(),
                                                        self.var_q2.get(),
                                                        self.var_q3.get(),
                                                        self.var_q4.get(),
                                                        self.var_q5.get(),
                                                    
                ))
                con.commit()
                messagebox.showinfo("Success","Feedback Given SUCCESSFULLY !!",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
            
    def update_content(self):
        time_=time.strftime('%I:%M:%S')    
        date_=time.strftime('%d:%m:%Y')
        self.lbl_clock.config(text=f"  You are Heartly Welcomed by PRASHANT KUMAR & SHOAIB REHMAN !!\t\t  Date: {str(date_)}\t\t Time:{str(time_)}")   
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
                cur.execute("select * from faculty where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
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
        self.fac_id.set(row[0])
        self.fac_name.set(row[1])
        
        
    def show(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            cur.execute("Select * from faculty")
            rows=cur.fetchall()
            self.facultyTable.delete(*self.facultyTable.get_children())
            for row in rows:
                self.facultyTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

            
            
    
    def clear(self):
        self.fac_id.set("")
        self.fac_name.set("")
        self.var_sem.set("Select")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.var_q1.set("Select")
        self.var_q2.set("Select")
        self.var_q3.set("Select")
        self.var_q4.set("Select")
        self.var_q5.set("Select")
        
        self.show()



    def logout_feed(self):
        self.root.destroy()
        os.chdir(r"Feedback System")
        os.system("python login.py")
    


if  __name__=="__main__":
    root=Tk()
    obj=Feedback(root)
    root.resizable(True,False)
    root.mainloop()
        