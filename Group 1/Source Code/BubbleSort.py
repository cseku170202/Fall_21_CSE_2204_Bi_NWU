import time
from tkinter import *


# Color Palate
# #ADD8E6 Default Blue
# #4ee44e Lime Green
# #4e3d6e Very Dark Desaturated Violet
# #ff8c8c Pink


# Bubble sort Algorithm
def bubble_sort(data, drawData, timeTick, listbox):
    n = len(data)

    for i in range(n):
        isSorted = False
        for j in range(0, n - i - 1):
            # Update the Listbox
            listbox.delete(0, END)
            listbox.insert(END, f"Iteration: {i + 1}")
            listbox.insert(END, f"Comparing: {data[j]} {'>' if data[j] > data[j + 1] else '<'} {data[j + 1]}")
            # Change colors when compared
            drawData(data, ['#4ee44e' if x == j else '#4ee44e' if x == j + 1 else '#4e3d6e' if x > n - i - 1 else '#ADD8E6' for x in range(len(data))])
            time.sleep(timeTick/2)
            if data[j] > data[j + 1]:
                # Update the listbox
                listbox.insert(END, "Swapping Numbers")
                listbox.update()
                # Swap the data
                data[j], data[j + 1] = data[j + 1], data[j]
                # Change colors when swapped
                drawData(data, ['#ff8c8c' if x == j else '#ff8c8c' if x == j + 1 else '#4e3d6e' if x > n - i - 1 else '#ADD8E6' for x in range(len(data))])
                time.sleep(timeTick/2)
    # Update listbox after finishing
    listbox.delete(0, END)
    listbox.insert(END, "Algorithm Finished")
    # Update the canvas after completion
    drawData(data, ['#4e3d6e' for x in range(len(data))])
