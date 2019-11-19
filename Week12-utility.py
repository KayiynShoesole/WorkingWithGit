# Kayiyn Shoemaker
# CSCI 102- Secion B
# Week 12- Part A

#   Function 1 : PrintOutput
def PrintOutput(string_to_print):
    print(f'OUTPUT {string_to_print}')

#Function 2: LoadFile
def LoadFile(filename):
    newfile = open(filename, 'r')
    contents = newfile.readlines()
    newfile.close()
    return contents

#Function 3: UpdateString
def UpdateString(string1, string2, index):
    startindex = index
    endindex = index+1
    newstring = string1[:startindex] + string2 + string1[endindex:]
    PrintOutput(newstring)

#Function 4: FindWordCount
def FindWordCount(function_list, function_str):
    function_list = str(function_list)
    count = function_list.count(function_str)
    return count

#Function 5: ScoreFinder
def ScoreFinder(players, scores, name):
    name = name.lower()
    player_found = False
    index = 0
    for player in players:
        player = player.lower()
        if player == name:
            PrintOutput(f'{players[index]} got a score of {scores[index]}')
            player_found = True
        index += 1
    if not player_found:
        PrintOutput('player not found')
        

