import tkinter as tk
import signup
import forgotpass
import loading
import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox


def signinw():
    signin_w = tk.Tk()
    signin_w.title("Pariwi Data (Sign In)")
    signin_w.configure(bg="#fff")
    signin_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = signin_w.winfo_screenwidth()
    screen_height = signin_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    signin_w.geometry("%dx%d+%d+%d" %
                      (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(signin_w, image=img, bg="white").place(x=0, y=0)
    img_icon = PhotoImage(
        file="travel.png")


    # Dekorasi
    kotak_biru = Frame(signin_w, width=342, height=432, bg="#2666FA").place(x=58, y=84)
    kotak_putih = Frame(signin_w, width=342, height=432, bg="white").place(x=400, y=84)

    dekorasi = PhotoImage(
        file="3.png")
    Label(signin_w, image=dekorasi, bg="#2666FA").place(x=84, y=98)


    # Judul dan Sub Judul
    judul = Label(signin_w, text="Hello! Welcome.", fg="black",
                  bg="white", font=("Inter", 18, "bold")).place(x=457, y=182)
    sub_judul = Label(signin_w, text="Log in with your account.",
                      fg="#646464", bg="white", font=("Inter", 8)).place(x=457, y=212.07)


    # Fungsi - fungsi
    def on_enter_u(e):
        username_box.delete(0, "end")

    def on_leave_u(e):
        nama = username_box.get()
        username_box.insert(0, "Enter your username") if nama == "" else None

    def on_enter_p(e):
        password_box.delete(0, "end")
        password_box.config(show="*")

    def on_leave_p(e):
        nama = password_box.get()
        password_box.insert(0, "Enter your password") if nama == "" else None
        password_box.config(show="")

    def show_pass_box():
        password_box.config(show="") if show_pass_var.get() else password_box.config(show="*")


    def signin_rekursif(username, password, reader):
        try:
            row = next(reader)
            if username == row['username'] and password == row['password']:
                mbox.showinfo("Success", "Login Successful!")
                return True
            else:
                return signin_rekursif(username, password, reader)
        except StopIteration:
            mbox.showerror("Invalid", "Username or Password Incorrect!")
            return False

    def fungsi_sign_in():
        username = username_box.get()
        password = password_box.get()

        login_successful = signin_rekursif(username, password, 
                csv.DictReader(open('user_data.csv', mode='r'))) if username and password else False

        if login_successful:
            signin_w.destroy()
            loading.loadingw()

    def fungsi_sign_up():
        signin_w.destroy()
        signup.signupw()

    def fungsi_forgot_pass():
        signin_w.destroy()
        forgotpass.newpassw()


    # Textbox
    username_text = Label(signin_w, text="Username", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=253)

    username_box = Entry(signin_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    username_box.place(x=452, y=269.04)
    username_box.insert(0, "Enter your username")

    username_box.bind("<FocusIn>", on_enter_u)
    username_box.bind("<FocusOut>", on_leave_u)


    password_text = Label(signin_w, text="Password", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=303.12)

    password_box = Entry(signin_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    password_box.place(x=452, y=319.15)
    password_box.insert(0, "Enter your password")

    password_box.bind("<FocusIn>", on_enter_p)
    password_box.bind("<FocusOut>", on_leave_p)


    # Tombol signin
    sign_in = Button(signin_w, width=33, pady=3, text="Sign In",
                     bg="#2666FA", fg="white", border=0, 
                     command=fungsi_sign_in).place(x=453, y=373.28)

    sign_up = Button(signin_w, width=33, pady=3, text="Sign Up",
                     bg="white", fg="#2666FA", border=1, 
                     command=fungsi_sign_up).place(x=453, y=407.78)


    # Lupa password
    forgot_pass = Button(signin_w, width=13, text="Forgot password?",
                         bg="white", fg="#2666FA", border=0, cursor="hand2", 
                         command=fungsi_forgot_pass).place(x=603, y=346.78)


    # Style
    style = ttk.Style()
    style.configure('TCheckbutton', background='white')


    # Show password
    show_pass_var = tk.BooleanVar()
    show_pass = ttk.Checkbutton(
        signin_w, text="Show password", style="TCheckbutton", variable=show_pass_var, 
        command=show_pass_box).place(x=452, y=346.78)


    signin_w.iconphoto(False, img_icon)
    signin_w.mainloop()


def main():
    signinw()


if __name__ == "__main__":
    main()
