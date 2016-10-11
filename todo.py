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

def add():
    item = input("Add an item: ")
    todo.append(item)
    marks.append("[ ]")
    print("Item added.")
    show()

def show():
    for i in (range(len(todo))):
        print(i+1, "\b.", marks[i], todo[i])

def mark(todo, marks):
    show()
    completed_mark = input("Which one you want to mark as completed: ")
    completed_mark = int(completed_mark)
    if (0 < completed_mark) and (len(marks) >= completed_mark):
        marks[completed_mark-1] = '[*]'
        print(todo[completed_mark-1], 'is completed')
    else:
        print("Please enter valid number!")
   
def archive():
    print("All completed tasks got deleted.")
    for id, line in enumerate(marks):
        if line == "[*]":
            marks.pop(id)
            todo.pop(id)

if first == "add":
    add() 

if first == "list":
    show()  

if first == "mark":
     mark(todo, marks)

if first == "archive":
    archive() 
    show()

if len(todo) != 0 :
    with open("todo.txt", "wb") as output:
        pickle.dump(todo, output)
    with open("marks.txt", "wb") as output:
        pickle.dump(marks, output)