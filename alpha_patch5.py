# this is the fourth shot at the rock paper scissors game
import tkinter
from tkinter import * # importing all modules to make things easier, we are not short on memory anyway
import random as ran

main_window=Tk() # this is the variable that declares the entire window as a workable object 
main_window.geometry("750x400")
main_window.title("RPS machine")
main_window.configure(bg="yellow")

#defined variables are here- 
entry=""
data_cpu=["rock","paper","scissors"]
cpu_choice=""
cpu_points=0
user_points=0
a=user_points
b=cpu_points
final_counter=False # as long as this is false, the buttons will work 


def labels():
	# all the labels will be under this function, we will call it in the end
	header=Label(main_window,text="The Rock Paper Scissors Game",font=("Impact",18),bg="pink")
	header.grid(row=0,column=1)
	                  
	mscore=Label(main_window,text="User Score")
	mscore.grid(row=450,column=0)

	cscore=Label(main_window,text="CPU Score")
	cscore.grid(row=450,column=2)
	final_winner=Label(main_window,text="",font=("Impact",16),bg="yellow")
	final_winner.grid(row=500,column=1)
	play_again=Label(main_window,text="",font=("Impact",15),bg="yellow") 
	play_again.grid(row=550,column=1)
		
def displays():
	global says_now
	global m_display
	global u_display
	global winner_is



	m_display=Entry(main_window,width=5,font=(10)) # my display is user display 
	m_display.grid(row=470,column=0)
	m_display.insert(0,"0") # default text 

	u_display=Entry(main_window,width=5,font=(10))
	u_display.grid(row=470,column=2)
	u_display.insert(0,"0") # default text

	says_now=Entry(main_window,width=10,font=(10))
	says_now.grid(row=550,column=3)
	says_now.insert(0,"CPU says...") # default text 

	winner_is=Entry(main_window,width=15,font=(10))
	winner_is.grid(row=550,column=0)
	winner_is.insert(0,"No winner yet") # default text 

def buttons():
	rock_bt=Button(main_window,text="ROCK",width=15,height=2,pady=5,padx=5,command=click_rock,bg="light blue",font="Impact")
	paper_bt=Button(main_window,text="PAPER",width=15,height=2,pady=5,padx=5,command=click_paper,bg="light blue",font="Impact")
	scissors_bt=Button(main_window,text="SCISSORS",width=15,height=2,pady=5,padx=5,command=click_scissors,bg="light blue",font="Impact")
	
	reset_bt=Button(main_window,text="Reset",command=click_reset,bg="red")


	rock_bt.grid(row=30,column=0)
	paper_bt.grid(row=30,column=1)
	scissors_bt.grid(row=30,column=2)
	
	reset_bt.grid(row=110,column=1)

''' ========================All the action functions come below this================================'''

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

	global a
	global b 
	global final_winner
	global final_counter

	if final_counter==False:
	
		entry="rock"
	    
		cpu_choice=data_cpu[ran.randrange(0,3,1)] # randrange (0,3,1) will pick either 0 1 or 2
		says_now.insert(0,cpu_choice) # updated text
		cpu_select=1
		if(cpu_select==1):
			if(cpu_choice=="rock"):
				cpu_points=cpu_points
				user_points=user_points
				winner_is.delete(0,END)
				winner_is.insert(0,"Draw")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show()
				
				
			elif(cpu_choice=="paper"):
				cpu_points=cpu_points+1
				b=cpu_points
				u_display.delete(0,END)
				u_display.insert(0,b) 
				winner_is.delete(0,END)
				winner_is.insert(0,"CPU Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
				
				
			elif(cpu_choice=="scissors"):
				user_points=user_points+1
				a=user_points
				m_display.delete(0,END)
				m_display.insert(0,a) # updated text 
				winner_is.delete(0,END)
				winner_is.insert(0,"You Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
			
			
	
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

	global a
	global b 
	global final_winner
	global final_counter

	if final_counter==False:
	
		entry="paper"
	    
		cpu_choice=data_cpu[ran.randrange(0,3,1)]
		says_now.insert(0,cpu_choice) # updated text
		cpu_select=1
		if(cpu_select==1):
			if(cpu_choice=="paper"):
				cpu_points=cpu_points
				user_points=user_points
				winner_is.delete(0,END)
				winner_is.insert(0,"Draw")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
				
				
			elif(cpu_choice=="scissors"):
				cpu_points=cpu_points+1
				b=cpu_points
				u_display.delete(0,END)
				u_display.insert(0,b) 
				winner_is.delete(0,END)
				winner_is.insert(0,"CPU Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
				
				
			elif(cpu_choice=="rock"):
				user_points=user_points+1
				a=user_points
				m_display.delete(0,END)
				m_display.insert(0,a) # updated text 
				winner_is.delete(0,END)
				winner_is.insert(0,"You Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show()
			
				
		
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

	global a
	global b 
	global final_winner
	global final_counter

	if final_counter==False:


	
		entry="scissors"
	    
		cpu_choice=data_cpu[ran.randrange(0,3,1)]
		says_now.insert(0,cpu_choice) # updated text
		cpu_select=1
		if(cpu_select==1):
			if(cpu_choice=="scissors"):
				cpu_points=cpu_points
				user_points=user_points
				winner_is.delete(0,END)
				winner_is.insert(0,"Draw")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
				
			elif(cpu_choice=="rock"):
				cpu_points=cpu_points+1
				b=cpu_points
				u_display.delete(0,END)
				u_display.insert(0,b) 
				winner_is.delete(0,END)
				winner_is.insert(0,"CPU Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
				
			elif(cpu_choice=="paper"):
				user_points=user_points+1
				a=user_points
				m_display.delete(0,END)
				m_display.insert(0,a) # updated text 
				winner_is.delete(0,END)
				winner_is.insert(0,"You Won!")
				says_now.delete(0,END)
				says_now.insert(0,cpu_choice)
				final_show() 
			



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

	global a 
	global b

	global play_again
	global final_counter

	

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
	a=0
	b=0
	final_counter=False


	final_winner=Label(main_window,text="                                              ",font=("Impact",16),bg="yellow")
	final_winner.grid(row=500,column=1)

	play_again=Label(main_window,text="                                       ",bg="yellow")
	play_again.grid(row=550,column=1)

def final_show():
	global a 
	global b
	global final_winner
	global final_counter


	 

	if(a>=3):
		final_winner=Label(main_window,text="You Won the Game !",font=("Impact",16),bg="light blue")
		final_winner.grid(row=500,column=1)
		play_again=Label(main_window,text="Hit Reset !",font=("Impact",15),bg="yellow") 
		play_again.grid(row=550,column=1)

		final_counter=True
		
		
	elif(b>=3):
		final_winner=Label(main_window,text="CPU Won the Game !",font=("Impact",16),bg="light blue")
		final_winner.grid(row=500,column=1)
		play_again=Label(main_window,text="Hit Reset !",font=("Impact",15),bg="yellow") 
		play_again.grid(row=550,column=1)

		final_counter=False
		

labels()
displays()
buttons()
final_show()
main_window.mainloop() # the closing line 