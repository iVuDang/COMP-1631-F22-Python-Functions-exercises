def score_wood(building: list) -> int: 
    """
    Determines the score for all dice representing wood material 
    in the building. 
    Each die scores 2 points per adjacent die around it.
    Returns the total dice score.
    """
    
    # iterates through list of lists
    # checks if first index of die value is 'W'
    # if yes, checks if it is in the left, middle, or right column
    # checks this to avoid out of bound errors
    # checks left and/or right spaces for die, depending on column
    wood_score = 0 
    for sublist in building: 
        for index in sublist: 
            if index[0] == 'W':
                if index == sublist[0]:
                    if sublist[1] != '--':
                        wood_score += 2
                elif index == sublist[1]:
                    if sublist[0] != '--':
                        wood_score += 2
                    if sublist[2] != '--':
                        wood_score += 2
                else:
                    if sublist[1] != '--':
                        wood_score +=2

    # iterates through list of lists 
    # second for loop uses range so index will be int and not str
    # checks if first index of die value is 'W'
    # if yes, checks which row this is 
    # checks this to avoid out of bound errors
    # checks top and/or bottom spaces for die, depending on row
    # index tracks sublist index value
    # j tracks building index value
    j = 0
    for sublist in building:
        for index in range(len(sublist)):
            if sublist[index][0] == 'W':
                if sublist == building[0]:
                    if building[j+1][index] != '--':
                        wood_score += 2
                elif sublist == building[len(building)-1]:
                    if building[j-1][index] != '--':
                        wood_score += 2
                else: 
                    if building[j-1][index] != '--':
                        wood_score += 2
                    if building[j+1][index] != '--':
                        wood_score += 2
        j += 1




    return wood_score
 