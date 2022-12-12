#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici



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

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
