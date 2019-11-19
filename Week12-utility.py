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
