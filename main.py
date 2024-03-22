import inventory as invent
import user_io as io

#import inventory, user_io modules
def main():
    active = True
    money = io.get_money()
    while active == True: #loop continues until user stops using machine

        print("Welcome to the vending machine")
        print("Your balance:", round(money,2))
        index = 1 #initiate index variable that increases for inventory items

        for key, value in invent.inventory_dict.items():
            print(f'{index}.{key}({value[0]}) : {value[1]} left') #provides options to user and inventory left
            index += 1 #increment index for # of items in list
            
        choice = io.get_choice() #determines user choice

        for key, value in invent.inventory_dict.items():
            if choice == key: #if user's choice is equal to one of the choices available in the machine, move to next if statement
                if money >= value[0]: #if your money value is greater than or equal to the item's cost, purchase is made
                    print("Purchased!")
                    value[1] = value[1] - 1 #quantity is decremented
                    money = money - value[0] #amount paid for item is decremented from money total
                else:
                    print("Inadequate funds")

        key_list = list(invent.inventory_dict.keys())
        value_list = list(invent.inventory_dict.values())

        continue_choice = input("Try again? ") #check if user wants to keep using machine
        
        if continue_choice == "yes":
            continue
        else:
            active = False #breaks loop and ends program if user does not say yes



#define main function that runs program
if __name__ == "__main__":
    main()