#dot dot dot animation cleaner version
from time import sleep
def dotanimation():
    
    max_no_of_dots = 3
    list_of_dots = ["."*i + " "*(max_no_of_dots-i) + "\r" for i in range (1, max_no_of_dots + 1)]
    list_of_dots.append(" "*max_no_of_dots + "\r")
    while True:
        for pattern in list_of_dots:
            print (pattern, end="") 
            sleep (0.2)