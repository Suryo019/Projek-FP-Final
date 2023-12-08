import tkinter as tk
import csv
import signin
import loading
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox


def signupw():
    signup_w = tk.Tk()
    signup_w.title("Pariwi Data (Sign Up)")
    signup_w.configure(bg="#fff")
    signup_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = signup_w.winfo_screenwidth()
    screen_height = signup_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    signup_w.geometry("%dx%d+%d+%d" %
                      (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(signup_w, image=img, bg="white").place(x=0, y=0)
    img_icon = PhotoImage(
        file="travel.png")


    # Dekorasi
    kotak_biru = Frame(signup_w, width=342, height=432, bg="#2666FA").place(x=58, y=84)
    kotak_putih = Frame(signup_w, width=342, height=432, bg="white").place(x=400, y=84)

    dekorasi = PhotoImage(
        file="3.png")
    Label(signup_w, image=dekorasi, bg="#2666FA").place(x=84, y=98)


    # Judul dan Sub Judul
    judul = Label(signup_w, text="Hello! Welcome.", fg="black",
                  bg="white", font=("Inter", 18, "bold")).place(x=457, y=182)
    sub_judul = Label(signup_w, text="Log in with your account.",
                      fg="#646464", bg="white", font=("Inter", 8)).place(x=457, y=212.07)


# Fungsi - fungsi
    def on_enter_u(e):
        username_box.delete(0, "end")

    def on_leave_u(e):
        nama = username_box.get()
        if nama == "":
            username_box.insert(0, "Enter your username")

    def on_enter_p(e):
        password_box.delete(0, "end")
        password_box.config(show="*")

    def on_leave_p(e):
        nama = password_box.get()
        if nama == "":
            password_box.insert(0, "Enter your password")
            password_box.config(show="")

    def on_enter_cp(e):
        confirm_password_box.delete(0, "end")
        confirm_password_box.config(show="*")

    def on_leave_cp(e):
        nama = confirm_password_box.get()
        if nama == "":
            confirm_password_box.insert(0, "Confirm your password")
            confirm_password_box.config(show="")

    def show_pass_box():
        if show_pass_var.get():
            password_box.config(show="")
            confirm_password_box.config(show="")
        else:
            password_box.config(show="*")
            confirm_password_box.config(show="*")

    def cek_username(username, reader):
        try:
            row = next(reader)
            if username == row['username']:
                mbox.showerror("Invalid", "Username already exists!")
                return True
            return cek_username(username, reader)
        except StopIteration:
            return False

    def fungsi_sign_up():
        username = username_box.get()
        password = password_box.get()
        confirm_password = confirm_password_box.get()

        if password != confirm_password:
            mbox.showerror(
                "Invalid", "Password and Confirm Password do not match!")
            return

        with open('user_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            if cek_username(username, reader):
                return

        with open('user_data.csv', mode='a', newline='') as file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow({'username': username, 'password': password})
            mbox.showinfo("Successful", "Successfully Sign Up")

        signup_w.destroy()
        loading.loadingw()

    def fungsi_sign_in():
        signup_w.destroy()
        signin.signinw()


    # Textbox
    username_text = Label(signup_w, text="Username", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=233)

    username_box = Entry(signup_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    username_box.place(x=452, y=248.04)
    username_box.insert(0, "Enter your username")

    username_box.bind("<FocusIn>", on_enter_u)
    username_box.bind("<FocusOut>", on_leave_u)


    password_text = Label(signup_w, text="Password", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=279)

    password_box = Entry(signup_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    password_box.place(x=452, y=295.04)
    password_box.insert(0, "Enter your password")

    password_box.bind("<FocusIn>", on_enter_p)
    password_box.bind("<FocusOut>", on_leave_p)


    confirm_password_text = Label(signup_w, text="Confirm Password", fg="black",
                                  bg="white", font=("Inter", 8, "bold")).place(x=457, y=326.33)

    confirm_password_box = Entry(signup_w, width=40, fg="black", border=1,
                                 bg="white", font=("Inter", 8))
    confirm_password_box.place(x=452, y=342.37)
    confirm_password_box.insert(0, "Confirm your password")

    confirm_password_box.bind("<FocusIn>", on_enter_cp)
    confirm_password_box.bind("<FocusOut>", on_leave_cp)


    # Tombol signup
    sign_up = Button(signup_w, width=33, pady=3, text="Sign Up",
                     bg="#2666FA", fg="white", border=1, command=fungsi_sign_up).place(x=453, y=407.78)


    # Punya akun
    have_account = Button(signup_w, width=13, text="Have account?",
                          bg="white", fg="#2666FA", border=0, cursor="hand2", 
                          command=fungsi_sign_in).place(x=598, y=370.44)


    # Style
    style = ttk.Style()
    style.configure('TCheckbutton', background='white')


    # Show password
    show_pass_var = tk.BooleanVar()
    show_pass = ttk.Checkbutton(
        signup_w, text="Show password", style="TCheckbutton", 
        variable=show_pass_var, command=show_pass_box).place(x=452, y=370.44)


    signup_w.iconphoto(False, img_icon)
    signup_w.mainloop()


# signupw()
