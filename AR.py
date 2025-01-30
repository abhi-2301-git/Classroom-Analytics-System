import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog

def Check_filepath(file_label,btn):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls;*.xlsx")])

    if file_path:
        file_label.config(text=file_path)  # Update the label with the selected file path
        btn.pack(pady=10) # pack upload button
    else:
        file_label.config(text="No file selected.")
        btn.pack_forget() #unpack upload button as no file selected

def AR_upload(Gui):
    # Create a frame for the file upload process
    Gui.upload_frame = tk.Frame(Gui.root)
    Gui.upload_frame.pack()

    # Title
    Gui.welcome = tk.Label(Gui.upload_frame,text="Upload File",font=('Georgia', 20))
    Gui.welcome.pack(pady=10)

    # stores file path
    Gui.file_label = tk.Label(Gui.upload_frame, text="", font=('Arial', 12), fg="blue")
    Gui.file_label.pack(pady=10)

    # upload button
    Gui.upload_btn = tk.Button(Gui.upload_frame,text="Uplaod File",font=('Tahoma', 14),command=lambda: get_filepath(Gui))

    # select button
    Gui.select_btn = tk.Button(Gui.upload_frame,text="Select File",font=('Tahoma', 14),command=lambda: Check_filepath(Gui.file_label,Gui.upload_btn))
    Gui.select_btn.pack(pady=10)

def get_filepath(Gui):
    # getting file path
    Gui.file_path = Gui.file_label.cget("text")
    make_report(Gui)

def make_report(Gui):
    # remove upload elements 
    Gui.upload_frame.pack_forget()

    # main frame
    Gui.main_frame = tk.Frame(Gui.root)
    Gui.main_frame.pack(pady=10, padx=10,fill=tk.BOTH, expand=True)
    # headings
    student_with_high_attendance = tk.Label(Gui.main_frame, text="Student with high attendance", font=('Tahoma', 14))
    student_with_low_attendance = tk.Label(Gui.main_frame, text="Student with low attendance", font=('Tahoma', 14))
    student_with_high_attendance.grid(row=0, column=0, padx=10)
    student_with_low_attendance.grid(row=0, column=1, padx=10)
    Gui.main_frame.grid_columnconfigure(0, weight=1)
    Gui.main_frame.grid_columnconfigure(1, weight=1)
    # dataframe
    stats = pd.read_excel(Gui.file_path)

    # high attendance
    high_attendance_dataframe = stats[stats["Attendance"] > 95][["Name", "Attendance"]]

    # low attendance
    low_attendance_dataframe = stats[stats["Attendance"] < 70][["Name", "Attendance"]]

    # sorting
    high_attendance_dataframe = high_attendance_dataframe.sort_values(by="Attendance", ascending=False)
    low_attendance_dataframe = low_attendance_dataframe.sort_values(by="Attendance", ascending=True)

    # treeview
    high_attendance_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Attendance"), show="headings")
    for _,row in high_attendance_dataframe.iterrows():
        high_attendance_tree.insert("", "end", values=(row["Name"], row["Attendance"]))

    # treeview
    low_attendance_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "A  ttendance"), show="headings")
    for _,row in low_attendance_dataframe.iterrows():
        low_attendance_tree.insert("", "end", values=(row["Name"], row["Attendance"]))

    # packing
    high_attendance_tree.grid(row=1, column=0, padx=10)
    low_attendance_tree.grid(row=1, column=1, padx=10)

    # total students with high attendance
    total_low_attendance = len(low_attendance_dataframe)
    low_attendance_label = tk.Label(Gui.main_frame, text=f"Total students with low attendance: {total_low_attendance}", font=('Tahoma', 13))
    low_attendance_label.grid(row=2, column=1, padx=10)

    #mainmenu button
    back_button = tk.Button(Gui.root, text="Back to Main Menu", font=('Tahoma', 14), command=Gui.back_to_mainmenu)
    back_button.pack(side='bottom', pady=20)
    Gui.to_be_hidden_list.append(back_button)

if __name__=="__main__":
    AR_upload()