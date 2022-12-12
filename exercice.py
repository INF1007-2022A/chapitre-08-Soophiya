#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici

def triple_spaces(doc3):

    #copy a text file and replace every space with three spaces

    with open(doc3, "r") as f1, open("doc3.txt", "w") as f2:
        for line in f1:
            f2.write(line.replace(" ", "   "))
    print("The file has been copied and modified")
    return


def compare_docs(doc1,doc2):

    #compare two documents line by line and chek if they are the same
    #signal the first difference

    with open(doc1, "r") as f1, open(doc2, "r") as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print("The first difference is on line {}:".format(line1))
                print("The first document says: {}".format(line1))
                print("The second document says: {}".format(line2))
                break
        else:
            print("The documents are identical")
    return 

def add_letter_grade():

    #for every line in a file, add a letter grade based on the percentage on the same line 

    with open('notes.txt', 'n') as f1, open('notes_avec_lettres.txt', 'w') as f2:
        for line in f1:
            if line == "":
                continue
            else:
                for key, value in PERCENTAGE_TO_LETTER.items():
                    if value[0] <= int(line) < value[1]:
                        f2.write(line + " " + key + "\n")
    return

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    triple_spaces("doc1.txt")
    compare_docs("doc1.txt", "doc2.txt")
    add_letter_grade()
    pass
