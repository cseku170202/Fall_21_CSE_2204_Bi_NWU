import time
from tkinter import *


# Color Palate
# #ADD8E6 Default Blue
# #4e3d6e Very Dark Desaturated Violet
# #4ee44e Green
# #F2921D Orange
# #DC143C Alarm Red

# Binary search algorithm

def binary_search(data, drawData, timeTick, item, listbox):
    n = len(data)
    low = 0
    high = n - 1
    isFound = False

    while low <= high:
        mid = (low + high) // 2

        # Update the canvas
        listbox.delete(0, END)
        listbox.insert(END, f"Checking the mid value: {data[mid]}")
        drawData(data, ['#4ee44e' if x == mid else '#ADD8E6' for x in range(len(data))])
        time.sleep(timeTick)

        if data[mid] == item:
            # Update the canvas and listbox when item is found
            listbox.delete(0, END)
            listbox.insert(END, f"Target element {item} found at index {mid}")
            drawData(data, ['#4e3d6e' if x == mid else '#ADD8E6' for x in range(len(data))])
            isFound = True
            break

        elif data[mid] < item:
            # Update the canvas and listbox when searching in the right half
            if mid + 1 <= high:
                listbox.delete(0, END)
                listbox.insert(END, f"Target element {item} is greater than {data[mid]}")
                listbox.insert(END, f"Searching in the right half")
                listbox.insert(END, f"Searching in the range [{data[mid + 1]}, {data[high]}]")
                drawData(data, ['#ADD8E6' if x > high or x < mid else '#F2921D' for x in range(len(data))])
                time.sleep(timeTick)
                low = mid + 1
            else:
                break

        else:
            # Update the canvas and listbox when searching in the left half
            if mid - 1 >= low:
                listbox.delete(0, END)
                listbox.insert(END, f"Target element {item} is less than {data[mid]}")
                listbox.insert(END, f"Searching in the left half")
                listbox.insert(END, f"Searching in the range [{data[low]}, {data[mid - 1]}]")
                drawData(data, ['#ADD8E6' if x < low or x > mid else '#F2921D' for x in range(len(data))])
                time.sleep(timeTick)
                high = mid - 1
            else:
                break

    if not isFound:
        # Update the canvas and listbox when item is not found
        listbox.delete(0, END)
        listbox.insert(END, f"Target element {item} is not present in the database")
        drawData(data, ['#DC143C' for x in range(len(data))])
