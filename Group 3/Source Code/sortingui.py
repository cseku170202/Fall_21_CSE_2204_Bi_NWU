from tkinter import *
from tkinter import ttk
import random

from PIL import ImageTk, Image

from mergesort import merge_sort

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1920, 1080)
root.config(bg='#48C9B0')

# Variables
selected_alg = StringVar()
data = []


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 580
    c_width = 1280
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]  # normalizing the data to scale with the canvas
    for i, height in enumerate(normalizedData):  # Create boxes
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 500
        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))  # Text over boxes
    root.update_idletasks()


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


# function to start the Merge sort algorithm
def StartAlgorithm():
    global data
    merge_sort(data, drawData, speedScale.get(), listbox)


# UI Base Frame

# Interface to hold the widgets
UI_frame = Frame(root, width=1280, height=200, bg='#44B95B')
UI_frame.grid(row=1, column=0, padx=20, pady=5)

# Interface for graphics
canvas = Canvas(root, width=1280, height=600, bg='white')
canvas.grid(row=0, column=0, padx=20, pady=5)
img = ImageTk.PhotoImage(Image.open("C:/Users/nayan/MergeSortVisualization/MergeSortVisualization/img/merge-sort.png"))
canvas.create_image(10, 50, anchor=NW, image=img)

# User Interface Area
# Row[0]
algo_label = Label(UI_frame, text='Algorithm:', bg='#34495E', fg='white', font=('Helvetica', 12, 'bold'))
algo_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

# Dropdown menu for algorithms
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Merge Sort'],
                       font=('Helvetica', 12, 'bold'))
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)  # Default value of dropdown box

# Speed Scale to choose how fast or slow
speedScale = Scale(UI_frame, from_=0, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
                   label="Select Speed [s]", font=('Helvetica', 10))
speedScale.set(1)
speedScale.grid(row=0, column=2, padx=5, pady=5)

# Start button to start the sorting process
start_button = Button(UI_frame, text='Start', command=StartAlgorithm, bg='#D50032', fg='white', font=('Helvetica', 12))
start_button.grid(row=0, column=3, padx=5, pady=5)

# Row[1]
# Scale to select the size of the array
sizeEntry = Scale(UI_frame, from_=3, to=15, resolution=1, orient=HORIZONTAL, label="Data Size", font=('Helvetica', 10))
sizeEntry.set(10)
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# Scale to select the minimum value of the array
minEntry = Scale(UI_frame, from_=0, to=30, resolution=1, orient=HORIZONTAL, label="Min Value", font=('Helvetica', 10))
minEntry.grid(row=1, column=1, padx=5, pady=5)

# Scale to select the maximum value of the array
maxEntry = Scale(UI_frame, from_=30, to=150, length=200, resolution=1, orient=HORIZONTAL, label="Max Value",
                 font=('Helvetica', 10))
maxEntry.set(50)
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

# Generate button to create random data
generate_button = Button(UI_frame, text='Generate', command=Generate, bg='#3498DB', fg='white', font=('Helvetica', 14))
generate_button.grid(row=1, column=3, padx=5, pady=5)

# Row[2]
# Text box for manual user input
input_label = Label(UI_frame, text='Input Values:', bg='#34495E', fg='white', font=('Helvetica', 12, 'bold'))
input_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)

input_box = Text(UI_frame, height=1, width=50, font=('Helvetica', 10))
input_box.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky=W)

# Listbox
listbox = Listbox(root, width=140, height=3)
listbox.grid(row=0, column=0, sticky=N, pady=5)
listbox.config(font=('Consolas Bold', 12), bd=0, highlightthickness=0, background="white", fg="black", justify="center")


# Main graphics loop
root.mainloop()
