import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog

def check_if_num(char):
    # chceking if input is number
    return char.isdigit()

def Check_filepath(file_label,btn):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls;*.xlsx")])

    if file_path:
        file_label.config(text=file_path)# Update the label with the selected file path
        btn.pack(pady=10) # packing upload button
    else:
        file_label.config(text="No file selected.")
        btn.pack_forget() # unpacking upload button as no file selected

def SAR_upload(Gui):
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
    file_path = Gui.file_label.cget("text")
    # loading excel to dataframe
    stats = pd.read_excel(file_path)
    # remove upload elements 
    Gui.upload_frame.pack_forget()
    # frame for better handling
    Gui.input_frame = tk.Frame(Gui.root)
    Gui.input_frame.pack()
    # lable
    Gui.ask= tk.Label(Gui.input_frame,font=('Tahoma', 16),text="Please enter the roll number")
    Gui.ask.pack(pady=10)
    # roll entry field
    Gui.validate_command = Gui.root.register(check_if_num)
    Gui.roll = tk.Entry(Gui.input_frame, font=('Tahoma', 16), validate="key", validatecommand=(Gui.root.register(check_if_num), '%S'))
    Gui.roll.pack()
    # search btn
    Gui.search_btn = tk.Button(Gui.input_frame,font=('Tahoma', 16),text="Search",command=lambda: get_stats(Gui,stats))
    Gui.search_btn.pack(pady=10)
    
def get_stats(Gui, stats):
    roll = Gui.roll.get().strip()
    roll = int(roll)

    # Hide previous output if any
    for widget in Gui.to_be_hidden_list:
        if widget.winfo_ismapped():  # Check if widget is currently visible 
            widget.pack_forget()

    student = stats[stats['Roll'] == roll]

    # Check if the student record is empty
    if student.empty:
        empty_msg = tk.Label(Gui.root, text="No student found with the given roll number", font=("Tahoma", 14))
        empty_msg.pack(pady=10)
        Gui.to_be_hidden_list.append(empty_msg) # Save this label to hide it later
    else:
        # Create a frame to hold the table
        table_frame = tk.Frame(Gui.root)
        table_frame.pack(fill='x', padx=10, pady=10)
        Gui.to_be_hidden_list.append(table_frame) 
        
        # Define custom styles with smaller font size
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Tahoma", 12))  # Smaller font size for rows
        style.configure("Custom.Treeview.Heading", font=("Tahoma", 14))  # Smaller font size for headers

        # Create and configure the table
        columns = list(student.columns)
        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            style="Custom.Treeview",
            height=2
        )
        table.pack(side='left', fill='x', expand=True)

        # Set up column headings with adjusted widths
        for col in columns:
            table.heading(col, text=col)
            table.column(col, anchor='center', width=100)  # Adjust width to fit smaller fonts

        # Insert the student's row into the table
        table.insert('', 'end', values=student.iloc[0].tolist())

        # check if failed in any
        verify = True
        result_str=[]
        if student['Maths'].values[0] < 30:
            verify = False
            result_str.append("Failed in Maths")
        if student['Physics'].values[0] < 30:
            verify = False
            result_str.append("Failed in Physics")
        if student['Chemistry'].values[0] < 30:
            verify = False
            result_str.append("Failed in Chemistry")
        if verify:
            result_str.append("Passed")

        # Create a result string with new lines
        result_text = "\n".join(result_str)

        # Create a frame for the result
        conclude_frame = tk.Frame(Gui.root)
        conclude_frame.pack(fill='x', padx=10, pady=10)
        Gui.to_be_hidden_list.append(conclude_frame) # Save this label to hide it later

        # Create the conclude label
        conclude_label = tk.Label(conclude_frame, text=result_text, font=("Tahoma", 14), anchor='w')
        conclude_label.pack(pady=5)

        # getting attendance
        attendance = stats[stats['Roll'] == roll]['Attendance'].values[0]

        attendance_label = tk.Label(conclude_frame, text=f"Attendance   - {attendance}%", font=("Tahoma", 14), anchor='w')
        attendance_label.pack(pady=10)

        # low attendance check
        if attendance < 70:
            attendance_low = tk.Label(conclude_frame,text="The attendance is below the standards set by the institute.",font=("Tahoma", 14),)
            attendance_low.pack(pady=2)
        # mainmenu button
        back_button = tk.Button(Gui.root, text="Back to Main Menu", font=('Tahoma', 14), command=Gui.back_to_mainmenu)
        back_button.pack(side='bottom', pady=20)
        Gui.to_be_hidden_list.append(back_button) 

if __name__=="__main__":
    SAR_upload()
