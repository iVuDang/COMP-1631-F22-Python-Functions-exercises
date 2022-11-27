
# Write in Excel with two columns with parallel lists
masses = [1000, 2200, 0.1]
units = ['kgs', 'lbs', 'tonnes']

outFile1 = open("2columns.csv", "w")

i = 0
while i < len(masses):
    val = str(masses[i]) + "," + units[i] + "\n"
    outFile1.write(val)
    i += 1
    
outFile1.close()

"""
Creates .csv file
1000	kgs
2200	lbs
0.1	    tonnes
"""


# Write in Excel with two rows with parallel lists 
"""
masses = [1000, 2200, 0.1]
units = ['kgs', 'lbs', 'tonnes']
"""
outFile2 = open('2rows.csv',"w")

i = 0
while i < len(masses):                    # masses has a count of 3, but max index position of 2
    if i != len(masses) - 1:              # if the iteration is NOT the last index position of 2
        val = str(masses[i]) + ","        # we'll assign the item with a comma 
    else:
        val = str(masses[i]) + "\n"       # otherwise all others add the item, and enter ona  new line. 

    outFile2.write(val)
    i += 1


j = 0
while j < len(units):
    if j != len(units) - 1:
        val = units[j] + ","
    else:
        val = units[j] + "\n"

    outFile2.write(val)
    j += 1    

    
outFile2.close()
print("files exported")

"""
1000	2200	0.1
kgs	    lbs	    tonnes
"""


"""
If we want a horizontal row, then use an empty accumulator to build the row
If we want a column, then return the value as each instance
"""



#1.	Create a function to read (import) the file that is organized as two-rows, passing it the file’s name and to produce a two row-, three column- list of lists.

inFile = open('2rows.csv')

raw_list= inFile.readlines()    # file.readlines() returns a list containing each line in the file as a list item. Stores the list in our created variable 'raw_list'

inFile.close()


result=[]
row=[]

i = 0
while i < len(raw_list):
    row = raw_list[i].split(",")
    result.append(row)
    i += 1

i=0
while i < len(result[0]):
    result[0][i] = float(result[0][i])
    i += 1
print(result)


# Create a function for the two-column file, producing a three-row- two-column- list of lists.. 

inFile= open('2columns.csv')

raw_list = inFile.readlines()

inFile.close()


result=[]

i = 0
while i < len (raw_list):
    row = raw_list[i].split(",")
    row[0] = float(row[0])
    result.append(row)
    i += 1
    
print(result)
