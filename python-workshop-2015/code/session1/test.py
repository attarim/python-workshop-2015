# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 11:04:32 2015

@author: Mina
"""

def flip_a_string(my_str):
    """
        Take a String and invert it
        ie 
        >>> flip_a_string ("Jeb")
        "Jeb"
    """
    
    my_list = list (my_str)
    my_list.reverse()
    
    my_str = "".join(my_list)
    
    return my_str
    
    # or return "".join(my_list)
  
    
    
def am_i_greater_than_forty (num):
    """ Check weather a number is indeed greater than forty
    Return a Boolean"""
    
    return num > 40
    
def is_this_greater_than_forty(num):
    """Return 'Yes' if the number is greater than 40,
    'No' otherwise """
    
    if am_i_greater_than_forty (num):
        return "Yes"
    else:
        return "No"
        
        
def the_third_element(my_list):
    """Return the third elemet in the mapping 
    """
    try:     
        return my_list[2]
    except TypeError:
        print "Ooops, what are you thinking?"
    # try inputing an ineger
     
def which_numbers_are_greater_than_forty(num_list):
    
    """ Returns a list of BOOlean objects depending on weather each number 
    is greater than 40
    """
    my_bool_list = []
    for i in num_list:
        my_bool_list.append(am_i_greater_than_forty(i))
    return my_bool_list
    
        