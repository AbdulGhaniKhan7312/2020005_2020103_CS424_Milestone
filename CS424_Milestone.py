import tkinter as tk
import re
 
def check_expression(expression):
    stack = []
    operators_count = 0
    operands_count = 0
    valid = True
 
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                valid = False
                break
            opening_bracket = stack.pop()
            if (char == ")" and opening_bracket != "(") or (char == "}" and opening_bracket != "{") or (char == "]" and opening_bracket != "["):
                valid = False
                break
            if operands_count > 0 and (operands_count - operators_count) != 1:
                valid = False
                break
            operands_count = 1
            operators_count = 0
        elif char in "+-*/":
            operators_count += 1
        elif char.isalnum():
            operands_count += 1
 
    if stack or not valid:
        return "Invalid Expression"
    elif operands_count > 0 and (operands_count - operators_count) != 1:
        return "Invalid Expression"
    else:
        return "Valid Expression"
 
def identify_identifiers_operators_numbers(expression):
    # Regular expressions for identifiers, operators, and numbers
    identifier_pattern = r'[a-zA-Z_]\w*'
    operator_pattern = r'[-+*/=]'
    number_pattern = r'\d+'
 
    # Find all identifiers, operators, and numbers
    identifiers = re.findall(identifier_pattern, expression)
    operators = re.findall(operator_pattern, expression)
    numbers = re.findall(number_pattern, expression)
 
    return identifiers, operators, numbers
 
def parse_expression():
    try:
        expression = entry.get()
        # Check expression validity
        result = check_expression(expression)
        result_label.config(text=result)
        # Identify identifiers, operators, and numbers
        identifier_list, operator_list, number_list = identify_identifiers_operators_numbers(expression)
        # Display identifiers
        identifiers_text.config(state="normal")
        identifiers_text.delete('1.0', tk.END)
        for identifier in identifier_list:
            identifiers_text.insert(tk.END, f"{identifier}\n")
        identifiers_text.config(state="disabled")
        # Display operators
        operators_text.config(state="normal")
        operators_text.delete('1.0', tk.END)
        for operator in operator_list:
            operators_text.insert(tk.END, f"{operator}\n")
        operators_text.config(state="disabled")
        # Display numbers
        numbers_text.config(state="normal")
        numbers_text.delete('1.0', tk.END)
        for number in number_list:
            numbers_text.insert(tk.END, f"{number}\n")
        numbers_text.config(state="disabled")
    except Exception as e:
        result_label.config(text="Error: " + str(e))
 
# Create GUI window
window = tk.Tk()
window.title("Expression Analyzer")
 
# Create input entry field
entry = tk.Entry(window, width=40)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
 
# Create parse button
parse_button = tk.Button(window, text="Analyze Expression", command=parse_expression)
parse_button.grid(row=0, column=2, padx=10, pady=10)
 
# Create label to display result
result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, columnspan=3)
 
# Create label for identifiers
identifier_label = tk.Label(window, text="Identifiers:")
identifier_label.grid(row=2, column=0, sticky="w", padx=10)
 
# Create text widget to display identifiers
identifiers_text = tk.Text(window, width=20, height=5, state="disabled")
identifiers_text.grid(row=3, column=0, padx=10)
 
# Create label for operators
operator_label = tk.Label(window, text="Operators:")
operator_label.grid(row=2, column=1, sticky="w", padx=10)
 
# Create text widget to display operators
operators_text = tk.Text(window, width=20, height=5, state="disabled")
operators_text.grid(row=3, column=1, padx=10)
 
# Create label for numbers
numbers_label = tk.Label(window, text="Numbers:")
numbers_label.grid(row=4, column=0, sticky="w", padx=10)
 
# Create text widget to display numbers
numbers_text = tk.Text(window, width=20, height=5, state="disabled")
numbers_text.grid(row=5, column=0, padx=10)
 
# Start GUI event loop
window.mainloop()