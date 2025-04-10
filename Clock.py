import tkinter as tk
from time import strftime

# Function to update the clock
def time():
    # Get the current time in 12-hour format with Am/Pm
    string = strftime('%I:%M:%S %p')  # %I gives 12-hour format, %p gives Am/Pm
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title('Flip Clock')

# Set window size and background color
root.geometry('600x200')
root.config(bg='black')

# Create a label to display the time with a new font style
label = tk.Label(root, font=('Old English Text MT', 75,), fg='pink', bg='black')
label.pack(anchor='center')

# Call the time function to start updating the clock
time()

# Run the GUI loop
root.mainloop()
