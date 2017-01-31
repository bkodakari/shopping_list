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

shopping_list = ["Bread", "Apples", "Cheese", "Milk"]


def main():
    print "Right now your list has:", shopping_list
    to_do = raw_input("Would you like to add? Y or N ").upper()
    if to_do == "Y":
        add_to_the_list()
    else:
        remove_from_list()

if __name__ == '__main__':
    main()
