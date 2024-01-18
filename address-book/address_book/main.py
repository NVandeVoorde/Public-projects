import tkinter as tk 
from tkinter import ttk
from functions import *

root = tk.Tk()
root.geometry("800x800")
root.title("Address book app")

# INTRO
frm_intro = tk.Frame(root)

tk.Label(frm_intro, 
         text="CRUD Application for address book", 
         font=("Arial", 15)).pack(anchor='w', pady = (10, 5))

tk.Label(frm_intro, 
         text="Use the buttons to add, delete or change records in the database", 
         font=("Arial", 11)).pack()

frm_intro.pack(anchor='w', padx = (15, 0), pady = (5, 5) )

# BUTTONS
frm_buttons = tk.Frame(
    root, 
    height = 2, 
    padx = 15, 
    pady = 5
    )
frm_buttons.columnconfigure(0, weight = 0)
frm_buttons.columnconfigure(1, weight = 0)
frm_buttons.columnconfigure(2, weight = 0)

def open_window_update(dict): 

    # Global names to return 
    global selected_id
    global ent_firstname
    global ent_lastname
    global ent_housenumber
    global ent_street
    global ent_zipcode

    selected_id = dict["id"]

    win_update = tk.Toplevel(root)
    win_update.geometry("300x350")
    win_update.title("Add or update entries")
    title_win = tk.Label(win_update, text = "Add entry here", padx = 5, pady = 10)
    title_win.pack(anchor = 'w')
    # first name
    lbl_firstname = tk.Label(win_update, text= "First name: ")
    lbl_firstname.pack(padx = 5, anchor = 'w')
    ent_firstname = tk.Entry(win_update)
    ent_firstname.insert(0, dict["first_name"])
    ent_firstname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # last name
    lbl_lastname = tk.Label(win_update, text= "Last name: ")
    lbl_lastname.pack(padx = 5, anchor = 'w')
    ent_lastname = tk.Entry(win_update)
    ent_lastname.insert(0, dict["last_name"])
    ent_lastname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # street
    lbl_street = tk.Label(win_update, text= "Street: ")
    lbl_street.pack(padx = 5, anchor = 'w')
    ent_street = tk.Entry(win_update)
    ent_street.insert(0, dict["street"])
    ent_street.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # house number
    lbl_housenumber = tk.Label(win_update, text= "House number: ")
    lbl_housenumber.pack(padx = 5, anchor = 'w')
    ent_housenumber = tk.Entry(win_update)
    ent_housenumber.insert(0, dict["house_number"])
    ent_housenumber.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # zipcode
    lbl_zipcode = tk.Label(win_update, text= "Zipcode: ")
    lbl_zipcode.pack(padx = 5, anchor = 'w')
    ent_zipcode = tk.Entry(win_update)
    ent_zipcode.insert(0, dict['zipcode'])
    ent_zipcode.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # submit button 
    btn_submit = tk.Button(win_update, 
                           text = "Submit", 
                           command = lambda: [  update_entry(entry_to_dict(new_id=False), selected_id), 
                                                refresh_table(tree), 
                                                win_update.destroy()])
    btn_submit.pack(anchor = 'w', padx = 5)

def open_window_add(): 

    # Global names to return 
    global ent_firstname
    global ent_lastname
    global ent_housenumber
    global ent_street
    global ent_zipcode

    win_add = tk.Toplevel(root)
    win_add.geometry("300x350")
    win_add.title("Add or update entries")
    title_win = tk.Label(win_add, text = "Add entry here", padx = 5, pady = 10)
    title_win.pack(anchor = 'w')
    # first name
    lbl_firstname = tk.Label(win_add, text= "First name: ")
    lbl_firstname.pack(padx = 5, anchor = 'w')
    ent_firstname = tk.Entry(win_add)
    ent_firstname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # last name
    lbl_lastname = tk.Label(win_add, text= "Last name: ")
    lbl_lastname.pack(padx = 5, anchor = 'w')
    ent_lastname = tk.Entry(win_add)
    ent_lastname.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # street
    lbl_street = tk.Label(win_add, text= "Street: ")
    lbl_street.pack(padx = 5, anchor = 'w')
    ent_street = tk.Entry(win_add)
    ent_street.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # house number
    lbl_housenumber = tk.Label(win_add, text= "House number: ")
    lbl_housenumber.pack(padx = 5, anchor = 'w')
    ent_housenumber = tk.Entry(win_add)
    ent_housenumber.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # zipcode
    lbl_zipcode = tk.Label(win_add, text= "Zipcode: ")
    lbl_zipcode.pack(padx = 5, anchor = 'w')
    ent_zipcode = tk.Entry(win_add)
    ent_zipcode.pack(anchor = 'w', padx = 5, pady = (2, 10))
    # submit button 
    btn_submit = tk.Button(win_add, text = "Submit", command = lambda: [insert_dict(entry_to_dict()),
                                                                        refresh_table(tree), 
                                                                        win_add.destroy()])
    btn_submit.pack(anchor = 'w', padx = 5)

    
def entry_to_dict(new_id = True): 
    """ Creates empty dict and fills it with data from window
    > I fail reacht the entries in the functions module
    """

    global ent_firstname
    global ent_lastname
    global ent_housenumber
    global ent_street
    global ent_zipcode

    dict_entry = {}
    if new_id == True: 
        random_int = randint(0, 100000) #maak betere id
        dict_entry.update( {'id': random_int} )
    elif new_id == False: 
        dict_entry.update( {'id': selected_id} ) 

    dict_entry.update( {'first_name': ent_firstname.get()} )
    dict_entry.update( {'last_name': ent_lastname.get()} )
    dict_entry.update( {'street': ent_street.get()} )
    dict_entry.update( {'house_number': ent_housenumber.get()} )
    dict_entry.update( {'zipcode': ent_zipcode.get()} )

    return dict_entry


btn_add = tk.Button(
    frm_buttons, 
    text = "Add entry", 
    width = 10,
    height = 1,
    padx = 5, 
    pady = 5, 
    command = open_window_add
)

btn_delete = tk.Button(
    frm_buttons, 
    text = "Delete entry", 
    width = 10,
    height = 1,
    padx = 5, 
    pady = 5,
    command = lambda: [delete_entry(tree), refresh_table(tree)]
)

btn_update = tk.Button(
    frm_buttons, 
    text = "Update entry", 
    width = 10,
    height = 1,
    padx = 5, 
    pady = 5, 
    command = lambda: [open_window_update(selected_row(tree))]
)

btn_add.grid(row = 0, column = 0, sticky = 'w', padx=(0,5))
btn_delete.grid(row = 0, column = 1, sticky = 'w', padx=(0,5))
btn_update.grid(row = 0, column = 2, sticky = 'w', padx=(0,5))

frm_buttons.pack(fill= 'x', pady = 15)


# TABLE
frm_table = tk.Frame(root)
tree = ttk.Treeview(frm_table,  selectmode='browse')

refresh_table(tree)

tree.pack(fill = 'both', padx = 15)
frm_table.pack(pady = 10, fill = 'both')

# END 
root.mainloop()

