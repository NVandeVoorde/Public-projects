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
frm_buttons = tk.Frame(root)
frm_buttons.columnconfigure(0, weight = 1)
frm_buttons.columnconfigure(1, weight = 1)

btn_add = tk.Button(
    frm_buttons, 
    text = "Add entry", 
    width = 20,
    height = 10,
    bg = 'black',
    fg = 'white',
)

btn_delete = tk.Button(
    frm_buttons, 
    text = "Delete entry", 
    width = 20,
    height = 10,
    bg = 'black',
    fg = 'white',
)

btn_add.grid(row = 0, column = 0)
btn_delete.grid(row = 0, column = 1)

frm_buttons.pack(fill= 'x')

# TABLE



# END 
root.mainloop()