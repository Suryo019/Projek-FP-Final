import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import signin
import chart_data
import add_data
import csv
from PIL import Image, ImageTk

filename_data = 'data.csv'

def tablew():
    table_w = tk.Tk()
    table_w.title("Pariwi Data (Table Data)")
    table_w.configure(bg="#fff")
    table_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = table_w.winfo_screenwidth()
    screen_height = table_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    table_w.geometry("%dx%d+%d+%d" %
                    (width_of_window, height_of_window, x_coordinate, y_coordinate))

    img = PhotoImage(
        file="bg1.png")
    Label(table_w, image=img, bg="white").place(x=0, y=0)
    search_icon = PhotoImage(
        file="searchic.png")
    img_icon = PhotoImage(
        file="travel.png")


    # Dekorasi
    kotak_biru = Frame(table_w, width=568, height=432, bg="#2666FA").place(x=176, y=83)
    kotak_putih = Frame(table_w, width=118, height=432, bg="white").place(x=58, y=83)


    # Judul
    judul = Label(table_w, text="DATA PENGUNJUNG", fg="white",
                bg="#2666FA", font=("Inter", 13, "bold")).place(x=200, y=116)


    # Fungsi - fungsi
    def on_enter_u(e):
        search_bar.delete(0, "end")

    def on_leave_u(e):
        nama = search_bar.get()
        if nama == "":
            search_bar.insert(0, "Search")

    def search_data():
        search_text = search_bar.get().lower()
        selected_asal = combobox.get().lower()

        def filter_condition(row):
            return (
                search_text.lower() in str(cell).lower() for cell in row
            ) and (selected_asal.lower() in row) if selected_asal != "asal" else any(
                search_text.lower() in str(cell).lower() for cell in row
            )


        filtered_data = list(filter(filter_condition, tabel_data))

        tabel.delete(*tabel.get_children())

        for i, row_data in enumerate(filtered_data):
            tag = odd_row_tags if i % 2 == 0 else even_row_tags
            tabel.insert(parent="", index="end", values=row_data, tags=(tag, content_tag))

    def delete_data():
        selected_item = tabel.selection()
        if selected_item:
            for item in selected_item:
                index = tabel.index(item)
                tabel.delete(item)
                del tabel_data[index]

            with open(filename_data, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(tabel_kolom)
                for row in tabel_data:
                    writer.writerow(row)

    def edit_data():
        selected_item = tabel.selection()
        if selected_item:
            item_data = tabel.item(selected_item)['values']

            edit_w = Toplevel(table_w)
            edit_w.title("Pariwi Data (Edit Data)")
            edit_w.configure(bg="#fff")
            edit_w.resizable(False, False)
            edit_w.iconphoto(False, img_icon)
            width_of_window = 300
            height_of_window = 350
            screen_width = edit_w.winfo_screenwidth()
            screen_height = edit_w.winfo_screenheight()
            x_coordinate = (screen_width/2)-(width_of_window/2)
            y_coordinate = (screen_height/2)-(height_of_window/2)
            edit_w.geometry("%dx%d+%d+%d" %
                            (width_of_window, height_of_window, x_coordinate, y_coordinate))

            image = Image.open(
                "bg5.png")
            photo = ImageTk.PhotoImage(image)
            
            label_gambar = Label(edit_w, image=photo, bg="white")
            label_gambar.image = photo
            label_gambar.place(x=0, y=0)

            # Dekorasi
            kotak_biru = Frame(edit_w, width=257, height=310, bg="#2666FA").place(x=22, y=21)

            # Judul
            judul = Label(edit_w, text="EDIT DATA", fg="white",
                        bg="#2666FA", font=("Inter", 8, "bold")).place(x=127, y=32)

            entry_widgets = []
            label_y_position = 57

            for i, column in enumerate(tabel_kolom):
                label = Label(edit_w, text=column, font=(
                    'Inter', 8), bg="#2666FA", fg="white")
                label.place(x=32, y=label_y_position)
                label_y_position += 30

                entry = Entry(edit_w, font=('Inter', 8), bd=0, relief='solid',
                            highlightbackground="white", highlightcolor="white", highlightthickness=1)
                entry.place(x=105, y=label_y_position - 30, width=153)
                entry.insert(0, item_data[i])
                entry_widgets.append(entry)

            def update_data():
                updated_data = [entry.get() for entry in entry_widgets]
                tabel.item(selected_item, values=updated_data)
                edit_w.destroy()

                index = tabel.index(selected_item)
                tabel_data[index] = updated_data

                with open(filename_data, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(tabel_kolom)
                    for row in tabel_data:
                        writer.writerow(row)

                messagebox.showinfo("Notification", "Data berhasil di update!")

            update_button = Button(edit_w, text="UPDATE", command=update_data,
                                width=8, pady=3, bg="white", fg="#2666FA", border=0).place(x=132, y=300, width=52, height=16)

    def chart_data_c():
        table_w.destroy()
        chart_data.chartw()

    def sign_out_c():
        table_w.destroy()
        signin.signinw()

    def add_data_c():
        table_w.destroy()
        add_data.add_dataw()

    def reload_table():
        tabel.delete(*tabel.get_children())

        for i, row_data in enumerate(tabel_data):
            tag = odd_row_tags if i % 2 == 0 else even_row_tags
            tabel.insert(parent="", index="end", values=row_data,
                        tags=(tag, content_tag))

    def reset_sb():
        search_bar.delete(0, "end")
        search_bar.insert(0, "Search")

    def reset_combobox():
        combobox.set("Asal")
        reset_sb()
        reload_table()


    # Tombol Utama
    table_data = Button(table_w, width=8, pady=3, text="Table Data",
                        bg="white", fg="black", border=0).place(x=86, y=132)

    add_datab = Button(table_w, width=8, pady=3, text="Add Data",
                    bg="white", fg="black", border=0, command=add_data_c).place(x=86, y=174)

    chart_datab = Button(table_w, width=8, pady=3, text="Chart Data",
                        bg="white", fg="black", border=0, command=chart_data_c).place(x=86, y=216)

    sign_out = Button(table_w, width=8, pady=3, text="Sign Out",
                    bg="white", fg="black", border=0, command=sign_out_c).place(x=86, y=453)


    # Tabel
    with open(filename_data, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        tabel_kolom = header
        tabel_data = list(reader)

    tabel = ttk.Treeview(table_w, columns=tabel_kolom, show="headings")

    for column in tabel_kolom:
        tabel.heading(column=column, text=column)
        tabel.column(column=column, width=70, stretch=False)

    odd_row_tags = 'odd_row'
    even_row_tags = 'even_row'
    content_tag = 'content'

    tabel.tag_configure(odd_row_tags, background='#CFDCFD')
    tabel.tag_configure(even_row_tags, background='#E1EAFF')
    tabel.tag_configure(content_tag, font=('Helvetica', 8))

    for i, row_data in enumerate(tabel_data):
        tag = odd_row_tags if i % 2 == 0 else even_row_tags
        tabel.insert(parent="", index="end", values=row_data,
                    tags=(tag, content_tag))

    heading_style = ttk.Style()
    heading_style.map('Treeview.Heading', background=[
                    ('active', '#053BBA'), ('!active', '#053BBA')])

    tabel.place(x=200, y=149, height=319, width=519)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", background="#053BBA",
                    fieldbackground="white", foreground="white")
    style.configure("Treeview", background="#CFDCFD",
                    fieldbackground="white", fg="white")


    # Search
    search_bar = Entry(table_w, width=20, font=('Inter', 8), bd=0, relief='solid',
                    highlightbackground="white", highlightcolor="white", highlightthickness=1)
    search_bar.insert(0, "Search")
    search_bar.bind("<FocusIn>", on_enter_u)
    search_bar.bind("<FocusOut>", on_leave_u)

    search_bar.place(x=584, y=117, width=133, height=16)
    search_bar.configure(bg="#2666FA", fg="white")

    search_button = Button(table_w, text="", width=2, height=1,
                        bg="white", fg="black", border=0, image=search_icon, command=search_data).place(x=701, y=117, width=16, height=16)


    # Combo Box
    with open(filename_data, 'r') as file:
        reader = csv.DictReader(file)
        unique_asal_values = set(row['asal'] for row in reader)

    asal_values = list(unique_asal_values)

    frame_putih = Frame(table_w, width=135, height=18, bg="white").place(x=440, y=116.2)

    combobox_style = ttk.Style()
    combobox_style.configure(
        "TCombobox", fieldbackground="#2666FA", foreground="white")

    combobox = ttk.Combobox(table_w, values=asal_values, style="TCombobox")
    combobox.insert(0, "Asal")
    combobox.place(x=441, y=117, width=133, height=16)


    # Delete
    delete_button = Button(table_w, text="DELETE",
                        bg="white", fg="#2666FA", border=0, command=delete_data).place(x=665, y=480, width=52, height=16)

    edit_button = Button(table_w, text="EDIT",
                        bg="white", fg="#2666FA", border=0, command=edit_data).place(x=603, y=480, width=52, height=16)

    refresh = Button(table_w, text="REFRESH", bg="white",
                    fg="#2666FA", border=0, command=reset_combobox).place(x=541, y=480, width=52, height=16)

    combobox.bind("<<ComboboxSelected>>", lambda event: search_data())


    table_w.iconphoto(False, img_icon)
    table_w.mainloop()

# tablew()