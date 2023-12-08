import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import pandas as pd
import signin
import chart_data
import table_data
from tkinter import messagebox as mbox
from functools import reduce

filename_data = 'data.csv'
filename_spot = "spot_wisata.csv"

harga_spot = []
spot_tuju = []
mboh = []
nama_spot = pd.read_csv(filename_spot)
data_harga_spot = nama_spot['harga masuk']

def add_dataw():
    add_data_w = tk.Tk()
    add_data_w.title("Pariwi Data (Add Data)")
    add_data_w.configure(bg="#fff")
    add_data_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = add_data_w.winfo_screenwidth()
    screen_height = add_data_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    add_data_w.geometry("%dx%d+%d+%d" %
                    (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(add_data_w, image=img, bg="white").place(x=0, y=0)
    img_icon = PhotoImage(
        file="travel.png")

    # Dekorasi
    kotak_biru = Frame(add_data_w, width=568, height=435, bg="#2666FA").place(x=176, y=83)
    kotak_putih = Frame(add_data_w, width=118, height=432, bg="white").place(x=58, y=83)


    # Fungsi-fungsi
    def chart_data_c():
        add_data_w.destroy()
        chart_data.chartw()

    def sign_out_c():
        add_data_w.destroy()
        signin.signinw()   

    def table_data_c():
        add_data_w.destroy()
        table_data.tablew() 

    def my_reset():
        for widget in add_data_w.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')
            elif isinstance(widget, ttk.Checkbutton):
                widget.state(['!selected'])

        var_papuma.set(0)
        var_wu.set(0)
        var_payangan.set(0)
        var_tl.set(0)

        spot_tuju.clear()
        harga_spot.clear()

    def harga_papuma():
        spot_tuju.append(0)
        harga_spot.append(data_harga_spot[0])

    def harga_watu_ulo():
        spot_tuju.append(1)
        harga_spot.append(data_harga_spot[1])

    def harga_payangan():
        spot_tuju.append(2)
        harga_spot.append(data_harga_spot[2])

    def harga_teluk_lope():
        spot_tuju.append(3)
        harga_spot.append(data_harga_spot[3])

    def fungsi_add():
        nama = nama_box.get()
        usia = usia_box.get()
        asal = asal_box.get()
        jumlah = int(jumlah_box.get())

        waktu = time.strftime("%A, %d - %m - %Y %H:%M:%S")

        total_harga_spot = sum(harga_spot)
        total_harga = jumlah * total_harga_spot

        with open(filename_data, mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if rows:
                last_row = rows[-1]
                id = int(last_row['id']) + 1
            else:
                id = 1

        with open('data.csv', mode='a', newline='') as file:
            fieldnames = ['id',
                        'nama',
                        'usia',
                        'asal',
                        'waktu',
                        'jumlah',
                        'spot',
                        'harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow({
                'id': id,
                'nama': nama,
                'usia': usia,
                'asal': asal,
                'waktu': waktu,
                'jumlah': jumlah,
                'spot': spot_tuju,
                'harga': total_harga
            })

            my_reset()
            mbox.showinfo("Berhasil", "Data telah ditambahkan")


    # Check button
    style = ttk.Style()
    style.configure("TCheckbutton", background="#2666FA",
                    foreground="white", font=("Inter", 10))

    var_papuma = tk.IntVar()
    cb_papuma = ttk.Checkbutton(add_data_w, text="PAPUMA", variable=var_papuma,
                                onvalue=1, offvalue=0, command=harga_papuma, style="TCheckbutton")
    cb_papuma.place(x=314, y=370, width=88, height=18)

    var_wu = tk.IntVar()
    cb_wu = ttk.Checkbutton(add_data_w, text="WATU ULO", variable=var_wu,
                            onvalue=2, offvalue=0, command=harga_watu_ulo, style="TCheckbutton")
    cb_wu.place(x=450, y=370, width=102, height=18)

    var_payangan = tk.IntVar()
    cb_payangan = ttk.Checkbutton(
        add_data_w, text="PAYANGAN", variable=var_payangan, onvalue=3, offvalue=0, 
        command=harga_payangan, style="TCheckbutton")
    cb_payangan.place(x=594, y=370, width=106, height=18)

    var_tl = tk.IntVar()
    cb_tl = ttk.Checkbutton(add_data_w, text="TELUK LOVE",
                            variable=var_tl, onvalue=4, offvalue=0, 
                            command=harga_teluk_lope, style="TCheckbutton")
    cb_tl.place(x=313, y=400, width=115, height=18)


    # Label
    label_nama = Label(add_data_w, text="NAMA", fg="white",
                    bg="#2666FA", font=("Inter", 13, "bold")).place(x=210, y=130)

    label_usia = Label(add_data_w, text="USIA", fg="white",
                    bg="#2666FA", font=("Inter", 13, "bold")).place(x=210, y=190)

    label_asal = Label(add_data_w, text="ASAL", fg="white",
                    bg="#2666FA", font=("Inter", 13, "bold")).place(x=210, y=250)

    label_jumlah = Label(add_data_w, text="JUMLAH", fg="white",
                        bg="#2666FA", font=("Inter", 13, "bold")).place(x=210, y=310)

    label_spot = Label(add_data_w, text="SPOT", fg="white",
                    bg="#2666FA", font=("Inter", 13, "bold")).place(x=210, y=370)


    # Entry box
    nama_box = Entry(add_data_w, width=50, fg="black",
                    border=1, bg="white", font=("Inter", 10))
    nama_box.place(x=320, y=130)

    usia_box = Entry(add_data_w, width=50, fg="black",
                    border=1, bg="white", font=("Inter", 10))
    usia_box.place(x=320, y=190)

    asal_box = Entry(add_data_w, width=50, fg="black",
                    border=1, bg="white", font=("Inter", 10))
    asal_box.place(x=320, y=250)

    jumlah_box = Entry(add_data_w, width=50, fg="black",
                    border=1, bg="white", font=("Inter", 10))
    jumlah_box.place(x=320, y=310)


    # Button
    table_data_b = Button(add_data_w, width=8, pady=3, text="Table Data",
                        bg="white", fg="black", border=0, command=table_data_c).place(x=86, y=132)

    add_datab = Button(add_data_w, width=8, pady=3, text="Add Data",
                    bg="white", fg="black", border=0).place(x=86, y=174)

    chart_data_b = Button(add_data_w, width=8, pady=3, text="Chart Data",
                        bg="white", fg="black", border=0, command=chart_data_c).place(x=86, y=216)


    sign_out = Button(add_data_w, width=8, pady=3, text="Sign Out",
                    bg="white", fg="black", border=0, command=sign_out_c).place(x=86, y=453)

    add_button = Button(add_data_w, text="ADD",
                        bg="white", fg="#2666FA", border=0, 
                        command=fungsi_add).place(x=665, y=480, width=52, height=16)

    reset_button = Button(add_data_w, text="RESET",
                        bg="white", fg="#2666FA", border=0, 
                        command=lambda: my_reset()).place(x=603, y=480, width=52, height=16)

    add_data_w.iconphoto(False, img_icon)
    add_data_w.mainloop()


# add_dataw()