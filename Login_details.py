#Login details
#This is going to be 5 windows
#1. Choose either Admin or User login
#2. Admin Login Window
#3. User Login Window
#4. For Admin, they can sign up or remove users.
#5. For Users, they can play connect 4.

#CHECKPOINTS 
#Starting window -> Admin or User? -> WORKING 
#Secondary windows -> Admin Login -> WORKING
#Secondary windows -> User Login (2 player login) -> WORKING
#Third tier window -> Admin create/delete account ->  WORKING
#Third tier window -> Connect 4 game -> WORKING

#Import libraries
import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import numpy as np
import pygame
import sys
import math
import re

#Close window
def close():
   #win.destroy()
   root.quit()

#This opens up the user login window
def userWindow():
   #Users Login
   #This takes login info for 2 players
   #It will check the info and then open up the actual connect 4 game
   def close2():
      #win.destroy()
      user.quit()
      #Checks login details
   def login_correct_users(username, password, filepath):
      password = password+"\n"
      with open(filepath, 'r') as file:
         lines = file.readlines()
         for line in lines:
               fields = line.split(",")
               if (fields[0] == username and fields[1] == password):
                  return True
      return False

   def logged_in_users():
      if (login_correct_users(Enter_player1_user.get(), Enter_player1_pass.get(), ("C:/Users/hpamn/OneDrive/Desktop/University/Term 2/OOP 1/OOP1 Quiz 4 Project/26406_ManahilFirdous_OOP1/Login_Details.txt" == True)) and (login_correct_users(Enter_player2_user.get(),Enter_player2_pass.get(),"Login_user.txt") == True)):
         if (Enter_player1_user.get() != Enter_player2_user.get()) and (Enter_player1_pass.get() != Enter_player2_pass.get()):
            messagebox.showinfo("Login","Login Successful!")
            connect4()
         else:
            messagebox.showerror("Error","Both logins are the same")
      else:
         messagebox.showerror("Error", "Login details incorrect")

   user = tkinter.Tk()
   user.title("Login for Connect 4 Game")
   canvas3 = tk.Canvas(user, width=250, height=250, bg='grey')
   canvas3.pack()

   #This label is for player 1
   Label2_1 = Label(user, text="Player 1: ", bg='grey',fg='black', font=('Times New Roman',12,'bold'))
   canvas3.create_window(55,19,window=Label2_1)

   #This label and entry is for Player 1 username
   player1_user = tk.Label(user, text="Username", bg="grey", fg="black", font=('Times New Roman',11))
   canvas3.create_window(40, 50, window=player1_user)

   # Entry field for username
   Enter_player1_user = tk.Entry(user, bd=1)
   canvas3.create_window(150, 50, window=Enter_player1_user)

   #This label and entry is for Player 1 password
   # Create password label
   player1_pass = tk.Label(user, text="Password", bg="grey", fg="black", font=('Times New Roman',11))
   canvas3.create_window(40, 90, window=player1_pass)

   # Entry field for the password
   Enter_player1_pass = tk.Entry(user, bd=1,show="*")
   canvas3.create_window(150, 90, window=Enter_player1_pass)


   #This label is for player 2
   Label2_2 = Label(user, text="Player 2: ", bg='grey',fg='black', font=('Times New Roman',12,'bold'))
   canvas3.create_window(55,120,window=Label2_2)

   #This label and entry is for Player 2 username
   player2_user = tk.Label(user, text="Username", bg="grey", fg="black", font=('Times New Roman',11))
   canvas3.create_window(40, 150, window=player2_user)

   # Entry field for username
   Enter_player2_user = tk.Entry(user, bd=1)
   canvas3.create_window(150, 150, window=Enter_player2_user)

   #This label and entry is for Player 2 password
   # Create password label
   player2_pass = tk.Label(user, text="Password", bg="grey", fg="black", font=('Times New Roman',11))
   canvas3.create_window(40, 190, window=player2_pass)

   # Entry field for the password
   Enter_player2_pass = tk.Entry(user, bd=1,show="*")
   canvas3.create_window(150, 190, window=Enter_player2_pass)

   #This will excecute the 'going to the actual window' command where the window corresponding to the button chosen will open up
   Submit_button3 = tkinter.Button(user, text="Submit",command=connect4,bg='grey', fg='white', width=6, height=1)
   canvas3.create_window(120,225,window=Submit_button3)

   #Menut_but
   my_menu2 = Menu(user)
   user.config(menu=my_menu2)
   #Create options menu
   options_menu2 = Menu(my_menu2, tearoff=False)
   my_menu2.add_cascade(label="Options", menu=options_menu2)
   #options_menu.add_command(label="Reset Game", command=reset)
   #This adds the close command to the options ribbon in the window.
   options_menu2.add_command(label="Close window", command=close2)

   user.mainloop()

#This opens up the admin login window
def adminWindow():
   #Closes window
   def close1():
      #win.destroy()
      admin.quit()

   #Checks login details
   def login_correct(username, password, filepath):
      password = password+"\n"
      with open(filepath, 'r') as file:
         lines = file.readlines()
         for line in lines:
               fields = line.split(",")
               if (fields[0] == username and fields[1] == password):
                  return True
      return False

   def logged_in():
      if login_correct(admin_user_entry.get(), Enter_admin_pass.get(), "C:/Users/hpamn/OneDrive/Desktop/University/Term 2/OOP 1/OOP1 Quiz 4 Project/26406_ManahilFirdous_OOP1/Login_admin.txt") == True:
         messagebox.showinfo("Login","Login Successful!")
         admin_add()
      else:
         messagebox.showerror("Error", "Login details incorrect")

   admin = tkinter.Tk()
   admin.title("Administrator")
   canvas2 = tk.Canvas(admin, width=250, height=200, bg='grey')
   canvas2.pack()

   Label1 = Label(admin, text="Enter the Administrator Details: ", bg='grey',fg='black')
   canvas2.create_window(95,15,window=Label1)

   admin_user = tk.Label(admin, text="Username", bg="grey", fg="black")
   canvas2.create_window(40, 50, window=admin_user)

   # Entry field for username
   admin_user_entry = tk.Entry(admin, bd=1)
   canvas2.create_window(150, 50, window=admin_user_entry)

   # Create password label
   admin_pass = tk.Label(admin, text="Password", bg="grey", fg="black")
   canvas2.create_window(40, 90, window=admin_pass)

   # Entry field for the password
   Enter_admin_pass = tk.Entry(admin, bd=1,show="*")
   canvas2.create_window(150, 90, window=Enter_admin_pass)

   #This will excecute the 'going to the actual window' command where the window corresponding to the button chosen will open up
   Submit_button2 = tkinter.Button(admin, text="Submit",command=logged_in, bg='grey', fg='white', width=6, height=1)
   canvas2.create_window(60,150,window=Submit_button2)

   #Menu
   my_menu1 = Menu(admin)
   admin.config(menu=my_menu1)

   #Create options menu
   options_menu1 = Menu(my_menu1, tearoff=False)
   my_menu1.add_cascade(label="Options", menu=options_menu1)

   #This adds the close command to the options ribbon in the window.
   options_menu1.add_command(label="Close window", command=close1)

   admin.mainloop()

#This opens up the admin add/remove user window
def admin_add():

   #This deletes the user's account
   def user_delete():
      import re
      infile = open("C:/Users/hpamn/OneDrive/Desktop/University/Term 2/OOP 1/OOP1 Quiz 4 Project/26406_ManahilFirdous_OOP1/Login_Details.txt", 'r+')
      content = infile.read()
      updated_content = re.sub(Enter_user_details.get()+","+Enter_user_pass.get()+"\n", '', content)
      infile.seek(0)
      infile.write(updated_content)
      infile.truncate()
      infile.close()
      return True

   #This adds the user's account
   def user_add():
      flag = False
         #strText = Enter_user_details.get()
         #pattern = re.compile("pass[a-zA-Z][0-9]{2,}[.]$")  
         #if pattern.match(strText):
      with open("C:/Users/hpamn/OneDrive/Desktop/University/Term 2/OOP 1/OOP1 Quiz 4 Project/26406_ManahilFirdous_OOP1/Login_Details.txt","r") as thefile:
         for user in thefile:
            if user.rstrip() != Enter_user_details.get():
               with open("Login_user.txt","a") as file:
                  file.write(Enter_user_details.get()+","+Enter_user_pass.get())
                  file.write('\n')
                  file.close()
                  flag = True
         #else:
         #   messagebox.showerror("Error!","Password should be 'pass',\n a letter,\n two or more numbers from 0 to 9,\n and a .")
         #flag = True

#Submit button
   def submit():
      if Enter_user_details.get() =="" and Enter_user_pass.get() == "":
               messagebox.showerror("Error!","Please enter username and password")
      else:
          messagebox.showinfo("Connect 4","Action completed")

   admin_user = tkinter.Tk()
   admin_user.title("Administrator")
   canvas4 = tk.Canvas(admin_user, width=250, height=250, bg='grey')
   canvas4.pack()

   var = IntVar()


   #This label is for user details
   Label3_1 = Label(admin_user, text="Enter user details: ", bg='grey',fg='black', font=('Times New Roman',12,'bold'))
   canvas4.create_window(70,19,window=Label3_1)

   #This label and entry is for user's username
   user_details = tk.Label(admin_user, text="Username", bg="grey", fg="black", font=('Times New Roman',11))
   canvas4.create_window(40, 50, window=user_details)

   # Entry field for username
   Enter_user_details = tk.Entry(admin_user, bd=1)
   canvas4.create_window(150, 50, window=Enter_user_details)

   #This label and entry is for user's password

   # Create password label
   user_pass = tk.Label(admin_user, text="Password", bg="grey", fg="black", font=('Times New Roman',11))
   canvas4.create_window(40, 90, window=user_pass)

   # Entry field for the password
   Enter_user_pass = tk.Entry(admin_user, bd=1,show="*")
   canvas4.create_window(150, 90, window=Enter_user_pass)


   #This label is for what you want to do with the user's account
   Label3_2 = Label(admin_user, text="What do you want to do? ", bg='grey',fg='black', font=('Times New Roman',12,'bold'))
   canvas4.create_window(90,140,window=Label3_2)

   #The radio buttons
   #This button will go to the admin login window
   R4_1 = tk.Radiobutton(admin_user, text="Create user account",variable=var,command=user_add, value=1, bg='grey')
   canvas4.create_window(68, 170, window=R4_1)

   #This button will go to the user login window
   R4_2 = tk.Radiobutton(admin_user, text="Delete user account",variable=var,command=user_delete, value=2, bg='grey')
   canvas4.create_window(68, 190, window=R4_2)

   #This will excecute the 'going to the actual window' command where the window corresponding to the button chosen will open up
   Submit_button4 = tkinter.Button(admin_user, text="Submit",command=submit, bg='grey', fg='white', width=6, height=1)
   canvas4.create_window(120,225,window=Submit_button4)

   admin_user.mainloop()

#This opens up the connect 4 game window
def connect4():
   #Connect4

   #This is the actual game that the 2 players will be able to play.
   #It has 2 colour disks- red and yellow
   #A player has to get in 4 of the same colour in a row to win.


   BROWN = (139, 69, 19)  # Brown color
   GREY = (128, 128, 128)  # Grey color
   RED = (255, 0, 0)       # Red color
   YELLOW = (255, 255, 0)  # Yellow color

   ROW_COUNT = 6
   COLUMN_COUNT = 7

   # Function to create the game board
   def create_board():
      board = np.zeros((ROW_COUNT, COLUMN_COUNT))
      return board

   # Function to drop a piece on the board
   def drop_piece(board, row, col, piece):
      board[row][col] = piece

   # Function to check if a location is valid for placing a piece
   def is_valid_location(board, col):
      return board[ROW_COUNT - 1][col] == 0

   # Function to get the next open row in a column
   def get_next_open_row(board, col):
      for r in range(ROW_COUNT):
         if board[r][col] == 0:
               return r

   # Function to print the board to the console
   def print_board(board):
      print(np.flip(board, 0))

   # Function to check if a player has won
   def winning_move(board, piece):
      # Check horizontal locations for win
      for c in range(COLUMN_COUNT - 3):
         for r in range(ROW_COUNT):
               if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                  return True

      # Check vertical locations for win
      for c in range(COLUMN_COUNT):
         for r in range(ROW_COUNT - 3):
               if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                  return True

      # Check positively sloped diagonals
      for c in range(COLUMN_COUNT - 3):
         for r in range(ROW_COUNT - 3):
               if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                  return True

      # Check negatively sloped diagonals
      for c in range(COLUMN_COUNT - 3):
         for r in range(3, ROW_COUNT):
               if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                  return True

   # Function to draw the game board
   def draw_board(board):
      for c in range(COLUMN_COUNT):
         for r in range(ROW_COUNT):
               pygame.draw.rect(screen, BROWN, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
               pygame.draw.circle(screen, GREY, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

      for c in range(COLUMN_COUNT):
         for r in range(ROW_COUNT):
               if board[r][c] == 1:
                  pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
               elif board[r][c] == 2:
                  pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
      pygame.display.update()

   # Create the game board
   board = create_board()
   print_board(board)
   game_over = False
   turn = 0

   # Initialize pygame
   pygame.init()

   # Set the screen size
   SQUARESIZE = 80
   width = COLUMN_COUNT * SQUARESIZE
   height = (ROW_COUNT + 1) * SQUARESIZE
   size = (width, height)
   RADIUS = int(SQUARESIZE / 2 - 5)

   screen = pygame.display.set_mode(size)
   draw_board(board)
   pygame.display.update()

   myfont = pygame.font.SysFont("monospace", 65)

   while not game_over:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
               sys.exit()

         if event.type == pygame.MOUSEMOTION:
               pygame.draw.rect(screen, GREY, (0, 0, width, SQUARESIZE))
               posx = event.pos[0]
               if turn == 0:
                  pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
               else:
                  pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
               pygame.display.update()

         if event.type == pygame.MOUSEBUTTONDOWN:
               pygame.draw.rect(screen, GREY, (0, 0, width, SQUARESIZE))
               posx = event.pos[0]
               col = int(math.floor(posx / SQUARESIZE))

               if is_valid_location(board, col):
                  row = get_next_open_row(board, col)
                  drop_piece(board, row, col, turn + 1)

                  if winning_move(board, turn + 1):
                     label = myfont.render(f"Player {turn + 1} wins!!", 1, RED if turn == 0 else YELLOW)
                     screen.blit(label, (5, 10))
                     game_over = True

               print_board(board)
               draw_board(board)

               turn += 1
               turn %= 2

               if game_over:
                  pygame.time.wait(900)

#This is the command to open the login windows
def open_login():
   if radiovar.get() == 1:
      adminWindow()
   elif radiovar.get() == 2:
      userWindow()

#Make the window
root = tkinter.Tk()
#Title the window
root.title("Connect 4 Game")
#Set the dimensions and background colour
canvas1 = tk.Canvas(root , width=250,height=150, bg='grey')
#Pack it 
canvas1.pack()

radiovar = IntVar()

#This will display the text at the top of the window
L1 = Label(root, text="Select how you want to enter: ", bg='grey',fg='black')
canvas1.create_window(90,15,window=L1)

#This button will go to the admin login window
R1 = tk.Radiobutton(root, text="Administrator",variable=radiovar, value=1, bg='grey')
canvas1.create_window(68, 50, window=R1)

#This button will go to the user login window
R2 = tk.Radiobutton(root, text="User/Players",variable=radiovar, value=2, bg='grey')
canvas1.create_window(63, 80, window=R2)

#This will excecute the 'going to the actual window' command where the window corresponding to the button chosen will open up
Submit_button = tkinter.Button(root, text="Submit", command=open_login, bg='grey', fg='white', width=6, height=1)
canvas1.create_window(60,130,window=Submit_button)

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
#options_menu.add_command(label="Reset Game", command=reset)
#This adds the close command to the options ribbon in the window.
options_menu.add_command(label="Close window", command=close)

root.mainloop()