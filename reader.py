import os
import re
import sys
import tkinter
from tkinter import messagebox
from tkinter import filedialog

class GUI:
    def __init__(self):
        self.path = None

        while not self.path:
            user_path = filedialog.askdirectory(title="Select the Directory you would like to Read")
            if user_path:
                self.path = user_path
            else:
                if not messagebox.askyesno("No Directory Selected!", "You have to select a directory to continue. Would you like to try again?"):
                    sys.exit()

        self.root = tkinter.Tk()

        self.root.title("File Reader App")
        self.root.geometry("470x580")
        self.root.configure(bg="#4A4A4A")

        tkinter.Label(self.root, 
                      text=f"Path: {self.path}",
                      bg="#4A4A4A", 
                      fg="white", 
                      font=("Roboto", 14,)
                      ).grid(row=0, columnspan=2, pady=5)

        tkinter.Label(self.root, text="Year:", 
                      bg="#4A4A4A", 
                      fg="white", 
                      font=("Roboto", 14)
                      ).grid(row=1, column=0, pady=5)
        
        tkinter.Label(self.root, 
                      text="Month:", 
                      bg="#4A4A4A", 
                      fg="white", 
                      font=("Roboto", 14)
                      ).grid(row=2, column=0, pady=5)
        
        tkinter.Label(self.root, 
                      text="Day:", 
                      bg="#4A4A4A", 
                      fg="white", 
                      font=("Roboto", 14)
                      ).grid(row=3, column=0, pady=5)

        self.year_entry = tkinter.Entry(self.root, font=("Roboto", 14))
        self.year_entry.grid(row=1, column=1)
        self.month_entry = tkinter.Entry(self.root, font=("Roboto", 14))
        self.month_entry.grid(row=2, column=1)
        self.day_entry = tkinter.Entry(self.root, font=("Roboto", 14))
        self.day_entry.grid(row=3, column=1)

        self.root.bind("<Return>", self.enter_shortcut)
        self.root.bind("<Control-r>", self.refresh_shortcut)
        
        tkinter.Button(self.root, 
                       text="Read Files", 
                       command=self.find_file, 
                       bg="#4A4A4A", 
                       fg="white", 
                       font=("Roboto", 14),
                       activebackground="#8E4585"
                       ).grid(row=4, columnspan=2, padx=(30, 0), pady=5, sticky="we")

        tkinter.Button(self.root, 
                text="Refresh", 
                command=self.refresh,
                bg="#4A4A4A", 
                fg="white", 
                font=("Roboto", 14),
                activebackground="#8E4585"
                ).grid(row=5, columnspan=2, padx=(30, 0), pady=5, sticky="we")

        self.scroller = tkinter.Scrollbar(self.root)
        self.scroller.grid(row=6, column=3, pady=5, sticky="ns")

        self.output_list = tkinter.Listbox(self.root, height=16, width=47, font=("Roboto", 12))
        self.output_list.grid(row=6, columnspan=2, padx=(12, 0), pady=5)

        self.output_list.config(yscrollcommand= self.scroller.set)
        self.scroller.config(command=self.output_list.yview)

        self.root.mainloop()


    def read_files(self):
        self.files = []
        date_list = []
        pattern = r"^Y([0-9]{4})M(0[0-9]|1[0-2])D(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.[0-9]{4}$"
        for file in os.scandir(self.path):
            matches = re.match(pattern, file.name)
            if file.is_file() and matches:
                self.files.append(file.name)
                date = []
                y = int(matches.group(1))
                m = int(matches.group(2))
                d = int(matches.group(3))
                date.append(y)
                date.append(m)
                date.append(d)
                date_list.append(date)
        return date_list


    def refresh(self):
        self.files = self.read_files()
        self.find_file()


    def find_file(self):
        date_list = self.read_files()

        y = self.year_entry.get().strip()
        m = self.month_entry.get().strip()
        d = self.day_entry.get().strip()
        found = False

        try:
            if y and m and d:
                y = int(self.year_entry.get())
                m = int(self.month_entry.get())
                d = int(self.day_entry.get())

                self.output_list.delete(0, tkinter.END)
                for index, filename in enumerate(date_list):
                    if y == filename[0] and m == filename[1] and d == filename[2]:
                        self.output_list.insert(tkinter.END, self.files[index])
                        found = True

            elif y and not m and not d:
                y = int(self.year_entry.get())
                
                self.output_list.delete(0, tkinter.END)
                for index, filename in enumerate(date_list):
                    if y == filename[0]:
                        self.output_list.insert(tkinter.END, self.files[index])
                        found = True
            elif not y and m and not d:
                    m = int(self.month_entry.get())
                
                    self.output_list.delete(0, tkinter.END)
                    for index, filename in enumerate(date_list):
                        if m == filename[1]:
                            self.output_list.insert(tkinter.END, self.files[index])
                            found = True
            elif not y and not m and d:
                    d = int(self.day_entry.get())
                
                    self.output_list.delete(0, tkinter.END)
                    for index, filename in enumerate(date_list):
                        if d == filename[2]:
                            self.output_list.insert(tkinter.END, self.files[index])
                            found = True
            if not found:
                self.output_list.insert(tkinter.END, "No matching files")
        except ValueError:
            messagebox.showerror("Value Error!", "Please double check your value(s)")


    def enter_shortcut(self, event):
        self.find_file()


    def refresh_shortcut(self, event):
        self.refresh()

if __name__ == "__main__":
    GUI()
