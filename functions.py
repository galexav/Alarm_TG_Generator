from tkinter import filedialog
import ttkbootstrap as tkb


def alm_tg_generate(alm_lst_filepath, dest_folder, site, cp, db):
    # Opens, reads user chosen .txt file containing a list of alarm names,
    # then adds each item to a list called 'alm_lst'.
    with open(alm_lst_filepath, 'r') as text_file:
        alm_lst = text_file.readlines()
    alm_lst = [item.strip() for item in alm_lst]  # Removes any whitespace from the list items.

    # Defines the replacements in a dictionary.
    replacements = {'Site_Name': site, 'CP_Name': cp, 'DB_Name': db}

    # Processes each item in 'alm_lst' list.
    for alarm_name in alm_lst:
        # Reads the template XML file.
        with open('Alarm_TG_Template.xml', 'r') as xml_template_file:
            template_content = xml_template_file.read()

        # Replaces all occurrences of 'Site_Name', 'CP_Name' & 'DB_Name' from the text in the
        # template file with the values from the 'replacements' dictionary. Also replaces
        # all occurrences of 'Alarm_Name' from the text in the template file with the
        # alarm names from the 'alm_lst' list.
        for old_text, new_text in replacements.items():
            template_content = template_content.replace(old_text, new_text)

            template_content = template_content.replace('Alarm_Name', alarm_name)

        # Writes the modified content to a new file.
        with open(f'{dest_folder}/{site}_{cp}_AlmTransGrp.xml', 'a') as xml_import_file:
            xml_import_file.write(template_content + '\n')

    # Adds the <Project> & <Groups> tags to the beginning & end of the file.
    with open(f'{dest_folder}/{site}_{cp}_AlmTransGrp.xml', 'r') as xml_import_file:
        text = xml_import_file.read()

    with open(f'{dest_folder}/{site}_{cp}_AlmTransGrp.xml', 'w') as xml_import_file:
        xml_import_file.write(f'<Project>\n<Groups>\n{text}</Groups>\n</Project>')


def open_file_dialog(entry):
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    entry.delete(0, tkb.END)
    entry.insert(0, file_path)


def open_folder_dialog(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tkb.END)
    entry.insert(0, folder_path)