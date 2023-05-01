"""
Spyder Editor

This is a temporary script file.
"""


my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

my_roster_list_upper = ['', '', '']
i = 0
for player in my_roster_list:
    my_roster_list_upper[i] = player.title()
    print(my_roster_list_upper[i])
    i = i + 1
    
for x in my_roster_dict:
    print(f"position: {x}")