import time
from tkinter import *


def merge_sort(data, drawData, timeTick, listbox):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick, listbox)


def merge_sort_alg(data, left, right, drawData, timeTick, listbox):
    if left < right:
        middle = (left + right) // 2
       
        merge_sort_alg(data, left, middle, drawData, timeTick, listbox)
        merge_sort_alg(data, middle + 1, right, drawData, timeTick, listbox)
        merge(data, left, middle, right, drawData, timeTick, listbox)


def merge(data, left, middle, right, drawData, timeTick, listbox):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle + 1]
    listbox.insert(END, f"Left Seperated part{data[left:middle+1]}")
    rightPart = data[middle + 1: right + 1]
    listbox.insert(END, f"Right Seperated part{data[middle+1:right+1]}")
    listbox.update()
    leftIdx = rightIdx = 0
    listbox.delete(0, END)
    listbox.insert(END, f"Swapping Elements")

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                listbox.insert(END, f"Swapped elements : {data[dataIdx]} and {rightPart[rightIdx]}")
                listbox.update()
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                listbox.insert(END, f"Swapped elements : {data[dataIdx]} and {leftPart[leftIdx]}")
                listbox.update()
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if left <= x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

    # Add progress information to the listbox
    
    listbox.insert(END, f"Left Part: {leftPart}")
    listbox.insert(END, f"Right Part: {rightPart}")
    listbox.insert(END, f"Merging after swapping")
    
    listbox.insert(END, f"Merge: {data[left:right + 1]}")
    listbox.yview(END)


def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if left <= i <= right:
            if left <= i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("aqua")

    return colorArray
