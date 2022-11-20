def read_building(filename: str) -> list:
    """
    Reads the building file and returns a list of lists
    """

    placeholder = [
        ["G1", "--, "G1"],
        ["G1", "--, "G1"],
        ["G1", "--, "G1"]
    ]

    return placeholder


Assume there is another type of material not found in the game - let's call it "steel", represented by purpledice. In a given building, if there are any steel dice with an even number on top, the building scores 0points; however, if all the steel dice have an odd number on top, the building scores 10 points.
Here are some acceptable algorithms for such a material:
let odd_steel_found = false
for every column in the building
    for every dice in the column
        if the dice is steel and is even then
            return a score of 0
        else
            let odd_steel_found = true

if odd_steel_found then
        return 10
    else
        return 0


let score = 0

for every dice in the first column
    if the dice is steel and is odd then
        let score = 10

for every dice in the second column
    if the dice is steel and is odd then
        let score = 10

for every dice in the third column
    if the dice is steel and is odd then
        let score = 10

return score