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
    line1 = ['p', '.', '.', '.', '■', 'i', '.', '.', '.', '■']
    line2 = ['■', '■', '■', '.', '■', '■', '■', '■', '.', '.']
    line3 = ['■', '■', '■', '.', '■', '■', '■', '■', '■', '.']
    line4 = ['■', '■', '■', '.', '.', '.', '.', '.', '.', '.']
    line5 = ['■', '■', '■', '.', '■', '■', '■', '■', '■', '■']
    line6 = ['■', '■', '■', '.', '.', '■', '■', '■', '.', '.']
    line7 = ['■', '■', '■', '■', '▒', '.', '.', '.', '.', '■']
    line8 = ['■', '■', '■', '■', '.', '.', '■', '■', '■', '■']
    line9 = ['■', '■', '■', '■', '.', '.', '.', '.', '.', '.']
    line10 = ['■', '■', '■', '■', '■', '■', '■', '■', '.', '@']
    hasKey = 0
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
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[3] == "e":
            coordinates = 4, 1
            line1[3] = "."
        if line1[5] == "e":
            hasKey = 1            
            coordinates = 6, 1
            line1[5] = "."
        if line1[6] == "e":
            coordinates = 7, 1
            line1[6] = "."
        if line1[7] == "e":
            coordinates = 8, 1
            line1[7] = "."
        if line1[8] == "e":
            coordinates = 9, 1
            line1[8] = "."
        if line2[3] == "e":
            coordinates = 4, 2
            line2[3] = "."
        if line2[8] == "e":
            coordinates = 9, 2
            line2[8] = "."
        if line2[9] == "e":
            coordinates = 10, 2
            line2[9] = "."
        if line3[3] == "e":
            coordinates = 4, 3
            line3[3] = "."
        if line3[9] == "e":
            coordinates = 10, 3
            line3[9] = "."
        if line4[3] == "e":
            coordinates = 4, 4
            line4[3] = "."
        if line4[4] == "e":
            coordinates = 5, 4
            line4[4] = "."
        if line4[5] == "e":
            coordinates = 6, 4
            line4[5] = "."
        if line4[6] == "e":
            coordinates = 7, 4
            line4[6] = "."
        if line4[7] == "e":
            coordinates = 8, 4
            line4[7] = "."
        if line4[8] == "e":
            coordinates = 9, 4
            line4[8] = "."
        if line4[9] == "e":
            coordinates = 10, 4
            line4[9] = "."
        if line5[3] == "e":
            coordinates = 4, 5
            line5[3] = "."
        if line6[3] == "e":
            coordinates = 4, 6
            line6[3] = "."
        if line6[4] == "e":
            coordinates = 5, 6
            line6[4] = "."
        if line6[8] == "e":
            coordinates = 9, 6
            line6[8] = "."
        if line6[9] == "e":
            coordinates = 10, 6
            line6[9] = "."
        if line7[4] == "e":
            coordinates = 5, 7
            if hasKey == 1:
                line7[4] = "."
                print("The door promptly falls off of its hinges and then disintegrates. You hope you don't meet the same fate.")
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."
        if line1[2] == "e":
            coordinates = 3, 1
            line1[2] = "."
        if line1[0] == "e":
            coordinates = 1, 1
            line1[0] = "."
        if line1[1] == "e":
            coordinates = 2, 1
            line1[1] = "."

            