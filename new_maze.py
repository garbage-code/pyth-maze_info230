def play():
    global line1
    global line2    
    global line3
    global line4
    global line5
    line1 = [".", ".", ".", ".", "e"]
    line2 = [".", "W", "W", "W", "W"]
    line3 = [".", ".", ".", ".", "."]
    line4 = ["W", "W", "W", "W", "."]
    line5 = ["@", ".", ".", ".", "."]    
    while line5[0] != "e":
        print(" ".join(line1))
        print(" ".join(line2))
        print(" ".join(line3))   
        print(" ".join(line4))  
        print(" ".join(line5)) #defines, prints the base table
        if line1[0] == "e":    #begin section a:          
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
        elif line1[4] == "e":        
            coordinates = 5, 1
            line1[4] = "."
        elif line2[0] == "e":
            coordinates = 1, 2
            line2[0] = "."
        elif line3[0] == "e":        
            coordinates = 1, 3
            line3[0] = "."
        elif line3[1] == "e":        
            coordinates = 2, 3
            line3[1] = "."
        elif line3[2] == "e":       
            coordinates = 3, 3
            line3[2] = "."
        elif line3[3] == "e":        
            coordinates = 4, 3
            line3[3] = "."
        elif line3[4] == "e":         
            coordinates = 5, 3
            line3[4] = "."
        elif line4[4] == "e":     
            coordinates = 5, 4
            line4[4] = "."
        elif line5[0] == "e":       
            coordinates = 1, 5
            line5[0] = "."
        elif line5[1] == "e":        
            coordinates = 2, 5
            line5[1] = "."
        elif line5[2] == "e":       
            coordinates = 3, 5
            line5[2] = "."
        elif line5[3] == "e":       
            coordinates = 4, 5
            line5[3] = "."
        elif line5[4] == "e":        
            coordinates = 5, 5 
            line5[4] = "."     #end section a - this part looks for e on the table, records the coordinates, then erases it
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
            return "You dun goofed." #end section b - this part takes the coordinates and adds to the tuple according to movement. if invalid, just states that it's invalid.
        if coordinates == (1, 1):  #begin section c             
            line1[0] = "e"
        elif coordinates == (2, 1):                      
            line1[1] = "e"
        elif coordinates == (3, 1):       
            line1[2] = "e"
        elif coordinates == (4, 1):        
            line1[3] = "e"
        elif coordinates == (5, 1):        
            line1[4] = "e"
        elif coordinates == (1, 2):
            line2[0] = "e"
        elif coordinates == (1, 3):        
            line3[0] = "e"
        elif coordinates == (2, 3):        
            line3[1] = "e"
        elif coordinates == (3, 3):       
            line3[2] = "e"
        elif coordinates == (4, 3):        
            line3[3] = "e"
        elif coordinates == (5, 3):         
            line3[4] = "e"
        elif coordinates == (5, 4):     
            line4[4] = "e"
        elif coordinates == (1, 5):       
            line5[0] = "e"
        elif coordinates == (2, 5):        
            line5[1] = "e"
        elif coordinates == (3, 5):       
            line5[2] = "e"
        elif coordinates == (4, 5):       
            line5[3] = "e"
        elif coordinates == (5, 5):        
            line5[4] = "e"         #end section c - looks for changed coordinates, changes . to e
        if coordinates == (5, 5):
            print("You won!")
        elif coordinates[0] < 0:
            print("Invalid move.")
        elif coordinates[1] < 0:
            print("Invalid move.")
        else:
            print(" ".join(line1))
            print(" ".join(line2))
            print(" ".join(line3))   
            print(" ".join(line4))  
            print(" ".join(line5))
