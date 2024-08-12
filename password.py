import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 5:
            raise ValueError("Password length must be greater than 5.")
        
        characters = ((string.ascii_lowercase if lowercase_var.get() else '') +
                      (string.ascii_uppercase if uppercase_var.get() else '') +
                      (string.digits if digits_var.get() else '') +
                      (string.punctuation if punctuation_var.get() else '')
                    )
        
        if not characters:
            messagebox.showerror("Error", "You must select at least one character type.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        generated_password.set(password)

    except ValueError as a :
        messagebox.showerror("Error", str(a))

root = tk.Tk()
root.geometry("290x230")
root.title("Password Generator")

length_label = tk.Label(root, text="Password length:").grid(row=0, column=0, padx=3)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Lowercase", variable=lowercase_var).grid(row=1, columnspan=2, pady=2, sticky=tk.W)

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Uppercase", variable=uppercase_var).grid(row=2, columnspan=2, pady=2, sticky=tk.W)

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Digits", variable=digits_var).grid(row=3, columnspan=2, pady=2, sticky=tk.W)

punctuation_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Punctuation", variable=punctuation_var).grid(row=4, columnspan=2, pady=2, sticky=tk.W)

tk.Button(root, text="Generate", command=generate_password).grid(row=5, columnspan=2, pady=10)

generated_password = tk.StringVar()
tk.Label(root, text="Password:").grid(row=6, column=0)
tk.Entry(root, textvariable=generated_password, state="readonly").grid(row=6, column=1)

root.mainloop()


