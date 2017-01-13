"""This is the entry point of the program."""


def highest_number_cubed(limit):

    #Make a list of empty numbers to use in for loop
    numbers = []
    
    #Create a for loop that makes a list using range from limit input
    for i in range(limit):
        
        #If the number in limit cubed is less than three, put said number
        #into list numbers
        if i**3 < limit:
            numbers.append(i)
    
    #Returns the last number in list numbers
    return numbers[-1] 

"""
def highest_number_cubed2(limit):
    previous_number = 1
    
    while True:
        current_number = previous_number + 1
        if current_number ** 3 > limit:
            return previous_number
        
        previous_number = current_number
"""
        
        
        
    
        
