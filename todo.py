import sys

todo = []
mark = []

first = input("Please specify a command [list, add, mark, archive]: ")

def add():
    print("add")

def show():
    print("show")

def mark():
    print("mark")

def archive():
    print("archive")

if first == "add":
    add() 

if first == "list":
    show()  

if first == "mark":
    mark()  

if first == "archive":
    archive()  
