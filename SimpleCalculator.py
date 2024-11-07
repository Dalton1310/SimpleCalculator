from tkinter import ttk
import tkinter as tk

root = tk.Tk()
my_menu = tk.Menu(root)

#Stylize Root
root.config(width=1920, height=1080, bg="#262626", menu=my_menu)
root.title("Simple Calculator")
root.attributes('-fullscreen',True)


theme_menu = tk.Menu(my_menu, tearoff=0)
our_themes = ttk.Style().theme_names()
my_menu.add_cascade(label="Themes",menu = theme_menu)

#Change Style
def changer(theme):
    style.theme_use(theme)

#Sub menu
for  t in our_themes:
    theme_menu.add_command(label=t, command = lambda t = t: changer(t))

#Define the Style
style = ttk.Style()
#style.theme_use("default")

#Widget Style Names
base_style = {'foreground': "#0adcf7", 'background': "#262626", 'font': ('Times', '20')}

# Apply the base style to each specific widget type
for widget in ['TButton', 'TEntry', 'TLabel', 'TCombobox']:
    style.configure(f'elder.{widget}', **base_style)


#Close function
def Close():
    root.destroy()

#Validate decimal value
#def validate():
    

#Shows welcome message at top of the screen
calculator_title = ttk.Label(text="Welcome to the Simple Calculator!", font=('Times','25'))
calculator_title.pack(side='top', anchor='center', pady=20)

term_one = ttk.Entry(style="elder.TEntry")
term_one.place(relx=0.35, rely=0.25, relwidth=0.10, relheight=0.05)

current_symbol = tk.StringVar()
math_symbol = ttk.Combobox(root, textvariable=current_symbol, state='readonly',style="elder.TCombobox")
math_symbol['values'] = ('+', '-', '/', '*', '%')
math_symbol.place(relx=0.48, rely=0.25, relwidth=0.04, relheight=0.05)

term_two = ttk.Entry(style="elder.TEntry")
term_two.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.05)

exit_button = ttk.Button(root, text="Exit Application", command=Close, style="elder.TButton")
exit_button.place(relx=0.4, rely=0.85, relwidth=0.2)

root.mainloop()