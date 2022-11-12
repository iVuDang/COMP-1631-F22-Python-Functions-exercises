even_nums = []  # accumulator variable to collect our results
num = -200  # variable to hold our results

while (num <= 20):
  even_nums.append(num)
  num = num + 2

print(even_nums)

'''
[-200, -198, -196, -194, -192, -190, -188, -186, -184, -182, -180, -178, -176, -174, -172, -170, -168, -166, -164, -162, -160, -158, -156, -154, -152, -150, -148, -146, -144, -142, -140, -138, -136, -134, -132, -130, -128, -126, -124, -122, -120, -118, -116, -114, -112, -110, -108, -106, -104, -102, -100, -98, -96, -94, -92, -90, -88, -86, -84, -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  
'''
#-------------------------------------------------------------------------------


even_nums2 = []

for a_value in range(-200, 21, 2):
  even_nums2.append(a_value)

print(even_nums2)

'''
[-200, -198, -196, -194, -192, -190, -188, -186, -184, -182, -180, -178, -176, -174, -172, -170, -168, -166, -164, -162, -160, -158, -156, -154, -152, -150, -148, -146, -144, -142, -140, -138, -136, -134, -132, -130, -128, -126, -124, -122, -120, -118, -116, -114, -112, -110, -108, -106, -104, -102, -100, -98, -96, -94, -92, -90, -88, -86, -84, -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  
'''
#-------------------------------------------------------------------------------


user_nums = []
again = 'y'

while (again == 'y'):
  userNumber = float(input('Tell me a number: '))
  user_nums.append(userNumber)
  again = input("More numbers (y/n)? ")

print(user_nums)

#-------------------------------------------------------------------------------

for num in range(0, 10, 2):  # generates 0, 2, 4, 6, 8
  square = num**2
  print(f'the square of {num} is {square}')

'''
the square of 0 is 0
the square of 2 is 4
the square of 4 is 16
the square of 6 is 36
the square of 8 is 64
'''
#-------------------------------------------------------------------------------

string = 'hello world'
for index in range(
    len(string)):  # 11 characters in hello world including the space
  print(f'at index {index} is letter {string[index]}')

'''
at index 0 is letter h
at index 1 is letter e
at index 2 is letter l
at index 3 is letter l
at index 4 is letter o
at index 5 is letter  
at index 6 is letter w
at index 7 is letter o
at index 8 is letter r
at index 9 is letter l
at index 10 is letter d
'''
