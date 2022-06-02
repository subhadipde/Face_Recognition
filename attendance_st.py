from tkinter import*
from tkinter import ttk
import customtkinter as ctk
from PIL import Image ,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

# custom tkinter setting
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

mydata=[]
class Attendance_st:
    def __init__(self, root):
        self.root=root

        # code for full screen height and width ----------------------------
        Width= root.winfo_screenwidth()               
        Height= root.winfo_screenheight()

        # for maximize the window -------------------------
        root.state('zoomed') 

        Grid.rowconfigure(root, index=0, weight=1)
        Grid.columnconfigure(root, index=0, weight=1)

        self.root.title("Face Recogniton System")

        # Variables -------------------------------------------------
        self.roll = StringVar()
        self.name = StringVar()
        self.dept = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.status = StringVar()
     
        # bg image
        img3=Image.open(r"images\bgimg.jpg")
        img3=img3.resize((Width, Height), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(width=Width,height=Height)

        title_lbl=ctk.CTkLabel(root, text="Attendance Check System")
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

        # # Attendance information
        left_inside_frame = ctk.CTkFrame(Left_frame,
                               width=wt/2+80,
                               height=550,
                               corner_radius=10)
        left_inside_frame.place(relx=0.5, rely=1, anchor=S)

        # Labeland entry
        # # Roll No
        studentId_label=ctk.CTkLabel(left_inside_frame, text="Roll No.: ")
        studentId_label.configure(font=("Lato",14))
        studentId_label.place(relx=0.2, rely=0.2, anchor=E)

        studentID_entry = ctk.CTkEntry(left_inside_frame,
                                textvariable=self.roll,
                                width=220,
                                height=40,
                                border_width=1,
                                corner_radius=10)
        studentID_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

        # # student name
        studenName_label=ctk.CTkLabel(left_inside_frame, text="Student Name: ")
        studenName_label.configure(font=("Lato",14))
        studenName_label.place(relx=0.25, rely=0.35, anchor=E)

        studentName_entry = ctk.CTkEntry(left_inside_frame,
                                textvariable=self.name,
                                width=220,
                                height=40,
                                border_width=1,
                                corner_radius=10)
        studentName_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

        # # Department
        dep_label=ctk.CTkLabel(left_inside_frame, text="Department: ")
        dep_label.configure(font=("Lato",14))
        dep_label.place(relx=0.8, rely=0.35, anchor=E)

        dep_combo=ttk.Combobox(left_inside_frame, textvariable=self.dept, font=("times new roman",12,"bold"), state="readonly", width=10)
        dep_combo["values"]=("Department", "CSE", "IT", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.place(relx=0.8, rely=0.35, anchor=W)

        # # Attendance Status
        att_label=ctk.CTkLabel(left_inside_frame, text="Attendance Status: ")
        att_label.configure(font=("Lato",14))
        att_label.place(relx=0.3, rely=0.5, anchor=E)

        att_combo=ttk.Combobox(left_inside_frame, textvariable=self.status, font=("times new roman",12,"bold"), state="readonly", width=10)
        att_combo["values"]=("Status", "Present", "Absent")
        att_combo.current(0)
        att_combo.place(relx=0.4, rely=0.5, anchor=CENTER)

        # # Date
        date_label=ctk.CTkLabel(left_inside_frame, text="Date: ")
        date_label.configure(font=("Lato",14))
        date_label.place(relx=0.20, rely=0.65, anchor=E)

        date_entry = ctk.CTkEntry(left_inside_frame,
                                textvariable=self.date,
                                width=140,
                                height=40,
                                border_width=1,
                                corner_radius=10)
        date_entry.place(relx=0.3, rely=0.65, anchor=CENTER)

        # # Time
        time_label=ctk.CTkLabel(left_inside_frame, text="Time: ")
        time_label.configure(font=("Lato",14))
        time_label.place(relx=0.65, rely=0.65, anchor=E)

        time_entry = ctk.CTkEntry(left_inside_frame,
                                textvariable=self.time,
                                width=180,
                                height=40,
                                border_width=1,
                                corner_radius=10)
        time_entry.place(relx=0.8, rely=0.65, anchor=CENTER)

        # #buttons
        
        # import_btn=ctk.CTkButton(left_inside_frame, command=self.importCsv, text="Import CSV", cursor="hand2")
        # import_btn.place(relx=0.3, rely=0.90, width=300, height=60, anchor=S)

        export_btn=ctk.CTkButton(left_inside_frame, command=self.exportCsv, text="Export CSV", cursor="hand2")
        export_btn.place(relx=0.7, rely=0.90, width=300, height=60, anchor=S)

        # # Right label frame
        Right_frame = ctk.CTkFrame(main_frame,
                               width=wt/2-75,
                               height=ht,
                               corner_radius=10)
        Right_frame.place(relx=0.56, rely=0.5, anchor=W)

        # # # ===========================Table Frame=======================================================
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(relx=0.5, rely=0.9,width=wt/2,height=ht-100,  anchor=S)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame, columns=("roll","name","dept","date","time","status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("dept", text="Department")
        self.AttendaceReportTable.heading("time", text="Time") 
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("status", text="Attendance")

        self.AttendaceReportTable["show"]="headings"

        self.AttendaceReportTable.column("roll",width=45)
        self.AttendaceReportTable.column("name",width=150)
        self.AttendaceReportTable.column("dept",width=95)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("status",width=110)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # # Exit button        
        exit_btn=ctk.CTkButton(Right_frame,text="Exit",cursor="hand2",command=root.destroy,fg_color="red",text_font=("Verdana",13,"bold"))
        exit_btn.place(relx=0.8, rely=0.95,width=200,height=60,  anchor=CENTER)

        self.first_fetch()

    # fetch data
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
    
    # # import csv
    # def importCsv(self):    
    #     global mydata
    #     mydata.clear()
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchData(mydata)
    
    # ======First fetching==============
    def first_fetch(self):
        global mydata
        mydata.clear()
        with open('attendance.csv','r') as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # Export CSV
    def exportCsv(self):    
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been Exported to"+os.path.basename(fln)+"Successfully")    
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.roll.set(rows[0])
        self.name.set(rows[1])
        self.dept.set(rows[2])
        self.time.set(rows[3])
        self.date.set(rows[4])
        self.status.set(rows[5])


if __name__ == "__main__":
    root=ctk.CTk()
    obj=Attendance_st(root)
    root.mainloop()