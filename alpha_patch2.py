# this is the first shot at the rock paper scissors game
import tkinter
from tkinter import * # importing all modules to make things easier, we are not short on memory anyway
import random as ran

main_window=Tk()
main_window.geometry("750x400")
main_window.title("RPS machine")
main_window.configure(bg="yellow")

#defined variables are here- 
entry=""
data_cpu=["rock","paper","scissors"]
cpu_choice=""
cpu_points=0
user_points=0



def labels():
	# all the labels will be under this function, we will call it in the end
	header=Label(main_window,text="The Rock Paper Scissors Game",font=("Impact",18),bg="pink")
	header.grid(row=0,column=1)
	                  
	mscore=Label(main_window,text="User Score")
	mscore.grid(row=450,column=0)

	cscore=Label(main_window,text="CPU Score")
	cscore.grid(row=450,column=2)
		
def displays():
	global says_now
	global m_display
	global u_display
	global winner_is

	m_display=Entry(main_window,width=5) # my display is user display 
	m_display.grid(row=470,column=0)
	m_display.insert(0,"0") # default text 

	u_display=Entry(main_window,width=5)
	u_display.grid(row=470,column=2)
	u_display.insert(0,"0") # default text

	says_now=Entry(main_window,width=10)
	says_now.grid(row=550,column=3)
	says_now.insert(0,"CPU says...") # default text 

	winner_is=Entry(main_window,width=15)
	winner_is.grid(row=550,column=0)
	winner_is.insert(0,"No winner yet") # default text 

def buttons():
	rock_bt=Button(main_window,text="ROCK",width=15,height=2,pady=5,padx=5,command=click_rock,bg="light blue",font="Impact")
	paper_bt=Button(main_window,text="PAPER",width=15,height=2,pady=5,padx=5,command=click_paper,bg="light blue",font="Impact")
	scissors_bt=Button(main_window,text="SCISSORS",width=15,height=2,pady=5,padx=5,command=click_scissors,bg="light blue",font="Impact")
	
	reset_bt=Button(main_window,text="Reset",command=click_reset,bg="red")
	#contin_bt=Button(main_window,text="CONTINUE",command=click_cont,bg="red")

	rock_bt.grid(row=30,column=0)
	paper_bt.grid(row=30,column=1)
	scissors_bt.grid(row=30,column=2)
	
	reset_bt.grid(row=110,column=1)
	#contin_bt.grid(row=130,column=1)



''' ========================All the action functions come below this================================'''
a=user_points
b=cpu_points

def click_rock():
	global entry
	global cpu_choice
	global cpu_points
	global user_points
	global data_cpu

	global m_display
	global u_display
	global winner_is

	global rock_bt
	
	
	entry="rock"
    
	cpu_choice=data_cpu[ran.randrange(0,3,1)]
	says_now.insert(0,cpu_choice) # updated text
	cpu_select=1
	if(cpu_select==1):
		if(cpu_choice=="rock" and entry=="rock"):
			cpu_points=cpu_points
			user_points=user_points
			winner_is.delete(0)
			winner_is.insert(0,"Draw")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="paper" and entry=="rock"):
			cpu_points=cpu_points+1
			b=cpu_points
			u_display.delete(0,END)
			u_display.insert(0,b) 
			winner_is.delete(0,END)
			winner_is.insert(0,"CPU Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="scissors" and entry=="rock"):
			user_points=user_points+1
			a=user_points
			m_display.delete(0,END)
			m_display.insert(0,a) # updated text 
			winner_is.delete(0,END)
			winner_is.insert(0,"You Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True

	
def click_paper():
	global entry
	global cpu_choice
	global cpu_points
	global user_points
	global data_cpu

	global m_display
	global u_display
	global winner_is

	global paper_bt
	
	
	entry="paper"
    
	cpu_choice=data_cpu[ran.randrange(0,3,1)]
	says_now.insert(0,cpu_choice) # updated text
	cpu_select=1
	if(cpu_select==1):
		if(cpu_choice=="paper" and entry=="paper"):
			cpu_points=cpu_points
			user_points=user_points
			winner_is.delete(0,END)
			winner_is.insert(0,"Draw")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="scissors" and entry=="paper"):
			cpu_points=cpu_points+1
			b=cpu_points
			u_display.delete(0,END)
			u_display.insert(0,b) 
			winner_is.delete(0,END)
			winner_is.insert(0,"CPU Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="rock" and entry=="paper"):
			user_points=user_points+1
			a=user_points
			m_display.delete(0,END)
			m_display.insert(0,a) # updated text 
			winner_is.delete(0,END)
			winner_is.insert(0,"You Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True	
	
def click_scissors():
	global entry
	global cpu_choice
	global cpu_points
	global user_points
	global data_cpu

	global m_display
	global u_display
	global winner_is

	global scissors_bt
	
	
	entry="scissors"
    
	cpu_choice=data_cpu[ran.randrange(0,3,1)]
	says_now.insert(0,cpu_choice) # updated text
	cpu_select=1
	if(cpu_select==1):
		if(cpu_choice=="scissors" and entry=="scissors"):
			cpu_points=cpu_points
			user_points=user_points
			winner_is.delete(0,END)
			winner_is.insert(0,"Draw")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="rock" and entry=="scissors"):
			cpu_points=cpu_points+1
			b=cpu_points
			u_display.delete(0,END)
			u_display.insert(0,b) 
			winner_is.delete(0,END)
			winner_is.insert(0,"CPU Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True
		elif(cpu_choice=="paper" and entry=="scissors"):
			user_points=user_points+1
			a=cpu_points
			m_display.delete(0,END)
			m_display.insert(0,a) # updated text 
			winner_is.delete(0,END)
			winner_is.insert(0,"You Won!")
			says_now.delete(0,END)
			says_now.insert(0,cpu_choice)
			pointupdate=True


def click_reset():
	global entry
	global cpu_choice
	global cpu_points
	global user_points
	global data_cpu
	global says_now
	global m_display
	global u_display
	global winner_is

	entry=0
	cpu_choice=0
	cpu_points=0
	user_points=0
	winner_is.delete(0,END)
	winner_is.insert(0,"No winner yet")# default text 
	#go_now.insert(0,"wait for it...") # default text 
	says_now.delete(0,END)
	says_now.insert(0,"CPU says...") # default text
	u_display.delete(0,END)
	u_display.insert(0,"0") # default text
	m_display.delete(0,END)
	m_display.insert(0,"0") # default text 

# def click_cont():

# 	global entry
# 	global cpu_choice
# 	global cpu_points
# 	global user_points
# 	global data_cpu
# 	global says_now
# 	global m_display
# 	global u_display
# 	global winner_is

# 	entry=0
# 	cpu_choice=0
# 	winner_is.delete(0,END)
# 	winner_is.insert(0,"No winner yet")# default text 
# 	#go_now.insert(0,"wait for it...") # default text 
# 	says_now.delete(0,END)
# 	says_now.insert(0,"CPU says...") # default text
# 	#u_display.delete(0,END)
# 	u_display.insert(0,b) # default text
# 	#m_display.delete(0,END)
# 	m_display.insert(0,a) # default text 


labels()
displays()
buttons()
main_window.mainloop() # the closing line 