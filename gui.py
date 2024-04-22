import ttkbootstrap as tkb
from tkinter import filedialog
from tkinter import ttk
from cli import alm_tg_generate


def open_file_dialog(entry):
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    entry.delete(0, tkb.END)
    entry.insert(0, file_path)


def open_folder_dialog(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tkb.END)
    entry.insert(0, folder_path)


# Create the main window
root = tkb.Window(themename="superhero", resizable=(False, False))
root.title('Alarms Transaction Group Generator')
root.geometry('850x200')
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=4)

# Create a labelframe for the entry boxes
entry_frame = tkb.LabelFrame(root, text='Parameters')
entry_frame.pack(padx=10, pady=15, side='left', ipady=5)

# Site Entry
site_lbl = tkb.Label(entry_frame, text='Site')
site_lbl.grid(row=0, column=0, sticky='w', padx=5, pady=5)
site_ent = tkb.Entry(entry_frame)
site_ent.grid(row=0, column=1, sticky='e', padx=5, pady=5, columnspan=5)

# PLC Entry
plc_lbl = tkb.Label(entry_frame, text='PLC')
plc_lbl.grid(row=1, column=0, sticky='w', padx=5, pady=5)
plc_ent = tkb.Entry(entry_frame)
plc_ent.grid(row=1, column=1, sticky='e', padx=5, pady=5)

# DB Entry
db_lbl = tkb.Label(entry_frame, text='DB')
db_lbl.grid(row=2, column=0, sticky='w', padx=5, pady=5)
db_ent = tkb.Entry(entry_frame)
db_ent.grid(row=2, column=1, sticky='e', padx=5, pady=5)

# Create a labelframe for file and folder selection
path_frame = tkb.LabelFrame(root, text='Path Selection')
path_frame.pack(padx=10, pady=5, fill='x', ipady=5)
path_frame.columnconfigure(1, weight=1)

# Choose File Button
file_button = tkb.Button(path_frame, text='Select', bootstyle="primary, outline",
                         command=lambda: open_file_dialog(file_entry))
file_button.grid(row=1, column=3, sticky='e', pady=5, padx=5)
file_entry = tkb.Entry(path_frame)
file_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
file_lbl = tkb.Label(path_frame, text='Alarm List .txt')
file_lbl.grid(row=1, column=0, sticky='e', padx=5, pady=5)

# Choose Folder Button
folder_button = tkb.Button(path_frame, text='Select', bootstyle="primary, outline",
                           command=lambda: open_folder_dialog(folder_entry))
folder_button.grid(row=0, column=3, sticky='e', pady=5, padx=5)
folder_entry = tkb.Entry(path_frame)
folder_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5, columnspan=2)
folder_lbl = tkb.Label(path_frame, text='Destination Path')
folder_lbl.grid(row=0, column=0, sticky='e', padx=5, pady=5)

# Submit Button

submit_button = tkb.Button(root, text='Generate', bootstyle="success, outline",
                           command=lambda: alm_tg_generate(file_entry.get(), folder_entry.get(), site_ent.get(), plc_ent.get(),
                                                           db_ent.get()))
submit_button.pack(side='right', padx=10, pady=5)


# Run the main loop
root.mainloop()
