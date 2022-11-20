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

* ''' *Use thriple tickmarks to multi-line comment* '''
* Use hashtag # to make single line comments, that are concise and adds understanding for the reader. 
* To test and debug, behind each line of code or variable, use ; print(variableName)
* **Indents matter** 
* Extensions in file names matter, javascript, python, html, css need to be saved: .js .py .html .css

* Create **one function** for **one action**. 
* Use verbs and underscores for for names of def functions, because functions DO something e.g. calc_tax, sum_sales. 

```python
def sumArray(arr): 

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
    theDegree = float(input("Enter the number:"))
    convertRadian(theDegree)

main()

```

### Visual Studio Code - Keyboard Shortcuts
* Ctrl Shift L: Replace all code that has the same text with newly typed or pasted value. 
* Ctrl + K + C: to comment out all code
 
