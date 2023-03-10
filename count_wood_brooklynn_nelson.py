def score_wood (building:list) -> int:
    '''finds wood die and counts number of adjacent die,
    returns total score for 2 points per adjacent die'''
    adjacent_die = 0
    i = 0
    while i < len(building):
        j = 0
        while j < len(building[i]):
            if building[i][j][0] == 'W':
                #check side to side
                if j == 0 or j == 2: #if die is on edges of row check middle
                    if building[i][1] != '--':
                        adjacent_die += 1

                    else:
                        pass
                else: #if die is in middle of row
                    if building[i][0] != '--' and building[i][-1] != '--': #both sides have die
                        adjacent_die += 2

                    elif building[i][0] != '--' or building[i][-1] != '--': #one side has dice
                        adjacent_die += 1

                    else:
                        pass

                #check up and down
                if i == len(building)-1: #die is on first level
                    if building [i-1][j] != '--':
                        adjacent_die += 1
                    else:
                        pass

                elif i == 0: #die on top of building
                    if building[i+1][j] != '--':
                        adjacent_die += 1
                    else:
                        pass

                else: #die in middle
                    if building[i-1][j] != '--' and building[i+1][j] != '--': #above and below have die
                        adjacent_die += 2

                    elif building[i-1][j] != '--' or building[i+1][j] != '--': #either above or below has a dice
                        adjacent_die += 1

                    else:
                        pass
                
                j += 1

            else:
                j += 1

        i += 1

    total = adjacent_die * 2
    return total