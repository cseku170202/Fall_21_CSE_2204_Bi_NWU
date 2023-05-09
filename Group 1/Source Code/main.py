# Updated project Git Link https://github.com/anonymousFaisal/Sorting-Visualizer-Using-Tkinter.git
# Project: Sorting Visualizer Using Tkinter and Python
# Author: Nahid Hasan
# Modified by: Nahid Hasan, Suchana Biswas, Limon Majumdar

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, simpledialog
import random
from BubbleSort import bubble_sort
from LinearSearch import linear_search
from BinarySearch import binary_search

# Color Palate
# #57447a Background Dark Violet
# #332848 Very Dark Violet
# #3c2f54 Very Dark Saturated Violet
# #ADD8E6 Default Graph Blue
# #4f69c3 Moderate Blue
# #bc2e51 Strong Red
# #257157 Very Dark Cyan-Lime Green

# Creating the main window
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1920, 1080)
root.config(bg='#57447a')

# Creating a gradient background
image = Image.open("image/gradient.png")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Variables
selected_alg = StringVar()
selected_search = StringVar()
data = []


# The main function that Draws the bars in the Canvas
def drawData(Data, colorArray):
    canvas.delete("all")
    c_height = 580
    c_width = 850
    x_width = c_width / (len(Data) + 1)
    offset = 35
    spacing = 10
    normalizedData = [i / max(Data) for i in Data]  # normalizing the data to scale with the canvas
    for i, height in enumerate(normalizedData):  # Create boxes
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 500
        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
        # Text over boxes
        x = (x0 + x1) / 2
        y = y0 - 10
        canvas.create_text(x, y, anchor='center', text=str(Data[i]), font=("Helvetica", 10))
    root.update_idletasks()


def edit_data():
    global data

    # Create a new window for editing the data
    edit_window = Toplevel(root)
    edit_window.title('Edit Data')
    edit_window.geometry('300x400')
    edit_window.config(bg="#3c2f54")

    # Create a listbox containing the current data list
    data_listbox = Listbox(edit_window)
    data_listbox.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    data_listbox.config(font=('Arial Rounded MT Bold', 14), highlightthickness=0, borderwidth=0)

    # Add a scrollbar
    scrollbar = Scrollbar(edit_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    data_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=data_listbox.yview)

    # Populate the listbox with data
    for item in data:
        data_listbox.insert(END, str(item))

    # Add a button for deleting the currently selected item from the listbox and data list
    def delete_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            data_listbox.delete(index)
            data.pop(index)

    delete_button = Button(edit_window, text='Delete Selected Item', command=delete_item, bg='#bc2e51', fg="white", width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    delete_button.pack()

    # Add a button for modifying the currently selected item in the listbox and data list
    def modify_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            new_value = simpledialog.askinteger('Modify Item', 'Enter new value:')
            if new_value is not None:
                data[index] = new_value
                data_listbox.delete(index)
                data_listbox.insert(index, str(new_value))

    modify_button = Button(edit_window, text='Modify Selected Item', command=modify_item, bg="#4f69c3", fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    modify_button.pack()

    # Add a button for adding a new item to the listbox and data list
    def add_item():
        new_value = simpledialog.askinteger('Add Item', 'Enter new value:')
        if new_value is not None:
            data.append(new_value)
            data_listbox.insert(END, str(new_value))

    add_button = Button(edit_window, text='Add Item', command=add_item, bg="#4f69c3", fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    add_button.pack()

    # Add a button for saving the changes and closing the window
    def save_changes():
        # Update the data list with the new values in the listbox
        new_data = []
        for i in range(data_listbox.size()):
            new_data.append(int(data_listbox.get(i)))
        Data = new_data
        edit_window.destroy()
        drawData(Data, ['#ADD8E6' for x in range(len(Data))])

    save_button = Button(edit_window, text='Save Changes', command=save_changes, bg='#257157', fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    save_button.pack()


# Function to generate values within given range
def Generate():
    global data

    # Clearing Listbox
    listbox.delete(0, END)

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    # Get input values from the input_box Text widget and split them into separate integers
    input_values = input_box.get(1.0, END).strip().split()
    input_values = [int(val) for val in input_values]

    # Add input values to the data list
    data = input_values + [random.randrange(minVal, maxVal + 1) for _ in range(size - len(input_values))]

    drawData(data, ['#ADD8E6' for x in range(len(data))])

    # Create an Edit button
    edit_button = Button(UI_Frame, text='Edit', command=edit_data, bg='#257157', fg='white', font=('Arial Rounded MT Bold', 14), width=9, pady=5)

    edit_button.grid(row=10, column=0, padx=5, pady=5)


# Function to start the bubble sort algorithm
def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedScale.get(), listbox)


# Function to start searching
def StartSearching():
    global data
    search_item = int(input_SearchBox.get(1.0, END))
    if selected_search.get() == "Linear Search":
        linear_search(data, drawData, SearchSpeedScale.get(), search_item, listbox)
    else:
        binary_search(data, drawData, SearchSpeedScale.get(), search_item, listbox)


# UI Base Frame

# Interface to hold the widgets
UI_Frame = Frame(root, width=400, height=800, bg='#332848')
UI_Frame.grid(row=0, column=1, padx=10, pady=10, sticky=N)

# Interface for graphics
canvas = Canvas(root, width=900, height=580, bg='#FFFFFF')
canvas.grid(row=0, column=0, padx=10, pady=10)

# User Interface Area
algo_label = Label(UI_Frame, text='Algorithm', bg='#332848', fg='#FFFFFF', font=('Helvetica', 16, 'bold'))
algo_label.grid(row=0, column=0, padx=5, pady=5)

# Listbox for Showing Real time text
listbox = Listbox(root, width=100, height=3)
listbox.grid(row=1, column=0, padx=5, pady=5)
listbox.config(font=('Consolas', 12), background="#332848", fg="#FFFFFF")
listbox.config(highlightthickness=0, borderwidth=0, justify=CENTER)


# Dropdown menu for algorithms
algMenu = ttk.Combobox(UI_Frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge sort'], font=('Consolas', 12))
algMenu.grid(row=1, column=0, padx=5, pady=5)
algMenu.current(0)  # Default value of dropdown box

# Speed Scale to choose how fast or slow
speedScale = Scale(UI_Frame, from_=0, to=3.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]", font=('Consolas', 10))
speedScale.set(0.5)
speedScale.configure(sliderrelief="flat", activebackground='#5b4882')
speedScale.grid(row=5, column=0, padx=5, pady=5)

# Start button to start the sorting process
start_button = Button(UI_Frame, text='Start', command=StartAlgorithm, bg='#bc2e51', fg='#FFFFFF', font=('Arial Rounded MT Bold', 14), width=9, pady=5)
start_button.grid(row=9, column=0, padx=5, pady=5)

# Scale to select the size of the array
sizeEntry = Scale(UI_Frame, from_=3, to=40, length=200, resolution=1, orient=HORIZONTAL, label="Data Size", font=('Consolas', 10))
sizeEntry.set(10)
sizeEntry.configure(sliderrelief="flat", activebackground='#5b4882')
sizeEntry.grid(row=2, column=0, padx=5, pady=5)

# Scale to select the minimum value of the array
minEntry = Scale(UI_Frame, from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Min Value", font=('Consolas', 10))
minEntry.configure(sliderrelief="flat", activebackground='#5b4882')
minEntry.grid(row=3, column=0, padx=5, pady=5)

# Scale to select the maximum value of the array
maxEntry = Scale(UI_Frame, from_=15, to=150, length=200, resolution=1, orient=HORIZONTAL, label="Max Value", font=('Consolas', 10))
maxEntry.set(50)
maxEntry.configure(sliderrelief="flat", activebackground='#5b4882')
maxEntry.grid(row=4, column=0, padx=5, pady=5)

# Generate button to create random data
generate_button = Button(UI_Frame, text='Generate', command=Generate, bg='#4f69c3', fg='#FFFFFF', font=('Arial Rounded MT Bold', 14), width=9, pady=5)
generate_button.grid(row=8, column=0, padx=5, pady=5)

# Text box for manual user input
input_label = Label(UI_Frame, text='Input Values', bg='#332848', fg='#FFFFFF', font=('Helvetica', 12, 'bold'))
input_label.grid(row=6, column=0, padx=5, pady=5)

input_box = Text(UI_Frame, height=1, width=30, font=('Consolas', 10))
input_box.grid(row=7, column=0, padx=5, pady=5, columnspan=2)

# The Searching Interface


# UI Search Frame
UI_SearchFrame = Frame(root, width=400, height=400, bg='#332848')
UI_SearchFrame.grid(row=0, column=2, padx=10, pady=10, sticky=N)

# User Interface Area for search

search_label = Label(UI_SearchFrame, text='Search', bg='#332848', fg='white', font=('Helvetica', 16, 'bold'))
search_label.grid(row=0, column=0, padx=5, pady=5)

# Dropdown menu for search
searchMenu = ttk.Combobox(UI_SearchFrame, textvariable=selected_search, values=['Linear Search', 'Binary Search'], font=('Consolas', 12))
searchMenu.grid(row=1, column=0, padx=5, pady=5)
searchMenu.current(1)  # Default value of dropdown search box

# Speed Scale For Search
SearchSpeedScale = Scale(UI_SearchFrame, from_=0, to=3.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]", font=('Consolas', 10))
SearchSpeedScale.set(1.0)
SearchSpeedScale.configure(sliderrelief="flat", activebackground='#5b4882')
SearchSpeedScale.grid(row=2, column=0, padx=5, pady=5)

# Text box for manual search input
input_SearchLabel = Label(UI_SearchFrame, text='Input search element', bg='#332848', fg='white', font=('Helvetica', 12, 'bold'))
input_SearchLabel.grid(row=3, column=0, padx=5, pady=5)
input_SearchBox = Text(UI_SearchFrame, height=1, width=30, font=('Consolas', 10))
input_SearchBox.grid(row=4, column=0, padx=5, pady=5)

# Search button to start the searching process
search_button = Button(UI_SearchFrame, text='Search', command=StartSearching, bg='#bc2e51', fg='white', font=('Arial Rounded MT Bold', 14), width=9, pady=5)
search_button.grid(row=5, column=0, padx=5, pady=5)


# Main graphics loop
root.mainloop()
