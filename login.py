from email import message
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

from matplotlib.pyplot import title

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #==============================
        self.bg=ImageTk.PhotoImage(file="Images/2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #==============================
        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)


        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#144273",bg="White").place(x=90,y=30);
        desc = Label(Frame_login,text="Swaasth Siddhi",font=("Goudy old Style",15,"bold"),fg="#144273",bg="White").place(x=90,y=100);

        lbl_user = Label(Frame_login,text="Username",font=("Goudy old Style",15,"bold"),fg="gray",bg="White").place(x=90,y=140);
        self.txt_user = Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_user = Label(Frame_login,text="Password",font=("Goudy old Style",15,"bold"),fg="gray",bg="White").place(x=90,y=210);
        self.txt_pass = Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn = Button(Frame_login,text="Forget Password?",bg="white",fg="#144273",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn = Button(self.root,command=self.login_function,text="Login",fg="white",bg="#144273",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="watson":
            messagebox.showerror("Error!", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Successfully Login", f"Welcome {self.txt_user.get()}", parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()
        