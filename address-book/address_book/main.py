import tkinter as tk 
from tkinter import ttk
from functions import get_all_data

import tkinter as tk 

root = tk.Tk()
root.geometry("800x800")
root.title("Address book app")

# INTRO
frm_intro = tk.Frame(root)

lbl_intro = tk.Label(frm_intro, text="CRUD Application for address book")
lbl_intro.pack()

frm_intro.pack()

# BUTTONS
frm_buttons = tk.Frame(
    root, 
    height = 2, 
    padx = 15, 
    pady = 5
    )
frm_buttons.columnconfigure(0, weight = 1)
frm_buttons.columnconfigure(1, weight = 1)
frm_buttons.columnconfigure(2, weight = 1)

def open_window(): 
    print("Open window")
    win_add = tk.Toplevel(root)
    win_add.geometry("300x400")
    win_add.title("Add or update entries")
    title_win = tk.Label(win_add, text = "Add entry here", padx = 5, pady = 10)
    title_win.pack(anchor = 'w')
    # first name
    lbl_firstname = tk.Label(win_add, text= "First name: ")
    lbl_firstname.pack(anchor = 'w')
    ent_firstname = tk.Entry(win_add)
    ent_firstname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # last name
    lbl_lastname = tk.Label(win_add, text= "Last name: ")
    lbl_lastname.pack(anchor = 'w')
    ent_lastname = tk.Entry(win_add)
    ent_lastname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # street
    lbl_street = tk.Label(win_add, text= "Street: ")
    lbl_street.pack(anchor = 'w')
    ent_street = tk.Entry(win_add)
    ent_street.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # house number
    lbl_housenumber = tk.Label(win_add, text= "House number: ")
    lbl_housenumber.pack(anchor = 'w')
    ent_housenumber = tk.Entry(win_add)
    ent_housenumber.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # zipcode
    lbl_zipcode = tk.Label(win_add, text= "Zipcode: ")
    lbl_zipcode.pack(anchor = 'w')
    ent_zipcode = tk.Entry(win_add)
    ent_zipcode.pack(anchor = 'w', padx = 5, pady = (2, 10))


btn_add = tk.Button(
    frm_buttons, 
    text = "Add entry", 
    width = 10,
    height = 2,
    bg = 'black',
    fg = 'white',
    padx = 5, 
    pady = 5, 
    command = open_window
)

btn_delete = tk.Button(
    frm_buttons, 
    text = "Delete entry", 
    width = 10,
    height = 2,
    bg = 'black',
    fg = 'white',
    padx = 5, 
    pady = 5
)

btn_update = tk.Button(
    frm_buttons, 
    text = "Update entry", 
    width = 10,
    height = 2,
    bg = 'black',
    fg = 'white',
    padx = 5, 
    pady = 5
)

btn_add.grid(row = 0, column = 0, sticky = 'w')
btn_delete.grid(row = 0, column = 1, sticky = 'w')
btn_update.grid(row = 0, column = 2, sticky = 'w')

frm_buttons.pack(fill= 'x')

#btn_add.bind("<Button-1>", open_window)


# TABLE
frm_table = tk.Frame(root)

df = get_all_data()

#columns = ('id', 'first_name', 'last_name', 'street', 'house_number', 'zipcode')

tree = ttk.Treeview(root)

tree['columns'] = df.columns.values.tolist()

for i in df.columns.values.tolist():
    tree.column(i, width=50)
    tree.heading(i, text=i)
for index, row in df.iterrows():
    tree.insert("", 'end', text=index, values=list(row))

tree.pack()
frm_table.pack()

# END 
root.mainloop()

quit()
df = get_all_data()
print(df)
