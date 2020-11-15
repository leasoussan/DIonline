# Here Are The Rules:
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# Hint
# To do this project, you basically need to program four functions: * display_board() – To display Tic Tac Toe board (GUI). * player_input(player) – To get input position from the player. * check_win() – To check winner of the game. * play() – More like the main function, which calls above function for gameplay.

# Note: The 4 functions above are just an example idea. You can implement many more helper functions or choose a completely different design if you want.

# Tips : Consider The Following:
# What actions will need to happen every turn to make this program work?
# With the question above in mind, think about how to break up your code into smaller pieces (functions)
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

# Functions to have:
# display_board() – To display Tic Tac Toe board (GUI). * 
# player_input(player) – To get input position from the player. * 
# check_win() – To check winner of the game. * 
# play() – More like the main function, which calls above function for gameplay.


board = [
    ["   ","   ","   "],
    ["   ","   ","   "],
    ["   ","   ","   "],
]

def display_board():
    
    star = "*"
    border_vertical =len(board)*4 * star
    print("Welcome to Tic Tac Toe of Lea ")
    print(border_vertical)
    print('*'+ board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '*')
    print('*'+ '---|---|---'+ '*')  
    print('*'+ board[1][0]+ '|' + board[1][1] + '|' + board[1][2]+ '*')
    print('*'+ "---|---|---"+ '*')    
    print('*'+ board[2][0] + '|' + board[2][1] + '|' + board[2][2]+ '*')
    print( border_vertical )
    

# # print(display_board())


players = {
    "player_1": "X",
    "player_2": "O"

            }


        

def player_input(player): 
        display_board() 
        
        turn_start =print(f"this is {player}\'s turn ")         
        row =[0]
        col = [0]
        play_row = (input("Choose a Row"))
        play_col = (input("Choose a colom"))
        
        for p in play_row:
            for pl in play_col:
            if 
        board[row][col] = "X"  

        return display_board    


print(player_input("X"))        


# # def play():
# #     board = display_board()
# #     player = player_input()

# #     if board[0][0] === board[0][1] == board[0][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
    
# #     if board[1][0] == board[1][1]== board[1][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")    
# #     if board[2][0] == board[2][1]== board[2][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")    
# #     if board[0][0] == board[1][1] == board[2][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
# #     if board[0][0] == board[1][0] == board[2][0]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
# #     if board[0][2] == board[1][2] == board[2][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
# #     if board[0][0] == board[1][1] == board[2][2]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
# #     if board[2][2] == board[1][1] == board[2][0]:
# #         print(f" well donnnnnnnnneee {player_input} WON")
    
# #     return board


# # check_win() – To check winner of the game. * 
#     # count = 0 

# # def play():
    




# # first we want to display board

# # let a player to start- set the players 
# # asking input -- get the input only if the space is empty >> then we will board[target]= X or O
# # 
# # first we want to know who's turn to play 

# # then we let him play function 

X = row =1, col =1
borad[row][col]="X"
make sure that when the response is 1 2 3 we should soubstract one