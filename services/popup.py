import tkinter as tk
from tkinter import simpledialog

def popup(head, prompt):        
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title=head, prompt=prompt)
    return USER_INP