import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import csv
import signin
import table_data
import add_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from datetime import datetime

filename_data = 'data.csv'

def chartw():
    # Window
    chart_w = tk.Tk()
    chart_w.title("Pariwi Data (Chart Data)")
    chart_w.configure(bg="#fff")
    chart_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = chart_w.winfo_screenwidth()
    screen_height = chart_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    chart_w.geometry("%dx%d+%d+%d" %
                    (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(chart_w, image=img, bg="white").place(x=0, y=0)
    search_icon = PhotoImage(
        file="searchic2.png")
    img_icon = PhotoImage(
        file="travel.png")


    # Dekorasi
    kotak_biru = Frame(chart_w, width=568, height=432, bg="#2666FA").place(x=176, y=83)
    kotak_putih = Frame(chart_w, width=118, height=432, bg="white").place(x=58, y=83)


    # Judul
    judul1 = Label(chart_w, text="KLIK SHOW", fg="white",
                bg="#2666FA", font=("Inter", 20, "bold")).place(x=347, y=253)
    judul2 = Label(chart_w, text="UNTUK MENAMPILKAN CHART", fg="white",
                bg="#2666FA", font=("Inter", 20, "bold")).place(x=248, y=292)


    # Fungsi-fungsi
    def format_waktu(waktu):
        dt_object = datetime.strptime(waktu, "%A, %d - %m - %Y %H:%M:%S")
        formatted_waktu = dt_object.strftime("%A, %d - %m - %Y")
        return formatted_waktu

    def sign_out_c():
        chart_w.destroy()
        signin.signinw()

    def table_data_c():
        chart_w.destroy()
        table_data.tablew()

    def add_data_c():
        chart_w.destroy()
        add_data.add_dataw()

    def show_chart():
        data = pd.read_csv(filename_data)

        data['waktu masuk'] = pd.to_datetime(
            data['waktu masuk'], format='%A, %d - %m - %Y %H:%M:%S')

        data['waktu masuk'] = data['waktu masuk'].dt.strftime('%d/%m/%Y')

        pengunjung_harian = data.groupby('waktu masuk')['jumlah'].sum()

        # pengunjung_harian = pengunjung_harian.head(5)

        fig, ax = plt.subplots(figsize=(530/80, 348/80), dpi=80)
        pengunjung_harian.plot(kind='bar', color='#2666FA', ax=ax, width=0.8)

        ax.set_title('PENGUNJUNG BERDASARKAN HARIAN')
        ax.set_xlabel('TANGGAL')
        ax.set_ylabel('PENGUNJUNG')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=15, ha='center')

        frame_chart = Frame(chart_w, bg="white")
        frame_chart.place(x=194, y=112, width=530, height=348)

        hbar = Scrollbar(frame_chart, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)

        canvas = FigureCanvasTkAgg(fig, master=frame_chart)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=TOP, fill=BOTH, expand=1)

        canvas_widget.config(xscrollcommand=hbar.set)
        hbar.config(command=canvas_widget.xview)

        canvas.draw()
        
    def income_data():
        income_w = Toplevel(chart_w)
        income_w.title("Pariwi Data (Income Data)")
        income_w.configure(bg="#fff")
        income_w.resizable(False, False)
        income_w.iconphoto(False, img_icon)
        width_of_window = 300
        height_of_window = 350
        screen_width = income_w.winfo_screenwidth()
        screen_height = income_w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        income_w.geometry("%dx%d+%d+%d" %
                        (width_of_window, height_of_window, x_coordinate, y_coordinate))

        image = Image.open("bg5.png")
        photo = ImageTk.PhotoImage(image)
        label_gambar = Label(income_w, image=photo, bg="white")
        label_gambar.image = photo
        label_gambar.place(x=0, y=0)


        # Dekorasi
        kotak_biru = Frame(income_w, width=257, height=310, bg="#2666FA").place(x=22, y=21)


        # Judul
        judul = Label(income_w, text="INCOME DATA", fg="white",
                    bg="#2666FA", font=("Inter", 8, "bold")).place(x=118, y=32)


        # Tabel
        with open(filename_data, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            tabel_kolom = ['waktu masuk', 'total harga']

            grouped_data = {}
            for row in reader:
                date = format_waktu(row[header.index('waktu masuk')])
                harga = sum(map(float, row[header.index('harga')].split(',')))
                if date in grouped_data:
                    grouped_data[date] += harga
                else:
                    grouped_data[date] = harga

            tabel_data = [[date, total_harga]
                        for date, total_harga in grouped_data.items()]

        tabel = ttk.Treeview(income_w, columns=tabel_kolom, show="headings")

        for column in tabel_kolom:
            tabel.heading(column=column, text=column)
            tabel.column(column=column, width=110, stretch=False)

        odd_row_tags = 'odd_row'
        even_row_tags = 'even_row'
        content_tag = 'content'

        tabel.tag_configure(odd_row_tags, background='#CFDCFD')
        tabel.tag_configure(even_row_tags, background='#E1EAFF')
        tabel.tag_configure(content_tag, font=('Helvetica', 7))

        for i, row_data in enumerate(tabel_data):
            tag = odd_row_tags if i % 2 == 0 else even_row_tags
            tabel.insert(parent="", index="end", values=row_data,
                        tags=(tag, content_tag))

        heading_style = ttk.Style()
        heading_style.map('Treeview.Heading', background=[
            ('active', '#053BBA'), ('!active', '#053BBA')])

        tabel.place(x=39, y=80, height=222, width=222)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", background="#053BBA",
                        fieldbackground="white", foreground="white")
        style.configure("Treeview", background="#CFDCFD",
                        fieldbackground="white", fg="white")

        # Fungsi - fungsi
        def on_enter_u(e):
            search_bar.delete(0, "end")

        def on_leave_u(e):
            nama = search_bar.get()
            if nama == "":
                search_bar.insert(0, "Search")

        def combo_box_search():
            selected_date = combobox.get()
            if selected_date != "Tanggal":
                with open(filename_data, 'r') as file:
                    reader = csv.DictReader(file)
                    grouped_data = {}
                    for row in reader:
                        date = format_waktu(row['waktu masuk'])
                        harga = sum(map(float, row['harga'].split(',')))
                        if date in grouped_data:
                            grouped_data[date] += harga
                        else:
                            grouped_data[date] = harga

                    unique_dates = list(grouped_data.keys())
                    combobox['values'] = unique_dates

                    filtered_data = [{'waktu masuk': date, 'total harga': grouped_data[date]}
                                    for date in unique_dates if date == selected_date]

                    tabel.delete(*tabel.get_children())

                    for i, row_data in enumerate(filtered_data):
                        tag = odd_row_tags if i % 2 == 0 else even_row_tags
                        tabel.insert(parent="", index="end", values=list(
                            row_data.values()), tags=(tag, content_tag))
            else:
                reload_table()

        def search_data():
            search_text = search_bar.get().lower()
            selected_date = combobox.get()

            with open(filename_data, 'r') as file:
                reader = csv.DictReader(file)
                grouped_data = {}

                for row in reader:
                    date = format_waktu(row['waktu masuk'])
                    harga = sum(map(float, row['harga'].split(',')))

                    if date in grouped_data:
                        grouped_data[date] += harga
                    else:
                        grouped_data[date] = harga

                filtered_data = []

                for date, total_harga in grouped_data.items():
                    if (selected_date == "Tanggal" or date == selected_date) and (search_text in date.lower() or search_text in str(total_harga).lower()):
                        filtered_data.append(
                            {'waktu masuk': date, 'total harga': total_harga})

                tabel.delete(*tabel.get_children())

                for i, row_data in enumerate(filtered_data):
                    tag = odd_row_tags if i % 2 == 0 else even_row_tags
                    tabel.insert(parent="", index="end", values=list(
                        row_data.values()), tags=(tag, content_tag))

        def reload_table():
            tabel.delete(*tabel.get_children())

            for i, row_data in enumerate(tabel_data):
                tag = odd_row_tags if i % 2 == 0 else even_row_tags
                tabel.insert(parent="", index="end", values=row_data,
                            tags=(tag, content_tag))

        def reset_combobox():
            combobox.set("Tanggal")
            reload_table()

        # Search
        search_bar = Entry(income_w, width=20, font=('Inter', 7), bd=0, relief='solid',
                        highlightbackground="white", highlightcolor="white", highlightthickness=1)
        search_bar.insert(0, "Search")
        search_bar.bind("<FocusIn>", on_enter_u)
        search_bar.bind("<FocusOut>", on_leave_u)

        search_bar.place(x=180, y=60, width=81, height=10)
        search_bar.configure(bg="#2666FA", fg="white")

        search_button = Button(income_w, text="", width=2, height=1,
                            bg="white", fg="black", border=0, image=search_icon, 
                            command=search_data).place(x=251, y=60, width=10, height=10)

        # Combo Box
        with open(filename_data, 'r') as file:
            reader = csv.DictReader(file)
            unique_tanggal = sorted(set(row['waktu masuk'] for row in reader), key=lambda x: pd.to_datetime(
                x, format='%A, %d - %m - %Y %H:%M:%S'))

        tanggal = list(unique_tanggal)

        frame_putih = Frame(income_w, width=83, height=11.7, bg="white").place(x=89, y=59.2)

        combobox_style = ttk.Style()
        combobox_style.configure(
            "TCombobox", fieldbackground="#2666FA", foreground="white")

        combobox = ttk.Combobox(income_w, values=tanggal, style="TCombobox")
        combobox.insert(0, "Tanggal")
        combobox.place(x=90, y=60, width=81, height=9.7)

        refresh = Button(income_w, text="REFRESH", bg="white",
                        fg="#2666FA", border=0, 
                        command=reset_combobox).place(x=210, y=308, width=52, height=11)

        combobox.bind("<<ComboboxSelected>>", lambda event: combo_box_search())


    # Tombol Utama
    table_data_b = Button(chart_w, width=8, pady=3, text="Table Data",
                        bg="white", fg="black", border=0, command=table_data_c).place(x=86, y=132)

    add_data_b = Button(chart_w, width=8, pady=3, text="Add Data",
                    bg="white", fg="black", border=0, command=add_data_c).place(x=86, y=174)

    chart_data = Button(chart_w, width=8, pady=3, text="Chart Data",
                        bg="white", fg="black", border=0).place(x=86, y=216)

    sign_out = Button(chart_w, width=8, pady=3, text="Sign Out",
                    bg="white", fg="black", border=0, command=sign_out_c).place(x=86, y=453)

    show_button = Button(chart_w, text="SHOW", bg="white",
                        fg="#2666FA", border=0, command=show_chart).place(x=610, y=474, width=52, height=16)

    income = Button(chart_w, text="INCOME", bg="white",
                    fg="#2666FA", border=0, command=income_data).place(x=672, y=474, width=52, height=16)


    chart_w.iconphoto(False, img_icon)
    chart_w.mainloop()

# chartw()