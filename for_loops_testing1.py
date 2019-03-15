#! python 3
'''Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For
example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********'''
some_list = ["Hello", "World", "in", "a", "frame.", "This", "is", "Sparta!", "Some","more",
             "testing!", "A", "bit", "SsssSSstringGgg"]

def frame_it(table):
    #create an empty list for the max lenght
    max_len_list = []
    for i in range(len(table)):
        max_len_list.append(len(table[i]))
     #assign the max lenght as variable   
    the_max_from_list = (max(max_len_list))
    
    print("*"*(the_max_from_list+4))
    #the printing of the string with *s
    for i in range(len(table)):
        print("* "+table[i]+(" "*((the_max_from_list+4)-(3+len(table[i])))+"*"))
        
    print("*"*(the_max_from_list+4))

frame_it(some_list)