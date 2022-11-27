god_string = 'Odin,Kihci Manito,An\nFrigg,Grandmother Fox,Nammu\nThor, Avas,Enki\nTyr,Pithsiw,Ershkigal'

print(god_string)
"""
Odin,Kihci Manito,An
Frigg,Grandmother Fox,Nammu
Thor, Avas,Enki
Tyr,Pithsiw,Ershkigal
"""

# Convert string to list of lists. Use .split to create lists 
# string.split(specifies the separator to use when splitting the string)
print("#1")

rows = god_string.split("\n") # splits the original string, into a LIST of LISTS separate by the indicator "\n", does not create a new line 

print(rows)
"""
['Odin,Kihci Manito,An', 'Frigg,Grandmother Fox,Nammu', 'Thor, Avas,Enki', 'Tyr,Pithsiw,Ershkigal']
"""


# .split AGAIN. We used .split on string to break string into a list, but the list has items that can be further split. .split() can split both an orignial string, and a list with items. 
# We can set up a list accumulator, and use list.append(elmnt) to append an element to the end of the list.
# Use the = str.split() method (and others) to create a list called godsList consisting of four rows, each as their own list.
# Hints, the split method will default to creating a list from a string based on the space character. You can instead choose "," or "\n"  as needed. 

gods_list = []  

i = 0

while i < len (rows):               # each row is considered an item in our previous list, being item 1 = 'Odin,Kihci Manito,An', item 2 = 'Frigg,Grandmother Fox,Nammu', item 3 = 'Thor, Avas,Enki', item 4 = 'Tyr,Pithsiw,Ershkigal']
    row_list = rows[i].split(",")   # in our previous list, the strings was separated by "," the while loop is used here to create items in the list one instance at a time, the instance indicated by ","
    print(row_list)

    gods_list.append(row_list)    # we had an empty list accumulator, we'll append the instances to this list, resulting in a horizontal list within a list. 
    i +=1

print(gods_list)
"""
['Odin', 'Kihci Manito', 'An']
['Frigg', 'Grandmother Fox', 'Nammu']
['Thor', ' Avas', 'Enki']
['Tyr', 'Pithsiw', 'Ershkigal']
"""
"""
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]
"""


# II.	Using indexing, print 'Enki'
print("#2")

"""
Recall
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]
"""

print(f'{gods_list[2][2]} is in column 2, row 2')
# Enki is in column 2, row 2


# 3.a. Two loops used to print each item one at a time
print("#3 v1")

"""
Recall
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]
"""

row = 0

while row < len(gods_list):            # while  0 < 4
    print(" | ", end = "")             # print | at the beginning, the end parameter (end='') indicates separated, AVOIDS default of printing on a newline

    column = 0

    while column < len(gods_list[row]):              # while 0 < 3, gods_list[row 0] => ['Odin', 'Kihci Manito', 'An'] 
        print(gods_list[row][column], end = " | " )  # gods_list[row 0][column 0] => Odin, will print all rows while [column] remains static until enter out of this loop, the end parameter (end=' | ') indicates separated by space | space rather than on default of printing on a newline
        column += 1                                  # column now becomes 1, the while loop INSIDE must complete before the while loop outside is runned,   

    print()     # Enters new line otherwise without this, it goes in one single line
    row += 1

    """
 | Odin | Kihci Manito | An |
 | Frigg | Grandmother Fox | Nammu |
 | Thor |  Avas | Enki |
 | Tyr | Pithsiw | Ershkigal |
 
 """

# 3.b. Two for loops to create a vertical display, one item printed per instance
print("#3 v2")

"""
Recall
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]

Perspective: we look at this where each item is a ROW, and each position is the COLUMN
"""

for each_row in gods_list:               # for each item in the list, [odin, kihchi, etc.], [frigg, etc.]    
    for each_name in each_row:           # for loop will prints out each instance within each row odin, kihchi, an
        print (each_name) 
"""
Odin
Kihci Manito
An
Frigg
Grandmother Fox
Nammu
Thor
 Avas
Enki
Tyr
Pithsiw
Ershkigal
"""
        
# 4 First column only, one at a time loop
print("#4")

"""
Recall
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]

Perspective: we look at this where each item is a ROW, and each position is the COLUMN
"""

i = 0

while i < len(gods_list):
    print(gods_list[i][0])      # 0 indicates the first item in a list, ['Odin', 'Kihci Manito', 'An'], the [i] indicates the items "columns" in the list
    i += 1 

"""
Odin
Frigg
Thor
Tyr
"""


# 5 list made of second row
print("#5")

"""
Recall
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]

Perspective: we look at this where each item is a ROW, and each position is the COLUMN
"""

new_list_r2 =[]
i = 0

while i < len(gods_list[1]):                      # refers to ['Frigg', 'Grandmother Fox', 'Nammu'], 3 items in this list
    new_list_r2.append(gods_list[1][i])           # 0 < 3, then we'll add the item starting at index 0 in this list to our new empty list accumulator 
    i += 1                                        # iterates to next item in the list ['Frigg', 'Grandmother Fox', 'Nammu']

print(new_list_r2)

"""
['Frigg', 'Grandmother Fox', 'Nammu']
"""