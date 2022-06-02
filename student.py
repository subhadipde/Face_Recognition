from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
import phonenumbers
import re

# custom tkinter setting
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class Student:
    def __init__(self, root):
        self.root=root

        # code for full screen height and width ----------------------------
        Width= root.winfo_screenwidth()               
        Height= root.winfo_screenheight()               
        # root.geometry("%dx%d" % (Width, Height))

        # for maximize the window -------------------------
        root.state('zoomed') 


        Grid.rowconfigure(root, index=0, weight=1)
        Grid.columnconfigure(root, index=0, weight=1)

         # for complete full screen view --------------------
        # root.attributes('-fullscreen', True)
        self.root.title("Face Recogniton System")



        # Variables -------------------------------------------------
        self.dep = StringVar()
        self.batch = StringVar()
        self.sem = StringVar()
        self.roll = StringVar()
        self.name = StringVar()
        self.gender = StringVar()
        self.phone = StringVar()
        self.dob = StringVar()
        self.place = StringVar()
        self.search = StringVar()
        self.search_entry = StringVar()

        # bg image
        img3=Image.open(r"images\bgimg.jpg")

        img3=img3.resize((Width, Height), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(width=Width,height=Height)

        title_lbl=ctk.CTkLabel(root, text="STUDENT MANAGEMENT SYSTEM")
        title_lbl.configure(font=("Lato",25))
        title_lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

        # height and width of the main frame
        ht = 550
        wt = 1200

        # Main Frame
        main_frame = ctk.CTkFrame(root,
                               width=wt,
                               height=ht,
                               corner_radius=10)
        main_frame.place(relx=0.5, rely=0.55, anchor=CENTER)


        
        # left label frame
        Left_frame = ctk.CTkFrame(main_frame,
                               width=wt/2+50,
                               height=ht,
                               corner_radius=10)
        Left_frame.place(relx=0.55, rely=0.5, anchor=E)

        # current course information
        current_course_frame = ctk.CTkFrame(Left_frame,
                               width=wt/2+80,
                               height=100,
                               corner_radius=10)
        current_course_frame.place(relx=0.5, rely=0, anchor=N)

        # Department
        dep_label=ctk.CTkLabel(current_course_frame, text="Department*")
        dep_label.configure(font=("Lato",15))
        dep_label.place(relx=0.2, rely=0.2, anchor=NE)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.dep, font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "IT", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.place(relx=0.4, rely=0.2, anchor=N)

        # # Year
        year_label=ctk.CTkLabel(current_course_frame, text="Batch*")
        year_label.configure(font=("Lato",15))
        year_label.place(relx=0.7, rely=0.7, anchor=E)

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.batch, font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"]=("Select Batch", "2018","2019", "2020","2021")
        year_combo.current(0)
        year_combo.place(relx=0.8, rely=0.6, anchor=N)

        # #Semester
        semester_label=ctk.CTkLabel(current_course_frame, text="Semester*")
        semester_label.configure(font=("Lato",15))
        semester_label.place(relx=0.2, rely=0.7, anchor=E)

        semester_combo=ttk.Combobox(current_course_frame, textvariable=self.sem, font=("times new roman",12,"bold"), state="readonly")
        semester_combo["values"]=("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8")
        semester_combo.current(0)
        semester_combo.place(relx=0.35, rely=0.6, anchor=N)


        # # Class Student information
        class_Student_frame = ctk.CTkFrame(Left_frame,
                               width=wt/2+80,
                               height=450,
                               corner_radius=10)
        class_Student_frame.place(relx=0.5, rely=1, anchor=S)

        # # Roll No
        studentId_label=ctk.CTkLabel(class_Student_frame, text="Roll No.*: ")
        studentId_label.configure(font=("Lato",14))
        studentId_label.place(relx=0.2, rely=0.2, anchor=E)

        studentID_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.roll,
                               placeholder_text="Enter Roll No here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentID_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

        # # student name
        studenName_label=ctk.CTkLabel(class_Student_frame, text="Student Name*: ")
        studenName_label.configure(font=("Lato",14))
        studenName_label.place(relx=0.25, rely=0.35, anchor=E)

        studentName_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.name,
                               placeholder_text="Enter Name here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentName_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

        # # Address
        add_label=ctk.CTkLabel(class_Student_frame, text="Address*: ")
        add_label.configure(font=("Lato",14))
        add_label.place(relx=0.20, rely=0.5, anchor=E)

        add_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.place,
                               placeholder_text="Enter Address here",
                               width=450,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        add_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # # Gender
        gender_label=ctk.CTkLabel(class_Student_frame, text="Gender: ")
        gender_label.configure(font=("Lato",14))
        gender_label.place(relx=0.8, rely=0.35, anchor=E)

        gender_combo=ttk.Combobox(class_Student_frame, textvariable=self.gender, font=("times new roman",12,"bold"), state="readonly", width=10)
        gender_combo["values"]=("Select", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.place(relx=0.8, rely=0.35, anchor=W)

        # # DOB
        dob_label=ctk.CTkLabel(class_Student_frame, text="DOB: ")
        dob_label.configure(font=("Lato",14))
        dob_label.place(relx=0.20, rely=0.65, anchor=E)

        dob_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.dob,
                               placeholder_text="DD/MM/YYYY",
                               width=140,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        dob_entry.place(relx=0.3, rely=0.65, anchor=CENTER)
        

        # # Phone no
        phone_label=ctk.CTkLabel(class_Student_frame, text="Phone No: ")
        phone_label.configure(font=("Lato",14))
        phone_label.place(relx=0.65, rely=0.65, anchor=E)

        phone_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.phone,
                               placeholder_text="Enter Phone No here",
                               width=180,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        phone_entry.place(relx=0.8, rely=0.65, anchor=CENTER)

        # #buttons
        
        save_btn=ctk.CTkButton(class_Student_frame, command=self.add_data, text="Save", cursor="hand2")
        save_btn.place(relx=0.15, rely=0.85,width=160,height=60,  anchor=S)

        update_btn=ctk.CTkButton(class_Student_frame, command=self.update_data, text="Update", cursor="hand2")
        update_btn.place(relx=0.35, rely=0.85,width=160,height=60,  anchor=S)

        delete_btn=ctk.CTkButton(class_Student_frame, command=self.delete_data, text="Delete", cursor="hand2", fg_color="red", text_font=("bold"))
        delete_btn.place(relx=0.65, rely=0.85,width=160,height=60,  anchor=S)

        reset_btn=ctk.CTkButton(class_Student_frame, command=self.reset_data, text="Reset", cursor="hand2")
        reset_btn.place(relx=0.85, rely=0.85,width=160,height=60,  anchor=S)

        take_photo_btn=ctk.CTkButton(class_Student_frame, command=self.take_photo, text="Take Photo", cursor="hand2")
        take_photo_btn.place(relx=0.3, rely=0.98, width=300, height=60, anchor=S)

        update_photo_btn=ctk.CTkButton(class_Student_frame, command=self.take_photo, text="Update Photo", cursor="hand2")
        update_photo_btn.place(relx=0.7, rely=0.98, width=300, height=60, anchor=S)

        # # Right label frame
        Right_frame = ctk.CTkFrame(main_frame,
                               width=wt/2-75,
                               height=ht,
                               corner_radius=10)
        Right_frame.place(relx=0.56, rely=0.5, anchor=W)

        # # ===========================Search System=======================================================
        search_label=ctk.CTkLabel(Right_frame, text="Search By: ")
        search_label.configure(font=("Lato",14))
        search_label.place(relx=0.05, rely=0.1, anchor=W)

        search_combo=ttk.Combobox(Right_frame, textvariable=self.search, font=("times new roman",12,"bold"), state="readonly", width=10)
        search_combo["values"]=("Select", "Roll No","Department")
        search_combo.current(0)
        search_combo.place(relx=0.27, rely=0.1, anchor=W)

        search_entry = ctk.CTkEntry(Right_frame,
                               textvariable=self.search_entry,
                               placeholder_text="Enter here",
                               width=200,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        search_entry.place(relx=0.5, rely=0.1, anchor=W)

        search_btn=ctk.CTkButton(Right_frame, command=self.search_data, text="Search", cursor="hand2")
        search_btn.place(relx=0.6, rely=0.2,width=180,height=60,  anchor=W)


        # # # ===========================Table Frame=======================================================
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(relx=0.5, rely=0.9,width=wt/2,height=ht-100, anchor=S)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("dep","batch","sem","roll","name","gender","phone","dob","place"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading ("name", text="Name")
        self.student_table.heading ("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading ("place", text="Address")
        # self.student_table.heading("photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=95)
        self.student_table.column("batch", width=90)
        self.student_table.column("sem", width=80)
        self.student_table.column("roll", width=35)
        self.student_table.column("name", width=150)
        self.student_table.column("gender", width=65)
        self.student_table.column("phone", width=90)
        self.student_table.column("dob", width=90)
        self.student_table.column("place", width=150)
        # self.student_table.column("photo", width=60)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        # # Exit button        
        b6_1=ctk.CTkButton(Right_frame,text="Exit", cursor="hand2", command = root.destroy, fg_color="red", text_font=("Verdana",13,"bold"))
        b6_1.place(relx=0.8, rely=0.95,width=200,height=60,  anchor=CENTER)

    # -----------------function works-----------------------------------------------------------------------
    def add_data(self):
        var_name=self.name.get()
        var_roll=self.roll.get()

        var_dob=self.dob.get()
        try:
            provide=datetime.strptime(var_dob,"%d/%m/%Y")
            res=False
            present=datetime.now()
            if(provide.date() > present.date()):
                res=True
        except Exception:
            res=True
        
        var_ph=self.phone.get()
        Pattern = re.compile("[6-9][0-9]{9}")

        if self.dep.get()=="Select Department" or self.batch.get()=="Select Batch" or self.sem.get()=="Select Semester" or var_roll=="" or self.place.get()=="" or var_name=="" or self.gender.get()=="Select" or var_ph=="" or var_dob=="" :
            messagebox.showerror("Error", "All (*) fields are required!", parent=self.root)
        elif any(ch.isdigit() for ch in var_name):
            messagebox.showerror("Error","Name can\'t have numbers", parent=self.root)
        elif any(ch.isalpha() for ch in var_roll):
            messagebox.showerror("Error","Please Provide Valid Roll No", parent=self.root)
        elif(res):
            messagebox.showerror("Error","Please provide correcet Date Formate",parent=self.root)
        elif not (Pattern.match(var_ph)):
            messagebox.showerror("Error","Please provide correcet Phone Number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.dep.get(),
                                                                                            self.batch.get(),
                                                                                            self.sem.get(),
                                                                                            var_roll,
                                                                                            var_name,
                                                                                            self.gender.get(),
                                                                                            var_ph,
                                                                                            var_dob,
                                                                                            self.place.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","The Student Data has saved", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)

    # ===============fetch Data====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    # ===============get cursor==================

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.dep.set(data[0]),
        self.batch.set(data[1]),
        self.sem.set(data[2]),
        self.roll.set(data[3]),
        self.name.set(data[4]),
        self.gender.set(data[5]),
        self.phone.set(data[6]),
        self.dob.set(data[7]),
        self.place.set(data[8])

        self.var_rol=self.roll.get()
    
    # ============update function================
    def update_data(self):
        var_name=self.name.get()

        var_dob=self.dob.get()
        try:
            provide=datetime.strptime(var_dob,"%d/%m/%Y")
            res=False
            present=datetime.now()
            if(provide.date() > present.date()):
                res=True
        except Exception:
            res=True
        
        var_ph=self.phone.get()
        Pattern = re.compile("[6-9][0-9]{9}")

        if self.dep.get()=="Select Department" or self.batch.get()=="Select Batch" or self.sem.get()=="Select Semester" or self.roll.get()=="" or self.place.get()=="" or var_name=="" or self.gender.get()=="Select" or var_ph=="" or var_dob=="" :
            messagebox.showerror("Error", "All (*) fields are required!", parent=self.root)
        elif self.roll.get()!=self.var_rol:
            messagebox.showerror("Error", "Roll No can't be changed", parent=self.root)
        elif any(ch.isdigit() for ch in var_name):
            messagebox.showerror("Error","Name can\'t have numbers", parent=self.root)
        elif(res):
            messagebox.showerror("Error","Please provide correcet Date Formate",parent=self.root)
        elif not (Pattern.match(var_ph)):
            messagebox.showerror("Error","Please provide correcet Phone Number",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dept=%s,batch=%s,sem=%s,name=%s,gender=%s,phone=%s,dob=%s,place=%s where roll=%s",(
                                                                                                                                        self.dep.get(),
                                                                                                                                        self.batch.get(),
                                                                                                                                        self.sem.get(),
                                                                                                                                        self.name.get(),
                                                                                                                                        self.gender.get(),
                                                                                                                                        self.phone.get(),
                                                                                                                                        self.dob.get(),
                                                                                                                                        self.place.get(),
                                                                                                                                        self.roll.get()

                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Students Details successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)
    

    # ============Delete function================
    def delete_data(self):
        if self.roll.get()=="":
            messagebox.showerror("Error","Student ID must be required!", parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete the details of this student", parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where roll=%s"
                    val=(self.roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Deletion Successful.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

    # ============Reset function================
    def reset_data(self):
        self.dep.set("Select Department")
        self.batch.set("Select Batch")
        self.sem.set("Select Semester")
        self.roll.set("")
        self.name.set("")
        self.gender.set("Select Gender")
        self.phone.set("")
        self.dob.set("")
        self.place.set("")
        
        messagebox.showinfo("Reset", "Reset successful")
    

    # =============Take Sample Photos====================
    def take_photo(self):
        var_name=self.name.get()

        var_dob=self.dob.get()
        try:
            provide=datetime.strptime(var_dob,"%d/%m/%Y")
            res=False
            present=datetime.now()
            if(provide.date() > present.date()):
                res=True
        except Exception:
            res=True
        
        var_ph=self.phone.get()
        Pattern = re.compile("[6-9][0-9]{9}")

        if self.dep.get()=="Select Department" or self.batch.get()=="Select Batch" or self.sem.get()=="Select Semester" or self.roll.get()=="" or self.place.get()=="" or var_name=="" or self.gender.get()=="Select" or var_ph=="" or var_dob=="" :
            messagebox.showerror("Error", "All (*) fields are required!", parent=self.root)
        elif self.roll.get()!=self.var_rol:
            messagebox.showerror("Error", "Roll No can't be changed", parent=self.root)
        elif any(ch.isdigit() for ch in var_name):
            messagebox.showerror("Error","Name can\'t have numbers", parent=self.root)
        elif(res):
            messagebox.showerror("Error","Please provide correcet Date Formate",parent=self.root)
        elif not (Pattern.match(var_ph)):
            messagebox.showerror("Error","Please provide correcet Phone Number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                mydata=my_cursor.fetchall()
                c=self.roll.get()
                my_cursor.execute("update student set dept=%s,batch=%s,sem=%s,name=%s,gender=%s,phone=%s,dob=%s,place=%s where roll=%s",(
                                                                                                                                        self.dep.get(),
                                                                                                                                        self.batch.get(),
                                                                                                                                        self.sem.get(),
                                                                                                                                        self.name.get(),
                                                                                                                                        self.gender.get(),
                                                                                                                                        self.phone.get(),
                                                                                                                                        self.dob.get(),
                                                                                                                                        self.place.get(),
                                                                                                                                        self.roll.get()

                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)      #scaling factor=1.3    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                count=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        count += 1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(c)+"."+str(count)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    else:
                        messagebox.showerror("Error","You are not visible properly!!!", parent=self.root)
                    
                    if cv2.waitKey(1)==13 or int(count)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)
    
    # ================Function for Search Button=================
    def search_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
        my_cursor=conn.cursor()
        if(self.search.get()=="Roll No"):
            sql="select * from student where roll=%s"
            val=(self.search_entry.get(),)
        elif(self.search.get()=="Department"):
            sql="select * from student where dept=%s"
            val=(self.search_entry.get(),)
        my_cursor.execute(sql,val)
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        else:
            messagebox.showwarning("Warning","Data not found!!!",parent=self.root)
        conn.close()


if __name__ == "__main__":
    root=ctk.CTk()
    obj=Student(root)
    root.mainloop()