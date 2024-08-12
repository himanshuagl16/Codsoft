import tkinter as tk
from tkinter import messagebox

def add_task(entry,listbox):
    task=entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Input Error","please enter a task")

def update_task(entry,listbox):
    selected_task_index=listbox.curselection()
    if selected_task_index:
        new_task=entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index,new_task)        
            entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Input Error","Please enter a task")
    else:
        messagebox.showwarning("selection error","Please select a task to update")
def delete_task(listbox):
    selected_task_index=listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("selection error","Please select a task to delete")    
def main():
    root=tk.Tk()
    root.title("To-Do Application")

    task_listbox=tk.Listbox(root,selectmode=tk.SINGLE,width=75,height=25)
    task_listbox.pack(padx=10,pady=5)

    add_task_entry=tk.Entry(root,width=50)
    add_task_entry.pack(padx=10,pady=5)

    add_task_button=tk.Button(root,text="Add Task",command=lambda:add_task(add_task_entry,task_listbox))
    add_task_button.pack(padx=10,pady=5)

    update_task_button=tk.Button(root,text="Update Task",command=lambda:update_task(add_task_entry,task_listbox))
    update_task_button.pack(padx=10,pady=5)
    
    delete_task_button=tk.Button(root,text="Delete Task",command=lambda:delete_task(task_listbox))
    delete_task_button.pack(padx=10,pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
    
 
