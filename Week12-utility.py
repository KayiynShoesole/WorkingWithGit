# Kayiyn Shoemaker
# CSCI 102- Section B
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
        
#Function 6: Union
def Union(list1, list2):
    list1.reverse() #Reverse lists so duplicates are removed from back
    list2.reverse()
    for a in list1:
        if not list1.count(a) == 1: #Check for duplicates
            list1.remove(a)
    for b in list2:
        if not list2.count(b) == 1: #Check for duplicates
            list2.remove(b)
    list1.reverse() #Reverse lists back to normal position
    list2.reverse()
    list3 = list1 + list2
    return list3

#Function 7: Intersection
def Intersection(list1, list2):
    list3 = []
    for a in list1:
        for b in list2:
            if a == b:
                list3 += [b]
    return list3

#Function 8: NotIn
def NotIn(list1, list2):
    list3 = []
    for a in list1:
        found = False
        for b in list2:
            if a == b:
                found = True #If a matches a value in b, say so
        if not found:
            list3 += [a] #If a does not match a value in b, add to list
    return list3
