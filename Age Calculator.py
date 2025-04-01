import datetime
import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.geometry("500x500")
window.configure(bg='light blue')
window.title("Age Calculator App")

# Show message
messagebox.showinfo("Age Calculator", "Click here to calculate your age")

# Labels
tk.Label(text="Name", bg='orange').grid(column=0, row=1)
tk.Label(text="Year", bg='white').grid(column=0, row=2)
tk.Label(text="Month", bg='green').grid(column=0, row=3)
tk.Label(text="Day").grid(column=0, row=4) 

# Entry fields
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1  # Adjust if the birthday hasn't occurred yet this year
        return age

def getInput():
    try:
        name = nameEntry.get()
        birthdate = datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get()))
        person = Person(name, birthdate)
        
        answer = f"Hey {person.name}! You are {person.age()} years old."
        
        # Display output in a text box
        textArea = tk.Text(master=window, height=15, width=50) 
        textArea.grid(column=1, row=6)
        textArea.insert(tk.END, answer)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for Date, Month, and Year.")

# Button to calculate age
tk.Button(window, text="Calculate Age", command=getInput, bg="red").grid(column=1, row=5)

window.mainloop()
