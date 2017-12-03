"""
File Format consists of comma deliminated lines of items to be generated.
Blank lines and lines starting with # are ignored, for formatting purposes.
Data lines can have the following formats:

    Itemname
    Itemname, Commonness
    Itemname, Commonness, minimum, maximum

Commonness is the number of times that item is put into the item pool.
The number of items found range from minimum to maximum
Missing values are assumed to be 1

Example:

    # Common weapons that can be found
    Stone, 6, 2, 5
    Hammer
    Sword, 2
    Dagger, 4, 1, 2
"""

import os.path
import csv
import random

class Loot:
    def __init__(self,filename=""):
        self.filename=filename
        self.itemList=[]

    def load(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            print("\tA file named " + filename + " does not exist.")
        else:
            with open(filename, 'r',newline='') as file:
                reader = csv.reader(file, delimiter=',', quotechar='|')
                counter = 0
                for row in reader:
                    counter += 1
                    try:
                        if row == [] or row[0][0] == "#":
                            pass
                        elif len(row) == 1:
                            self.itemList.append([row[0],1,1])
                        elif len(row) == 2:
                            for i in range(0,int(row[1])):
                                self.itemList.append([row[0],1,1])
                        elif len(row) == 4:
                            for i in range(0,int(row[1])):
                                self.itemList.append([row[0],row[2],row[3]])
                        else:
                            print("\t! Format error on line {}, '{}' not loaded.".format(counter, row[0]))
                    except ValueError :
                        print("\tValue error at "+str(counter))
            print("\tFinished loading "+filename)

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

def clear():
    import os, platform
    if platform.system() == 'Windows':
        _=os.system('cls')
    else:
        _=os.system('clear')

def main():
    """
    Starts a prompt allowing the user to load loot files and pull random items from them.
    """
    clear()             
    running = True
    loot = Loot()
    while running:
        args = input( 'Lootgen> ' ).split()
        args[0] = args[0].lower()
        if args[0] == "load":
            if len( args ) > 1:
                loot.load( args[1] )
            else:
                print( "\tPlease enter a file name after 'load'" )
        elif is_number( args[0] ):
            print( "\tFound:" )
            items = loot.pick( args[0] )
            for item in items:
                print( "\t\t"+item )
        elif args[0] == "current":
            print( "\tCurrent loaded file: "+loot.filename )
        elif args[0] == "quit":
            quit()
        elif args[0] =="format":
            print("""
            File Format consists of comma deliminated lines of items to be generated.
            Blank lines and lines starting with # are ignored, for formatting purposes.
            Data lines can have the following formats:

                Itemname
                Itemname, Commonness
                Itemname, Commonness, minimum, maximum

            Commonness is the number of times that item is put into the item pool.
            The number of items found range from minimum to maximum
            Missing values are assumed to be 1

            Example:

                # Common weapons that can be found
                Stone, 6, 2, 5
                Hammer
                Sword, 2
                Dagger, 4, 1, 2
            """)
        else:
            print( "\tAvailable commands: load [file], current, help, format, [number], quit" )   
        print()  



if __name__ == '__main__':
    main()