print('Imported my module....')

test = "THIS IS JUST FOR PRACTICE"

def find_index(to_search, target):
    """ to find the index of the value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


