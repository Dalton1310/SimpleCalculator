from tkinter import ttk
import tkinter as tk

def switch_page(page_name):
    # Clear the content frame and add content for the selected page
    for widget in content_frame.winfo_children():
        widget.pack_forget()  # Hide the current frame before showing the new one

    if page_name == "Calculator":
        calculator_frame.pack(fill="both", expand=True)
    elif page_name == "Test":
        test_frame.pack(fill="both", expand=True)

root = tk.Tk()
my_menu = tk.Menu(root)

# Stylize Root
root.config(width=1920, height=1080, bg="#262626", menu=my_menu)
root.title("Simple Calculator")
root.attributes('-fullscreen', True)
root.option_add('*TCombobox*Listbox.font', ('Times', '15'))

# Frame for the navigation panel
nav_frame = ttk.Frame(root)
nav_frame.place(relwidth=0.2, relheight=1)

# Content frame where different pages will be displayed
content_frame = ttk.Frame(root)
content_frame.place(relx=0.2, relwidth=0.8, relheight=1)  # Make content_frame occupy the rest of the space

# Define the Style
style = ttk.Style()
# Widget Style Names
base_style = {'foreground': "#0adcf7", 'background': "#262626", 'font': ('Times', '20')}
for widget in ['TButton', 'TEntry', 'TLabel', 'TCombobox']:
    style.configure(f'{widget}', **base_style)
style.configure("TCombobox", foreground="#0adcf7", font=('Times', '20'), padding=5, arrowsize=2, arrowcolor="White")
style.configure("Calculator.TFrame", background="#262626")

# Calculator frame that will hold all calculator-related widgets
calculator_frame = ttk.Frame(content_frame, style="Calculator.TFrame")
test_frame = ttk.Frame(content_frame, style="Calculator.TFrame")

# Define Listbox for navigation
nav_listbox = tk.Listbox(nav_frame)
nav_listbox.pack(fill="y", expand=True)  # Ensure it takes up the full height of nav_frame

# Insert items/pages into the Listbox
pages = ["Calculator", "Test"]
for page in pages:
    nav_listbox.insert("end", page)

# Bind the Listbox selection to switch pages
def on_nav_select(event):
    selection = nav_listbox.curselection()
    if selection:
        page_name = nav_listbox.get(selection[0])
        switch_page(page_name)

nav_listbox.bind("<<ListboxSelect>>", on_nav_select)

theme_menu = tk.Menu(my_menu, tearoff=0)
our_themes = ttk.Style().theme_names()
my_menu.add_cascade(label="Themes", menu=theme_menu)

# Change Style
def changer(theme):
    style.theme_use(theme)

# Sub menu
for t in our_themes:
    theme_menu.add_command(label=t, command=lambda t=t: changer(t))

# Close application function
def Close():
    root.destroy()

# Validate decimal values of both terms
def validate():
    if term_one.get().isdecimal() and term_two.get().isdecimal():
        calculate()
    else:
        error_val["text"] = "One of your terms has an invalid character or is empty!"
        total_label['text'] = ""

# Calculates the end result once the user data is validated
def calculate():
    result = 0
    error_val['text'] = ""
    first_term = float(term_one.get())
    second_term = float(term_two.get())
    symbol = current_symbol.get()
    match symbol:
        case '+':
            result = first_term + second_term
        case '-':
            result = first_term - second_term
        case '*':
            result = first_term * second_term
        case '/':
            if second_term == 0:
                error_val["text"] = "Cannot Divide by 0!"
                return
            else:
                result = first_term / second_term
        case '%':
            result = first_term % second_term
    total_label['text'] = f"The total is: {result}"
    total_label.place(relx=0.45, rely=0.60, anchor=tk.CENTER)

# Shows welcome message at top of the screen
calculator_title = ttk.Label(calculator_frame, text="Welcome to the Simple Calculator!",
                             style="TLabel", font=('Times', '25'))
calculator_title.pack(side='top', anchor='center', pady=20)

# Entry that is used as the first term for calculations
term_one = ttk.Entry(calculator_frame, style="TEntry", foreground="black", font=('Times', '20'))
term_one.place(relx=0.35, rely=0.25, relwidth=0.10, relheight=0.05)

# Combobox that is used as the mathematical symbol for calculations
current_symbol = tk.StringVar()
math_symbol = ttk.Combobox(calculator_frame, textvariable=current_symbol, 
                           state='readonly', style="TCombobox", font=('Times', '20'))
math_symbol['values'] = ('+', '-', '/', '*', '%')
math_symbol.place(relx=0.48, rely=0.25, relwidth=0.04, relheight=0.05)

# Entry that is used as the second term for calculations
term_two = ttk.Entry(calculator_frame, style="TEntry", foreground="black", font=('Times', '20'))
term_two.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.05)

# Any potential Error messages shown to user
error_val = ttk.Label(calculator_frame, style="TLabel")
error_val.place(anchor=tk.CENTER, relx=0.5, rely=0.35)

# Button that calls for validation of user input and to calculate the function if valid data
calculate_button = ttk.Button(calculator_frame, text="Calculate", command=validate, style="TButton")
calculate_button.place(relx=0.4, rely=0.5, relwidth=0.2)

# Label that gives the total for a function
total_label = ttk.Label(calculator_frame, text="", style="TLabel")

# Exits the application
exit_button = ttk.Button(calculator_frame, text="Exit Application", command=Close, style="TButton")
exit_button.place(relx=0.4, rely=0.85, relwidth=0.2)

# Initially display the calculator page
switch_page("Calculator")

root.mainloop()
