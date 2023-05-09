import time
from tkinter import *


# Color Palate
# #ADD8E6 Default Blue
# #4e3d6e Very Dark Desaturated Violet
# #F2921D Orange
# #DC143C Alarm Red

# Linear search algorithm
def linear_search(data, drawData, timeTick, item, listbox):
    n = len(data)
    isFound = False
    for i in range(n):
        # Update the canvas and listbox
        listbox.delete(0, END)
        listbox.insert(END, f"Iteration: {i + 1}")
        listbox.insert(END, f"Checking if current item ({data[i]}) is equal to target element ({item})")
        drawData(data, ['#F2921D' if x == i else '#ADD8E6' for x in range(len(data))])
        time.sleep(timeTick)

        if data[i] == item:
            # Update the canvas and listbox when Item is Found
            drawData(data, ['#4e3d6e' if x == i else '#ADD8E6' for x in range(len(data))])
            isFound = True
            listbox.insert(END, f"Target element {item} is found at index {i}")
            break

    if not isFound:
        # Update the canvas and listbox when item is not found
        drawData(data, ['#DC143C' for x in range(len(data))])
        listbox.delete(0, END)
        listbox.insert(END, f"Target element {item} is not present in the database")
