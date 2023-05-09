from tkinter import *
import time
from tkinter import ttk, simpledialog


# The Insertion sort algorithm
def insertion_sort(arr, canvas):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        listbox.delete(0, END)
        listbox.insert(END, f"Iteration: {i}")
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            listbox.delete(0, END)
            listbox.insert(END, f"Iteration: {i}")
            listbox.insert(END, f"Comparing: {arr[j + 1]} < {arr[j]}")
            drawArray(arr, canvas,
                      ["#110b38" if a == j or a == j + 1 else "#e06ca2" if a > j + 1 else "#ADD8E6" for a in
                       range(len(arr))])
            time.sleep(speedScale.get() / 2)
        arr[j + 1] = key
        drawArray(arr, canvas, ['#ADD8E6' for x in range(len(arr))])
        time.sleep(speedScale.get() / 2)

    listbox.delete(0, END)
    listbox.insert(END, "Algorithm Finished")
    drawArray(arr, canvas, ['#ADD8E6' for x in range(len(arr))])


def sort():
    c = canvas
    a = input()
    insertion_sort(a, c)
    print(a)


# Draw array
# tithy
def drawArray(data, canvas, color):
    canvas.delete("all")
    c_height = 420
    c_width = 600
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
    return bar


# input function
def input():
    input_str = inputBox.get()
    data = list(map(int, input_str.split()))

    return data


def generate():
    c = canvas
    data = input()
    drawArray(data, c, ['#ADD8E6' for x in range(len(data))])

    # edit_button = Button(frame, text='Edit', command=edit_data, bg='#D50032', fg='white', font=('Arial Rounded MT Bold', 14), width=9, pady=5)

    # edit_button.grid(row=0, column=4, padx=5, pady=5)


# window
window = Tk()
window.title("Insertion Sort")
window.maxsize(1920, 1080)
window.config(bg="#51087E")

# UI
canvas = Canvas(window, width=1180, height=400)
canvas.grid(row=0, column=0, padx=10, pady=5)

listbox = Listbox(window, width=20, height=4)
listbox.grid(row=1, column=0)
listbox.config(font=('Consolas', 15), background="#deaafe", fg="black")
listbox.config(highlightthickness=0, borderwidth=0)

frame = Frame(window, width=800, height=300, bg='#41c726')
frame.grid(row=2, column=0, padx=10, pady=5)

# input data
l_label = Label(frame, text="Enter the numbers:", bg="#81c4f0", height=2,
                font=("italic", 16, 'bold'), width=50).grid(row=0, column=0, pady=5, padx=5)
inputBox = Entry(frame, width=80)
inputBox.config()
inputBox.grid(row=1, column=0, padx=5)

input_str = inputBox.get()
data = list(map(int, input_str.split()))
# speed
speedScale = Scale(frame, from_=0, to=3.0, length=250, digits=2, resolution=0.1, orient=HORIZONTAL,
                   label="Sorting Speed [s]", font=('Cold Warm', 12))
speedScale.set(1.0)
speedScale.configure(sliderrelief="raised", activebackground='#ada8b6', relief="raised", bd=5)
speedScale.grid(row=0, column=1, padx=5, columnspan=3)

# buttons
g_button = Button(frame, text="Insert", bg='#62b4d1', width=10, height=5, relief="raised", bd=5,
                  font=('arial', 10, 'bold'), command=generate).grid(row=1, column=1, pady=10, padx=5)

s_button = Button(frame, text="Sort", bg='#8474a1', width=10, height=5, relief="raised", bd=5,
                  font=('arial', 10, 'bold'), command=sort).grid(row=1, column=2, pady=10, padx=5)

r_button = Button(frame, text="Exit", bg='#d676a4', width=10, height=5, relief="raised", bd=5,
                  font=('arial', 10, 'bold'), command=lambda: [window.destroy()]).grid(row=1, column=3, pady=10, padx=5)


window.mainloop()