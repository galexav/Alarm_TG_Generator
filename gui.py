import ttkbootstrap as tkb
from functions import *

# Creates the main window.
root = tkb.Window(themename="superhero", resizable=(False, False))
root.title('Alarms Transaction Group Generator')
root.geometry('1000x210')
root.columnconfigure(1, weight=1)

frame_one = tkb.Frame(root)
frame_one.grid(row=0, column=0, sticky='w')

frame_two = tkb.Frame(root)
frame_two.grid(row=0, column=1, sticky='ew')
frame_two.grid_columnconfigure(0, weight=1)

# Creates a labelframe for the entry boxes.
entry_frame = tkb.LabelFrame(frame_one, text='Parameters')
entry_frame.grid(row=0, column=0, sticky='n', padx=10, pady=10, ipady=5)

# Site name text entry field.
site_lbl = tkb.Label(entry_frame, text='Site')
site_lbl.grid(row=0, column=0, sticky='w', padx=5, pady=5)
site_ent = tkb.Entry(entry_frame)
site_ent.grid(row=0, column=1, sticky='e', padx=5, pady=5)

# PLC name text entry field.
plc_lbl = tkb.Label(entry_frame, text='PLC')
plc_lbl.grid(row=1, column=0, sticky='w', padx=5, pady=5)
plc_ent = tkb.Entry(entry_frame)
plc_ent.grid(row=1, column=1, sticky='e', padx=5, pady=5)

# DB name text entry field.
db_lbl = tkb.Label(entry_frame, text='DB')
db_lbl.grid(row=2, column=0, sticky='w', padx=5, pady=5)
db_ent = tkb.Entry(entry_frame)
db_ent.grid(row=2, column=1, sticky='e', padx=5, pady=5)

# Creates a labelframe for file and folder selection.
path_frame = tkb.LabelFrame(frame_two, text='File Path Selection')
path_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=10, ipady=5)
path_frame.columnconfigure(1, weight=1)

# 'Select .txt file' button.
file_button = tkb.Button(path_frame, text='Select', bootstyle="primary, outline",
                         command=lambda: open_file_dialog(file_entry))
file_button.grid(row=0, column=3, sticky='e', pady=5, padx=5)
file_entry = tkb.Entry(path_frame)
file_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
file_lbl = tkb.Label(path_frame, text='Alarm List File')
file_lbl.grid(row=0, column=0, sticky='e', padx=5, pady=5)

# 'Select destination path' button.
folder_button = tkb.Button(path_frame, text='Select', bootstyle="primary, outline",
                           command=lambda: open_folder_dialog(folder_entry))
folder_button.grid(row=1, column=3, sticky='e', pady=5, padx=5)
folder_entry = tkb.Entry(path_frame)
folder_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
folder_lbl = tkb.Label(path_frame, text='Destination Path')
folder_lbl.grid(row=1, column=0, sticky='e', padx=5, pady=5)

# 'Generate' button.
gen_button = tkb.Button(frame_two, text='Generate', bootstyle="success, outline",
                        command=lambda: alm_tg_generate(file_entry.get(), folder_entry.get(), site_ent.get(),
                                                        plc_ent.get(),
                                                        db_ent.get()))
gen_button.grid(row=1, column=0, sticky='e', padx=10, pady=5)

# Run the main loop.
root.mainloop()
