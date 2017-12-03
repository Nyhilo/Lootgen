"""
Functions
    Load file
    Generate Items
"""

import os.path
import csv
import random

class Loot:
    def __init__(self,filename=""):
        self.filename=filename
        self.itemList=[]

    def load(self, filename):
        if not os.path.exists(filename):
            print("A file named " + filename + " does not exist.")
        else:
            with open(filename, 'r',newline='') as file:
                reader = csv.reader(file, delimiter=',', quotechar='|')
                counter = 0
                for row in reader:
                    counter += 1
                    if len(row) == 1:
                        self.itemList.append([row[0],1,1])
                    elif len(row) == 2:
                        for i in range(0,int(row[1])):
                            self.itemList.append([row[0],1,1])
                    elif len(row) == 4:
                        for i in range(0,int(row[1])):
                            self.itemList.append([row[0],row[2],row[3]])
                    else:
                        print("Format error on line " + str(counter) + ". Line not loaded.")

    def pick(self, n):
        outlist = []
        for i in range(0,int(n)):
            # print(self.itemList)
            item = random.choice(self.itemList)
            outstring = str(random.randint(int(item[1]),int(item[2]))) + "x " + item[0]
            outlist.append(outstring)
        return outlist

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    running = True
    loot = Loot()
    while running:
        choice = input('Lootgen> ').lower().split() 
        if choice[0] == "load":
            if len(choice) > 1:
                loot.load(choice[1])
            else:
                print("Please enter a file name after 'load'")
        elif is_number(choice[0]):
            items = loot.pick(choice[0])
            for item in items:
                print(item)
        else:
            print(choice[0] + " not recognized as a valid command.")     



if __name__ == '__main__':
    main()