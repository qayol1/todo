import pickle
import os

todo = []
marks = []

if os.path.isfile("todo.txt")==False:
    f1 = open("todo.txt","a")
    f2 = open("marks.txt", "a")

if os.stat("todo.txt").st_size != 0:
    with open("todo.txt", "rb") as data:
        todo = pickle.load(data)
    with open("marks.txt", "rb") as data:
        marks = pickle.load(data)

first = input("Please specify a command [list, add, mark, archive]: ")

def add(marks,todo):
    item = input("Add an item: ")
    todo.append(item)
    marks.append("[ ]")
    print("Item added.")

def show(marks,todo):
    if len(todo) == 0 :
        print("The todo list is empty.")
    else:
        if len(todo) > 1 :
            print("You saved the following todo items:")
        else:
            print("You saved the following todo item:")
        for i in (range(len(todo))):
            print(i+1, "\b.", marks[i], todo[i])

def mark(marks,todo):
    show(marks,todo)
    completed_mark = input("Which one you want to mark as completed: ")
    completed_mark = int(completed_mark)
    if (0 < completed_mark) and (len(marks) >= completed_mark):
        marks[completed_mark-1] = '[*]'
        print(todo[completed_mark-1], 'is completed')
        show(marks,todo)
    else:
        print("Please enter valid number!")
   
def archive(marks,todo):
    print("All completed tasks got deleted.")
    i = len(marks)
    while i > 0 :
        if marks[i-1] == "[*]":
            marks.pop(i-1)
            todo.pop(i-1)
        i = i-1

if first == "add":
    add(marks,todo) 
    show(marks,todo)

if first == "list":
    show(marks,todo)  

if first == "mark":
     mark(marks,todo)

if first == "archive":
    archive(marks,todo) 
    show(marks,todo)

if len(todo) != 0 :
    with open("todo.txt", "wb") as output:
        pickle.dump(todo, output)
    with open("marks.txt", "wb") as output:
        pickle.dump(marks, output)

if len(todo) == 0 :
    os.remove("todo.txt")
    os.remove("marks.txt")