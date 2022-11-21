"""
Design and implement a Python function named get_courses that returns
a list of strings containing student courses. Your function should behave as follows

Enter the name of a course to add, or press Enter to finish: COMP 1501
Enter the name of a course to add, or press Enter to finish: MATH 1505
Enter the name of a course to add, or press Enter to finish:

2 courses added

Hints:
o Set up the function with no ideal parameters.
o Within the function, use a loop to prompt the user, but make sure to
think about your exit condition.
o The number of courses added will not always be 2 - this should be
calculated.
 You could use an accumulator that is incremented with a
condition, OR look for a Python built-in function

"""

def get_courses():
  resulting_courses = []
  name = "1"

  while name != "":
    name = input(
      "Enter the name of a course to add, or press Enter to finish: ")
    resulting_courses.append(name)

  tally = len(resulting_courses)
  print(f'{tally} courses added')
  return resulting_courses


def main():
  my_courses = get_courses()


main()



#-------------------------------------------------------------------------------


"""
Python Programming for Beginner - Jason Cannon 
"""

to_do_list = [] # empty array list accumulator
finished = False  # stopper

while not finished:
  task = input('Enter a task. Press <enter> to end:')
  if len(task) == 0:
    finished = True
  else:
    to_do_list.append(task) #appends the task input to our list array
    print('Task added.') #after adding, it prints the message
  print(to_do_list)


print('Your To-Do List:')
print('-' *16)

for task in to_do_list:
  print(task)


#-------------------------------------------------------------------------------


user_nums = []
again = 'y'

while (again == 'y'):
  userNumber = float(input('Tell me a number: '))
  user_nums.append(userNumber)
  again = input("More numbers (y/n)? ")

print(user_nums)