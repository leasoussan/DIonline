from game import *


# Rock-Paper-Scissors.Py : Create 3 Functions
# get_user_menu_choice() - this should display a simple menu, 
# get the user’s choice (with data validation), and return the choice. No looping should occur here.

# print_results(results) – this should print the results of the games played. 
# It should have a single parameter named results; 
# which will be a dictionary of the results of the games played. 
# It should display these results in a user-friendly way, 
# and thank the user for playing.
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. 
# Bear in mind that this dictionary will need to be created and populated in some other part of our code, 
# and passed in to the print_results function at the right time.

# main() - the main function. It should take care of 3 things:

# displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)
# When the user chooses to play a game:
# Create a new Game object (see below), and call its play()* function, receiving the result of the game that is returned.
# Remember the results of every game that is played. More about this below.
# When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.




def get_user_menu_choice():
    print("Menu")
    print("(g) Play a game")
    print("(x) Show scores and Exit")
    choice_input =input("")
    if choice_input not in ["x", "g"]:
        raise ValueError("Please choose g or x")
    else:
        print("lets' Start***")
        return choice_input



# 
# this should print the results of the games played. 
# It should have a single parameter named results; which will be a dictionary 
# of the results of the games played. It should display these results in a 
# user-friendly way, and thank the user for playing.
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. 
# Bear in mind that this dictionary will need to be created and populated in 
# some other part of our code, and passed in to the print_results function at 
# the right time.



def print_results(results):
    
    print(f"\
    Game Results:\n\
     Your won: {results['win']} times \n\
     You lost: {results['loss']} \n\
     You drew {results['draw']} \n\
    \n\
Thank you for Playing")






# for key, values in results:
# You results {results[key]} {results[values]} ")

 




def main():
    results = {
        "win":0,
        "loss": 0,
        "draw" :0
    }
    while True:
        user_menu_choice = get_user_menu_choice()
        if user_menu_choice == "g":
            round_result = Game().play()
            results[round_result] += 1

        elif user_menu_choice in ["x", "q"]:    
            print_results(results)
            break

        else:
            print("wrong Input")
            continue

            





# displaying the menu repeatedly, 
# until the user types in the value to exit the program: ‘x’ or ‘q’,
# whatever you decide. (Make use of the get_user_menu_choice function)
# When the user chooses to play a game:
# Create a new Game object (see below), and call its play()* function, 
# receiving the result of the game that is returned.
# Remember the results of every game that is played. More about this below.
# When the user chooses to exit the program, 
# call the print_results function in order to display a summary of all 
# the games played.

