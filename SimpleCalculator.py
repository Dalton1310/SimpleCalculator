from tkinter import ttk
import tkinter as tk

root = tk.Tk()

root.config(width=1920, height=1080, bg="light blue")
root.title("Simple Calculator")
root.attributes('-fullscreen',True)

#Close function
def Close():
    root.destroy()

#Validate decimal value
#def validate():
    

#Shows welcome message at top of the screen
calculator_title = tk.Label(text="Welcome to the Simple Calculator!", font=('Times', '25'), fg="black", bg="light blue")
calculator_title.pack(side='top', anchor='center', pady=20)

term_one = ttk.Entry()
term_one.place(relx=0.35, rely=0.25, relwidth=0.10, relheight=0.05)

current_symbol = tk.StringVar()
math_symbol = ttk.Combobox(root, textvariable=current_symbol, state='readonly')
math_symbol['values'] = ('+', '-', '/', '*', '%')
math_symbol.place(relx=0.48, rely=0.25, relwidth=0.04, relheight=0.05)

term_two = ttk.Entry()
term_two.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.05)

exit_button = tk.Button(root, text="Exit Application", font=('Times', '15'), command=Close)
exit_button.place(relx=0.4, rely=0.85, relwidth=0.2)

root.mainloop()