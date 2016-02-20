# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:04:00 2016

@author: Mike
"""

def play():
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global line8
    global line9
    global line10
    line1 = ['e', '.', '.', '.', '■', 'i', '.', '.', '.', '■']
    line2 = ['■', '■', '■', '.', '■', '■', '■', '■', '.', '.']
    line3 = ['■', '■', '■', '.', '■', '■', '■', '■', '■', '.']
    line4 = ['■', '■', '■', '.', '.', '.', '.', '.', '.', '.']
    line5 = ['■', '■', '■', '.', '■', '■', '■', '■', '■', '■']
    line6 = ['■', '■', '■', '.', '.', '■', '■', '■', '.', '.']
    line7 = ['■', '■', '■', '■', '▒', '.', '.', '.', '.', '■']
    line8 = ['■', '■', '■', '■', '.', '■', '■', '■', '■', '■']
    line9 = ['■', '■', '■', '■', '.', '.', '.', '.', '.', '.']
    line10 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '@']
    hasKey = 0
    coordinates = (1, 1)
    while line10[9] != "e":
        print(" ".join(line1))
        print(" ".join(line2))
        print(" ".join(line3))   
        print(" ".join(line4))  
        print(" ".join(line5))
        print(" ".join(line6))
        print(" ".join(line7))
        print(" ".join(line8))   
        print(" ".join(line9))  
        print(" ".join(line10))
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        elif line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        elif line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        elif line1[3] == "e":
            coordinates = 4, 1
            line1[3] = "."
        elif line1[5] == "e":
            hasKey = 1            
            coordinates = 6, 1
            line1[5] = "."
        elif line1[6] == "e":
            coordinates = 7, 1
            line1[6] = "."
        elif line1[7] == "e":
            coordinates = 8, 1
            line1[7] = "."
        elif line1[8] == "e":
            coordinates = 9, 1
            line1[8] = "."
        elif line2[3] == "e":
            coordinates = 4, 2
            line2[3] = "."
        elif line2[8] == "e":
            coordinates = 9, 2
            line2[8] = "."
        elif line2[9] == "e":
            coordinates = 10, 2
            line2[9] = "."
        elif line3[3] == "e":
            coordinates = 4, 3
            line3[3] = "."
        elif line3[9] == "e":
            coordinates = 10, 3
            line3[9] = "."
        elif line4[3] == "e":
            coordinates = 4, 4
            line4[3] = "."
        elif line4[4] == "e":
            coordinates = 5, 4
            line4[4] = "."
        elif line4[5] == "e":
            coordinates = 6, 4
            line4[5] = "."
        elif line4[6] == "e":
            coordinates = 7, 4
            line4[6] = "."
        elif line4[7] == "e":
            coordinates = 8, 4
            line4[7] = "."
        elif line4[8] == "e":
            coordinates = 9, 4
            line4[8] = "."
        elif line4[9] == "e":
            coordinates = 10, 4
            line4[9] = "."
        elif line5[3] == "e":
            coordinates = 4, 5
            line5[3] = "."
        elif line6[3] == "e":
            coordinates = 4, 6
            line6[3] = "."
        elif line6[4] == "e":
            coordinates = 5, 6
            line6[4] = "."
        elif line6[8] == "e":
            coordinates = 9, 6
            line6[8] = "."
        elif line6[9] == "e":
            coordinates = 10, 6
            line6[9] = "."
        elif line7[4] == "e":
            coordinates = 5, 7
            line7[4] = "."
        elif line7[5] == "e":
            coordinates = 6, 7
            line7[5] = "."
        elif line7[6] == "e":
            coordinates = 7, 7
            line7[6] = "."
        elif line7[7] == "e":
            coordinates = 8, 7
            line7[7] = "."
        elif line7[8] == "e":
            coordinates = 9, 7
            line7[8] = "."
        elif line8[4] == "e":
            coordinates = 5, 8
            line8[4] = "."
        elif line9[4] == "e":
            coordinates = 5, 9
            line9[4] = "."
        elif line9[5] == "e":
            coordinates = 6, 9
            line9[5] = "."
        elif line9[6] == "e":
            coordinates = 7, 9
            line9[6] = "."
        elif line9[7] == "e":
            coordinates = 8, 9
            line9[7] = "."
        elif line9[8] == "e":
            coordinates = 9, 9
            line9[8] = "."
        elif line9[9] == "e":
            coordinates = 10, 9
            line9[9] = "."
        elif line10[9] == "e":
            coordinates = 10, 10
            line10[9] = "."
            print("You won!")
        precontrol_coords = coordinates
        control = input("> ")  #briefs for input
        if control == "w":     #begin section b
            coordinates = coordinates[0], coordinates[1] - 1
        elif control == "a":
            coordinates = coordinates[0] - 1, coordinates[1]
        elif control == "s":
            coordinates = coordinates[0], coordinates[1] + 1
        elif control == "d":
            coordinates = coordinates[0] + 1, coordinates[1]
        else:
            coordinates = coordinates
            print("Please reconsider.")
        if coordinates == (1, 1):
            line1[0] = "e"
        elif coordinates == (2, 1):
            line1[1] = "e"
        elif coordinates == (3, 1):
            line1[2] = "e"
        elif coordinates == (4, 1):
            line1[3] = "e"
        elif coordinates == (6, 1):
            line1[5] = "e"
            hasKey = 1
            print("You found the oddly shaped key? Is this even a key?")
        elif coordinates == (7, 1):
            line1[6] = "e"
        elif coordinates == (8, 1):
            line1[7] = "e"
        elif coordinates == (9, 1):
            line1[8] = "e"
        elif coordinates == (4, 2):
            line2[3] = "e"
        elif coordinates == (9, 2):
            line2[8] = "e"
        elif coordinates == (10, 2):
            line2[9] = "e"
        elif coordinates == (4, 3):
            line3[3] = "e"
        elif coordinates == (10, 3):
            line3[9] = "e"
        elif coordinates == (4, 4):
            line4[3] = "e"
        elif coordinates == (5, 4):
            line4[4] = "e"
        elif coordinates == (6, 4):
            line4[5] = "e"
        elif coordinates == (7, 4):
            line4[6] = "e"
        elif coordinates == (8, 4):
            line4[7] = "e"
        elif coordinates == (9, 4):
            line4[8] = "e"
        elif coordinates == (10, 4):
            line4[9] = "e"
        elif coordinates == (4, 5):
            line5[3] = "e"
        elif coordinates == (4, 6):
            line6[3] = "e"
        elif coordinates == (5, 6):
            line6[4] = "e"
        elif coordinates == (9, 6):
            line6[8] = "e"
        elif coordinates == (10, 6):
            line6[9] = "e"
        elif coordinates == (5, 7):
            if hasKey == 1:
                line7[4] = "e"
                print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
            elif hasKey == 0:
                print("You need a key to open this oddly printed screen door!")
        elif coordinates == (6, 7):
            line7[5] = "e"
        elif coordinates == (7, 7):           
            line7[6] = "e"
        elif coordinates == (8, 7):           
            line7[7] = "e"
        elif coordinates == (9, 7):
            line7[8] = "e"
        elif coordinates == (5, 8):
            line8[4] = "e"
        elif coordinates == (5, 9):    
            line9[4] = "e"
        elif coordinates == (6, 9):    
            line9[5] = "e"
        elif coordinates == (7, 9):
            line9[6] = "e"
        elif coordinates == (8, 9): 
            line9[7] = "e"
        elif coordinates == (9, 9):           
            line9[8] = "e"
        elif coordinates == (10, 9):         
            line9[9] = "e"
        elif coordinates == (10, 10):       
            line10[9] = "e"
            print("You won!")    
        if coordinates[0] == 0:
            print("Invalid move. In a perfect world, you'd have fallen into an impecabbly animated pit of lava around the maze. Alternatively, you've fallen outside of this 5 x 5 ascii set of lists.")
            coordinates = precontrol_coords
            if coordinates == (1, 1):
                line1[0] = "e"
            elif coordinates == (2, 1):
                line1[1] = "e"
            elif coordinates == (3, 1):
                line1[2] = "e"
            elif coordinates == (4, 1):
                line1[3] = "e"
            elif coordinates == (6, 1):
                line1[5] = "e"
                hasKey = 1
                print("You found the oddly shaped key? Is this even a key?")
            elif coordinates == (7, 1):
                line1[6] = "e"
            elif coordinates == (8, 1):
                line1[7] = "e"
            elif coordinates == (9, 1):
                line1[8] = "e"
            elif coordinates == (4, 2):
                line2[3] = "e"
            elif coordinates == (9, 2):
                line2[8] = "e"
            elif coordinates == (10, 2):
                line2[9] = "e"
            elif coordinates == (4, 3):
                line3[3] = "e"
            elif coordinates == (10, 3):
                line3[9] = "e"
            elif coordinates == (4, 4):
                line4[3] = "e"
            elif coordinates == (5, 4):
                line4[4] = "e"
            elif coordinates == (6, 4):
                line4[5] = "e"
            elif coordinates == (7, 4):
                line4[6] = "e"
            elif coordinates == (8, 4):
                line4[7] = "e"
            elif coordinates == (9, 4):
                line4[8] = "e"
            elif coordinates == (10, 4):
                line4[9] = "e"
            elif coordinates == (4, 5):
                line5[3] = "e"
            elif coordinates == (4, 6):
                line6[3] = "e"
            elif coordinates == (5, 6):
                line6[4] = "e"
            elif coordinates == (9, 6):
                line6[8] = "e"
            elif coordinates == (10, 6):
                line6[9] = "e"
            elif coordinates == (5, 7):
                if hasKey == 1:
                    line7[4] = "e"
                    print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
                elif hasKey == 0:
                    print("You need a key to open this oddly printed screen door!")
            elif coordinates == (6, 7):
                line7[5] = "e"
            elif coordinates == (7, 7):           
                line7[6] = "e"
            elif coordinates == (8, 7):           
                line7[7] = "e"
            elif coordinates == (9, 7):
                line7[8] = "e"
            elif coordinates == (5, 8):
                line8[4] = "e"
            elif coordinates == (5, 9):    
                line9[4] = "e"
            elif coordinates == (6, 9):    
                line9[5] = "e"
            elif coordinates == (7, 9):
                line9[6] = "e"
            elif coordinates == (8, 9): 
                line9[7] = "e"
            elif coordinates == (9, 9):           
                line9[8] = "e"
            elif coordinates == (10, 9):         
                line9[9] = "e"
            elif coordinates == (10, 10):       
                line10[9] = "e"
                print("You won!")  
        elif coordinates[1] == 0:
            print("Invalid move. In a perfect world, you'd have fallen into an impecabbly animated pit of lava around the maze. Alternatively, you've fallen outside of this 5 x 5 ascii set of lists.")
            coordinates = precontrol_coords
            if coordinates == (1, 1):
                line1[0] = "e"
            elif coordinates == (2, 1):
                line1[1] = "e"
            elif coordinates == (3, 1):
                line1[2] = "e"
            elif coordinates == (4, 1):
                line1[3] = "e"
            elif coordinates == (6, 1):
                line1[5] = "e"
                hasKey = 1
                print("You found the oddly shaped key? Is this even a key?")
            elif coordinates == (7, 1):
                line1[6] = "e"
            elif coordinates == (8, 1):
                line1[7] = "e"
            elif coordinates == (9, 1):
                line1[8] = "e"
            elif coordinates == (4, 2):
                line2[3] = "e"
            elif coordinates == (9, 2):
                line2[8] = "e"
            elif coordinates == (10, 2):
                line2[9] = "e"
            elif coordinates == (4, 3):
                line3[3] = "e"
            elif coordinates == (10, 3):
                line3[9] = "e"
            elif coordinates == (4, 4):
                line4[3] = "e"
            elif coordinates == (5, 4):
                line4[4] = "e"
            elif coordinates == (6, 4):
                line4[5] = "e"
            elif coordinates == (7, 4):
                line4[6] = "e"
            elif coordinates == (8, 4):
                line4[7] = "e"
            elif coordinates == (9, 4):
                line4[8] = "e"
            elif coordinates == (10, 4):
                line4[9] = "e"
            elif coordinates == (4, 5):
                line5[3] = "e"
            elif coordinates == (4, 6):
                line6[3] = "e"
            elif coordinates == (5, 6):
                line6[4] = "e"
            elif coordinates == (9, 6):
                line6[8] = "e"
            elif coordinates == (10, 6):
                line6[9] = "e"
            elif coordinates == (5, 7):
                if hasKey == 1:
                    line7[4] = "e"
                    print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
                elif hasKey == 0:
                    print("You need a key to open this oddly printed screen door!")
            elif coordinates == (6, 7):
                line7[5] = "e"
            elif coordinates == (7, 7):           
                line7[6] = "e"
            elif coordinates == (8, 7):           
                line7[7] = "e"
            elif coordinates == (9, 7):
                line7[8] = "e"
            elif coordinates == (5, 8):
                line8[4] = "e"
            elif coordinates == (5, 9):    
                line9[4] = "e"
            elif coordinates == (6, 9):    
                line9[5] = "e"
            elif coordinates == (7, 9):
                line9[6] = "e"
            elif coordinates == (8, 9): 
                line9[7] = "e"
            elif coordinates == (9, 9):           
                line9[8] = "e"
            elif coordinates == (10, 9):         
                line9[9] = "e"
            elif coordinates == (10, 10):       
                line10[9] = "e"
                print("You won!")  
        elif coordinates[0] == 11:
            print("Invalid move. In a perfect world, you'd have fallen into an impecabbly animated pit of lava around the maze. Alternatively, you've fallen outside of this 5 x 5 ascii set of lists.")
            coordinates = precontrol_coords
            if coordinates == (1, 1):
                line1[0] = "e"
            elif coordinates == (2, 1):
                line1[1] = "e"
            elif coordinates == (3, 1):
                line1[2] = "e"
            elif coordinates == (4, 1):
                line1[3] = "e"
            elif coordinates == (6, 1):
                line1[5] = "e"
                hasKey = 1
                print("You found the oddly shaped key? Is this even a key?")
            elif coordinates == (7, 1):
                line1[6] = "e"
            elif coordinates == (8, 1):
                line1[7] = "e"
            elif coordinates == (9, 1):
                line1[8] = "e"
            elif coordinates == (4, 2):
                line2[3] = "e"
            elif coordinates == (9, 2):
                line2[8] = "e"
            elif coordinates == (10, 2):
                line2[9] = "e"
            elif coordinates == (4, 3):
                line3[3] = "e"
            elif coordinates == (10, 3):
                line3[9] = "e"
            elif coordinates == (4, 4):
                line4[3] = "e"
            elif coordinates == (5, 4):
                line4[4] = "e"
            elif coordinates == (6, 4):
                line4[5] = "e"
            elif coordinates == (7, 4):
                line4[6] = "e"
            elif coordinates == (8, 4):
                line4[7] = "e"
            elif coordinates == (9, 4):
                line4[8] = "e"
            elif coordinates == (10, 4):
                line4[9] = "e"
            elif coordinates == (4, 5):
                line5[3] = "e"
            elif coordinates == (4, 6):
                line6[3] = "e"
            elif coordinates == (5, 6):
                line6[4] = "e"
            elif coordinates == (9, 6):
                line6[8] = "e"
            elif coordinates == (10, 6):
                line6[9] = "e"
            elif coordinates == (5, 7):
                if hasKey == 1:
                    line7[4] = "e"
                    print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
                elif hasKey == 0:
                    print("You need a key to open this oddly printed screen door!")
            elif coordinates == (6, 7):
                line7[5] = "e"
            elif coordinates == (7, 7):           
                line7[6] = "e"
            elif coordinates == (8, 7):           
                line7[7] = "e"
            elif coordinates == (9, 7):
                line7[8] = "e"
            elif coordinates == (5, 8):
                line8[4] = "e"
            elif coordinates == (5, 9):    
                line9[4] = "e"
            elif coordinates == (6, 9):    
                line9[5] = "e"
            elif coordinates == (7, 9):
                line9[6] = "e"
            elif coordinates == (8, 9): 
                line9[7] = "e"
            elif coordinates == (9, 9):           
                line9[8] = "e"
            elif coordinates == (10, 9):         
                line9[9] = "e"
            elif coordinates == (10, 10):       
                line10[9] = "e"
                print("You won!")  
        elif coordinates[1] == 11:
            print("Invalid move. In a perfect world, you'd have fallen into an impecabbly animated pit of lava around the maze. Alternatively, you've fallen outside of this 5 x 5 ascii set of lists.")
            coordinates = precontrol_coords
            if coordinates == (1, 1):
                line1[0] = "e"
            elif coordinates == (2, 1):
                line1[1] = "e"
            elif coordinates == (3, 1):
                line1[2] = "e"
            elif coordinates == (4, 1):
                line1[3] = "e"
            elif coordinates == (6, 1):
                line1[5] = "e"
                hasKey = 1
                print("You found the oddly shaped key? Is this even a key?")
            elif coordinates == (7, 1):
                line1[6] = "e"
            elif coordinates == (8, 1):
                line1[7] = "e"
            elif coordinates == (9, 1):
                line1[8] = "e"
            elif coordinates == (4, 2):
                line2[3] = "e"
            elif coordinates == (9, 2):
                line2[8] = "e"
            elif coordinates == (10, 2):
                line2[9] = "e"
            elif coordinates == (4, 3):
                line3[3] = "e"
            elif coordinates == (10, 3):
                line3[9] = "e"
            elif coordinates == (4, 4):
                line4[3] = "e"
            elif coordinates == (5, 4):
                line4[4] = "e"
            elif coordinates == (6, 4):
                line4[5] = "e"
            elif coordinates == (7, 4):
                line4[6] = "e"
            elif coordinates == (8, 4):
                line4[7] = "e"
            elif coordinates == (9, 4):
                line4[8] = "e"
            elif coordinates == (10, 4):
                line4[9] = "e"
            elif coordinates == (4, 5):
                line5[3] = "e"
            elif coordinates == (4, 6):
                line6[3] = "e"
            elif coordinates == (5, 6):
                line6[4] = "e"
            elif coordinates == (9, 6):
                line6[8] = "e"
            elif coordinates == (10, 6):
                line6[9] = "e"
            elif coordinates == (5, 7):
                if hasKey == 1:
                    line7[4] = "e"
                    print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
                elif hasKey == 0:
                    print("You need a key to open this oddly printed screen door!")
            elif coordinates == (6, 7):
                line7[5] = "e"
            elif coordinates == (7, 7):           
                line7[6] = "e"
            elif coordinates == (8, 7):           
                line7[7] = "e"
            elif coordinates == (9, 7):
                line7[8] = "e"
            elif coordinates == (5, 8):
                line8[4] = "e"
            elif coordinates == (5, 9):    
                line9[4] = "e"
            elif coordinates == (6, 9):    
                line9[5] = "e"
            elif coordinates == (7, 9):
                line9[6] = "e"
            elif coordinates == (8, 9): 
                line9[7] = "e"
            elif coordinates == (9, 9):           
                line9[8] = "e"
            elif coordinates == (10, 9):         
                line9[9] = "e"
            elif coordinates == (10, 10):       
                line10[9] = "e"
                print("You won!")  
        else:
            print(" ".join(line1))
            print(" ".join(line2))
            print(" ".join(line3))   
            print(" ".join(line4))  
            print(" ".join(line5))

            