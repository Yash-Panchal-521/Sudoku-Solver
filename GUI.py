from tkinter import *
from Solver import Solver

root = Tk()
root.title("Sudoku")
root.geometry("330x400")

label = Label(root,text="Fill the number and click solve").grid(row=0,column=1,columnspan=10)

errLabel = Label(root,text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=10)

Done = Label(root,text="",fg="green")
Done.grid(row=15,column=1,columnspan=10,pady=10)

cells = {}

def validNumber(P):
    out = (P.isdigit() or P=="")and len(P)<2
    return out

reg = root.register(validNumber)


def draw3x3(r,c,color):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width=5,bg=color,justify="center",validate="key",validatecommand=(reg,"%P"))
            e.grid(row=r+i+1,column=c+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(r+i+1,c+j+1)]=e

def drawGrid():
    color = "#CBA0AE"
    for r in range(1,10,3):
        for c in range(0,9,3):
            draw3x3(r,c,color)
            if color=="#CBA0AE":
                color="#76549A"
            else:
                color="#CBA0AE"
                
                
def clear():
    errLabel.configure(text="")
    Done.configure(text="")
    
    for r in range(2,11):
        for c in range(1,10):
            cell = cells[(r,c)]
            cell.delete(0,"end")
            
def getVal():
    board = []
    errLabel.configure(text="")
    Done.configure(text="")
    for r in range(2,11):
        rows=[]
        for c in range(1,10):
            val = cells[(r,c)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateVal(board)

        
btn = Button(root,command=getVal,text="Solve",width=10)
btn.grid(row=20,column=1,columnspan=5,pady=20)

btn = Button(root,command=clear,text="Clear",width=10)
btn.grid(row=20,column=5,columnspan=5,pady=20)

def updateVal(s):
    sol = Solver(s)
    if sol !="no":
        for r in range(2,11):
            for c in range(1,10):
                cells[(r,c)].delete(0,"end")
                cells[(r,c)].insert(0,sol[r-2][c-1])
        Done.configure(text="Solved!!")
    else:
        errLabel.configure(text="No Solution Exists")
                

drawGrid()
root.mainloop()

