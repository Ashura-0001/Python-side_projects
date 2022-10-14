'''
A big code for a simple log maker that stores your logs as a dietian


'''



print("What do you want to do ?")
print("For adding a log Press [1]")
print("For checking log Press [2]")
a = (int(input()))
def hclog(a):
    newl = "\n"
    if (a==1):#choose between log or see
        name = str(input("What is the patients name?\n"))
        b = int(input("Choose Between Diet log [press 1] or excecise log [press 2]\n"))#choose between diet or excercise
        if (b==1):
            def getdate():
                import datetime
                return datetime.datetime.now()
            v = getdate()
            f1 = open("{}(diet).txt".format(name), "a")
            d = str(input("what have you eaten?\n"))
            f1.write("{}[{}] {}".format (newl, v, d))
            e = str(input("anything else? (y/n)\n"))
            while (True):
                if (e=="y"):
                    food = str(input("what else have you eaten? "))
                    f1.write("{}[{}] {}".format (newl, v, food))
                    g = str(input("anything else? (y/n)\n"))
                    if (g == "y"):
                        continue
                    if (g == "n"):
                        break
                if (e == "n"):
                    break
            print ("*****Operation successfully excecuted*****")
        elif (b==2):
            def getdate():
                import datetime
                return datetime.datetime.now()
            v = getdate()
            f1 = open("{}(excercise).txt".format(name), "a")
            d = str(input("what excercise have you done?\n"))
            f1.write("{}[{}] {}".format (newl, v, d))
            while (True):
                e = str(input("anything else? (y/n)"))
                if (e=="y"):
                    exc = str(input("what else have you done? "))
                    f1.write("{}[{}] {}".format (newl, v, exc))
                    g = str(input("anything else? (y/n)"))
                    if (g == "y"):
                        continue
                    if (g == "n"):
                        break
                elif (e == "n"):
                    break
            print ("*****Operation successfully excecuted*****")    
    elif (a==2):
        name = str(input("Enter Patient's Name\n"))
        print ("\nwhat type of log would you like to see :-")
        print ("For diet Press 1")
        print ("For Excercise Press 2")
        c = int(input())
        if (c==1):
            f2 = open("{}(diet).txt".format(name), "rt")
            content = f2.read()
            print (content)
            print ("*****Operation successfully excecuted*****")
        elif (c==2):
            f2 = open("{}(excerise).txt".format(name), "rt")
            content = f2.read()
            print (content)
            print ("*****Operation successfully excecuted*****")
hclog(a)