import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    lst = ['a', 'b', 'c']
    lstvar = tk.Variable(value=lst)
    lb = tk.Listbox(root, listvariable=lstvar, height=10, selectmode=tk.SINGLE)
    lb.bind('<Button-3>', lambda x: print(lb.get(lb.curselection())))
    lb.pack()
    root.mainloop()