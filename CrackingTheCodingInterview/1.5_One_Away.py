# 30.7.2023
# CTCI Chapter 1 Q1.5

####### QUESTION: Given two strings, write a function to check if they are one edit (or zero edits) away.

def OneAway(stringA,stringB):
    TotalEdits = 0
                            # All further tests done having first checked that they are different:
    if stringA != stringB:
                            # First check: if they are the same length,
        if len(stringA) == len(stringB):
                            # is the total of characters which differ equal to 1
            differences = 0

            for char in len(stringA):
                if stringA[char] != stringB[char]:
                    differences += 1

            TotalEdits += differences

                            # if they are of different lengths, find the first divergent character...
        else:
            if len(stringA) > len(stringB):
                count = len(stringB)
            else:
                count = len(stringA)

            for char in range(count):

                stringA_chardeleted, stringB_chardeleted = "",""

                if stringA[char] != stringB[char]:

                    if stringA_chardeleted == "":
                        stringA_chardeleted = stringA.replace(stringA[char],"")
                    if stringB_chardeleted == "":
                        stringB_chardeleted = stringB.replace(stringB[char],"")
                    print(stringA,stringB,stringA_chardeleted,stringB_chardeleted)
                    if stringA_chardeleted == stringB:
                        TotalEdits = 1
                    elif stringA == stringB_chardeleted:
                        TotalEdits = 1
                    else:
                        TotalEdits = 2

    return TotalEdits


if __name__ == "__main__":
    A = "ple"
    B = "pale"

    print(OneAway(A,B))