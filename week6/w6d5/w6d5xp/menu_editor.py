from menu_manager import *



def load_manager():
    menu_load = MenuManager(menu)
    return menu_load 


    

def show_user_menu(): 
    # will show the program menu (not menu)
    # call appropriate function that matche user input
    program_menu = (f"\
     MENU:\n\
    (a) ADD ITEM\n\
    (d) DELETE AN ITEM \n\
    (v) VIEW THE MENU \n\
    (x) EXIT\n\
        ")

    while True:
            menu_choice = input("Input your choice")
            options = ["a", "s", "v", "x"]
            if menu_choice in options:
                menu_choice = menu_choice.lower()
                if menu_choice == "a":
                    add = add_item_to_menu()
                    
            else:
                print("Invalide Entry")
                continue

def add_item_to_menu():
    menu = load_manager()
    print(menu)
    add_item = input("Item/plate name")
    add_price = input("Price")
    
    add_to_menu = MenuManager(menu).add_item(add_item,add_price)
    menu[add_item]= add_price
    save = save_to_file()
    if add_item == menu[add_item]:
        print("Item added with success ") 
    else: 
        print("we had a n issues addin it")

def remove_item_from_menu():
    # will call function from class 
    # print message if it was done or Not
    pass

def show_restaurant_menu():
    # show the menu GUI 
    pass




class MenuItem()

    def __init__(self, name, price):
        self.name = name
        self.price = price

    

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):


    def all(self):
        # allitems in menu
        pass

    def get_by_name(self):
        query= "SELECT "





        