grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = len(grid[0]) #If we increase the grid with another row(s) this will adapt
y = len(grid)    #itself instead of hardcoding the ranges.

for i in range (x):
    for j in range (y):
        print (grid[j][i], end="")     
    print()

"""
Create any list and print all the list items with a ","
and "and" before the last item. I went one step further
and decided to ask the user for the list items.

"""

list1 = []
str1 = ""
#ask user for list input break by enter
while True:
    user_input = input("Please enter an item (Enter to quit): ")
    if user_input == "":
        break
    list1.append(user_input)
for i in range (len(list1)-1):
    str1 = str1 + list1[i] + ", " #add to the empty string with ", " at the end 
if len(list1) == 1: #check if list len is 1. if yes, print the first item of the list
    str1 = list1[0] #print the first item otherwise it will print the list with []
    print (str1)
else:
    print (str1 + "and " + list1[-1])
