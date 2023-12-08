import tkinter as tk
import csv
import loading
import signin
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox


def newpassw():
    newpass_w = tk.Tk()
    newpass_w.title("Pariwi Data (Forgot Pass)")
    newpass_w.configure(bg="#fff")
    newpass_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = newpass_w.winfo_screenwidth()
    screen_height = newpass_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    newpass_w.geometry("%dx%d+%d+%d" %
                       (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(newpass_w, image=img, bg="white").place(x=0, y=0)
    img_icon = PhotoImage(
            file="travel.png")


    # Dekorasi
    kotak_biru = Frame(newpass_w, width=342, height=432, bg="#2666FA").place(x=58, y=84)
    kotak_putih = Frame(newpass_w, width=342, height=432, bg="white").place(x=400, y=84)

    dekorasi = PhotoImage(
        file="3.png")
    Label(newpass_w, image=dekorasi, bg="#2666FA").place(x=84, y=98)


    # Judul dan Sub Judul
    judul = Label(newpass_w, text="Hello! Welcome.", fg="black",
                  bg="white", font=("Inter", 18, "bold")).place(x=457, y=182)
    sub_judul = Label(newpass_w, text="Let's create your new password.",
                      fg="#646464", bg="white", font=("Inter", 8)).place(x=457, y=212.07)


    # Fungsi - fungsi
    def on_enter_u(e):
        username_box.delete(0, "end")

    def on_leave_u(e):
        nama = username_box.get()
        if nama == "":
            username_box.insert(0, "Enter your username")

    def on_enter_np(e):
        newpass_box.delete(0, "end")
        newpass_box.config(show="*")

    def on_leave_np(e):
        nama = newpass_box.get()
        if nama == "":
            newpass_box.insert(0, "Create new password")
            newpass_box.config(show="")

    def on_enter_cp(e):
        confpass_box.delete(0, "end")
        confpass_box.config(show="*")

    def on_leave_cp(e):
        nama = confpass_box.get()
        if nama == "":
            confpass_box.insert(0, "Confirm password")
            confpass_box.config(show="")

    def show_pass_box():
        if show_pass_var.get():
            newpass_box.config(show="")
            confpass_box.config(show="")
        else:
            newpass_box.config(show="*")
            confpass_box.config(show="*")

    def update_pass(rows, username, newpass, found=False):
        if not rows:
            return rows, found

        row = rows[0]
        if username == row['username']:
            found = True
            row['password'] = newpass

        updated_rows, updated_found = update_pass(rows[1:], username, newpass, found)
        return [row] + updated_rows, updated_found

    def fungsi_newpass():
        username = username_box.get()
        newpass = newpass_box.get()
        confpass = confpass_box.get()

        if newpass != confpass:
            mbox.showerror("Invalid", "Password and Confirm Password do not match!")
            return

        with open('user_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        updated_rows, found = update_pass(rows, username, newpass)

        if not found:
            mbox.showerror("Invalid", "Username Incorrect!")
            return

        with open('user_data.csv', mode='w', newline='') as file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)
            mbox.showinfo("Successful", "Password updated successfully")

        newpass_w.destroy()
        loading.loadingw()

    def fungsi_remember_pass():
        newpass_w.destroy()
        signin.signinw()


    # Textbox
    username_text = Label(newpass_w, text="Username", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=233)

    username_box = Entry(newpass_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    username_box.place(x=452, y=248.04)
    username_box.insert(0, "Enter your username")

    username_box.bind("<FocusIn>", on_enter_u)
    username_box.bind("<FocusOut>", on_leave_u)


    newpass_text = Label(newpass_w, text="New Password", fg="black",
                         bg="white", font=("Inter", 8, "bold")).place(x=457, y=279)

    newpass_box = Entry(newpass_w, width=40, fg="black", border=1,
                        bg="white", font=("Inter", 8))
    newpass_box.place(x=452, y=295.04)
    newpass_box.insert(0, "Create new password")

    newpass_box.bind("<FocusIn>", on_enter_np)
    newpass_box.bind("<FocusOut>", on_leave_np)


    confpass_text = Label(newpass_w, text="Confirm Password", fg="black",
                          bg="white", font=("Inter", 8, "bold")).place(x=457, y=326.33)

    confpass_box = Entry(newpass_w, width=40, fg="black", border=1,
                         bg="white", font=("Inter", 8))
    confpass_box.place(x=452, y=342.37)
    confpass_box.insert(0, "Confirm password")

    confpass_box.bind("<FocusIn>", on_enter_cp)
    confpass_box.bind("<FocusOut>", on_leave_cp)


    # Tombol confirm
    confirm = Button(newpass_w, width=33, pady=3, text="Confirm",
                     bg="#2666FA", fg="white", border=0, 
                     command=fungsi_newpass).place(x=453, y=407.78)


    # Ingat password
    remember_pass = Button(newpass_w, width=13, text="Remember Pass?",
                         bg="white", fg="#2666FA", border=0, cursor="hand2", 
                         command=fungsi_remember_pass).place(x=603, y=370.44)


    # Style
    style = ttk.Style()
    style.configure('TCheckbutton', background='white')


    # Show password
    show_pass_var = tk.BooleanVar()
    show_pass = ttk.Checkbutton(
        newpass_w, text="Show password", style="TCheckbutton", 
        variable=show_pass_var, command=show_pass_box).place(x=452, y=370.44)


    newpass_w.iconphoto(False, img_icon)
    newpass_w.mainloop()

# newpassw()