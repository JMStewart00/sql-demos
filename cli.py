# print('''
#         _____________________________________________
#       //:::::::::::::::::::::::::::::::::::::::::::::\\\\
#     //:::_______:::::::::________::::::::::_____:::::::\\\\
#   //:::_/   _-"":::_--"""        """--_::::\_  ):::::::::\\\\
#  //:::/    /:::::_"                    "-_:::\/:::::|^\:::\\\\
# //:::/   /~::::::I__                      \:::::::::|  \:::\\\\
# \\\\:::\   (::::::::::""""---___________     "--------"  /::://
#  \\\\:::\  |::::::::::::::::::::::::::::""""==____      /::://
#   \\\\:::"\/::::::::::::::::::::::::::::::::::::::\   /~::://
#     \\\\:::::::::::::::::::::::::::::::::::::::::::)/~::://
#       \\\\::::\""""""------_____::::::::::::::::::::::://
#         \\\\:::"\               """""-----_____:::::://
#           \\\\:::"\    __----__                )::://
#             \\\\:::"\/~::::::::~\_         __/~:://
#               \\\\::::::::::::::::""----""":::://
#                 \\\\::::::::::::::::::::::::://
#                   \\\\:::\^""--._.--""^/::://
#                     \\\\::"\         /":://
#                       \\\\::"\     /":://
#                         \\\\::"\_/":://
#                           \\\\::::://
#                             \\\\_//
# ''')

main_menu = '''
    Weclome to SQL Heroes!

    You can:
    (1) Sign up a new hero!
    (2) Lookup a list of heroes by name.
    (3) Make a new friend
    (4) Make a new enemy
    (5) Add a new ability to the hero db
    (6) Leave and never return!
'''

print(main_menu)
selection = input("Enter selection:")

def switch(case):
  if case == "1":
    print("uno")
 
  elif case == "2":
    print("deuce")
 
  elif case == "3":
    print("tree")
 
  elif case == "4":
    print("foh")
 
  elif case == "5":
    print("cinco")
 
  else:
    print("Is that even a thing?")
    new_selection = input("Enter selection:")
    switch(new_selection)

switch(selection)