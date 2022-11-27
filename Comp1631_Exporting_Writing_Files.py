ages = [19,18,24,54,18,21,22,23]

#1 1.	Export the list to a file called ages_in_row.txt 
#as row.txt

# set a variable, and use function 'open(file, mode)'
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, CREATES the file if it does not exist
"w" - Write - Opens a file for writing, CREATES the file if it does not exist
"""

outFile = open('ages_in_row.txt', "w")       # set up variable outFile to use open function to CREATE a .txt file, and to write into it. 

"""
ages = [19, 18, 24, 54, 18, 21, 22, 23]
"""
i = 0
while i < len(ages):                            
    string2B_exported = str(ages[i]) + ","   # assigns to variable in string format, adds at each iteration "19," "18," etc. NOT written into the file yet. 
    outFile.write(string2B_exported)         # write() method writes a specified text to the file, depending on file mode in our previous "open(file name.extension, "a" or "w")
    i += 1
    
outFile.close()                              # always end with applying .close() to our initial variable that created/write a file. 

print('Done...check for the new file')

"""
Where the specified text will be inserted depends on the file mode in our previous "open(file name.extension, "a" or "w")
"a":  The text will be inserted at the current file stream position, default at the end of the file.
"w": The file will be emptied before the text will be inserted at the current file stream position, default 0.
"""

"""
Creates in .txt file
19,18,24,54,18,21,22,23,
"""

#2 2.	Export the list to a file called ages_in_column.csv 
# as columns...USING A FUNCTION

def export_column(filename:str, data:list)-> None: # VOID function
    '''any list, exported as a column to local folder'''

    filename += ".csv"                          # In a function, where it takes the name of the file as a paramter, we can crate a varaible to add an ".extension" to turn that parameter into a file
    outFile = open(filename, "w")               # outFile to open/create the file, in "w" mode. 

    i = 0
    while i < len (data):                       # data refers to our second paramter, meant to be a list. 
        outFile.write(str(data[i]) + "\n")      # write() method writes a specified text to the file, depending on file mode in our previous "open(file name.extension, "a" or "w"), 
        i += 1

    print("done...check for new file")          #unnecessary except for debugging
    
    outFile.close()                             # Sequence always involve 3 phases, outFile.open(file name, "a or w mode"), .write( "variable" or direct code), and outFile.close()
    
export_column("ages_in_columns", ages)          # name of file, ages = [19, 18, 24, 54, 18, 21, 22, 23] 

"""
Creates in Excel file:
19
18
24
54
18
21
22
23
"""

#3 exporting a file with label AND without trailing empty data

masses = [5, 44, 8.8] 

fileObjectName = open('demo_row_clean.csv', 'w') 

#optional chance to send a label to file
fileObjectName.write("masses,")                   # simple and fast way to write a string/label in the first row or first column

i=0
while i < len(masses):
    if i < len(masses) - 1:                  # this applies to 5, and 44
        dataToWrite = str(masses[i]) + ','   # "5," and "44,"
    else:                                    # this applies to 8.8
        dataToWrite = str(masses[i])         # "8.8"

    fileObjectName.write(dataToWrite)        # refers to our initiate variable that created the file, .write("variable that contain code")
    i+=1

fileObjectName.close()

"""
Creates an excel file:
masses	5	44	8.8
"""


# 4.	Without combining the parallel lists into a new list, export the the data to a single file consisting of two rows: one with the numbers and one with the streets
# exporting a 2 row file

numbers = [130, 343, 2, 29]
streets = ["4th Ave.", "10th St.", "Memorial Ave", "Harding Ave."]       # these two lists need to be parallel, contain same count of index positions 

outFile = open('2rows.txt', 'w')

i = 0 
while i < len(numbers):
    if i != (len(numbers) - 1):
        val = str(numbers[i]) + ","       # "130," "343," "2,"
    else:
        val = str(numbers[i]) + "\n"      # "2" and enters new line 
    outFile.write(val)    
    i += 1

i = 0
while i < len(streets):
    if i != (len(streets) - 1):
        val = streets[i] + ","            # "4th Ave.,"  "10th St.," "Memorial Ave,""
    else:
        val = streets[i] + "\n"           # "Harding Ave." and enters new line
    outFile.write(val)    
    i += 1 
    
print("Done 4")
"""
130,343,2,29
4th Ave.,10th St.,Memorial Ave,Harding Ave.
"""


# A single file consisting of two columns: one the numbers and the next the streets.
# 5 as two columns
"""
numbers = [130, 343, 2, 29]
streets = ["4th Ave.", "10th St.", "Memorial Ave", "Harding Ave."] 
"""

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