import tkinter as tk
from tkinter import simpledialog

def popup(head, prompt):
    """Prompts the user for input
    
    Parameters:
        head (string): Title of pop up window
        prompt (string): Text to display in window

    Returns:
        USER_INP (string): Users input
    """
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title=head, prompt=prompt)
    return USER_INP

def passpopup(head, prompt):
    """Prompts the user for password input
    
    Parameters:
        head (string): Title of pop up window
        prompt (string): Text to display in window

    Returns:
        USER_INP (string): Users input
    """        
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title=head, prompt=prompt, show='*')
    return USER_INP

# merge functions and split with conditional statements to comply with DRY principles



