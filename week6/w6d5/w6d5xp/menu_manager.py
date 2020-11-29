import json



# menu = {
#     "items": [
#         {
#             "name": "Vegetable soup",
#             "price": 30
#         },
#         {
#             "name": "Hamburger",
#             "price": 44.9
#         },
#         {
#             "name": "Milkshake",
#             "price": 22.5
#         },
#         {
#             "name": "Artichoke",
#             "price": 18
#         },
#         {
#             "name": "Beef stew",
#             "price": 52.5
#         }
#     ]
# }



 
# menu_to_json = open("menu.json", "w") 
  
# json.dump(menu, menu_to_json, indent = 6) 
  
# menu_to_json.close() 





menu = 'menu.json'
with open(menu, 'r') as j_menu:
    menu = json.load(j_menu)




# menu = {}

class MenuManager():
    
    def __init__(self, menu):
        self.menu = menu
    
    
    # def __repr__(self):
    #     return self.menu

    def add_item(self, name, price):
        if name == menu[add_item]:
            return f'New Item added {name}' 
        else: 
            ("something when wrong")

    def remove_item(self, name):
        if name in menu:
            self.menu[name]= name
            del self.menu[name]
            return True
        else:
            return False


    def save_to_file(self, menu):
        
        with open('menu.json', 'w') as change_menu:
            json.dump(self.menu, change_menu)
        




# close_menu = json.dumps(menu)
# print(type(close_menu))


