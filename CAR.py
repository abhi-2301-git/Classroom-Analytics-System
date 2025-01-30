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

def CAR_upload(Gui):
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
    maths_top_label = tk.Label(Gui.main_frame, text="Topper in Maths", font=('Tahoma', 14))
    physics_top_label = tk.Label(Gui.main_frame, text="Topper in Physics", font=('Tahoma', 14))
    chemistry_top_label = tk.Label(Gui.main_frame, text="Topper in Chemistry", font=('Tahoma', 14))

    # formatting
    Gui.main_frame.grid_columnconfigure(0, weight=1)
    Gui.main_frame.grid_columnconfigure(1, weight=1)
    Gui.main_frame.grid_columnconfigure(2, weight=1)

    # packing headings
    maths_top_label.grid(row=0, column=0, padx=10)
    physics_top_label.grid(row=0, column=1, padx=10)
    chemistry_top_label.grid(row=0, column=2, padx=10)

    # dataframe
    stats = pd.read_excel(Gui.file_path)

    # maths topper dataframe
    maths_topper_dataframe = stats[stats["Maths"] > 80][["Name", "Maths"]]
    maths_topper_dataframe = maths_topper_dataframe.sort_values(by="Maths", ascending=False)

    # physics topper dataframe
    physics_topper_dataframe = stats[stats["Physics"] > 80][["Name", "Physics"]]
    physics_topper_dataframe = physics_topper_dataframe.sort_values(by="Physics", ascending=False)

    # chemistry topper dataframe
    chemistry_topper_dataframe = stats[stats["Chemistry"] > 80][["Name", "Chemistry"]]
    chemistry_topper_dataframe = chemistry_topper_dataframe.sort_values(by="Chemistry", ascending=False)

    # Treeview for Maths toppers
    maths_top_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Maths"), show="headings", height=5)
    for _, row in maths_topper_dataframe.iterrows():
        maths_top_tree.insert("", "end", values=(row["Name"], row["Maths"]))
    maths_top_tree.grid(row=1, column=0, padx=10)

    # Treeview for Physics toppers
    physics_top_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Physics"), show="headings", height=5)
    for _, row in physics_topper_dataframe.iterrows():
        physics_top_tree.insert("", "end", values=(row["Name"], row["Physics"]))
    physics_top_tree.grid(row=1, column=1, padx=10)

    # Treeview for Chemistry toppers
    chemistry_top_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Chemistry"), show="headings", height=5)
    for _, row in chemistry_topper_dataframe.iterrows():
        chemistry_top_tree.insert("", "end", values=(row["Name"], row["Chemistry"]))
    chemistry_top_tree.grid(row=1, column=2, padx=10)

    # failed labels
    maths_failed_label = tk.Label(Gui.main_frame, text="Failed in Maths", font=('Tahoma', 14))
    physics_failed_label = tk.Label(Gui.main_frame, text="Failed in Physics", font=('Tahoma', 14))
    chemistry_failed_label = tk.Label(Gui.main_frame, text="Failed in Chemistry", font=('Tahoma', 14))

    # formatting
    Gui.main_frame.grid_columnconfigure(0, weight=1)
    Gui.main_frame.grid_columnconfigure(1, weight=1)
    Gui.main_frame.grid_columnconfigure(2, weight=1)

    # packing failed labels
    maths_failed_label.grid(row=2, column=0, padx=10)
    physics_failed_label.grid(row=2, column=1, padx=10)
    chemistry_failed_label.grid(row=2, column=2, padx=10)

    # maths failed dataframe
    maths_failed_dataframe = stats[stats["Maths"] < 30][["Name", "Maths"]]
    maths_failed_dataframe = maths_failed_dataframe.sort_values(by="Maths", ascending=True)

    # physics failed dataframe
    physics_failed_dataframe = stats[stats["Physics"] < 30][["Name", "Physics"]]
    physics_failed_dataframe = physics_failed_dataframe.sort_values(by="Physics", ascending=True)

    # chemistry failed dataframe
    chemistry_failed_dataframe = stats[stats["Chemistry"] < 30][["Name", "Chemistry"]]
    chemistry_failed_dataframe = chemistry_failed_dataframe.sort_values(by="Chemistry", ascending=True)

    # Treeview for Maths failed students
    maths_fail_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Maths"),show="headings", height=5)
    for _,row in maths_failed_dataframe.iterrows():
        maths_fail_tree.insert("","end",values=(row["Name"],row["Maths"]))
    maths_fail_tree.grid(row=3, column=0, padx=10)

    # Treeview for Physics failed students
    physics_fail_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Physics"),show="headings", height=5)
    for _,row in physics_failed_dataframe.iterrows():
        physics_fail_tree.insert("","end",values=(row["Name"],row["Physics"]))
    physics_fail_tree.grid(row=3, column=1, padx=10)

    # Treeview for Chemistry failed students
    chemistry_fail_tree = ttk.Treeview(Gui.main_frame, columns=("Name", "Chemistry"),show="headings", height=5)
    for _,row in chemistry_failed_dataframe.iterrows():
        chemistry_fail_tree.insert("","end",values=(row["Name"],row["Chemistry"]))
    chemistry_fail_tree.grid(row=3, column=2, padx=10)

    # maths passing percentage
    maths_passing_percentage=stats[stats["Maths"]>30].shape[0]/stats.shape[0]*100
    maths_passing_label = tk.Label(Gui.main_frame, text=f"Passing Percentage in Maths: {maths_passing_percentage:.2f}%", font=('Tahoma', 12))
    maths_passing_label.grid(row=4, column=0, pady=10)

    # physics passing percentage
    physics_passing_percentage=stats[stats["Physics"]>30].shape[0]/stats.shape[0]*100
    physics_passing_label = tk.Label(Gui.main_frame, text=f"Passing Percentage in Physics: {physics_passing_percentage:.2f}%", font=('Tahoma', 12))
    physics_passing_label.grid(row=4, column=1, pady=10)

    # chemistry passing percentage
    chemistry_passing_percentage=stats[stats["Chemistry"]>30].shape[0]/stats.shape[0]*100
    chemistry_passing_label = tk.Label(Gui.main_frame, text=f"Passing Percentage in Chemistry: {chemistry_passing_percentage:.2f}%", font=('Tahoma', 12))
    chemistry_passing_label.grid(row=4, column=2, pady=10)

    # average attendance
    avg_attendance = stats["Attendance"].mean()
    attendance_label = tk.Label(Gui.main_frame, text=f"Average Attendance: {avg_attendance:.2f}%", font=('Tahoma', 12))
    attendance_label.grid(row=5, column=1, pady=10)

    # Mainmenu button
    back_button = tk.Button(Gui.root, text="Back to Main Menu", font=('Tahoma', 14), command=Gui.back_to_mainmenu)
    back_button.pack(side='bottom', pady=20)
    Gui.to_be_hidden_list.append(back_button)

if __name__=="__main__":
    CAR_upload()