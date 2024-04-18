# ENTER YOUR SITE AND CP NAMES HERE
########################################################################################################
# Defines values for variables used to replace text in 'Alarm_TG_Template.xml'
site = 'AKR1'  # Replace value with the site name
cp = 'CP01'  # Replace value with the CP name
########################################################################################################

# Filepaths
template_filepath = 'Alarm_TG_Template.xml'  # Template XML file.
alarm_list_filepath = 'Alarm_List.txt'  # File containing the SCADA alarm names to import.

# Opens, reads the Alarm_List.txt file, then adds each item to a list called 'alarm_list'.
with open(alarm_list_filepath, 'r') as text_file:
    alarm_list = text_file.readlines()
alarm_list = [item.strip() for item in alarm_list]  # Removes any whitespace from the list items.

# Defines the replacements in a dictionary.
replacements = {'Site_Name': site, 'CP_Name': cp}

# Processes each item in 'alarm_list'.
for alarm_name in alarm_list:
    # Reads the template XML file.
    with open('Alarm_TG_Template.xml', 'r') as xml_template_file:
        template_content = xml_template_file.read()

    # Replaces all occurrences of 'Site_Name' and 'CP_Name' from the text in the
    # template file with the values from the 'replacements' dictionary.
    for old_text, new_text in replacements.items():
        template_content = template_content.replace(old_text, new_text)

        # Replaces all occurrences of 'Alarm_Name' from the text in the
        # Alarm_TG_Template.xml file with the alarm name from the 'alarm_list'.
        template_content = template_content.replace('Alarm_Name', alarm_name)

    # Writes the modified content to a new file.
    with open(f'{site}_{cp}_AlmTransGrp.xml', 'a') as xml_import_file:
        xml_import_file.write(template_content)

# Adds the <Project> & <Groups> tags to the beginning & end of the file.
with open(f'{site}_{cp}_AlmTransGrp.xml', 'r') as xml_import_file:
    text = xml_import_file.read()

with open(f'{site}_{cp}_AlmTransGrp.xml', 'w') as xml_import_file:
    xml_import_file.write(f'<Project><Groups>{text}</Groups></Project>')

# Closes the files.
xml_template_file.close()
xml_import_file.close()
text_file.close()

print(f'Transaction Group import file, {site}_{cp}_AlmTransGrp.xml,has been created for {site}-{cp}.')