# GLOBAL VARIABLE - FILE TO PROCESS
file_input = "datafiles/building.txt"


#  1) Function to import data from file.extension
def import_file_transform_data() -> list:
  ## Reads the imported file as is 
  import_file= open(file_input)
  raw_data = import_file.read().strip() 
  """
  G1|--|G1
  G1|--|G1
  G1|--|G1
  """
  import_file.close()


  ## Format the data into a list with sublists. 
  raw_list_split = raw_data.split("\n") 
  # ['G1|--|G1', 'G1|--|G1', 'G1|--|G1']

  test_list = []

  for set in raw_list_split:
    sub_list = set.split("|")  
    """
    ['G1', '--', 'G1']
    ['G1', '--', 'G1']
    ['G1', '--', 'G1']
    """
    test_list.append(sub_list) 
    """
    [
      ['G1', '--', 'G1'], 
      ['G1', '--', 'G1'], 
      ['G1', '--', 'G1']
      ]
    """
  return test_list

print(import_file_transform_data())
"""
[
  ['G1', '--', 'G1'], 
  ['G1', '--', 'G1'], 
  ['G1', '--', 'G1']
  ]
"""

# Global variable to TEST
imported_list = import_file_transform_data()


# 2) Function for GLASS score 
def count_glass_score(glass_list: list) -> int:

  glass_score = 0
  
  for each_row in glass_list:      
      for each_slot in each_row:   
        if (each_slot[0] == 'G'):
          glass_score += int(each_slot[1])

  return glass_score

print("glass score:")
print(count_glass_score(imported_list))


# 3) Function for RECYCLED score
def count_recycled_score(recycled_list: list) -> int:
  r_score_list = [2, 5, 10, 15, 20, 30]
  r_dice_count = 0
  
  for each_row in recycled_list:      
      for each_slot in each_row:   
        if (each_slot[0] == 'R'):
          r_dice_count += 1

  return 0 if (r_dice_count == 0) else (r_score_list[r_dice_count - 1])

print("recycled score:")
print(count_recycled_score(imported_list))


# 4) Functiion for STONE score 
def count_stone_score(stone_list: list) -> int:

  s_score_list = [2, 3, 5, 8, 8, 8]
  stone_score = 0 

  new_stone_list = stone_list.copy()
  new_stone_list.reverse()

  row = 0       
  while row < len(new_stone_list):               
    column = 0

    while column < len(new_stone_list[row]):
      if (new_stone_list[row][column][0] == "S"):
        if (stone_list[row]) == 0:           # this entire if statement set is run if S is found 
          stone_score += s_score_list[row]
        elif (new_stone_list[row] == 1):
          stone_score += s_score_list[row]
        elif (new_stone_list[row] == 2):
          stone_score += s_score_list[row]
        else:
          stone_score += s_score_list[row]
          
      column += 1
    row += 1
  
  return stone_score

print("stone score:")
print(count_stone_score(imported_list))


# 5) Function for WOOD score 
## Function to count the wood score from our vertical loop
def score_vertical_wood(wood_list) -> int: 

  vertical_score = 0
  # TO ADD WHEN WORKING 

  return vertical_score
  


print("print vertical score:")
print(score_vertical_wood(imported_list))


## Function to count the horizontal score 
def score_horizontal_wood(wood_list) -> int: 

  horizontal_score = 0

  i = 0
  while i < len(wood_list):        
    if (wood_list[i][0][0] == 'W'):  # first column check for wood dices
      if (wood_list[i][1] != '--'): 
        horizontal_score += 2
    if (wood_list[i][2][0] == 'W'):  # last column check for wood dices
      if (wood_list[i][1] != '--'): 
        horizontal_score += 2
    if (wood_list[i][1][0] == 'W'):  # for middle column check for wood dices
      if (wood_list[i][0] != '--') and (wood_list[i][2] != '--'):
        horizontal_score += 4
      elif (wood_list[i][0] != '--') or (wood_list[i][2] != '--'):
        horizontal_score += 2
      else:
        horizontal_score += 0
    i += 1

  return horizontal_score

print("print horizontal score:")
print(score_horizontal_wood(imported_list))


## Function to add the vertical and horizontal loops to get the full wood score
def count_wood_score(wood_list):
    vertical_wood_score = score_vertical_wood(wood_list)
    horizontal_wood_score = score_horizontal_wood(wood_list)

    total_wood_score = vertical_wood_score + horizontal_wood_score

    return total_wood_score

print("print wood score:")
print(count_wood_score(imported_list))



# 6) Function to format into f'string and write and export the file
def export_write_scores(glass_score, recycled_score, stone_score, wood_score, total_score) -> str:

    export_file = open("scoring-results.txt", "w")

    import_file= open(file_input)
    raw_data = import_file.read().strip()

    two_lines = '\n' + '\n'
    str_row_1 = "+----------+----+\n"
    str_row_2 = f'| glass    |  {glass_score:>2} |\n'        # in the object :>2 aligns to the right by 2 spaces
    str_row_3 = f'| recycled |  {recycled_score:>2} |\n'
    str_row_4 = f'| stone    |  {stone_score:>2} |\n'
    str_row_5 = f'| wood     |  {wood_score:>2} |\n'
    str_row_6 = f'+==========+====+\n'
    str_row_7 = f'| total    |  {total_score:>2} |\n'
    str_row_8 = "+----------+----+"
    
    str_table = two_lines + str_row_1 + str_row_2 + str_row_3 + str_row_4 +str_row_5 + str_row_6 + str_row_7 + str_row_8

    export_file.write(raw_data)
    export_file.write(str_table)
    export_file.close()


# 7) Main function integrate and run all functions at once. 
def main():
    
    the_imported_list = import_file_transform_data()

    the_glass_score = count_glass_score(the_imported_list)
    the_recycled_score = count_recycled_score(the_imported_list)
    the_stone_score = count_stone_score(the_imported_list)
    the_wood_score = count_wood_score(the_imported_list)

    the_total_score = the_glass_score + the_recycled_score + the_stone_score + the_wood_score

    export_write_scores(the_glass_score, the_recycled_score, the_stone_score, the_wood_score, the_total_score)

main()



"""
CITATIONS:

* Discussed with Patrick Perri for ideas on wooden dice approach, and structure/purpose of the main function for this assignment.

* File practice exercises / examples on importing and exporting files provided by Patrick Perri. 

* Shared ideas/code with Aarav from another class. 

* Difference between .readlines() vs .read()
https://www.askpython.com/python/built-in-methods/python-read-file

.read()
Python
C
C++
Java
Kotlin

.readlines() 
['Python\n', 'C\n', 'C++\n', 'Java\n', 'Kotlin']


* Creating sublists of 3 items from a list: list[x:x + 3] for x in range(0, len(list), 3)
https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
  

* range() fuction 
https://www.w3schools.com/python/ref_func_range.asp


* for loop
https://www.w3schools.com/python/python_for_loops.asp


* append() method
https://www.w3schools.com/python/ref_list_append.asp


* reverse() - how to reverse a copy of the list 
https://www.scaler.com/topics/how-to-reverse-a-list-in-python/


* Other file types to convert list of lists in python 
https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/


* Aligning f'strings
https://miguendes.me/73-examples-to-help-you-master-pythons-f-strings

"""


