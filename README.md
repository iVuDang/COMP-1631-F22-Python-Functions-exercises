# COMP-1631-F22-Functions-exercises
## Purpose:
* I created python functions to process inputs into desired outputs, involving use of input() to take parameters from the user, and main() to call upon previous functions. 

## Citations:
* Problems provided by **Comp 1631 F22 - Prof. Patrick Perri** - Mount Royal University. 

## Preview:
<img src="https://github.com/iVuDang/COMP-1631-F22-Functions-exercises/blob/main/Comp1631_Preview_Image.png" width=100% height=100%>


## Technologies: 
* Python 

## Tools:
* Replit
* Visual Studio Code


---
## Outcome:

* See attached "Comp1631_Python_Functions.py"

---

## What I learned: 

* Break problems into **small enough problems** so that the problems cannot be wrong when solving them.
* Return smaller expected values, rather than aggregated calcs. Use ;print(name of variable) beside each code line to check. 
* Comment the result after the print with # 

* ''' *Use thriple tickmarks to multi-line comment* '''
* Use hashtag # to make single line comments, that are concise and adds understanding for the reader. 
* To test and debug, behind each line of code or variable, use ; print(variableName)
* **Indents matter** 
* Extensions in file names matter, javascript, python, html, css need to be saved: .js .py .html .css

* Create **one function** for **one action**. 
* Use verbs and underscores for for names of def functions, because functions DO something e.g. calc_tax, sum_sales. 

```python
def sum_array(arr): 

```

* For variables and functions in Python, use snake_case (JavaScript uses camelCase).
* Variable = equal sign means whatever on this side is assigned to the variable. Think of them as storage sites. 
* Use explanatory variables - name the variable on what it does/what it is, so when you read it, you know exactly it’s purpose is in the algorithm. 

```python
saleBonus:  

```

* For constant variables, use all uppercase CAPS.

```python
TAXRATE: 

```

* For final variables in main(), indicate them with 'the' in front.
* For input, by default it is in string, therefore, need to use float() or int() in front to permit input type. 

```python
def main():
    the_degree = float(input("Enter the number:"))
    convert_radian(the_degree)

main()

```


* string.split(separator) method can be used to convert a string OR an existing list (with items be broken further), into a list. 
* For loops are good for printing items per instance in each new line 
```python
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]

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
```

* While loops with an empty accumulator variable are good for compiling/printing items in a horizontal row or list. 
* A while loop nested within a while loop is a good way to iterate across a row and all columns, and repeat for next row(s). 

```python
gods_list = [['Odin', 'Kihci Manito', 'An'], ['Frigg', 'Grandmother Fox', 'Nammu'], ['Thor', ' Avas', 'Enki'], ['Tyr', 'Pithsiw', 'Ershkigal']]

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
```

* Two ways to remove an unwanted separator at the end of a list, is to use 
    * pop() method removes the element at the specified position, default value is -1 
    * use an if statement isolating the last index position within the while loop

```python

numbers = [130, 343, 2, 29]
streets = ["4th Ave.", "10th St.", "Memorial Ave", "Harding Ave."] 


outFile = open('2columns.txt',"w")

i = 0
while i < len(numbers):                                         # len represents 4, if i < 4, there's 4 items in the list, but only 3 index positions
    if i != (len(numbers) - 1):                                 # if i is NOT 3, 3 representing the last indexed position. 
        val = str(numbers[i]) + "," + streets[i] + "\n"         # all items before the last item e.g. 130, 343, 2, and 4th ave, 10th st, memorial ave, will follow this
    else:
        val = str(numbers[i]) + "," + streets[i]                # else for our last item, 29, and harding ave, will follow this code. 
    outFile.write(val)
    i += 1
    
outFile.close()

print("all done")
"""
130,4th Ave.
343,10th St.
2,Memorial Ave
29,Harding Ave.
"""
```


### Visual Studio Code - Keyboard Shortcuts
* **Ctrl Shift L**: Replace all code that has the same text with newly typed or pasted value. 
* **Ctrl + K + C**: to comment out all code.
* **Ctrl + S**: to save regularly. 
 
