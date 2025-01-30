import tkinter as tk
from SAR import SAR_upload
from FSD import FSD_upload
from CAR import CAR_upload
from AR import AR_upload

class Gui:
    def __init__(self):
        # root title geometry
        self.root = tk.Tk()
        self.root.geometry("1000x500")
        self.root.title("Classroom Analytics System")
        self.root.resizable(False, False) 

        self.to_be_hidden_list = []

        # Initialize the main menu
        self.mainmenu = tk.Frame(self.root)
        self.mainmenu.pack()
        
        # Add a welcome label to the main menu
        self.welcome = tk.Label(self.mainmenu, text="WELCOME", font=('Georgia', 20))
        self.welcome.pack(pady=10)

        self.mainmenu_buttons() # Setup main menu buttons

        self.root.mainloop()
        
    def mainmenu_buttons(self):
        self.button1 = tk.Button(self.mainmenu, text="Student Academic Report", font=('Tahoma', 14), command=self.show_student_report)
        self.button1.pack(padx=10, pady=10, fill='x')

        self.button2 = tk.Button(self.mainmenu, text="Class Academic Report", font=('Tahoma', 14), command=self.show_class_report)
        self.button2.pack(padx=10, pady=10, fill='x')

        self.button3 = tk.Button(self.mainmenu, text="Attendance Report", font=('Tahoma', 14), command=self.show_attendance_report)
        self.button3.pack(padx=10, pady=10, fill='x')

        self.button4 = tk.Button(self.mainmenu, text="Filter Student Data", font=('Tahoma', 14), command=self.filter_student_data)
        self.button4.pack(padx=10, pady=10, fill='x')

        self.button5 = tk.Button(self.mainmenu, text="Exit", font=('Tahoma', 14), command=self.exit_program)
        self.button5.pack(padx=10, pady=10, fill='x')

        self.by_abhinav_label = tk.Label(self.mainmenu, text="By Abhinav", font=('Georgia', 10))
        self.by_abhinav_label.pack(pady=10)

    def show_student_report(self):
        self.mainmenu.pack_forget()
        SAR_upload(self)  

    def show_class_report(self):
        self.mainmenu.pack_forget()
        CAR_upload(self)

    def show_attendance_report(self):
        self.mainmenu.pack_forget()
        AR_upload(self)

    def filter_student_data(self):
        self.mainmenu.pack_forget()
        FSD_upload(self) 

    def exit_program(self):
        self.root.quit()  # Close the program

    def reset_to_mainmenu(self):
        # Reset the screen and re-show the main menu
        for widget in self.root.winfo_children():
            widget.pack_forget()
        # mainmenu frame
        self.mainmenu = tk.Frame(self.root)
        self.mainmenu.pack()

        # Add welcome label again
        self.welcome = tk.Label(self.mainmenu, text="WELCOME", font=('Georgia', 20))
        self.welcome.pack(pady=10)

        self.mainmenu_buttons()  # Show the main menu buttons again

    def back_to_mainmenu(self):
        # This function can be used for any screen to go back to the main menu
        self.reset_to_mainmenu()

# Running the application
if __name__ == "__main__":
    Gui()
