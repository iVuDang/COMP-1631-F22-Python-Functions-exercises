def slicer_method(any_list) -> int:
    result_numbers = [] # empty list accumulator
    i = 0 # iteration accumulator AND acts as index location reference
  
    while i < len(any_list): #len counts amount of items, to loop through entire list

        number_portion = int(any_list[i][5::])  ;print(number_portion) # slices the item
        result_numbers.append(number_portion) # adds the sliced items to our list accumulator
        i += 1 #adjusts our iteration accumulator up, and so it can move to next item

    largest = max(result_numbers) #after while loop reaches the len count, return largest value in our list accumulator
    where = result_numbers.index(largest) # finds the position of the largest value in our list accumulator
    # could also do in just one line .index(max(largest))

    return where     


def listsOlists_method(a_list) -> int:

    name_number_list = []
    just_names = []
    just_numbers = []

    i = 0
    while i < len(a_list):

        sub_list = a_list[i].split()  ;print(sub_list) # splits "COMP 1501" into  ['COMP', '1501']
        name_number_list.append(sub_list)  

        just_names.append(name_number_list[i][0]) ;print(just_names) #accumulates just the text e.g. 'COMP'
        just_numbers.append(name_number_list[i][1]) ;print(just_numbers) #accumulates the numbers e.g. '1501'

        i += 1
      
    print(name_number_list)
    
    largest = max(just_numbers)  # returns the largest number
    where = just_numbers.index(largest)  # finds index position of the largest number
    return where



def main() -> None:

    courses = ["COMP 1501", "Math 1505", "GNED 1401", "GNED 1103", "MKTG 2150",
    "COMP 1502", "COMP 2511", "MGMT 3210", "HRES 2170", "GNED 1101"]

    location_largest_one = slicer_method(courses)  
    location_largert_two = listsOlists_method(courses) 

    print("the biggest number is", courses[location_largest_one] )
    print("the biggest number is", courses[location_largert_two] )

main()


