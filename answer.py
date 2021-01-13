def print_every_third_element(l, start=0):
    '''
    Function that prints every third element of an input list recursively.
    Params:
    l: list
    start: index from where we should start printing
    '''
    
    if start < len(l):
        print(l[start])
        print_every_third_element(l, start=start+3)

    # else return
    

if __name__ == "__main__":
    print_every_third_element([1, 2, 3, 4, 5, 6, 7, 8, 9])