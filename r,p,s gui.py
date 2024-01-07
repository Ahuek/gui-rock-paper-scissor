from tkinter import *
from tkinter import messagebox
import random
root=Tk()


options=['rock','paper','scissors']
computer=random.choice(options)


root.configure(background='blue')
label=Label(root,text='welcome to rock,paper ,scissors,Do you want to play')
label.pack()
yes=Button(root,text='yes',bg='orange')
yes.pack()
no=Button(root,text='no and quit',bg='orange',command=quit)
no.pack()
image=PhotoImage(file='rps.png')
label=Label(root,image=image,width=7000,height=800)
label.pack()


def whenclicked(choice):
  player_choice=choice
  if player_choice== computer :
     messagebox.showinfo ('Result','it is a tie')
     quit()
  elif (player_choice=='rock' and computer=='scissors') or (player_choice=='paper' and computer=='rock') or (player_choice=='scissors' and computer=='paper'):
    messagebox.showinfo ('Result','You won!!!!')
  else:
        
    
        messagebox.showinfo('Reesult','you lost,computer chose' +computer)
        quit()



root.title('Rock,paper,scissors')
rock=Button(root,text='Rock',padx=100,pady=100,command=lambda:whenclicked('rock'),bg='yellow')
paper=Button(root,text='paper',padx=100,pady=100,command=lambda: whenclicked('paper'),bg='yellow')
scissors=Button(root,text='scissors',padx=100,pady=100,command=lambda:whenclicked('scissors'),bg='yellow')
rock.pack()
paper.pack()
scissors.pack()


root.mainloop()