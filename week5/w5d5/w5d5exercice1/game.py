# gamee - game against computer 
# get results and retrun them 
import random


class Game():

    # def __init__(self, user_item, computer_item):
    #     self.user_item = user
    #     self.computer_item = computer


    def get_user_item(self):
        while True:
            choice_played =input("please select R:Rock ;  S:Scisors ; P:Paper")
            options = ["r", "s", "p"]
            if choice_played in options:
                return choice_played.lower()
                break
            else:
                print("Invalide Entry")
                continue



    def get_computer_item(self):
        computer_choice = random.choice(["s", "r", "p"])
        return computer_choice



    def get_game_result(self, user_item, computer_item):
        
        if user_item == computer_item:
            return "draw"
        
        if user_item == "r" and computer_item == "s":
            return 'win'

        if user_item == "s" and computer_item == "p":
            return 'win'
        
        if user_item == "P" and computer_item == "r":
            return 'win'
        
        else:
            return 'loss'
            

# here we are only looking at the scoors of the winner - as if he wins the other lose.
# 


# we use the static methode that we ll be able to use it outside of the class-storing inside the class but use if aas well outside

    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        round_result = self.get_game_result(user_choice, computer_choice)
        print(f'you played {user_choice} The Computer played{computer_choice} you {round_result}')
        return round_result