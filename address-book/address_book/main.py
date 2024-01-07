import tkinter as tk 

root = tk.Tk()

# INTRO
frm_intro = tk.Frame(root)

lbl_intro = tk.Label(frm_intro, text="CRUD Application for address book")
lbl_intro.grid(0,0)

frm_intro.grid(0,0)

# BUTTONS
frm_buttons = tk.Frame(root)

frm_buttons.grid(1, 0)

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

btn_add.grid(0, 0)
btn_delete.grid(0, 1)


# TABLE



# END 
root.mainloop()