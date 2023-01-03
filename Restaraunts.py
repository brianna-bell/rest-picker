import random
import os

class Restaraunt:
    name = ''
    type = ''

    def __init__(self, name, type):
        self.name = name
        self.type = type

def RestarauntPicker():

    currentDir = os.getcwd()

    if((os.path.isfile(currentDir+"\ListOfRest.txt"))):
        f = open("ListOfRest.txt")
    else:
        return


    # w = ['Zaxbys', 'Tenders', 'Chikfila', 'Slim Chickens', 'Wayback', 'Crickets', 'Johnny Grylls', 'Farm Burger', 'Arbys', 'Cracker Barrel',
    #     'Mellow Mushroom', 'Brickhouse', 'Cheddars', 'Viet Huong', 'Stone Age Korean BBQ', 'Big Oh\'s', 'Sam and Greg\'s', 'Old Black Bear',
    #     'Panda Express', 'Wendys', 'Kamado Ramen', 'McDonalds', 'Nothing But Noodles', 'Jacks', 'I heart Sushi', 'Buffalo Wild Wings', 
    #     'Subway', 'Firehouse', 'Outback', 'Twin Peaks', 'Waffle House', 'Cook Out', 'Bojangles', 'Super Chix']       

    AllRestaraunts = []
    # AllTypes = []

    for line in f:
        x = line.split(", ")
        restName = x[0]
        
        #AllRestaraunts.append(restName)
        restType = x[1].strip()
        #AllTypes.append(restType)
        AllRestaraunts.append(Restaraunt(restName,restType))


    for r in AllRestaraunts:
        print("Name: " + r.name + "\tType: " + r.type)

    # for t in AllTypes:
    #     print(t)


    # firstChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    # secondChoice = random.randint(0, len(w)-1)    # Generate the computer's choice
    # while (secondChoice == firstChoice):
    #     secondChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    # thirdChoice = random.randint(0, len(w)-1)    # Generate the computer's choice
    # while (thirdChoice == secondChoice | thirdChoice == firstChoice):
    #     thirdChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    # print('Your options are:\n\t* ' + w[firstChoice] + '\n\t* ' + w[secondChoice] + '\n\t* ' + w[thirdChoice] + '\n')

    # ans = input("Are these good? n to continue, x to quit\n")

    # while(ans != 'x'):
        
    #     firstChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    #     secondChoice = random.randint(0, len(w)-1)    # Generate the computer's choice
    #     while (secondChoice == firstChoice):
    #         secondChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    #     thirdChoice = random.randint(0, len(w)-1)    # Generate the computer's choice
    #     while (thirdChoice == secondChoice | thirdChoice == firstChoice):
    #         thirdChoice = random.randint(0, len(w)-1)    # Generate the computer's choice

    #     print('Your options are:\n\t* ' + w[firstChoice] + '\n\t* ' + w[secondChoice] + '\n\t* ' + w[thirdChoice] + '\n')

    #     ans = input("Are these good? n to continue, x to quit\n")

RestarauntPicker()
