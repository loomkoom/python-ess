class ListItem:
    def __init__(self, name):
        assert isinstance(name, str)
        self.__name = name
        self.__next = None

    def next(self):
        return self.__next

    def add_next(self, next_item):
        assert isinstance(next_item, ListItem)
        self.__next = next_item

    def __str__(self):
        return self.__name

today = ListItem('Today')
tomorrow = ListItem('Tomorrow')
yesterday = ListItem('Yesterday')

today.add_next(tomorrow)
yesterday.add_next(today)

print(str(yesterday))
print(str(today.next()))

# Create yesterday and tomorrow objects of the ListItem class,
# give them a meaningful name,
# and link them together in the correct order.


# Print out the String representation of the yesterday object.


# Using your today object, print out the String representation of the item that follows it.


# Complete the following function so that it prints out the received ListItem object and
#  all existing subsequent objects.

def print_list_items(list_item):
    if list_item is not None:
        print(list_item)
        return print_list_items(list_item.next())

print_list_items(yesterday)

# Call the print_list_items() function with your yesterday object as a parameter value, and
# check that it prints out the days in the correct order.


