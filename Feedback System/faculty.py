from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class facultyClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback Management System !!")
        self.root.geometry("1225x670+255+125")
        self.root.config(bg="#ecf8f9")
        self.root.focus_force()
        # ======================
        #  All variables========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_fac_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_fac_name=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        
        # ======================================================
        searchFrame=LabelFrame(self.root,text="Search Faculty",font=("goudy old style",15,"bold"),bd=4,relief=RIDGE,bg="#ecf8f9",fg="#f30f0f")
        searchFrame.place(x=350,y=10,width=600,height=70)
        
        # ==========Option================
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","FAC_NAME","FAC_ID"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=10)
        
        btn_search=Button(searchFrame,command=self.search,text="Search",cursor="hand2",font=("goudy old style",15,"bold"),bg="#ffdab9",fg="#ff00ff").place(x=410,y=8,width=150,height=30)
        
        # =======Title===============
        title=Label(self.root,text="Faculty Details",font=("times new roman" "bold",18,"bold"),bd=3,relief=RIDGE,bg="#faf0e6",fg="#c71585").place(x=50,y=120,width=1100)
        
        #========Content===================
        
        #============ Row 1 ==============================
        lbl_facid=Label(self.root,text="Faculty ID",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=180)
        
        lbl_gender=Label(self.root,text="Gender",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=450,y=180)

        lbl_contact=Label(self.root,text="Contact",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=800,y=180)
        
        txt_facid=Entry(self.root,textvariable=self.var_fac_id,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=180)
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style", 13,"bold"))
        
        cmb_gender.place(x=550,y=180,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=900,y=180)
        
        #============ Row 2 ==============================
        lbl_name=Label(self.root,text="Name",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=230)
        
        lbl_doj=Label(self.root,text="D.O.J.",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=800,y=230)
        
        txt_name=Entry(self.root,textvariable=self.var_fac_name,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=230)
        

        
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=900,y=230)

        #============ Row 3 ==============================
        lbl_email=Label(self.root,text="Email",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=50,y=280)
        
        lbl_password=Label(self.root,text="Password",font=("times new roman" ,18,"bold"),bg="#ecf8f9").place(x=450,y=250)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435").place(x=200,y=280)
        
        self.txt_password=Entry(self.root,textvariable=self.var_password,font=("goudy old style",15,"bold"),bg="lightyellow",fg="#f51435")
        self.txt_password.place(x=565,y=250)
        
        
        
        
        
        # ======= Buttons====================
        btn_add=Button(self.root,text="Save",cursor="hand2",command=self.add,font=("goudy old style",15,"bold"),bg="#4682b4",fg="white").place(x=550,y=400,width=100,height=30)
        
        btn_update=Button(self.root,text="Update",cursor="hand2",command=self.update,font=("goudy old style",15,"bold"),bg="#228b22",fg="white").place(x=700,y=400,width=100,height=30)
        
        btn_delete=Button(self.root,text="Delete",cursor="hand2",command=self.delete,font=("goudy old style",15,"bold"),bg="#f94d00",fg="white").place(x=850,y=400,width=100,height=30)
        
        btn_clear=Button(self.root,text="Clear",cursor="hand2",command=self.clear,font=("goudy old style",15,"bold"),bg="red",fg="white").place(x=1010,y=400,width=100,height=30)
        
        #======= Faculty Details ========================
        
        fac_frame=Frame(self.root,bd=4,relief=RIDGE)
        fac_frame.place(x=0,y=450,relwidth=1,height=220)
        
        scrollx=Scrollbar(fac_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(fac_frame,orient=VERTICAL)
        
        self.facultyTable=ttk.Treeview(fac_frame,columns=("fac_id","fac_name","gender","contact","doj","email","password"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.facultyTable.xview)
        scrolly.config(command=self.facultyTable.yview)
        
        self.facultyTable.heading("fac_id",text="FAC ID")
        self.facultyTable.heading("fac_name",text="FAC Name") 
        self.facultyTable.heading("gender",text="Gender")
        self.facultyTable.heading("contact",text="Contact")   
        self.facultyTable.heading("doj",text="DOJ")
        self.facultyTable.heading("email",text="Email")
        self.facultyTable.heading("password",text="Password")
        self.facultyTable["show"]="headings"
        
        self.facultyTable.column("fac_id",width=70)
        self.facultyTable.column("fac_name",width=100)
        self.facultyTable.column("gender",width=100)
        self.facultyTable.column("contact",width=100)
        self.facultyTable.column("doj",width=100)
        self.facultyTable.column("email",width=100)
        self.facultyTable.column("password",width=100)
        self.facultyTable.pack(fill=BOTH,expand=1)
        self.facultyTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================ Functions ===============================        
    def add(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.var_fac_id.get()=="":
                messagebox.showerror("Error","Faculty ID Must be Required",parent=self.root)
            elif self.var_fac_name.get()=="":
                messagebox.showerror("Error","Faculty Name Must be Required",parent=self.root)
                
            else:
                cur.execute("Select * from faculty where fac_id=?",(self.var_fac_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Faculty ID already asssigned , Try different FacultyID")
                else:
                    cur.execute("Insert into faculty(fac_id , fac_name ,  gender , contact , doj ,email , password  ) values(?,?,?,?,?,?,?)",(
                                                    self.var_fac_id.get(),
                                                    self.var_fac_name.get(),
                                                    self.var_gender.get(),
                                                    self.var_contact.get(),
                                                    self.var_doj.get(),
                                                    self.var_email.get(),
                                                    self.var_password.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Faculty Added SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

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
            
    def get_data(self,ev):
        f=self.facultyTable.focus()
        content=(self.facultyTable.item(f))
        row=content['values']
        self.var_fac_id.set(row[0])
        self.var_fac_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_contact.set(row[3])
        self.var_doj.set(row[4])
        self.var_email.set(row[5])
        self.var_password.set(row[6])

        
        
    def update(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.var_fac_id.get()=="":
                messagebox.showerror("Error","Faculty ID Must be Required",parent=self.root)
            
            else:
                cur.execute("Select * from faculty where fac_id=?",(self.var_fac_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Faculty ID")
                else:
                    cur.execute("Update faculty set    fac_name=?,gender=? , contact=? ,  doj=? ,email=? , password=? where fac_id=?",(
                                                    self.var_fac_name.get(),
                                                    self.var_gender.get(),
                                                    self.var_contact.get(),
                                                    self.var_doj.get(),
                                                    self.var_email.get(),
                                                    self.var_password.get(),
                                                    self.var_fac_id.get()
                                                    
                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Faculty Updated SUCCESSFULLY !!",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'fms.db' )
        cur=con.cursor()
        try:
            if self.var_fac_id.get()=="":
                messagebox.showerror("Error","Faculty ID Must be Required",parent=self.root)
                
            else:
                op=messagebox.askyesno("CONFIRM","Do You Really want to DELETE ??",parent=self.root)
                if op==True:
                    cur.execute("Delete from faculty where fac_id=?",(self.var_fac_id.get(),))
                    con.commit()
                    messagebox.showinfo("DELETE","Faculty Deleted SUCCESSFULLY !!",parent=self.root)
                    self.clear()
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_fac_id.set("")
        self.var_fac_name.set("")
        self.var_gender.set("Select")
        self.var_contact.set("") 
        self.var_doj.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
    
        

                
        
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
                
        

if  __name__=="__main__":
    root=Tk()
    obj=facultyClass(root)
    root.mainloop()