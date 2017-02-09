shopping_list = {"target": "socks, advil, coffee", "safeway": "eggs, milk, cheese"}


def print_menu():
    print "0 - Main Menu"
    print "1 - Show all lists"
    print "2 - Show a specific list"
    print "3 - Add a new shopping list"
    print "4 - Add an item to a shopping list"
    print "5 - Remove an item from a shopping list"
    print "6 - Remove a list by nickname"
    print "7 - Exit when you are done"


def add_to_the_list():
    new_item = raw_input("What do you want to add? ").title()
    if new_item in shopping_list[0:]:
        print "You've already got that on the list"
        shopping_list.sort()
        print shopping_list
        return shopping_list
    else:
        shopping_list.append(new_item)
        shopping_list.sort()
        print shopping_list
        return shopping_list


def remove_from_list():
    remove_item = raw_input("What do you want to remove? ").title()
    print remove_item
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        shopping_list.sort()
        print "Your updated list is now:", shopping_list
        return shopping_list
    else:
        print "You don't have that on your list anyway!"
        return shopping_list

# create a dictionary of shopping lists
# create a function that prints out the main Menu
# for the first option (0) on the main menu, create a shortcut back to the main menu
# for the second option (1) on the main menu, print out all of the available shopping lists
# for the third option (2) on the main menu, print out a specific list -- for example: print the list for target (key: value) in alphabetical order  --  .title()
# for the fourth option (3) on the main menu, add a new shoppping list to the dictionary (new key) if the list is not already there --  .title()  --  print out new list
# for the fifth option (4) on the main menu, add a new item to an existing shopping list if it is not already on there  -- .title()  --  print out a new list  --  loop (are you done?)
# for the sixth option (5) on the main menu, Remove an item from an existing shopping list if it is on there  --  print out a new list  --  loop (are you done?)
# for the seventh option (6) on the main menu, Remove an entire list from the dictionary (by nickname)
# for the final option (7): exit the loop (break)http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python

def main():
    print_menu()
    menu_option = int(raw_input("What would you like to do? Pick a number: 0-7 "))

    if menu_option == 0:
        main()

    if menu_option == 1:
        for my_lists in shopping_list:
            print my_lists.title()

    if menu_option == 2:
        for my_lists in shopping_list:
            print my_lists.title()
        list_of_choice = raw_input("What list would you like to see? ").lower()
        print shopping_list[list_of_choice].title()

    if menu_option == 3:
        for my_lists in shopping_list:
            print my_lists.title()
        new_list = raw_input("Where do you want to shoppping now?").lower()
        shopping_list[new_list] = " "
        print shopping_list

    if menu_option == 4:
        for my_lists in shopping_list:
            print my_lists.title()
        what_list = raw_input("Which list would you like to add to?").lower()
        print shopping_list[what_list]
        add_to_the_list()



if __name__ == '__main__':
    main()
