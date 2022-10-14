from time import sleep

def dotanimation():
    
    max_no_of_dots = 3
    list_of_dots = ["."*i + " "*(max_no_of_dots-i) + "\r" + "Processing" for i in range (1, max_no_of_dots + 1)]
    list_of_dots.append(" "*max_no_of_dots + "\r")
    print ("Processing", end="")
    for x in range (0,3):  
        for pattern in list_of_dots:
            print (pattern, end="") 
            sleep (0.2)

dotanimation()