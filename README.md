# Lootgen
Random Loot Generator for DND purposes

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