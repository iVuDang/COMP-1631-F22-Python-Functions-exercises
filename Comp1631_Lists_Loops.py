even_nums = []  # accumulator variable to collect our results
num = -200  # variable to hold our results

while (num <= 20):
  even_nums.append(num)
  num = num + 2

print(even_nums)

print('---------------------')

even_nums2 = []

for a_value in range(-200, 21, 2):
  even_nums2.append(a_value)

print(even_nums2)

print('---------------------')

user_nums = []
again = 'y'

while (again == 'y'):
  userNumber = float(input('Tell me a number: '))
  user_nums.append(userNumber)
  again = input("More numbers (y/n)? ")

print(user_nums)

print('---------------------')

for num in range(0, 10, 2):  # generates 0, 2, 4, 6, 8
  square = num**2
  print(f'the square of {num} is {square}')

print('-----------------------')

string = 'hello world'
for index in range(
    len(string)):  # 11 characters in hello world including the space
  print(f'at index {index} is letter {string[index]}')
