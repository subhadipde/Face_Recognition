from tkinter import*
from colorama import Cursor
import customtkinter as ctk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from face_recog_st import Face_Recognition_System_st
from register import Register
import mysql.connector
from face_recog import Face_Recognition_System
from face_recog_st import Face_Recognition_System_st

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def main():
    win=ctk.CTk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root_login):
        self.root_login = root_login

        # code for full screen height and width --------------------
        width= root_login.winfo_screenwidth()               
        height= root_login.winfo_screenheight()               
        # root_login.geometry("%dx%d" % (width, height))
        # for maximize the window ---------------------------
        root_login.state('zoomed') 

        self.root_login.title("Login")

        # bg image
        img3=Image.open(r"images\bgimg.jpg")

        img3=img3.resize((width, height), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root_login, image=self.photoimg3)
        bg_img.place(width=width,height=height)

        frame = ctk.CTkFrame(self.root_login, corner_radius=10)
        frame.configure(fg_color="black")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER,width=540,height=750)

        img1 = Image.open(r"images\login.png")
        img1 = img1.resize((300,300),Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(image=self.photoimage1,bg="black", borderwidth=0)
        lblimg1.place(relx=0.5, rely=0.2, anchor=CENTER, width=300, height=90)

        get_str = ctk.CTkLabel(frame,text="Get Started")
        get_str.configure(font=("times new roman",20,"bold"),fg="white")
        get_str.place(relx=0.5, rely=0.25, anchor=CENTER)

        # ============ labels ====================

        #  username lebel =======
        username_lbl = ctk.CTkLabel(frame,text="Username")
        username_lbl.configure(font=("times new roman",20,"bold"),fg="white")
        username_lbl.place(relx=0.3, rely=0.35, anchor=CENTER)


        # Username ICON =========
        img2 = Image.open(r"images\user.jpg")
        img2 = img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(frame,image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(relx=0.5, rely=0.35, anchor=CENTER)

        # Username entry =========
        self.txtuser = ctk.CTkEntry(frame,width=250)
        self.txtuser.place(relx=0.5, rely=0.43, anchor=CENTER)


        # password lebel =========
        password_lbl = ctk.CTkLabel(frame,text="Password")
        password_lbl.configure(font=("times new roman",20,"bold"),fg="white")
        password_lbl.place(relx=0.3, rely=0.51, anchor=CENTER)

        # password ICON =========
        img3 = Image.open(r"images\password.jpg")
        img3 = img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(frame,image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(relx=0.5, rely=0.51, anchor=CENTER)

        # password entry =========
        self.txtpass = ctk.CTkEntry(frame,show="*",width=250)
        self.txtpass.place(relx=0.5, rely=0.59, anchor=CENTER)

        # loginBuutton
        loginbtn = ctk.CTkButton(frame,command=self.login,text="Login",text_font=("Verdana",18),cursor="hand2",fg_color="red")
        loginbtn.place(relx=0.5, rely=0.7, anchor=CENTER, width=180, height=55)

        # registrationButton
        registerbtn = ctk.CTkButton(frame,text="New User Register",cursor="hand2",command=self.register_window,text_font=("Verdana",8))
        registerbtn.place(relx=0.2, rely=0.85, anchor=CENTER)

        # forgetpasswordButton
        forgetbtn = ctk.CTkButton(frame,text="Forget Password",cursor="hand2",command=self.register_window,text_font=("Verdana",8))
        forgetbtn.place(relx=0.2, rely=0.92, anchor=CENTER)


    def register_window(self):
        self.new_window=Toplevel(self.root_login)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
            open_main=messagebox.askyesno("YesNo","Acess only Admin")
            if open_main>0:
                self.new_window=Toplevel(self.root_login)
                self.app=Face_Recognition_System(self.new_window)
            else:
                if not open_main:
                    return
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only Student")
                if open_main>0:
                    self.new_window=Toplevel(self.root_login)
                    self.app=Face_Recognition_System_st(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #===============reset password======================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","Provide your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid security answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()

    #============forgot password window=========================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the Username to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman", 20, "bold"),bg="white", fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)


if __name__ == "__main__":
    main()