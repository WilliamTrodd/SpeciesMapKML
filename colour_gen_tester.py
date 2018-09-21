#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      willi_000
#
# Created:     20/09/2018
# Copyright:   (c) willi_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def colour_list_generator(species_list):
    colour_list = {}
    for species in species_list:
        colour_list[species] = colour_gen(species)  ## aabbrrgg

    return colour_list

def colour_gen(word):
    int_from_str = 0
    for i in range(len(word)):
        int_from_str += ord(word[i])
    colour = "#00"
    for i in range(3):
        value = (int_from_str >> (i*2)) & 0xFF    ## Can mess about with the
        to_add = hex(value).strip("0x")           ## bitshifting here to change
        if len(to_add) == 1:                      ## colours (change what i is
            to_add += "0"                         ## multiplied by)
        colour+=(to_add)
    return colour
sp_lst = ['NONE', 'P. pygmaeus', 'P. pipistrellus', 'Myotis sp.', 'Myotis nattereri', 'Sp. 2', 'NSL', 'Sp. 3', 'Sp. 1']
'''
print(colour_gen("NONE"))
print(colour_gen("P. pygmaeus"))
print(colour_gen("P. pipistrellus"))
print(colour_gen("Myotis sp."))
print(colour_gen("Myotis nattereri"))
print(colour_gen("Sp. 2"))
print(colour_gen("Sp. 1"))
print(colour_gen("NSL"))
print(colour_gen("Sp. 3"))
'''
print(colour_list_generator(sp_lst))

def kml_format():

    file_in = open("kml_template.txt", "r")
    as_string = ""
    for line in file_in:
        as_string += (line)

    file_in.close()

    return as_string

print(kml_format())
