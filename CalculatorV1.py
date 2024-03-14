from tkinter import *

def calculate():
    global current_value, operation, previous_value
    if operation:
        if operation == '+':
            current_value = previous_value + int(v2.get())
        elif operation == '-':
            current_value = previous_value - int(v2.get())
        elif operation == '*':
            current_value = previous_value * int(v2.get())
        elif operation == '/':
            try:
                current_value = previous_value / int(v2.get())
            except ZeroDivisionError:
                current_value = "Ошибка"
        v2.delete(0, END)
        v2.insert(0, str(current_value))
        operation = None

def my_function(i):
    global current_value, operation, previous_value
    if str(i).isdigit():
        if v2.get() == "0" or reset_entry:
            v2.delete(0, END)
            v2.insert(0, str(i))
        else:
            v2.insert(END, str(i))
    elif i in ['+', '-', '*', '/']:
        previous_value = int(v2.get())
        operation = i
        v2.delete(0, END)
    elif i == '=':
        calculate()

v = Tk()
v.geometry('310x500')
v['bg'] = 'gray'

current_value = 0
operation = None
previous_value = 0
reset_entry = False

v1 = Label(text='Ответ:')
v1.pack(pady=10)

v2 = Entry(bg='gray', bd='7')
v2.pack(pady=10)

digits_frame = Frame(v)
digits_frame.pack(pady=10)

for i in range(10):
    Button(digits_frame, text=str(i), command=lambda i=i: my_function(i)).pack(side=LEFT)

operations_frame = Frame(v)
operations_frame.pack(pady=10)

for op in ['+', '-', '*', '/', '=']:
    Button(operations_frame, text=op, command=lambda op=op: my_function(op)).pack(side=LEFT, padx=5)

v.mainloop()