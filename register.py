from tkinter import*
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")

class Register:
    def __init__(self, root_login):
        self.root_login = root_login

        # code for full screen height and width --------------------
        width= root_login.winfo_screenwidth()               
        height= root_login.winfo_screenheight()               
        # root_login.geometry("%dx%d" % (width, height))
        # for maximize the window ---------------------------
        root_login.state('zoomed') 

        self.root_login.title("Login")

        # variables ----------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # bg image
        img3=Image.open(r"images\bgimg.jpg")

        img3=img3.resize((width, height), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root_login, image=self.photoimg3)
        bg_img.place(width=width,height=height)

        # #left image
        # self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\nepal.jpg")#photo ka dekh lena yaha
        # left_lbl = Label(self.root_login,image=self.bg1)
        # left_lbl.place(x=50,y=100,width=470,height=550)

        # main frame
        frame=Frame(self.root_login,bg="black")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="cyan",bg="black")
        register_lbl.place(relx=0.5, rely=0.1, anchor=CENTER,)

        # =============label and entry===============================
        #row1
        fname = Label(frame,text="First Name", font=("times new roman", 15, "bold"), fg="white",bg="black")
        fname.place(relx=0.15, rely=0.2, anchor=CENTER)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(relx=0.25, rely=0.25, anchor=CENTER, width=250)

        l_name = Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        l_name.place(relx=0.7, rely=0.2, anchor=CENTER)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15)) #yaha confusion h lname me check kr lena
        self.txt_lname.place(relx=0.8, rely=0.25, anchor=CENTER, width=250)


        #row2
        contact = Label(frame,text="Contact No",font=("times new roman", 15, "bold"), fg="white",bg="black")
        contact.place(relx=0.15, rely=0.35, anchor=CENTER)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(relx=0.25, rely=0.4, anchor=CENTER, width=250)

        email= Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        email.place(relx=0.68, rely=0.35, anchor=CENTER)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))  
        self.txt_email.place(relx=0.8, rely=0.4, anchor=CENTER, width=250)


        #row3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="white",bg="black")
        security_Q.place(relx=0.23, rely=0.5, anchor=CENTER)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth place", "Your Dad's name", "Your Mom's name")
        self.combo_security_Q.place(relx=0.25, rely=0.55, anchor=CENTER, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="white",bg="black")
        security_A.place(relx=0.73, rely=0.5, anchor=CENTER)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15))
        self.txt_security.place(relx=0.8, rely=0.55, anchor=CENTER, width=250)


        #row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        pswd.place(relx=0.15, rely=0.65, anchor=CENTER)

        self.txt_pswd= ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15))
        self.txt_pswd.place(relx=0.25, rely=0.7, anchor=CENTER, width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        confirm_pswd.place(relx=0.74, rely=0.65, anchor=CENTER)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 15))
        self.txt_confirm_pswd.place(relx=0.8, rely=0.7, anchor=CENTER, width=250)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I am Agreed with the terms and conditions", font=("times new roman", 8, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(relx=0.5, rely=0.76,anchor=CENTER)

        #buttons
        img = Image.open(r"images\register.jpg")
        img = img.resize((200, 55), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,command=self.register_data,image=self.photoimage, borderwidth=0, cursor="hand2",font=("times new roman", 15, "bold"), bg="black")
        b1.place(relx=0.3, rely=0.85, anchor=CENTER)


        img1 = Image.open(r"images\login_now.jpg")
        img1 = img1.resize((200, 45), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2",font=("times new roman", 15, "bold"), bg="black")
        b1.place(relx=0.7, rely=0.85, anchor=CENTER)


    # ...............function...................
    def register_data(self):
        var_ph=self.var_contact.get()
        Pattern = re.compile("[6-9][0-9]{9}")
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error","All fills are required",parent=self.root_login)
        elif any(ch.isdigit() for ch in self.var_fname.get()) or any(ch.isdigit() for ch in self.var_lname.get()):
            messagebox.showerror("Error","Name can\'t have numbers",parent=self.root_login)
        elif not (Pattern.match(var_ph)):
            messagebox.showerror("Error","Please provide correcet Phone Number",parent=self.root_login)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm password must be same",parent=self.root_login)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root_login)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","User already exist, try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root_login.destroy()


if __name__ == "__main__":
    root_login=ctk.CTk()
    app=Register(root_login)
    root_login.mainloop()