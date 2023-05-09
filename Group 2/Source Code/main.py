from tkinter import *
import time
from tkinter import ttk, simpledialog

# Global variable
Data = []


# The selection sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            listbox.delete(0, END)
            listbox.insert(END, f"Iteration: {i + 1}")
            listbox.insert(END, f"Comparing: {arr[j]} {'<' if arr[j] < arr[min_idx] else '>'} {arr[min_idx]}")

            drawArray(arr, ["#69ffdc" if a == min_idx or a == i else "#e06ca2" if a <= i else "#ADD8E6" for a in range(len(arr))])
            time.sleep(speedScale.get() / 2)
            if arr[j] < arr[min_idx]:
                min_idx = j
                drawArray(arr, ["#fc5dad" if a == min_idx or a == j else "#e06ca2" if a <= i else "#ADD8E6" for a in range(len(arr))])
                time.sleep(speedScale.get() / 2)

        # swapping
        listbox.insert(END, f"Selected elements : {arr[j]} and {arr[i]}")
        if i != min_idx:
            listbox.insert(END, "Swapping Numbers")
            listbox.insert(END, f"After Swapping: {arr}")
            listbox.update()
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
            # color changing
            drawArray(arr, ["#f39ffc" if a == min_idx or a == i else "#e06ca2" if a <= i else "#ADD8E6" for a in range(len(arr))])
            time.sleep(speedScale.get() / 2)
        

    listbox.delete(0, END)
    listbox.insert(END, "Algorithm Finished")
    listbox.insert(END, f"Sorted Array: {arr}")
    drawArray(arr, ['#ADD8E6' for x in range(len(arr))])


def sort():
    global Data
    selection_sort(Data)
    print(Data)


#tithy
def edit_data():
    global Data

    # Create a new window for editing the data
    edit_window = Toplevel(window)
    edit_window.title('Edit Data')
    edit_window.geometry('300x400')
    edit_window.config(bg="#393053")

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
    for item in Data:
        data_listbox.insert(END, str(item))

    # Add a button for deleting the currently selected item from the listbox and data list
    def delete_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            data_listbox.delete(index)
            Data.pop(index)

    delete_button = Button(edit_window, text='Delete Selected Item', command=delete_item,bd=5, bg='#576CBC', fg="white", width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    delete_button.pack()

    # Add a button for modifying the currently selected item in the listbox and data list
    def modify_item():
        selected = data_listbox.curselection()
        if selected:
            index = selected[0]
            new_value = simpledialog.askinteger('Modify Item', 'Enter new value:')
            if new_value is not None:
                Data[index] = new_value
                data_listbox.delete(index)
                data_listbox.insert(index, str(new_value))

    modify_button = Button(edit_window, text='Modify Selected Item', command=modify_item,bd=5, bg="#9E4784", fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    modify_button.pack()

    # Add a button for adding a new item to the listbox and data list
    def add_item():
        new_value = simpledialog.askinteger('Add Item', 'Enter new value:')
        if new_value is not None:
            Data.append(new_value)
            data_listbox.insert(END, str(new_value))

    add_button = Button(edit_window, text='Add Item', command=add_item,bd=5, bg="#9E4784", fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    add_button.pack()

    # Add a button for saving the changes and closing the window
    def save_changes():
        # Update the data list with the new values in the listbox
        new_data = []
        for i in range(data_listbox.size()):
            new_data.append(int(data_listbox.get(i)))
        Data = new_data
        edit_window.destroy()
        drawArray(Data, ['#ADD8E6' for x in range(len(Data))])

    save_button = Button(edit_window, text='Save Changes', command=save_changes,bd=5, bg='#5F264A', fg='white', width=18, font=('Arial Rounded MT Bold', 8), pady=5)
    save_button.pack()


# Draw array
def drawArray(data, color):
    canvas.delete("all")
    c_height = 380
    c_width = 1000
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    bars = []
    normalizedData = [i / max(data) for i in data]  # normalizing the data to scale with the canvas
    for i, height in enumerate(normalizedData):  # Create boxes
        # top left

        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = c_height
        bar = canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))  # Text over boxes
        bars.append(bar)
    window.update_idletasks()


def generate():
    global Data

    input_values = inputBox.get().strip().split()
    input_values = [int(val) for val in input_values]
    Data = input_values
    drawArray(Data, ['#ADD8E6' for x in range(len(Data))])
    edit_button = Button(frame, text='Edit', command=edit_data, bg='#D4ADFC',relief='raised',bd=5, fg='white', font=('Arial Rounded MT Bold', 14), width=9, pady=5)
    edit_button.grid(row=0, column=4, padx=5, pady=5)

#tisha
# window
window = Tk()
window.title("Selection Sort")
window.maxsize(1920, 1080)
window.config(bg="#393053")

# UI
Label(window,text="Visualization Of Selection Sort ", font=("italic", 16, 'bold'),bg="#393053",fg="#A5D7E8").grid(row=0,column=0)
canvas = Canvas(window, width=1000, height=400)
canvas.grid(row=1, column=0, padx=10, pady=5)

listbox = Listbox(window, width=100, height=5)
listbox.grid(row=2, column=0)
listbox.config(font=('Consolas', 14), background="#18122B", fg="#A5D7E8")
listbox.config(highlightthickness=0, borderwidth=0)

frame = Frame(window, width=800, height=300, bg='#18122B')
frame.grid(row=3, column=0, padx=10, pady=5)

# input data
Label(frame, text="Enter the numbers that you want to sort  :", bg="#443C68", height=5, font=("italic", 13, 'bold'), width=50,fg='#A5D7E8').grid(row=0, column=0, pady=5, padx=5)
inputBox = Entry(frame, width=100)

inputBox.grid(row=1, column=0, padx=5)

# speed
speedScale = Scale(frame, from_=0, to=3.0, length=250, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]", font=('Consolas', 12))
speedScale.set(1.0)
speedScale.configure(sliderrelief="raised", activebackground='#ada8b6', relief="raised", bd=5)
speedScale.grid(row=0, column=1, padx=5, columnspan=3)

# buttons
g_button = Button(frame, text="Generate", bg='#576CBC', width=8,height=2, bd=5, font=('arial', 10, 'bold'), command=generate,fg='#A5D7E8')
g_button.grid(row=1, column=1, pady=10, padx=5)

s_button = Button(frame, text="Sort", bg='#9E4784', width=8, height=2, bd=5, font=('arial', 10, 'bold'), command=sort,fg='#A5D7E8')
s_button.grid(row=1, column=2, pady=10, padx=5)

r_button = Button(frame, text="Exit", bg='#5F264A', width=8, height=2, bd=5, font=('arial', 10, 'bold'), command=lambda: [window.destroy()],fg='#A5D7E8')
r_button.grid(row=1, column=3, pady=10, padx=5)

window.mainloop()
