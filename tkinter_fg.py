import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Simple Calculator")


def on_click(event):
    current_text = result_label['text']
    button_text = event.widget.cget('text')

    if button_text == '=':
        try:
            result = eval(current_text)
            result_label.config(text=str(result))
        except:
            result_label.config(text="Error")
    elif button_text == 'C':
        result_label.config(text="")
    else:
        result_label.config(text=current_text + button_text)



# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.grid(row=0, column=0, columnspan=4)

# Define the buttons and their positions
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]
row = 1
col = 0


for text in button_texts:
    button = tk.Button(root, text=text, padx=1, pady=0, font=("Helvetica", 18))
    button.grid(row=row, column=col)
    button.bind('<Button-1>', on_click)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
