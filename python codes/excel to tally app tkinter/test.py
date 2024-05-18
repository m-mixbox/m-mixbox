import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import xml_tree_generator as x_tree
import master_generater as master

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label_username = tk.Label(self, text="Username:")
        self.label_password = tk.Label(self, text="Password:")
        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        self.button_login = tk.Button(self, text="Login", command=self.login)

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "admin" and password == "MBSPL@2024":
            self.controller.show_frame(DashboardPage)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class DashboardPage(tk.Frame):
    def voucher_converter(self):
        try:
            input_file_path = filedialog.askopenfilename(title="Select Input File",filetypes=[("Excel files", ".xlsx .xls")])
            try :
                output_file_path = filedialog.askdirectory(title="Select Output Folder")
                directory = x_tree.xml_generater(input_file_path,output_file_path)
                output = 'File is in ' + output_file_path
                messagebox.showinfo("File Converted Successfully", output)
            except FileNotFoundError as e:
                error , output_file_path = x_tree.create_directory()
                directory = x_tree.xml_generater(input_file_path,output_file_path)
                output = 'File is in ' + directory
                messagebox.showinfo("File Converted Successfully", output)
        except FileNotFoundError as e:
            messagebox.showinfo("Error", str(e))

    def master_converter(self):
        try:
            input_file_path = filedialog.askopenfilename(title="Select Input File",filetypes=[("Excel files", ".xlsx .xls")])
            try :
                output_file_path = filedialog.askdirectory(title="Select Output Folder")
                directory = master.generate_xml(input_file_path,output_file_path)
                output = 'File is in ' + output_file_path
                messagebox.showinfo("File Converted Successfully", output)
            except FileNotFoundError as e:
                error , output_file_path = x_tree.create_directory()
                directory = master.generate_xml(input_file_path,output_file_path)
                output = 'File is in ' + directory
                messagebox.showinfo("File Converted Successfully", output)
        except FileNotFoundError as e:
            messagebox.showinfo("Error", str(e))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text="Dashboard Page")
        label.pack()
        instruction_label = tk.Label(self, text="Select your input file", font=("Arial", 12))
        instruction_label.pack()
        convert_button_voucher = tk.Button(self, text="excel to tally voucher", font=("Arial", 14), command=self.voucher_converter)
        convert_button_voucher.pack(pady=20)
        convert_button_master = tk.Button(self, text="excel to tally master", font=("Arial", 14), command=self.master_converter)
        convert_button_master.pack(pady=20)

        button_logout = tk.Button(self, text="Logout", command=self.logout)
        button_logout.pack()

    def logout(self):
        self.controller.show_frame(LoginPage)

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        title_label = tk.Label(self, text="Convert Your Files Easily!", font=("Arial", 18))
        title_label.pack(pady=20)
        #instruction_label = tk.Label(self, text="Select your input file", font=("Arial", 12))
        #instruction_label.pack()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("500x450")  # Adjust window size as needed

    # Top label with title and instructions
        

    # Single button with clear icon and functionality
        #convert_button_excel = tk.Button(self, text="excel to tally ", font=("Arial", 14) )
        #convert_button_excel.pack(pady=20)

        self.frames = {}
        for F in (LoginPage, DashboardPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
