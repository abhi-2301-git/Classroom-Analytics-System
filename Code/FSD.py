import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog

def check_if_num(char,current_value):
    # Check if the new character is a digit and the length of the current value
    if not char.isdigit():
        return False  # Disallow non-digit input
    if len(current_value + char) > 3:
        return False  # Disallow more than 2 digits
    return True  # Allow valid input

def Check_filepath(file_label,btn):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls;*.xlsx")])

    if file_path:
        file_label.config(text=file_path)  # Update the label with the selected file path
        btn.pack(pady=10) # pack upload button
    else:
        file_label.config(text="No file selected.")
        btn.pack_forget() #unpack upload button as no file selected

def FSD_upload(Gui):
    # Create a frame for the file upload process
    Gui.upload_frame = tk.Frame(Gui.root)
    Gui.upload_frame.pack()
    # Title
    Gui.welcome = tk.Label(Gui.upload_frame,text="Upload File",font=('Georgia', 20))
    Gui.welcome.pack(pady=10)
    # stores file path
    Gui.file_label = tk.Label(Gui.upload_frame, text="", font=('Arial', 12), fg="blue")
    Gui.file_label.pack(pady=10)
    # upl;oad button
    Gui.upload_btn = tk.Button(Gui.upload_frame,text="Uplaod File",font=('Tahoma', 14),command=lambda: get_filepath(Gui))
    # select button
    Gui.select_btn = tk.Button(Gui.upload_frame,text="Select File",font=('Tahoma', 14),command=lambda: Check_filepath(Gui.file_label,Gui.upload_btn))
    Gui.select_btn.pack(pady=10)
    
def get_filepath(Gui):
    # getting file path
    Gui.file_path = Gui.file_label.cget("text")
    show_filter_options(Gui)

def show_filter_options(Gui):
    # remove upload elements 
    Gui.upload_frame.pack_forget()
    # start
    Gui.main_frame = tk.Frame(Gui.root)
    Gui.main_frame.pack()
    # var storing if subject or attendance
    Gui.main_choice_value = tk.IntVar()
    # subject and attendance radio buttons
    Gui.radio_subject= tk.Radiobutton(Gui.main_frame, text="Subject",font=('Gerogia', 20), 
                        variable=Gui.main_choice_value, value=1,command=lambda: show_checkboxes(Gui))
    Gui.radio_attendance= tk.Radiobutton(Gui.main_frame, text="Attendance",font=('Gerogia', 20),
                            variable=Gui.main_choice_value, value=2,command=lambda: show_checkboxes(Gui))
    Gui.radio_subject.grid(row=0, column=0, padx=30, pady=20,)
    Gui.radio_attendance.grid(row=0, column=1, padx=30, pady=20)
    # parent frame to handle subject and attendance
    Gui.check_parent=tk.Frame(Gui.root)
    Gui.check_parent.pack()

    # frame for subject checkboxes
    Gui.checkbox_frame = tk.Frame(Gui.check_parent)
    Gui.checkbox_frame.grid(pady=10, row=0,column=0)  

    # subject Checkboxes
    Gui.maths_var = tk.BooleanVar()
    Gui.physics_var = tk.BooleanVar()
    Gui.chemistry_var = tk.BooleanVar()
 
    Gui.maths_check = tk.Checkbutton(Gui.checkbox_frame, text="Maths", font=('Georgia', 16),variable=Gui.maths_var)
    Gui.physics_check = tk.Checkbutton(Gui.checkbox_frame, text="Physics", font=('Georgia', 16),variable=Gui.physics_var)
    Gui.chemistry_check = tk.Checkbutton(Gui.checkbox_frame, text="Chemistry", font=('Georgia', 16),variable=Gui.chemistry_var)

    #high and low value variable
    Gui.sub_choice_value=tk.IntVar()

    # high and low radio buttons
    Gui.radio_high=tk.Radiobutton(Gui.check_parent,text="Higher than",font=('Georgia', 16),variable=Gui.sub_choice_value, value=1)
    Gui.radio_low=tk.Radiobutton(Gui.check_parent,text="Lower than",font=('Georgia', 16),variable=Gui.sub_choice_value, value=2)

    # Enter value below  label
    Gui.value_label = tk.Label(Gui.check_parent,text="Enter value below",font=('Georgia', 16))

    # command to check if input is number and only 2 digit
    Gui.validate_command =  Gui.root.register(
        lambda new_char, current_value: check_if_num(new_char, current_value)
    )
    Gui.criteria_entry = tk.Entry(Gui.check_parent,font=('Lucida Console', 16),width=10,justify='center',
                        validate="key", validatecommand=(Gui.validate_command, '%S','%P'))

    Gui.search_btn=tk.Button(Gui.check_parent,text="Search",font=('Georgia', 20),command=lambda: check_option(Gui))

    Gui.root.mainloop()

def show_checkboxes(Gui):        
        if Gui.main_choice_value.get() == 1:
            for widget in Gui.checkbox_frame.winfo_children():
                widget.grid_forget()

            Gui.maths_check.grid(row=0, column=0, padx=100, pady=5,sticky="w")
            Gui.physics_check.grid(row=1, column=0, padx=100, pady=5,sticky="w")
            Gui.chemistry_check.grid(row=2, column=0, padx=100, pady=5,sticky="w")
            # high and low boxes
            Gui.radio_high.grid(padx=10,row=0,column=1)
            Gui.radio_low.grid(padx=10,row=0,column=2)

            Gui.value_label.grid(row=1,column=1)
            Gui.criteria_entry.grid(row=2,column=1,pady=0,sticky='n')

            Gui.search_btn.grid(row=4, column=0, columnspan=3, pady=30)

        else: 
            for widget in Gui.checkbox_frame.winfo_children():
                widget.grid_forget()

            Gui.radio_high.grid(padx=20,row=0,column=0)
            Gui.radio_low.grid(padx=80,row=0,column=1)

            Gui.value_label.grid(row=1,column=0,columnspan=3)
            Gui.criteria_entry.grid(row=2,column=0,columnspan=3)

            Gui.search_btn.grid(row=3, column=0, columnspan=3, pady=30)

def check_option(Gui):
    # forget previous window
    Gui.main_frame.pack_forget()
    Gui.check_parent.pack_forget()
    # Check if subject or attendance selected
    if Gui.main_choice_value.get() == 1:
        print("no error")
        filter_by_marks(Gui)
        
    elif Gui.main_choice_value.get() == 2:
        print("no error")
        filter_by_attendance(Gui)
    else:
        Gui.root.quit() 
            
def filter_by_marks(Gui):
    stats = pd.read_excel(Gui.file_path)
    # Gui.maths_var.get() is boolean for checkbox
    # Gui.sub_choice_value.get() holds 1 for above and 2 for below
    # Gui.criteria_entry.get() holds value given by user
    if Gui.maths_var.get():
        if Gui.sub_choice_value.get() == 1:
            stats = stats[stats["Maths"] > int(Gui.criteria_entry.get())]
        elif Gui.sub_choice_value.get() == 2:
            stats = stats[stats["Maths"] < int(Gui.criteria_entry.get())]
        else:
            Gui.root.quit() 
    if Gui.physics_var.get():
        if Gui.sub_choice_value.get() == 1:
            stats = stats[stats["Physics"] > int(Gui.criteria_entry.get())]
        elif Gui.sub_choice_value.get() == 2:
            stats = stats[stats["Physics"] < int(Gui.criteria_entry.get())]
        else:
            Gui.root.quit() 
    if Gui.chemistry_var.get():
        if Gui.sub_choice_value.get() == 1:
            stats = stats[stats["Chemistry"] > int(Gui.criteria_entry.get())]
        elif Gui.sub_choice_value.get() == 2:
            stats = stats[stats["Chemistry"] < int(Gui.criteria_entry.get())]
        else:
            Gui.root.quit() 
    # Frame to display the table 
    Gui.FSD_result_window = tk.Frame(Gui.root)
    Gui.FSD_result_window.pack(fill='x',padx=10, pady=10)
    # style for the treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Tahoma", 12), rowheight=25)  # Adjusted font size and row height for rows
    style.configure("Custom.Treeview.Heading", font=("Tahoma", 14), background="lightgrey", foreground="black")  # Header style

    # Create and configure the table
    columns = list(stats.columns)
    tree = ttk.Treeview(
        Gui.FSD_result_window,
        columns=columns,
        show='headings',
        style="Custom.Treeview",
        height=10  # Adjust the number of rows visible
    )
    tree.pack(side='left', fill='x', expand=True)

    # Set up column headings with adjusted widths
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center', width=100)  # Adjust width to fit the content and smaller fonts

    # Insert all rows from the DataFrame into the table
    for _, row in stats.iterrows():
        tree.insert('', 'end', values=row.tolist())
    # Mainmenu button
    back_button = tk.Button(Gui.root, text="Back to Main Menu", font=('Tahoma', 14), command=Gui.back_to_mainmenu)
    back_button.pack(side='bottom', pady=20)
    Gui.to_be_hidden_list.append(back_button) 

def filter_by_attendance(Gui):
    stats = pd.read_excel(Gui.file_path)

    if Gui.sub_choice_value.get() == 1:
        stats = stats[stats["Attendance"] > int(Gui.criteria_entry.get())]
    elif Gui.sub_choice_value.get() == 2:
        stats = stats[stats["Attendance"] < int(Gui.criteria_entry.get())]
    else:
        Gui.root.quit()
    # Frame to display the table 
    Gui.FSD_result_window = tk.Frame(Gui.root)
    Gui.FSD_result_window.pack(fill='x',padx=10, pady=10)
    # style for the treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Tahoma", 12), rowheight=25)  # Adjusted font size and row height for rows
    style.configure("Custom.Treeview.Heading", font=("Tahoma", 14), background="lightgrey", foreground="black")  # Header style

    # Create and configure the table
    columns = list(stats.columns)
    tree = ttk.Treeview(
        Gui.FSD_result_window,
        columns=columns,
        show='headings',
        style="Custom.Treeview",
        height=10  # Adjust the number of rows visible
    )
    tree.pack(side='left', fill='x', expand=True)

    # Set up column headings with adjusted widths
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center', width=100)  # Adjust width to fit the content and smaller fonts

    for _, row in stats.iterrows():
        tree.insert('', 'end', values=row.tolist())
    # Mainmenu button
    back_button = tk.Button(Gui.root, text="Back to Main Menu", font=('Tahoma', 14), command=Gui.back_to_mainmenu)
    back_button.pack(side='bottom', pady=20)
    Gui.to_be_hidden_list.append(back_button)

if __name__=="__main__":
    FSD_upload()
    