# COMP-1631-F22-Functions-exercises
## Purpose:
* I created python functions to process inputs into desired outputs, involving use of input() to take parameters from the user, and main() to call upon previous functions. 

## Citations:
* Problems provided by **Comp 1631 F22 - Prof. Patrick Perri** - Mount Royal University. 

## Preview:
<img src="https://github.com/iVuDang/COMP-1631-F22-Functions-exercises/blob/main/Comp1631_FunctionsExercises.png" width=100% height=100%>


## Technologies: 
* Python 

## Tools:
* Replit
* Visual Studio Code


---


## What I learned: 

* Break problems into **small enough problems** so that the problems cannot be wrong when solving them. 

* ''' *Use thriple tickmarks to multi-line comment* '''
* Use hashtag # to make single line comments, that are concise and adds understanding for the reader. 
* To test and debug, behind each line of code or variable, use ; print(variableName)
* **Indents matter** 

* Create **one function** for **one action**. 
* Use verbs for for names of def functions, because functions DO something e.g. find, calc, sum, convert.

```python
def sumArray(arr): 

```

* For variables, use camelCase.
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
 